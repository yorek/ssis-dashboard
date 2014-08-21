import pyodbc
from configuration import *

class monitor(object):  
    all = 'all'
    none = 'none'

    status_codes = {
            0: 'all',
            1: 'created',
            2: 'running',
            3: 'cancelled',
            4: 'failed',
            5: 'pending',
            6: 'halted',
            7: 'succeeded',
            8: 'stopping',
            9: 'completed'
            }

    project_name = all
    package_name =  none
    status =  all
    execution_id = none
    
    def __init__(self):        
        self.config = Configuration('config.txt')      

    def get_engine_info(self):
        result = self.__execute_query_onerow('engine-info.sql')       
        return result

    def get_engine_kpi(self):
        result = self.__execute_query(
            'engine-kpi.sql', 
            self.config.hourSpan, 
            self.__get_proper_project_name(self.project_name)
            )

        proper_result = dict([v,0] for v in self.status_codes.values())
              
        for r in result: 
            proper_result[self.status_codes[r['status_code']]] = r['status_count']

        return proper_result

    def get_package_kpi(self):
        result = self.__execute_query_onerow(
            'package-kpi.sql', 
            self.config.hourSpan, 
            self.__get_proper_project_name(self.project_name), 
            self.__get_proper_execution_id(self.execution_id)
            )            
        return result

    def get_package_list(self):
        result = self.__execute_query(
            'package-list.sql', 
            self.config.hourSpan, 
            self.__get_proper_project_name(self.project_name),
            self.__get_proper_status_code(self.status)
            )
        return result

    def get_package_info(self):
        result = self.__execute_query_onerow(
                'package-info.sql', 
                self.__get_proper_execution_id(self.execution_id)
                )       
        return result

    def get_package_executables(self):
        result = self.__execute_query(
            'package-executables.sql', 
            self.__get_proper_execution_id(self.execution_id)
            )
        return result

    def get_package_details(self, detail_type):
        query_file = 'package-details-' + detail_type + '.sql'
        result = self.__execute_query(
            query_file, 
            self.__get_proper_execution_id(self.execution_id)
            )
        return result

    def get_package_history(self):
        query_file = 'package-history.sql'
        result = self.__execute_query(
            query_file, 
            self.__get_proper_package_name(self.package_name),
            self.__get_proper_project_name(self.project_name)
            )
        return result

    def __execute_query(self, query_file, *args):
        file = open('query/' + query_file, 'r')
        query = file.read()
        cnxn = pyodbc.connect(self.config.connectionString)
        cursor = cnxn.cursor()
        cursor.execute(query, args)
        rows = cursor.fetchall()
        result = [dict(zip([cd[0] for cd in cursor.description], row)) for row in rows]
        cursor.close()
        return result
        
    def __execute_query_onerow(self, query_file, *args):
        file = open('query/' + query_file, 'r')
        query = file.read()
        cnxn = pyodbc.connect(self.config.connectionString)
        cursor = cnxn.cursor()
        cursor.execute(query, args)
        row = cursor.fetchone()
        if (row == None):
            result = {}
        else:
            result = dict(zip([cd[0] for cd in cursor.description], row))
        cursor.close()
        return result

    def __get_proper_execution_id(self, execution_id):
        result = 0    
        if (self.execution_id != monitor.none): 
            result = execution_id
        return result

    def __get_proper_project_name(self, project_name):
        result = '%'    
        if (self.project_name != monitor.all): 
            result = project_name.replace('*', '%')
        return result

    def __get_proper_package_name(self, package_name):
        result = '%'    
        if (self.package_name != monitor.none): 
            result = package_name 
        return result

    def __get_proper_status_code(self, status):
        result = 0
        status_descriptions = {}
        for k in self.status_codes.keys():
            status_descriptions[self.status_codes[k]] = k 

        return status_descriptions[status]



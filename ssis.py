import pyodbc
from app import app

class Configuration:
    pass

class monitor(object):  
    all = 'all'

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

    folder_name = all
    project_name = all
    package_name =  all
    status =  all
    execution_id = all
    
    def __init__(self):        
        self.config = Configuration()      
        self.config.hourSpan = app.config["HOUR_SPAN"]
        self.config.connectionString = app.config["CONNECTION_STRING"]

    def get_engine_info(self):
        result = self.__execute_query('engine-info.sql', True)       
        return result

    def get_engine_folders(self):
        result = self.__execute_query('engine-folders.sql', False)
        return result

    def get_engine_projects(self):
        result = self.__execute_query('engine-projects.sql', False)
        return result

    def get_engine_kpi(self):
        result = self.__execute_query(
            'engine-kpi.sql', 
            False,
            self.config.hourSpan, 
            self.__get_proper_name_filter(self.folder_name),
            self.__get_proper_name_filter(self.project_name)
            )

        proper_result = dict([v,0] for v in self.status_codes.values())
              
        for r in result: 
            proper_result[self.status_codes[r['status_code']]] = r['status_count']

        return proper_result

    def get_package_kpi(self):
        result = self.__execute_query(
            'package-kpi.sql', 
            True,
            self.config.hourSpan, 
            self.__get_proper_name_filter(self.folder_name), 
            self.__get_proper_name_filter(self.project_name), 
            self.__get_proper_execution_id(self.execution_id)
            )            
        return result

    def get_package_list(self):
        result = self.__execute_query(
            'package-list.sql', 
            False,
            self.config.hourSpan, 
            self.__get_proper_name_filter(self.folder_name), 
            self.__get_proper_name_filter(self.project_name), 
            self.__get_proper_status_code(self.status)
            )

        for r in result:
            r["status_desc"] = self.status_codes[r["status"]].title()

        return result
    
    def get_package_info(self):
        result = self.__execute_query(
                'package-info.sql', 
                True,
                self.__get_proper_execution_id(self.execution_id)
                )       
        return result

    def get_package_executables(self):
        result = self.__execute_query(
            'package-executables.sql', 
            False,
            self.__get_proper_execution_id(self.execution_id)
            )
        return result

    def get_package_children(self):
        result = self.__execute_query(
            'package-children.sql', 
            False,
            self.__get_proper_execution_id(self.execution_id)
            )
        return result

    def get_package_details(self, detail_type):
        query_file = 'package-details-' + detail_type + '.sql'
        result = self.__execute_query(
            query_file, 
            False,
            self.__get_proper_execution_id(self.execution_id)
            )
        return result

    def get_package_history(self):
        query_file = 'package-history.sql'
        result = self.__execute_query(
            query_file, 
            False,
            self.__get_proper_name_filter(self.folder_name), 
            self.__get_proper_name_filter(self.project_name), 
            self.__get_proper_name_filter(self.package_name)
            )
        return result

    def __execute_query(self, query_file, onerow, *args):
        result = {}
        file = open('query/' + query_file, 'r')
        query = file.read()
        cnxn = pyodbc.connect(self.config.connectionString)
        cursor = cnxn.cursor()
        cursor.execute(query, args)
        if (onerow == False):
            rows = cursor.fetchall()
            result = [dict(zip([cd[0] for cd in cursor.description], row)) for row in rows]
        else:
            row = cursor.fetchone()
            if (row != None):
                result = dict(zip([cd[0] for cd in cursor.description], row))
        cursor.close()
        return result

    def __get_proper_execution_id(self, execution_id):
        result = 0    
        if (self.execution_id != monitor.all): 
            result = execution_id
        return result

    def __get_proper_name_filter(self, name_filter):
        result = '%'    
        if (name_filter != monitor.all): 
            result = name_filter.replace('*', '%')
        return result

    def __get_proper_status_code(self, status):
        result = 0
        status_descriptions = {}
        for k in self.status_codes.keys():
            status_descriptions[self.status_codes[k]] = k 

        return status_descriptions[status]



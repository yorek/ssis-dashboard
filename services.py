import json
import pyodbc
from flask import jsonify
from flask import abort

configFile = open('config.txt')
configData = json.load(configFile)
configFile.close()

connectionString = configData['connectionString']
hourSpan = configData['hourSpan']
projectNameFilter = configData['projectNameFilter']

def get_package_execution_status():
    file = open('query/q1.sql', 'r')
    query = file.read()
    cnxn = pyodbc.connect(connectionString)
    cursor = cnxn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    statuses = [dict(zip([cd[0] for cd in cursor.description], row)) for row in rows]
    return statuses

def get_package_execution_events(execution_id):
    file = open('query/q4.sql', 'r')
    query = file.read()
    cnxn = pyodbc.connect(connectionString)
    cursor = cnxn.cursor()
    cursor.execute(query, execution_id)
    rows = cursor.fetchall()
    execute_events = [dict(zip([cd[0] for cd in cursor.description], row)) for row in rows]
    return execute_events

#def get_package_execution_history():
#    file = open('query/q2.sql', 'r')
#    query = file.read()
#    cnxn = pyodbc.connect(connectionString)
#    cursor = cnxn.cursor()
#    cursor.execute(query)
#    rows = cursor.fetchall()
#    history = [dict(zip([cd[0] for cd in cursor.description], row)) for row in rows]
#    return history

def get_package_execution_kpi(project_name_pattern, execution_id):
    file = open('query/kpi-execution.sql', 'r')
    query = file.read()
    cnxn = pyodbc.connect(connectionString)
    cursor = cnxn.cursor()
    cursor.execute(query, hourSpan, project_name_pattern, execution_id)
    row = cursor.fetchone()
    kpi = dict(zip([cd[0] for cd in cursor.description], row))       
    return kpi

def get_engine_status_kpi(project_name_pattern):
    file = open('query/kpi-engine.sql', 'r')
    query = file.read()
    cnxn = pyodbc.connect(connectionString)
    cursor = cnxn.cursor()
    cursor.execute(query, hourSpan, project_name_pattern)
    rows = cursor.fetchall()
    kpi = {}
    for row in rows:
        kpi[row.status_description] = row.status_count   
    return kpi
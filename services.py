import json
import pyodbc
from configuration import *
from flask import jsonify
from flask import abort

config = Configuration('config.txt')

def get_engine_kpi(project_name_pattern):
    file = open('query/engine-kpi.sql', 'r')
    query = file.read()
    cnxn = pyodbc.connect(config.connectionString)
    cursor = cnxn.cursor()
    cursor.execute(query, config.hourSpan, project_name_pattern)
    rows = cursor.fetchall()
    kpi = {}
    for row in rows:
        kpi[row.status_description] = row.status_count   
    return kpi

def get_package_kpi(project_name_pattern, execution_id):
    file = open('query/package-kpi.sql', 'r')
    query = file.read()
    cnxn = pyodbc.connect(config.connectionString)
    cursor = cnxn.cursor()
    cursor.execute(query, config.hourSpan, project_name_pattern, execution_id)
    row = cursor.fetchone()
    kpi = dict(zip([cd[0] for cd in cursor.description], row))       
    return kpi

def get_package_execution_info(execution_id):
    file = open('query/package-execution-info.sql', 'r')
    query = file.read()
    cnxn = pyodbc.connect(config.connectionString)
    cursor = cnxn.cursor()
    cursor.execute(query, execution_id)
    row = cursor.fetchone()
    if (row == None):
        info = {}
    else:
        info = dict(zip([cd[0] for cd in cursor.description], row))       
    return info

def get_package_details(execution_id, detail_type):
    file = open('query/package-details-' + detail_type + '.sql', 'r')
    query = file.read()
    cnxn = pyodbc.connect(config.connectionString)
    cursor = cnxn.cursor()
    cursor.execute(query, execution_id)
    rows = cursor.fetchall()
    warnings = [dict(zip([cd[0] for cd in cursor.description], row)) for row in rows]
    return warnings

#tasks = [
#    {
#        'id': 1,
#        'title': u'Buy groceries',
#        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
#        'done': False
#    },
#    {
#        'id': 2,
#        'title': u'Learn Python',
#        'description': u'Need to find a good Python tutorial on the web', 
#        'done': False
#    }
#]

#def get_tasks():
#    return jsonify( { 'tasks': tasks } )

#def get_task(task_id):
#    task = filter(lambda t: t['id'] == task_id, tasks)
#    if len(task) == 0:
#        abort(404)
#    return jsonify( { 'task': task[0] } )

def get_package_execution_status():
    file = open('query/q1.sql', 'r')
    query = file.read()
    cnxn = pyodbc.connect(config.connectionString)
    cursor = cnxn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    statuses = [dict(zip([cd[0] for cd in cursor.description], row)) for row in rows]
    return statuses

def get_package_execution_events(execution_id):
    file = open('query/q4.sql', 'r')
    query = file.read()
    cnxn = pyodbc.connect(config.connectionString)
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


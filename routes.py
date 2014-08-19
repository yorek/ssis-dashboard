from datetime import datetime
from flask import render_template
from flask import make_response
from flask import jsonify
from app import app
from ssis import monitor

# Set app version 
version = "0.4 (beta)"

# Define routes
@app.route('/')
def all():
    return package(monitor.all, monitor.all, monitor.none)

@app.route('/project/<project_name>')
def project(project_name):
    return package(project_name, monitor.all, monitor.none)

@app.route('/execution/<int:execution_id>')
def execution(execution_id):
    return package(monitor.all, monitor.all, execution_id)

@app.route('/project/<project_name>/status/<status>')
def project_status(project_name, status):
    return package(project_name, status, monitor.none)

@app.route('/status/<status>')
def status(status):
    return package(monitor.all, status, monitor.none)

@app.route('/project/<project_name>/status/<status>/execution/<int:execution_id>')
def package(project_name, status, execution_id):
    m = monitor()
    m.project_name = project_name 
    m.status = status
    m.execution_id = execution_id

    environment = {
        'version': version,
        'timestamp': datetime.now(),
        'execution_id': execution_id,
        'project_name': project_name,
        'status': status
        }

    engine_kpi = m.get_engine_kpi()
    engine_info = m.get_engine_info()
    package_info = m.get_package_info()
    package_kpi = m.get_package_kpi()
    package_list = m.get_package_list()
    package_executables = m.get_package_executables()

    return render_template(
        'index.html',
        environment = environment,
        engine_info = engine_info,
        engine_kpi = engine_kpi,
        package_info = package_info,
        package_kpi = package_kpi,
        package_list = package_list,
        package_executables = package_executables
    )

@app.route('/execution/<int:execution_id>/details/<detail_type>')
def package_details(execution_id, detail_type):
    m = monitor()
    m.project_name = monitor.none 
    m.status = monitor.none
    m.execution_id = execution_id

    environment = {
        'version': version,
        'timestamp': datetime.now(),
        'execution_id': execution_id,
        }

    engine_kpi = m.get_engine_kpi()
    engine_info = m.get_engine_info()
    package_info = m.get_package_info()
    package_kpi = m.get_package_kpi()
    package_details = m.get_package_details(detail_type)

    return render_template(
        'details.html',
        environment = environment,
        engine_info = engine_info,
        package_info = package_info,
        package_kpi = package_kpi,
        package_details = package_details
    )

#@app.route('/tasks', methods = ['GET'])
#def get_tasks():
#    return services.get_tasks()

#@app.route('/tasks/<int:task_id>', methods = ['GET'])
#def get_task(task_id):
#    return services.get_task(task_id)

#@app.route('/ssis/execution-status', methods = ['GET'])
#def get_statuses():
#    execution_status = services.get_package_execution_status()
#    return jsonify ( { 'data': execution_status } )

#@app.route('/<int:execution_id>/execution-history', methods = ['GET'])
#def get_execution_history():
#    history = services.get_package_execution_history()
#    return jsonify ( { 'data': history } )

#@app.route('/ssis/execution-events/<int:execution_id>', methods = ['GET'])
#def get_package_execution_events(execution_id):
#    execution_events = services.get_package_execution_events(execution_id)
#    return jsonify ( { 'data': execution_events } )

#@app.route('/ssis/execution-kpi/<int:execution_id>', methods = ['GET'])
#def get_package_execution_kpi(execution_id):
#    kpi = services.get_package_execution_kpi(execution_id)
#    return jsonify( { 'data': kpi } )

#@app.route('/sample', methods = ['GET'])
#def get_sample():
#    return jsonify({'result': 123})

@app.errorhandler(404)
def not_found(error):
    environment = {
        'version': version,
        'timestamp': datetime.now()
        }

    return render_template(
        '404.html',
        environment = environment        
    )


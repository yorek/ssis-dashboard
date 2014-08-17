from datetime import datetime
from flask import render_template
from flask import make_response
from flask import jsonify
from app import app

import services

# Set app version 
version = "0.2 (beta)"

# Define routes
@app.route('/')
@app.route('/home')
def home():
    return execution_status_full('', 0)

@app.route('/project/<project_name>')
def home2(project_name):
    return execution_status_full(project_name, 0)

@app.route('/execution/<int:execution_id>')
def home3(execution_id):
    return execution_status_full('', execution_id)

def execution_status_full(project_name, execution_id):
    project_name_pattern = project_name + '%'
    execution_kpi = services.get_package_kpi(project_name_pattern, execution_id)
    engine_kpi = services.get_engine_kpi(project_name_pattern)
    execution_info = services.get_package_execution_info(execution_id)
    execution_status = services.get_package_execution_status()
    execution_events = services.get_package_execution_events(execution_id)
    return render_template(
        'index.html',
        version = version,
        timestamp = datetime.now(),
        statuses = execution_status,
        events = execution_events,
        kpi_execution = execution_kpi,
        kpi_engine = engine_kpi,
        info_execution = execution_info,
        selected_execution_id = execution_id
    )

@app.route('/execution/<int:execution_id>/details/<detail_type>')
def package_details(execution_id, detail_type):
    execution_kpi = services.get_package_kpi('%', execution_id)
    events = services.get_package_details(execution_id, detail_type)
    return render_template(
        'details.html',
        version = version,
        timestamp = datetime.now(),
        selected_execution_id = execution_id,
        kpi_execution = execution_kpi,
        events = events
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
    return make_response(jsonify( { 'error': 'Not found' } ), 404)


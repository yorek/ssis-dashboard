from app import app

@app.template_filter('project')
def project(text):
    result = ''
    if (text != 'all'):
        result = ' "' + text + '"'
    return result
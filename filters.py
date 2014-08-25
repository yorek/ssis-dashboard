from app import app

@app.template_filter('project')
def project(text):
    result = ''
    if (text != 'all'):
        result = ' for "' + text + '"'
    return result

@app.template_filter('folder')
def folder(text):
    result = ''
    if (text != 'all'):
        result = ' in "' + text + '"'
    return result
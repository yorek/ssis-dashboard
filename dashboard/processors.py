from dashboard import app

@app.context_processor
def utility_processor():
    def tile_color(kpi_value):
        result = 'green'
        if (kpi_value == 0) :
            result = 'primary' 
        if (kpi_value > 0) :
            result = 'red' 
        return result
    return dict(tile_color = tile_color)

@app.context_processor
def utility_processor():
    def tile_color_inv(kpi_value):
        result = 'green'
        if (kpi_value == 0) :
            result = 'primary' 
        if (kpi_value < 0) :
            result = 'red' 
        return result
    return dict(tile_color_inv = tile_color_inv)

@app.context_processor
def utility_processor():
    def package_status_class(status):
        result = {
                0 : 'default',
                1 : 'default',
                2 : 'info',
                3 : 'danger',
                4 : 'danger',
                5 : 'default',
                6 : 'danger',
                7 : 'success',
                8 : 'warning',
                9 : 'default' 
                }
        return result[status]
    return dict(package_status_class = package_status_class)

@app.context_processor
def utility_processor():
    def executable_status_class(status):
        result = {
                0 : 'success',
                1 : 'danger',
                2 : 'default',
                3 : 'danger'              
                }
        return result[status]
    return dict(executable_status_class = executable_status_class)
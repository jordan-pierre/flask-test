from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jordan'}
    return '''
<html>
    <head>
        <title>Home Page - Test Site</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''

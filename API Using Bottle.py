from bottle import route, run,template,error,static_file,request,os

# allowing multiple decorators to route to same function
@route('/hello')
@route('/hi/<name>')
def hello(name='pulkit'):
    return template ("Hello World!{{name}}",name=name)

 # handling 404 error aka not found
@error(404)
def error404(error):
    return 'Nothing here, sorry'

# displaying images
 
@route('/images/<filename:re:.*\.png>')
def send_image(filename):
    return static_file(filename, root='C://Users//pulkit.jain//Desktop', mimetype='image/png')

# displaying file content

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='C://Users//pulkit.jain//Desktop//Pip installation script')

# downloading file content

@route('/download/<filename:path>')
def download(filename):
    return static_file(filename, root='C://Users//pulkit.jain//Desktop//Pip installation script', download=filename)

# authentication

@route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if username == "pulkit" and password == "123":
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

# file upload 

@route('/upload')
def upload():
    return '''
        <form action="/upload" method="post" enctype="multipart/form-data">
  			Category:      <input type="text" name="category" />
  			Select a file: <input type="file" name="upload" />
  			<input type="submit" value="Start upload" />
		</form>
    '''


@route('/upload', method='POST')
def do_upload():
    category   = request.forms.get('category')
    upload     = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png','.jpg','.jpeg'):
        return 'File extension not allowed.'

    save_path = "C://Users//pulkit.jain//Desktop"
    upload.save(save_path) # appends upload.filename automatically
    return 'OK'

run(host='localhost', port=8080, debug=True)
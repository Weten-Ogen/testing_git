@app.route('/')
def index():
  return '<h1>Hello World</h1>'

@app.route('/register')
def regis():
  return '<h2>this good morning</h2>'

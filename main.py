from flask import Flask,render_template
app=Flask('__name__')
@app.route('/')
def hello():
  return render_template('index.html')
if('__name__' == '__main__'):
  app.run(server='127.0.0.1',port=8080,debug=True)

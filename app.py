from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello():
  return "Hello, world!"

@app.route('/money')
def money():
  return "돈을 입력하시오"

@app.route('/showmoney')
def showmoney():
  return render_template("smoney.html")
   #   return '''
   #   <iframe width="420" height="345" src="https://www.youtube.com/embed/tgbNymZ7vqY">
   #  </iframe>
   #'''       

if __name__ == '__main__':
  app.run()  
from flask import Flask, request, render_template, request
app = Flask(__name__)

@app.route('/')
def hello():
  return "Hello, world!"

@app.route('/money')
def money():
  return render_template("money.html")

@app.route('/show', methods=['GET', 'POST'])
def show():
  if request.method == 'GET':
    return "Get으로 들어온 페이지"
  else:
    # form 으로 전달된 데이터를 받아서 뻥튀기 해주야 함!!
    money = request.form['money']
    print("전달된 값은? ", int(money) * 2)
    im = money_pung(int(money))
    return "당신의 능력을 보여줘~ 얍<br></b>{}원 드립니다.format(im)"
    # return "당신의 능력을 보여줘~ 얍<br><b>원 드립니다".format(money_pung)

@app.route('/showmoney')
def showmoney():
  return render_template("smoney.html")
   #   return '''
   #   <iframe width="420" height="345" src="https://www.youtube.com/embed/tgbNymZ7vqY">
   #  </iframe>
   #'''       

if __name__ == '__main__':
  app.run()  
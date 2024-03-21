from flask import Flask,render_template,request


app=Flask(__name__)

@app.route('/',methods=['get'])
def homepage():
     return 'you are in home page'

@app.route('/index',methods=['get'])
def index():
     return render_template('index.html')

@app.route('/index2',methods=['get'])
def index2():
     return render_template('index2.html')

@app.route('/login-form',methods=['post'])
def login_form_data():
     num1 = request.form['a_val']
     num2 = request.form['b_val']
     return {'response': int(num1)+int(num2)}

@app.route('/add',methods=['GET'])
def addition():
    return render_template('add.html')

@app.route('/addition',methods=['POST'])
def addition_form():
    num1 = request.form['a_val']
    num2 = request.form['b_val']
    return {'res':abs(int(num1)+int(num2))}

@app.route('/sub',methods=['GET'])
def substraction():
    return render_template('sub.html')

@app.route('/substraction',methods=['POST'])
def substraction_form():
    num1 = request.form['a_val']
    num2 = request.form['b_val']
    return [abs(int(num1)-int(num2))]

@app.route('/mul',methods=['GET'])
def multiplication():
    return render_template('mul.html')

@app.route('/multiplication',methods=['POST'])
def multiplication_form():
    num1 = request.form['a_val']
    num2 = request.form['b_val']
    return [abs(int(num1)*int(num2))]

@app.route('/div',methods=['GET'])
def division():
    return render_template('div.html')

@app.route('/division',methods=['POST'])
def division_form():
    num1 = request.form['a_val']
    num2 = request.form['b_val']
    return {'res':abs(int(num1)/int(num2))}

app.run(port=8000)
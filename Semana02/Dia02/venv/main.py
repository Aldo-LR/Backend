from flask import Flask,render_template,request
import requests
URL = "https://api.github.com/users/Aldo-LR"

data = requests.get(URL)
data = data.json()

print(data)

app = Flask(__name__)

lstProductos = ['LAPTOP','IMPRESORA','PARLANTES']

@app.route('/index')
def index():
    nombre = request.args.get('nombre','no hay nombre')
    
    context = {
        'nombre':nombre,
        'productos':lstProductos
        
    }
    return render_template('index.html',**context)

@app.route('/')
def home():
    return render_template('home.html',**data)

@app.route('/portafolio')
def portafolio():
    return render_template('portafolio.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True,port=5000)
from flask import Flask,render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']='byhtlft0ndjrpyrimmge-mysql.services.clever-cloud.com'
app.config['MYSQL_USER']='u9tvahhw6xhwixj6'
app.config['MYSQL_PASSWORD'] = '5jb0VYVYJbDXAv3kz4aD'
app.config['MYSQL_DB'] = 'byhtlft0ndjrpyrimmge'

mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute('select id,sistema,procesador,memoria from computadoras')
    data = cursor.fetchall()
    cursor.close()
    print(data)
    
    context = {
        'data':data
    }
    
    return render_template('index.html',**context)
app.run(debug=True,port=4000)

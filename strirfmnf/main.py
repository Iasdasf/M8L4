#Импорт
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#Подключение SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Создание db
db = SQLAlchemy(app)


#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')



#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template('index.html', button_python=button_python,   
    button_discord=button_discord,button_html=button_html, button_db=button_db)


app.run(host='0.0.0.0', port=81)
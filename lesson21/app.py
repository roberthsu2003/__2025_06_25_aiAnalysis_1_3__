from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# 配置數據庫
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 首頁路由
@app.route('/')
def home():
    return '歡迎來到 Flask 應用！'

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

# 首頁路由
@app.route('/')
def home():
    return '歡迎來到 Flask 應用！'

if __name__ == '__main__':
    app.run(debug=True)

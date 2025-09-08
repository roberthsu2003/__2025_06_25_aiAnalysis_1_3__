from flask import Flask, render_template, request
from google import genai


app = Flask(__name__)

# 初始化 Gemini 客戶端
client = genai.Client()

# 首頁路由
@app.route('/')
def home():
    return render_template('home.html')

# Gemini 路由
@app.route('/gemini', methods=['GET', 'POST'])
def gemini():
    response = None
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        if user_input:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_input
            )
    return render_template('gemini.html', response=response)

from flask import Flask, render_template, request
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)

# 初始化 Gemini 客戶端
client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

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

if __name__ == '__main__':
    app.run(debug=True)


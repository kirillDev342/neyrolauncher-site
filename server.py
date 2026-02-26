from flask import Flask, request, jsonify, Response
import requests
import os
import base64
from datetime import datetime

app = Flask(__name__)

# Настройки пользователей
USERS = {
    "user1": "123456",
    "free": "freevpn",
    "test": "test123"
}

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>🔥 МОЙ VPN</title>
        <meta charset="utf-8">
        <style>
            body {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                font-family: Arial;
                text-align: center;
                padding: 20px;
            }
            .card {
                background: rgba(255,255,255,0.1);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                padding: 40px;
                max-width: 400px;
                margin: 0 auto;
            }
            .status {
                background: #00ff0044;
                border: 2px solid #00ff00;
                border-radius: 50px;
                padding: 10px;
                margin: 20px 0;
            }
            .test-account {
                background: #ffffff22;
                padding: 15px;
                border-radius: 10px;
                margin: 20px 0;
            }
            .btn {
                background: linear-gradient(45deg, #ff6b6b, #f0f);
                color: white;
                border: none;
                padding: 15px 30px;
                border-radius: 50px;
                text-decoration: none;
                display: inline-block;
                margin: 10px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🔥 МОЙ VPN</h1>
            <div class="status">✅ СЕРВЕР РАБОТАЕТ</div>
            
            <div class="test-account">
                <h3>📱 ТЕСТОВЫЕ АККАУНТЫ</h3>
                <p><b>Логин:</b> test<br><b>Пароль:</b> test123</p>
                <p><b>Логин:</b> free<br><b>Пароль:</b> freevpn</p>
            </div>
            
            <a href="/status" class="btn">📊 СТАТУС</a>
            <a href="/youtube" class="btn">▶️ YOUTUBE</a>
            <a href="/instagram" class="btn">📸 INSTAGRAM</a>
        </div>
    </body>
    </html>
    '''

@app.route('/status')
def status():
    return jsonify({
        "server": "online",
        "time": datetime.now().strftime("%H:%M:%S"),
        "users": list(USERS.keys())
    })

@app.route('/youtube')
def youtube():
    return proxy_page('youtube.com')

@app.route('/instagram')
def instagram():
    return proxy_page('instagram.com')

@app.route('/tiktok')
def tiktok():
    return proxy_page('tiktok.com')

@app.route('/proxy/<path:url>')
def proxy(url):
    return proxy_page(url)

def proxy_page(url):
    try:
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=15)
        return Response(response.content, response.status_code, {
            'Content-Type': response.headers.get('Content-Type', 'text/html')
        })
        
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

from flask import Flask, request, Response
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head><title>VPN Proxy</title></head>
    <body>
        <h2>Введи ссылку:</h2>
        <form method="get" action="/go">
            <input name="url" size=50 value="google.com">
            <button>Открыть</button>
        </form>
    </body>
    </html>
    '''

@app.route('/go')
def go():
    url = request.args.get('url')
    if not url:
        return 'Нет url'
    
    if not url.startswith('http'):
        url = 'https://' + url
    
    try:
        r = requests.get(url, timeout=10)
        return Response(r.content, r.status_code)
    except:
        return 'Ошибка загрузки'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

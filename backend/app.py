from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Backend</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-image: url('https://verpex.com/assets/uploads/images/blog/How-to-become-a-Backend-Developer.jpg?v=1665484477');
                background-size: cover;
                background-position: center;
                margin: 0;
            }
            .container {
                text-align: center;
                padding: 20px;
                background: rgba(255, 255, 255, 0.8);
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #00796b;
            }
            p {
                color: #004d40;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Добро пожаловать на Backend</h1>
            <p>Это страница сервера Flask</p>
        </div>
    </body>
    </html>
    '''

@app.route('/data')
def data():
    return jsonify(message="Hello from backend!")

if __name__ == '__main__':
    app.run(host='0.0.0.0')


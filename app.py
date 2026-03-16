from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

print()

@app.route('/')
def home():
    return render_template('index.html', title='home')

@app.route('/login', methods=['POST', 'GET']) 
def login():
    req = request.get_json()
    print(request.method)
    username = req['username']
    password = req['password']
    return jsonify({ "username": username, "password": password })

@app.route('/user/<name>')
def user(name): 
    return f'<h1>Hello, {name}</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
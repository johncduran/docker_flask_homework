from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Coffee Lover!'

@app.route('/order/<coffee_type>')
def order_coffee(coffee_type):
    return render_template('order.html', coffee_type=coffee_type)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)




from flask import Flask, render_template

app = Flask(__name__)

# Dummy data for groceries
groceries = [
    {'name': 'Apple', 'price': 3.5},
    {'name': 'Banana', 'price': 1.2},
    {'name': 'Carrot', 'price': 0.8},
    {'name': 'Milk', 'price': 1.5}
]

@app.route('/')
def home():
    return render_template('index.html', groceries=groceries)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=9090)


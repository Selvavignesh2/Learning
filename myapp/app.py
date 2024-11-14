from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! This is a simple Flask web application."

if __name__ == '__main__':
    # Run the application on port 9090
    app.run(host='0.0.0.0', port=9090)

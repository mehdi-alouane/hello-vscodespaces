from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return {"message": "Hello, GH Codespaces!"}, 200

app.run(host='0.0.0.0', port=8080, debug=False)
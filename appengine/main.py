from flask import Flask
app = Flask(__name__)

@app.route('/')
def hola():
    return 'Ola ke ace'

if __name__ == '__main__':
    app.run ()
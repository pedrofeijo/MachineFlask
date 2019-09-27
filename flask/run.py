from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    # return 'Hello, World!'
    return render_template("home.html") #retornar ao template HTML

if __name__ == '__main__':
    app.run(debug=True)

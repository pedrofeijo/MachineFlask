from flask import Flask, render_template, json, request
app = Flask(__name__)

@app.route('/')
def index():
    # return 'Hello, World!'
    return render_template("home.html") #retornar ao template HTML

@app.route('/hello', methods=['GET'])
def hello():
    if request.method == 'GET': #this block is only entered when the form is submitted
        data = {"resposta": request.args.get('nome'),
                'salario': request.args.get('salario')} #

        response = app.response_class(
                response=json.dumps(data),
                status=200,
                mimetype='application/json'
        )
        return response


@app.route('/predict',  methods=['GET'])
def predict():
     if request.method == 'GET': #this block is only entered when the form is submitted
        data = request.json #

        response = app.response_class(
                response=json.dumps(data),
                status=200,
                mimetype='application/json'
        )
        return response

if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=6969)

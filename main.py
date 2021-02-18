from flask import Flask,render_template,request
from flask_restful import Api, Resource, fields, marshal_with


app = Flask(__name__)
api = Api(app)



todos = {}


@app.route('/notes', methods=['GET', 'POST', 'DELETE'])
def getURL():
    if request.method == 'POST':
        id = request.form['id']
        data = request.form['data']
        print(id, data)
        todos[id] = data
        return {id: data}

    if request.method == 'GET':
        return todos

    if request.method == 'DELETE':
        id = request.form['id']
        del todos[id]
        return todos


if __name__ == "__main__":
    app.run(debug=True)

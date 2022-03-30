from flask import Flask
from flask import Flask
from flask_restful import Resource, Api
import subprocess, os

app = Flask(__name__)
api = Api(app)


def test_func(cmd):
    return "The command to be executed is: {}".format(cmd)


class ExecuteCode(Resource):

    def get(self,name):
        pass

    def post(self,robot_file):
        cmd = "robot " + robot_file
        return os.system(cmd)

    def delete(self,name):
        pass

class TestCode(Resource):

    def post(self,test):
        cmd = "robot " + test
        output = test_func(cmd)
        return output

class AllScripts(Resource):

    def get(self,hello):
        return "test endpoint"

@app.route('/')
def index():
    return '<h1>Hello world, using os</h1>'

api.add_resource(ExecuteCode,'/robot/<string:robot_file>')
api.add_resource(TestCode,'/test/<string:test>')
api.add_resource(AllScripts,'/hello/<string:hello>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


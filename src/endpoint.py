try:
    import calculations as calc
    from operation import Operation
    from inmemorystorage import InMemoryStorage
except:
    import src.calculations as calc
    from src.operation import Operation
    from src.inmemorystorage import InMemoryStorage
from flask import Flask, Response
from time import time
import json
import uuid

app = Flask(__name__)
app.config['STORAGE'] = InMemoryStorage()

def handle(calculationFunc, operand1, operand2, calculationName):
    result = calculationFunc(operand1, operand2)
    operation = Operation(operand1, operand2, calculationName, result, time(), uuid.uuid4())
    app.config['STORAGE'].persist(operation)

    return Response(str(result), mimetype='text/plain')

@app.route("/add/<operand1>/<operand2>")
def add(operand1, operand2):
    return handle(calc.add, float(operand1), float(operand2), 'addition')

@app.route("/subtract/<operand1>/<operand2>")
def subtract(operand1, operand2):
    return handle(calc.subtract, float(operand1), float(operand2), 'subtraction')

@app.route("/multiply/<operand1>/<operand2>")
def multiply(operand1, operand2):
    return handle(calc.multiply, float(operand1), float(operand2), 'multiplication')

@app.route("/divide/<operand1>/<operand2>")
def divide(operand1, operand2):
    return handle(calc.divide, float(operand1), float(operand2), 'division')

@app.route("/history")
def get_history():
    def todict(o):
        return {
            'uid': str(o.uid),
            'operand1': o.operand1,
            'operand2': o.operand2,
            'calculation': o.calculation,
            'result': o.result,
            'timestamp': o.timestamp
        }

    operations = app.config['STORAGE'].retrieve_all()
    dictionaries = [todict(o) for o in operations]
    return Response(json.dumps(dictionaries), mimetype='application/json')

@app.route("/history", methods=["DELETE"])
def clear_history():
    app.config['STORAGE'].clear()
    return Response(status=200)

if __name__ == "__main__":
    app.run()

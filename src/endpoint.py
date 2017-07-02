try:
    from calculations import *
    from operation import Operation
    from inmemorystorage import InMemoryStorage
except:
    from src.calculations import *
    from src.operation import Operation
    from src.inmemorystorage import InMemoryStorage
from flask import Flask, Response
from time import time
import json
import uuid

app = Flask(__name__)
app.config['STORAGE'] = InMemoryStorage()

@app.route("/execute/<operand1>/<calculation>/<operand2>")
def execute(operand1, calculation, operand2):
    op1, op2 = float(operand1), float(operand2)

    if calculation == "addition":
        result = add(op1, op2)
    elif calculation == "subtraction":
        result = subtract(op1, op2)
    elif calculation == "multiplication":
        result = multiply(op1, op2)
    elif calculation == "division":
        result = divide(op1, op2)
    else:
        raise Exception('calculation not recognized (' + calculation + ')')

    operation = Operation(op1, op2, calculation, result, time(), uuid.uuid4())
    app.config['STORAGE'].persist(operation)

    return Response(str(result), mimetype='text/plain')

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

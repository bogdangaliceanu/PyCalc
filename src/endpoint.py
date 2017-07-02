# from operation import Operation
# from filestorage import FileStorage
# import time
# import uuid

# class App:

#     def __init__(self, storage):
#         self.storage = storage

# o = Operation(2, 5, 'addition', 7, time.time(), uuid.uuid4())
# storage = FileStorage(r".\operations")
# storage.persist(o)
# allOps = storage.retrieve_all()
# o2 = storage.retrieve(o.uid)

from calculations import *
from flask import Flask
app = Flask(__name__)

@app.route("/execute/<operand1>/<calculation>/<operand2>")
def execute(operand1, calculation, operand2):
    if calculation == "addition":
        return str(add(float(operand1), float(operand2)))

# @app.route("/history")
# def get_history():


# @app.route("/history", methods=["DELETE"])
# def clear_history():


if __name__ == "__main__":
    app.run()
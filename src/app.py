from calculations.addition import add
from operation import Operation
from filestorage import FileStorage
import time
import uuid

class App:

    def __init__(self, storage):
        self.storage = storage

o = Operation(2, 5, 'addition', 7, time.time(), uuid.uuid4())
storage = FileStorage(r".\operations")
storage.persist(o)
allOps = storage.retrieve_all()
o2 = storage.retrieve(o.uid)
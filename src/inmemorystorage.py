class InMemoryStorage:

    def __init__(self):
        self._operations = dict()

    def persist(self, operation):
        self._operations[operation.uid] = operation

    def retrieve(self, uid):
        return self._operations[uid]

    def retrieve_all(self):
        return self._operations.values()

    def clear(self):
        self._operations.clear()

import pickle
import os

class FileStorage:

    def __init__(self, path):
        self.path = path
        if not os.path.isdir(path):
            os.mkdir(path)

    def persist(self, operation):
        with open(self.path + '\\' + str(operation.uid), 'wb') as f:
            pickle.dump(operation, f)

    def retrieve(self, uid):
        with open(self.path + '\\' + str(uid), 'rb') as f:
            return pickle.load(f)

    def retrieve_all(self):
        uids = os.listdir(self.path)
        return list(map(self.retrieve, uids))

import os

class Reader:
    def read_all(self, path):
        with open(path, 'r') as f:
            return f.read()

    
    def add_sth(self, path, new_line):
        with open(path, 'a') as f:
            f.write(new_line)
    
    def delete(self, path):
        os.remove(path)
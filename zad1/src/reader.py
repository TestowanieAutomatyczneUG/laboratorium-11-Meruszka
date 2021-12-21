class Reader:
    def read_all(self, file):
        file.read()

    
    def add_sth(self, file, new_line):
        with open(str(file), 'a') as f:
            f.write(new_line)
    
    def delete(self, file):
        with open(str(file), 'w') as f:
            f.write('')
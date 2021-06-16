class Reader:
    def __init__(self, file):
        self.file = open(file, 'r')
        self.is_done = False
    
    def read_char(self):
        self.is_done = True
        return self.file.readlines()

reader = Reader('text1.txt')
while not reader.is_done:
    print(reader.read_char(), end='')






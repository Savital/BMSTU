

class DataReader():
    def __init__(self, name):
        super(DataReader, self).__init__()
        self.name = name
        self.construct()

    def __del__(self):
        pass

    def construct(self):
        pass

    def get(self):
        f = open(self.name, 'r')
        text = f.read()
        print(text)
        #for line in f:
        #    print(line)
        f.close()


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
        results = []
        f = open(self.name, 'r')
        for line in f:
            list = []
            i = 0
            num = ""
            while i < len(line):
                if line[i] == ' ':
                    list.append(num)
                    num = ""
                if line[i] == '\n':
                    list.append(num)
                    break
                num += line[i]
                i += 1
            results.append(list)
        f.close()

        return results

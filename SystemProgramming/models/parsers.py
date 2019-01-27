# Savital https://github.com/Savital
# Reads data from proc

import os

class ProcReader():
    def __init__(self):
        super(ProcReader, self).__init__()
        self.construct()

    def __del__(self):
        pass

    def construct(self):
        pass

    def get(self, path):
        if not os.path.exists(path):
            return False

        results = []
        f = open(path, 'r')
        for line in f:
            list = []
            i = 0
            elm = ""
            while i < len(line):
                if line[i] == ' ':
                    list.append(elm.strip())
                    elm = ""
                if line[i] == '\n':
                    list.append(elm.strip())
                    break
                elm += line[i]
                i += 1
            results.append(list)
        f.close()
        print(results)
        return results

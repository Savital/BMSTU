# Savital https://github.com/Savital
# Implements methods to calculate stats by log data

class Calc():
    funcKeys = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12']
    alphabetLowerRU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    alphabetUpperRU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    alphabetRU = alphabetLowerRU + alphabetUpperRU
    # жи ши ча ща чу щу чк чн

    def __init__(self):
        super(Calc, self).__init__()
        self.construct()

    def __del__(self):
        pass

    def construct(self):
        pass

    def recProt(self):
        pass

    def cntShortcuts(self):
        states = []
        for item in self.list:
            states.append(False)
            pass

        count = 0
        i = 0
        while i < len(self.list):
            breakFlag = False
            j = 1
            while (i + j < len(self.list)):
                if self.list[i + j][5] == self.list[i][5]:
                    breakFlag = True
                    break
                j += 1
            if breakFlag == True:
                states[i] = True
                states[i + j] = True

                #k = 0
                #while k < j:
                #    p = 0
                #    k += 1
                if j > 1:
                    count += 1
            i += 1


        return count

    def cntFuncs(self):
        count = 0
        for item in self.list:
            if item[4] in self.funcKeys:
                count += 1
        return count // 2

    def formStats(self, list):
        if len(list) == 0:
            return [0.0, 0.0, 0.0, 0, 0]
        self.list = list

        self.count = 0
        self.sumDowntime = 0.0
        self.sumSearchtime = 0.0
        for item in self.list:
            if item[2] != 0:
                self.sumDowntime += item[2]
                self.sumSearchtime += item[3]
                self.count += 1

        if self.count == 0:
            return [0.0, 0.0, 0.0, 0, 0]

        self.avrDowntime = self.sumDowntime / self.count
        self.avrSearchtime = self.sumSearchtime / self.count
        self.inpSpeed = 1000 * self.count / (self.sumDowntime + self.sumSearchtime)

        results = [self.avrDowntime, self.avrSearchtime, self.inpSpeed, self.cntShortcuts(), self.cntFuncs()]

        return results

    def analyzeRuShortcuts(self, list):
        results = []
        if len(list) == 0:
            return results

        self.list = list
        for item in self.list:
            if item[4] in self.alphabetRU:
                print(item)
                results += item

        return results
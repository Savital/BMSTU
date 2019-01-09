# Savital https://github.com/Savital
# Implements methods to calculate stats by log data

class Calc():
    def __init__(self):
        super(Calc, self).__init__()
        self.construct()

    def __del__(self):
        pass

    def construct(self):
        pass

    def averageDowntime(self, list):
        average = 0.0
        for item in list:
            average += item[2]
        average /= len(list)
        return average

    def averageSearchtime(self, list):
        average = 0.0
        for item in list:
            average += item[3]
        average /= len(list)
        return average

    def inputSpeed(self, list):
        sum = 0
        for item in list:
            sum += item[2] + item[3]
        return 1000 * len(list) / (sum)

    def formStats(self, list):
        results = []
        if len(list) == 0:
            results.extend([0.0, 0.0, 0.0, 0.0, 0.0])
        elif len(list[0]) == 1:
            results.extend([list[0][2], list[0][3], 1 / (list[0][2] + list[0][3]), 0.0, 0.0])
        else:
            results.extend([self.averageDowntime(list), self.averageSearchtime(list), self.inputSpeed(list), 0.0, 0.0])

        return results
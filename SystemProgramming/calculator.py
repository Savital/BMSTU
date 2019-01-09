class Calculator():
    def __init__(self):
        super(Calculator, self).__init__()
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
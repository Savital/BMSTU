from threading import Timer, Thread, Event

class EventTimerGenerator():
    def __init__(self,t,hFunction):
        self.t=t
        self.hFunction = hFunction
        self.thread = Timer(self.t, self.handle_function)

    def handle_function(self):
        self.hFunction()
        self.thread = Timer(self.t, self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()

def printer():
    print("Hello")

t = EventTimerGenerator(0.01, printer)
t.start()
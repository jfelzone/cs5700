#going to open and create the publisher for the data
import time
from thread import start_new_thread

class Subject:
    def __init__(self):
        self.subscribers = set()

    def register(self, who):
        self.subscribers.add(who)
    
    def unregister(self, who):
        self.subscribers.discard(who)

    def dispatch(self, data):
        for subscriber in self.subscribers:
            subscriber.update(data)
            print subscriber.name

    def dataSimulate(self):
        file = open("simulation.csv", "r")

        for line in file:
            if line == "---\n":
                time.sleep(0.25)
            #print line.split(',')
            self.dispatch(line.rstrip('\n').split(','))
    
    def threadedSimFunc(self):
        start_new_thread(self.dataSimulate, ())
        #self.p = Process(target=self.dataSimulate,)
        #self.p.start()
        #self.p.join()



class Subscriber():
    def __init__(self, name):
        self.name = name
    def update(self, data):
        print self.name , ":" , data


class updater(Subscriber):
    def __init__(self, name):
        self.name = name
        self.data = []
    def update(self,data):
        print self.getString(data)

    def getString(self, data):
        return data[1]

class decorator(updater):
    def __init__(self, updater):
        self.updater = updater

    def update(self, data):
        print self.getString(data)

    def getString(self, data):
        return data[0] + " " + self.updater.getString(data)

class decoratorTwo(updater):
    def __init__(self, updater):
        self.updater = updater

    def update(self, data):
        print self.getString(data)

    def getString(self, data):
        return data[2] + " " + self.updater.getString(data)

# print "Hello"

# sub = Subject() 
# test = Subscriber('test')
# sub.register(test)

# sub.threadedSimFunc()


# decorate = updater('baseline')
# sub.register(updater)
data = ['jake', 'kayden', 'logan']

decor = updater('test')

decor.update(data)

decor = decorator(decor)

decor.update(data)
decor.update(data)

decor = decoratorTwo(decor)

decor.update(data)

decor = decorator(decor)

decor.update(data)

decor = updater('test')

decor.update(data)


#from subscriber import Subscriber
class Subscriber():
    def __init__(self, name):
        self.name = name
    def update(self, data):
        print self.name , ":" , data


class GuiTicker(Subscriber):

    def __init__(self, name, canvas, xcoord, ycoord, jerseynumber, totaldistance, totalwindowsize):
        self.name = name
        self.canvas = canvas
        self.shape = canvas.create_rectangle(xcoord, ycoord, 20, 5, fill = "blue")
        self.jerseynumber = jerseynumber
        self.totaldistance = totaldistance
        self.totalwindowsize = totalwindowsize
        self.movementList = [0]

    def calculateMovement(self, currentPosition):
        x = (self.totalwindowsize*currentPosition)/self.totaldistance
        return x - self.movementList[-1]

    def update(self,data): 
        if data[0] == "OnCourse" and int(data[1]) == int(self.jerseynumber): 
            print self.name , ":" , data
            if (self.calculateMovement(int(float(data[3]))) + self.movementList[-1]) < self.totalwindowsize:
                self.canvas.move(self.shape, self.calculateMovement(int(float(data[3]))), 0)
                self.movementList.append(self.movementList[-1] + self.calculateMovement(int(float(data[3]))))



class emailObserver(Subscriber):
    def __init__(self, name, jerseynumber, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.starttls()
        self.server.login(email, password)
        self.jerseynumber = jerseynumber

    def update(self, data):
        if data[0] == "OnCourse" and int(data[1]) == int(self.jerseynumber): 
            self.server.sendmail("App", "2089546530@vtext.com", str(data[1])+","+str(data[0])+","+str(data[3]))
            #+", "+str(data[1])+", "+str(data[2])+", "+str(data[3]))
            print self.name , ":" , data[0], data[1] , data[2], data[3]

class listObserver(Subscriber):
    def __init__(self, name, listbox, jerseynumber):
        self.name = name
        self.listbox = listbox
        self.jerseynumber = jerseynumber

    def update(self,data):
        if data[0] == "OnCourse" and int(data[1]) == int(self.jerseynumber): 
            print self.name , ":" , data
            string = str(data[1])+", "+str(data[0])+", "+str(data[2])+", "+str(data[3])
            self.listbox.insert(0, string)


#so baseline without decorator will just desplay the top 10 guys' number
class topRacersObserver(Subscriber):
    def __init__(self, name, listbox):

        self.name = name
        self.data = []
        self.topTen = []
        self.topTenDist = []
        self.listbox = listbox

    def updateTopTen(self):
        if len(self.topTen) < 10:
            self.topTen.append(self.data)
            self.topTenDist.append(self.data[3])
            self.topTenDist.sort(reverse=True)
        elif len(self.topTen) >= 10 and self.data[3] > self.topTenDist[0]:
            tracker = 0
            for index, x in enumerate(self.topTen):
                if x[3] == self.data[3]:
                    tracker = index
            del self.topTen[tracker]
            self.topTenDist.pop(0)

            self.topTen.append(self.data)
            self.topTenDist.append(self.data[3])
            self.topTenDist.sort(reverse=True)


    def update(self, data):
        if data[0] == "OnCourse": 
            self.data = data
            self.updateTopTen()
            self.listbox.delete(0,END)
            for i in self.topTen: 
                #keep in mind the order on this guy and how we are going to have to sort
                self.listbox.insert(0, i[1])



class streamer(Subscriber):
    def __init__(self, name, listbox):
        self.name = name
        self.data = []
        self.listbox = listbox
    def update(self,data):
        if data[0] != "---":
            print self.name , ":" , data
            string = self.getString(data)
            self.listbox.insert(0, string)

    def getString(self, data):
        return data[1]


class decorator(streamer):
    def __init__(self, updater):
        self.updater = updater
        self.name = self.updater.name
        self.listbox = self.updater.listbox

    def update(self, data):
        if data[0] != "---":
            string = self.getString(data)
            self.updater.listbox.insert(0, string)

    def getString(self, data):
        return data[0] + " " + self.updater.getString(data)


class decoratorTwo(streamer):
    def __init__(self, updater):
        self.updater = updater
        self.name = self.updater.name

    def update(self, data):
        if data[0] != "---":
            string = self.getString(data)
            self.updater.listbox.insert(0, string)

    def getString(self, data):
        return data[2] + " " + self.updater.getString(data)



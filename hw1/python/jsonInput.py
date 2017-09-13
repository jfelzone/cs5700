#jake felzien
# the file for jsonspecific input that inherits from the general datainput class
#from dataInput import dataInput
from dataInput import dataInput

class jsonInput(dataInput):
    
    def read(self, fileName):
        returnList = []
        dataFile = open("Data/"+fileName)
        data = json.load(dataFile)
        for i in data:
            newPerson = Person(i["BirthCounty"], i["BirthDay"], i["BirthMonth"], i["BirthOrder"], i["BirthYear"], i["FirstName"], i["Gender"], i["IsPartOfMultipleBirth"], i["LastName"], i["MiddleName"], i["MotherFirstName"], i["MotherLastName"], i["MotherMiddleName"], i["NewbornScreeningNumber"], i["ObjectId"], i["Phone1"], i["Phone2"], i["SocialSecurityNumber"], i["StateFileNumber"])
            returnList.append(newPerson)
        return returnList

# Jake Felzien
# moving classes to other files
class Person():
    def __init__(self, BirthCounty, BirthDay, BirthMonth, BirthOrder, BirthYear, FirstName, Gender, IsPartOfMultipleBirth, LastName, MiddleName, MotherFirstName, MotherLastName, MotherMiddleName, NewbornScreeningNumber, ObjectId, Phone1, Phone2, SocialSecurityNumber, StateFileNumber):
        self.BirthCounty = BirthCounty
        self.BirthDay = BirthDay
        self.BirthMonth = BirthMonth 
        self.BirthOrder = BirthOrder
        self.BirthYear = BirthYear
        self.FirstName = FirstName
        self.Gender = Gender
        self.IsPartOfMultipleBirth = IsPartOfMultipleBirth
        self.LastName = LastName
        self.MiddleName = MiddleName
        self.MotherFirstName = MotherFirstName
        self.MotherLastName = MotherLastName
        self.MotherMiddleName = MotherMiddleName
        self.NewbornScreeningNumber = NewbornScreeningNumber
        self.ObjectId = ObjectId
        self.Phone1 = Phone1
        self.Phone2 = Phone2
        self.SocialSecurityNumber = SocialSecurityNumber
        self.StateFileNumber = StateFileNumber
    def printPerson(self):
        stringer = "\t"+str(self.ObjectId)+" "+ str(self.FirstName) + " " +str(self.MiddleName)+ " " + str(self.LastName) + " " + str(self.BirthDay)+"/"+str(self.BirthMonth) + "/"+ str(self.BirthYear)
        print stringer
# Jake Felzien
# generating my thoughts and first implementing the assignment in a language that i am much more familiar with
import sys
import json
from pprint import pprint
from person import Person
import personCollection
import dataInput
import jsonInput
import xmlInput

class matchPair():
    def __init__(self, person1, person2):
        self.match1 = person1
        self.match2 = person2


class resultOutput():
    def __init__(self, name):
        self.name = name
    def output():
        pass

class fileOutput(resultOutput):
    def output():
        pass

class consoleOutput(resultOutput):
    def output(matcherList):
        for i in matchList:
            print "Match:"
            i.match1.printPerson(), i.match2.printPerson()
            print '----\n'

class matcher():
    #personCollection
    #matchedPersonsList = []
    def __init__(self, name):
        self.name = name

    def findMatches():
        pass
        

class matcherOne(matcher):
    
    def findMatches(self, personCollection):
        personCollectioner = personCollection
        matchedPersonsList = []
        for index, i in enumerate(personCollection.personCollectionArray):
            for index2, j in enumerate(personCollection.personCollectionArray):
                if index2 <= index:
                    continue
                else:
                    if i.FirstName == j.FirstName and i.LastName == j.LastName:
                        newMatch = matchPair(i, j)
                        matchedPersonsList.append(newMatch)
                        break
        return matchedPersonsList

class matcherTwo(matcher):

    def findMatches(self, personCollection):
        personCollectioner = personCollection
        matchedPersonsList = []
        for index, i in enumerate(personCollection.personCollectionArray):
            for index2, j in enumerate(personCollection.personCollectionArray):
                if index2 <= index:
                    continue
                else:
                    if i.FirstName == j.FirstName and i.LastName == j.LastName and i.SocialSecurityNumber == j.SocialSecurityNumber:
                        newMatch = matchPair(i, j)
                        matchedPersonsList.append(newMatch)
                        break
        return matchedPersonsList

class matcherThree(matcher):

    def findMatches(self, personCollection):
        personCollectioner = personCollection
        matchedPersonsList = []
        for index, i in enumerate(personCollection.personCollectionArray):
            for index2, j in enumerate(personCollection.personCollectionArray):
                if index2 <= index:
                    continue
                else:
                    birthday1 = str(i.BirthDay)+"/"+str(i.BirthMonth)+"/"+str(i.BirthYear)
                    birthday2 = str(j.BirthDay)+"/"+str(j.BirthMonth)+"/"+str(j.BirthYear)
                    
                    if birthday1 == birthday2 and i.FirstName == j.FirstName and i.LastName == j.LastName:
                        newMatch = matchPair(i, j)
                        matchedPersonsList.append(newMatch)
                        break
        return matchedPersonsList

#code in prep for the main function
dataInputList = []

newInput = jsonInput("json")
dataInputList.append(newInput)
newInput = xmlInput("xml")
dataInputList.append(newInput)

matcherList = []

newMatcher = matcherOne("1")
matcherList.append(newMatcher)
newMatcher = matcherTwo("2")
matcherList.append(newMatcher)
newMatcher = matcherThree("3")
matcherList.append(newMatcher)

dataOutputList = []

newDataOutput = consoleOutput("1")
dataOutputList.append(newDataOutput)
newDataOutput = fileOutput("2")
dataOutputList.append(newDataOutput)

#have to put this up here
# will pull other code into other class files
def getFileTypeFromArgs(fileName):
    extension = fileName.split('.')[1]
    for inputItem in dataInputList:
        if inputItem.name == extension:
            return inputItem
    return None

def getMatchingTypeFromArgs(argu):
    matcherval = str(argu)
    for matcherItem in matcherList:
        if matcherItem.name == matcherval:
            return matcherItem
    return None

def getOutputType(argu):
    outputType = str(argu)
    for item in dataOutputList:
        if item.name == outputType:
            return item
    return None


if __name__ == "__main__":
    print sys.argv
    print len(sys.argv)
    dataFile = open("Data/"+sys.argv[2])
    data = json.load(dataFile)

    # pprint(data)
    # print "\n Tring to play around with JSON and how it works:"
    # print data[0]["BirthCounty"]

    for inputItem in dataInputList:
        print inputItem.name
    
    print "\n Now selecting the file:\n"    
    newDataInput = getFileTypeFromArgs(sys.argv[2])
    print newDataInput.name

    personList = personCollection()
    personList.loadPeopleIntoCollection(newDataInput, sys.argv[2])
    print len(personList.personCollectionArray)
    print personList.personCollectionArray[0].BirthCounty

    print "\n Now selecting the matching algorithm:\n"
    newMatcherArg = getMatchingTypeFromArgs(sys.argv[1])
    print "Matching name:", newMatcherArg.name

    print "\nNow attempting to return matches:"
    matchList = newMatcherArg.findMatches(personList)
    try:
        outputvar = sys.argv[3]
    except:
        outputvar = "1"
    
    newOutputType = getOutputType(outputvar)
    newOutputType.output()

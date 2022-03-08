import random


class NameList:

    # Will store full names by alphanumeric code
    listOfNames: "dict[int, list[str]]" = {}
    firstNames: "list[str]"
    lastNames: "list[str]"

    def __init__(self):

        self.listOfNames = {}
        self.firstNames = []
        self.lastNames = []
        
        # Gets list of first names from file
        with open("first-names.txt") as f:
            lines = f.readlines()
        for name in lines:
            self.firstNames.append(name[:-1].lower())

        # Gets list of surnames from file
        with open("last-names.txt") as f:
            lines = f.readlines()
        for name in lines:
            self.lastNames.append(name[:-1].lower())

    def set_sample(self):

        # Produces 100 names by combining a random first name with a random surname
        while len(self.listOfNames) < 101:
            randFirstName = self.firstNames[random.randrange(len(self.firstNames))]
            randLastName = self.lastNames[random.randrange(len(self.lastNames))]
            name = randFirstName.capitalize() + " " + randLastName.capitalize()

            # Gets alphanumeric code for the generated name
            code = self.getNameCode(randFirstName) + self.getNameCode(randLastName)
            if code not in self.listOfNames:
                self.listOfNames[code] = [name]
            else:
                self.listOfNames[code].append(name)

    # Returns an alphanumeric code for the specified name
    def getNameCode(self, name: str) -> int:
        total = 0
        for c in name:
            if ord(c) != 32:  # Ignores spaces
                total += (ord(c) - 96)
        return total

    # Prints the alphanumeric code followed by a list of names with this code
    def printReport(self):
        for k in self.listOfNames.keys():
            print(str(k) + ": " + str(self.listOfNames[k]))

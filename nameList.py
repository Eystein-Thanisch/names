import random


class NameList:

    # Will store full names by alphanumeric code
    listOfNames: "dict[int, list[str]]" = {}

    def __init__(self):

        self.listOfNames = {}

    def set_sample(self):

        self.listOfNames = {}    

        # Gets list of first names from file
        firstNames: list[str] = list()
        with open("first-names.txt") as f:
            lines = f.readlines()
        for name in lines:
            firstNames.append(name[:-1].lower())

        # Gets list of surnames from file
        lastNames: list[str] = list()
        with open("last-names.txt") as f:
            lines = f.readlines()
        for name in lines:
            lastNames.append(name[:-1].lower())

        # Produces 100 names by combining a random first name with a random surname
        while len(self.listOfNames) < 101:
            randFirstName = firstNames[random.randrange(len(firstNames))]
            randLastName = lastNames[random.randrange(len(lastNames))]
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

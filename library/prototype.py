
class Prototype(object)  :

    def __init__(self, records):
        self.records = records

    def getRecords(self) :
        return self.records;

    def getAttributes(self):
        print "Prototype.getAttributes()"
        raise NotImplementedError("Should implemented getAttributes().")

    def getCollections(self):
        print "Prototype.getCollections()"
        raise NotImplementedError("Should implement getCollections().")

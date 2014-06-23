import clr
clr.AddReference("System.Xml")
clr.AddReference("System.Xml.Linq")
clr.AddReference("System.Core")

import System
clr.ImportExtensions(System.Linq)
clr.ImportExtensions(System.Xml.XPath)

import copy
from library.xmlParser import XmlParser

class ProcessResult(object) :
    """ Processing output """
    pass

class Expando(object) :
    """
    Simple dynamic object, we can extend propery dynamically.
    """
    pass

class PrototypeProcessor(object) :
    """ Prototype processor """

    def __init__(self, prototype) :
        """ Initialize variable """
        self.parser = XmlParser()
        self.records = prototype.getRecords()
        self.attributes = prototype.getAttributes()
        self.collections = prototype.getCollections()

    def process(self):
        rs = ProcessResult()

        records = self.records
        record = records.ElementAt(0)

        attributes = self.attributes
        collections = self.collections

        newAtts = self.parseAttributes(attributes, record)
        newColls = self.parseCollections(collections, records)

        rs.attributes = newAtts
        rs.collections = newColls
        return rs

    def parseAttributes(self, attributes , record):
        atts = copy.deepcopy(attributes)
        self.parser.parseAttributes(atts, record)
        return atts

    def parseCollections(self, collections, records):
        colls = copy.deepcopy(collections)
        self.parser.parseCollections(colls, records)
        return colls

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

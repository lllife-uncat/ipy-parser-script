from library.xmlParser import XmlParser
from library.models import ProcessResult
import copy

import System
import clr
#clr.AddReference("System.Xml")
#clr.ImportExtensions(System.Xml.XPath)

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
        record = self.records[0]

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

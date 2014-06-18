import clr
clr.AddReference("System.Xml")
clr.AddReference("System.Xml.Linq")
clr.AddReference("System.Core")

import System
clr.ImportExtensions(System.Linq)
clr.ImportExtensions(System.Xml.XPath)

from library.xmlParser import XmlParser

class Expendo(object) :
    """
    Simple dynamic object, we can extend propery dynamically.
    """
    pass

class Template() :
    """
    Template prototype for all document in system.
    @attribute {Expendo} attributes - List of simple type.
    @attribute {Expendo} collections - List of complex type to generate as table.
    @attribute {Expendo} images - List of image in template.
    @attribute {String} fileName - File name in ECM.
    @attribute {String} path - Path in ECM.
    @attribute {Exepndo} properties - List of ECM property.
    """

    def __init__(self):
        """
        Intilize class attributes.
        """
        self.attributes = Expendo()
        self.collections = Expendo()
        self.images = Expendo()
        self.fileName = ""
        self.path = ""
        self.properties = Expendo()


class Prototype() :
    def __init__(self, records) :
        self.attributes = Expendo()
        self.collections = Expendo()
        self.images = Expendo()

        self.defineAttributes()
        self.defineCollections()

        record = records.ElementAt(0)
        parser = XmlParser()
        parser.parseAttributes(self.attributes, record)
        parser.parseCollections(self.collections, records)

    def defineAttributes(self) :
        atts = self.attributes
        atts.A001 = "policy_holder_1"
        atts.A002 = "policy_holder_2"
        atts.A003 = "address1"
        atts.A004 = "address2"
        atts.A005 = "address3"
        atts.A006 = "district"
        atts.A007 = "province"
        atts.A008 = "postalcode"
        atts.A009 = "letter_number"

    def defineCollections(self):
        colls = self.collections
        colls.C001 = {
            "A001": "policy_holder_1",
            "A002": "policy_holder_2",
            "A003": "address1",
            "A004": "address2",
            "A005": "address3",
            "A006": "district",
            "A007": "province",
            "A008": "postalcode",
            "A009": "letter_number"
        }

    def getAttributes(self) :
        atts = self.attributes
        return atts

    def getCollections(self) :
        colls = self.collections
        return colls

    def getPath(self):
        return ""

    def getFileName(self) :
        return ""

    def getImages(self):
        imgs = self.images
        return imgs

class TestPrototype(Prototype) :
    def __init__(self, element) :
        Prototype.__init__(self, element)



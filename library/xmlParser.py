# Import .net clr module.
import clr
clr.AddReference("System.Core")

# Import .Net extension method from System.Xml.Xpath,
# for 'XPathSelectElement'.
import System
clr.ImportExtensions(System.Xml.XPath)

# Import expando prototype from models.
from library.models import Expando

class XmlParser() :
    """
    Class XmlParser - Parse input xml.
    """

    def __init__(self) :
        """
        Default constructor.
        """
        pass

    def parseAttributes(self, attributeDef, element) :
        """
        Use extension method from XPath to extract value.
            attributeDef - Expando object represent all attribute in template.
            element - XElement object.

        return update version of attributeRef.
        """

        atts = [x for x in attributeDef.__dict__]
        values = [x for x in attributeDef.__dict__.values()]
        for idx, att in enumerate(atts) :
            value = values[idx]
            #xmlValue = element.XPathEvaluate("/" + value)
            xmlValue = element.XPathSelectElement("/" + value).Value
            setattr(attributeDef, att, xmlValue)

        # return update version of attributeDef.
        return attributeDef

    def parseCollections(self, collectionDef, records) :
        """
        Extract collection from record section.
            colletionRef - Collection definition.
            records - Record section.

        return {Expando} - Update version of collectionDef.
        """
        collNames= [x for x in collectionDef.__dict__]
        collValues = [x for x in collectionDef.__dict__.values()]
        for collNameIndex, collName in enumerate(collNames):
            collValue = collValues[collNameIndex]
            newCollValue = []
            for record in records :
                attNames = [x for x in collValue.keys()]
                attValues= [x for x in collValue.values()]
                for idx, attName in enumerate(attNames) :
                    item = Expando()
                    value = attValues[idx]
                    xmlValue = record.XPathSelectElement("/" + value).Value
                    setattr(item, attName, xmlValue)
                    newCollValue.append(item)
            setattr(collectionDef, collName, newCollValue)

        return collectionDef

    def parseFileName(self, fileNameDef) :
        pass

    def parsePath(self, pathDef) :
        pass

    def parseProperty(self, propertyDef) :
        pass

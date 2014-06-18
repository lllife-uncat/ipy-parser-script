import clr

clr.AddReference("System.Core")

import System
clr.ImportExtensions(System.Xml.XPath)

class Expando(object) :
    pass

class XmlParser() :
    """
    Class XmlParser - Parse input xml update input definition.
    @attribute {XElement} element - Element cantain of definition of xml in record section.
    """

    def __init__(self) :
        """
        Default constructor.
        @parameter {XElement}  element
        """
        pass

    def parseAttributes(self, attributeDef, element) :
        """
        Use extension method from XPath to extract value.
        @para{Expendo} attributeDef - Expendo object represent all attribute in template.
        @return {Expendo} - An update version of attributeRef.
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
        @param {Expando} colletionRef - Collection definition.
        @param {XElement} records - Record section.
        @return {Expando} - Update version of collectionDef
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

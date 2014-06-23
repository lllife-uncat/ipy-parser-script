# -*- coding: utf-8 -*-

import clr
clr.AddReference("System.Xml")
clr.AddReference("System.Xml.Linq")
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Core")

import System
clr.ImportExtensions(System.Linq)

from System.Xml import XmlDocument
from System import String
from System.Globalization import CultureInfo
from System import DateTime

clr.AddReference("Newtonsoft.Json.dll")
clr.AddReference("MongoDB.Bson.dll")
clr.AddReference("MongoDB.Driver.dll")
clr.AddReference("Editor.exe")

from Newtonsoft.Json import Formatting
from Newtonsoft.Json.Linq import JObject, JValue, JArray
from Generator.Models.Template import XParser
from System.IO import File
from Generator.Editor import PropertyEditor
from Newtonsoft.Json import JsonConvert
from MongoDB.Bson.Serialization import *
from MongoDB.Bson import *

import sys
sys.path.append(r"E:\runtime\generator.env\Template.OLI_Template\Item.Script")

from template.testPrototype import TestPrototype
from template.prototype import PrototypeProcessor


class ParsingManager() :
    """
    class Parser - Parse input xml as json object.
    Extract each property by name.
    """

    def __init__(self) :
        """
        Set editor config.
        """
        pass

    def assignAttributes(self, item, attrs) :
        names = [x for x in attrs.__dict__]
        values = [x for x in attrs.__dict__.values()]

        for idx, name in enumerate(names) :
            value = values[idx]
            setattr(item, name, value)

    def assignCollections(self, item, colls) :
        collNames = [x for x in colls.__dict__]
        collValues = [x for x in colls.__dict__.values()]
        for idx, coll in enumerate(collNames) :
            value = collValues[idx]
            item.Collections[coll] = value

    def extractElements(self, inputXml, tag) :
        elements = XParser.XMLToXElements(inputXml, tag)
        return elements

    def extractFirstElement(self, inputXml, tag) :
        return self.extractElements(inputXml, tag).ElementAt(0);

    def extractRecords(self, itemElement) :
        records = self.extractElements(itemElement.ToString(), "record")
        return records

    def start(self, inputXml) :
        """
        Start parsing xml.
        - Extract type, batch, process, location, batchno and elixirid for future reference.
        - Use sax parser to extract items.
        - Walk over item and extract attribute and collection.

        @parameter {String} InputXml - Xml from C# application.
        @return {List} - List of item extract from script.

        """

        typeElement = self.extractFirstElement(inputXml, "type")
        batch = self.extractFirstElement(inputXml, "batch")

        process = typeElement.Element("process")
        location = typeElement.Element("location")

        batchno = batch.Element("batchno")
        elixirid = batch.Element("elixirid")

        # use sax parser to extract each item.
        items = self.extractElements(inputXml, "item")
        results = []

        # walk over
        for element in items :

            item = Item()
            item.Collections = {}

            templateId = element.Element("templateid").Value
            records = self.extractRecords(element)

            if templateId == "UWLD001" :
                prototype = TestPrototype(records)
                processor = PrototypeProcessor(prototype)
                rs = processor.process()

                # extract attributes
                atts = rs.attributes
                self.assignAttributes(item, atts)

                # extract Collections
                colls = rs.collections
                self.assignCollections(item, colls)

            results.append(item)

        # return result to caller.
        return results

class Item(object) :
    """
    class Item - Store data from xml as property | collection.
    No predefined property, it free to extension. """

    def __init__(self) : pass

class Extractor :
    """
    class Extractor - Extract xml string as collection if item.
    Each item contain property and collection.
    Number of property and collection is dynamic up to configuration in script editor.

    All naming in class is c# convention. """

    def __init__(self) :
        pass

    def Extracts(self, inputXML) :
        """
        Start extract files.
        """
        parser = ParsingManager()
        items = parser.start(inputXML)
        return items

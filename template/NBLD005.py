from library.models import Expando
from library.prototype import Prototype

class NBLD005(Prototype) :

    def __init__(self, records) :
        #super(TestPrototype, self).__init__(records)
        Prototype.__init__(self, records)

    def getAttributes(self) :
        atts = Expando()
        atts.A001 = "policy_holder_1"
        atts.A002 = "policy_holder_2"
        atts.A003 = "address1"
        atts.A004 = "address2"
        atts.A005 = "address3"
        atts.A006 = "district"
        atts.A007 = "province"
        atts.A008 = "postalcode"
        atts.A009 = "letter_number"
        return atts

    def getCollections(self):
        colls = Expando()
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
        return colls

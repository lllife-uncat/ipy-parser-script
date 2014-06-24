import logging
logging.basicConfig(level = logging.INFO)

class TemplateLoader(object) :
    def __init__(self) :
        pass

    @staticmethod
    def load(name) :
        """ Load class by specific name.
        class have to locate in <Name>.py under 'template' directory.

        Example:
            > template/TestTemplate.py
            > template/D001.py
        """

        logging.info("load template: " + name);

        mod = __import__("template.{0}".format(name) , fromlist= [name])
        Template = getattr(mod, name)
        return Template


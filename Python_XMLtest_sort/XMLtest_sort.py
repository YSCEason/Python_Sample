import xml.etree.ElementTree as ET
import xml.dom.minidom

tree = ET.parse("data.xml")

def getkey(elem):
    return elem.findtext("number")

container = tree.find("entries")

container[:] = sorted(container, key=getkey)

tree.write("new-data.xml")



#xml = xml.dom.minidom.parse("new-data.xml") # or xml.dom.minidom.parseString(xml_string)
#pretty_xml_as_string = xml.toprettyxml()

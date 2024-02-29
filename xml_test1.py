import xml.etree.ElementTree as ET


def generateXML(filename):
    root = ET.Element('Catalog')

    m1 = ET.Element('mobile')
    root.append(m1)

    b1 = ET.SubElement(m1, 'brand')
    b1.text = 'Apple'
    b2 = ET.SubElement(m1, 'price')
    b2.text = '6999'

    m2 = ET.Element('mobile')
    root.append(m2)

    b3 = ET.SubElement(m2, 'brand')
    b3.text = 'Samsung'
    b4 = ET.SubElement(m2, 'price')
    b4.text = '5999'

    tree = ET.ElementTree(root)
    with open(filename, 'wb') as f:
        tree.write(f)

# <Catalog>
#     <mobile>
#         <brand>Apple</brand>
#         <price>6999</price>
#     </mobile>
#     <mobile>
#         <brand>Samsung</brand>
#         <price>5999</price>
#     </mobile>
# </Catalog>

generateXML('Catalog.xml')

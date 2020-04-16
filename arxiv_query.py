import urllib.request
import xml.etree.ElementTree as ET

url = 'http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=10'
data = urllib.request.urlopen(url).read()
root = ET.fromstring(data)

print(root.tag)
print(root.attrib)

for child in root:
    print("    " + str(child.text))
    print("    " + str(child.tag) + " " + str(child.attrib))
    
    for child_2 in child:
        print("        " + str(child_2.text))
        print("        " + str(child_2.tag) + " " + str(child_2.attrib))

        for child_3 in child_2:
            print("            " + str(child_3.text))
            print("            " + str(child_3.tag) + " " + str(child_3.attrib))


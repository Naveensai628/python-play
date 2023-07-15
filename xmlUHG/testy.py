import xml.etree.ElementTree as ET


tree = ET.parse('test.xml')
root = tree.getroot()

def getElements(a):
    for tag in root.iter('segment'):
        print('loop')
        ex_ids = set()
        for dat in tag.findall('data'):
            ex_ids.add(int(dat.attrib['id']))
            
        print(ex_ids)
        max_existing_id = max(ex_ids)
        missing_ids = set(range(1, max_existing_id + 1)).difference(ex_ids)
        print(missing_ids)
        for missing_id in sorted(missing_ids):
            if(len(str(missing_id))==1):
                new_data = ET.SubElement(tag, 'data', {'id': '0'+str(missing_id)})
            else:
                new_data = ET.SubElement(tag, 'data', {'id': str(missing_id)})
        

getElements(root)
tree.write('output.xml')


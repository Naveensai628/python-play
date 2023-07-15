import xml.etree.ElementTree as ET

tree = ET.parse('test.xml')
root = tree.getroot()

def insert_missing_ids():
    for segment in root.iter('segment'):
        ex_ids = set()
        for data in segment.findall('data'):
            ex_ids.add(int(data.attrib['id'])) #clear

        max_existing_id = max(ex_ids)
        missing_ids = set(range(1, max_existing_id + 1)).difference(ex_ids) #clear


        for missing_id in sorted(missing_ids):      #Revisit
            data_elements = segment.findall('data')
            insert_index = 0
            for i, data in enumerate(data_elements):
                if int(data.attrib['id']) > missing_id:
                    insert_index = i
                    break


            if len(str(missing_id)) == 1:   #clear
                new_data = ET.Element('data', {'id': '0' + str(missing_id)})
            else:
                new_data = ET.Element('data', {'id': str(missing_id)})

            segment.insert(insert_index, new_data)
            new_data.tail = '\n        '

insert_missing_ids()
tree.write('output.xml', encoding='UTF-8', xml_declaration=True)
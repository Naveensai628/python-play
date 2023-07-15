import xml.etree.ElementTree as ET
# Load the XML file
tree = ET.parse('test.xml')
root = tree.getroot()

# # Traverse the XML and add missing IDs to the data tags
# for loop in root.findall('loop'):
#     existing_ids = set()
#     for segment in loop.findall('segment'):
#         for data in segment.findall('data'):
#             existing_ids.add(int(data.attrib['id']))
#     print(existing_ids)
#     max_existing_id = max(existing_ids)
#     missing_ids = set(range(1, max_existing_id + 1)).difference(existing_ids)
#     print(missing_ids)
#     for segment in loop.findall('segment'):
#         for missing_id in sorted(missing_ids):
#             new_data = ET.SubElement(segment, 'data', {'id': str(missing_id), 'type': 'S', 'map': ''})
#             print(ET.SubElement(segment, 'data', {'id': str(missing_id), 'type': 'S', 'map': ''}))

# Traverse the XML and add missing IDs to the data tags
for loop in root.findall('.//loop'):
    existing_ids = set()
    for segment in loop.findall('.//segment'):
        for data in segment.findall('data'):
            existing_ids.add(int(data.attrib['id']))

    max_existing_id = max(existing_ids)
    missing_ids = set(range(1, max_existing_id + 1)).difference(existing_ids)

    for segment in loop.findall('.//segment'):
        for missing_id in sorted(missing_ids):
            new_data = ET.SubElement(segment, 'data', {'id': str(missing_id)})

# Save the modified XML
tree.write('output.xml')
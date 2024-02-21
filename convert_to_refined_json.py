import json


with open('./refinedJson/input.json', 'r') as json_file:
    data = json.load(json_file)


filtered_data = []
for item in data:

    for key in ['canUnlink', 'displayName', 'calculationMethod', 'calculationInt', 'masteryPoints', 'canEdit', 'canArchive']:
        item['node'].pop(key, None)
    item['node'].pop('friendlyDescription', None)

    filtered_data.append(item)

with open('./refinedJson/output.json', 'w') as json_file:
    json.dump(filtered_data, json_file, indent=2)


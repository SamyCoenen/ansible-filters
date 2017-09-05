#!/usr/bin/python

DOCUMENTATION = '''
---
module: esrally_csv_to_json

version_added: "2.2"

short_description: Converts the resulting csv from the esrally benchmarking tool
to a JSON-formatted document.

author:
    - "Samy Coenen (Contact@samycoenen.be)"

'''

from ansible.errors import AnsibleError
import json
import collections

# Recursively loop through a dictionary to look for a key, if it's not found it
# gets added. Else this new key:value get's inserted into another
# key:$(key:value)
def update_dict(source_dict, update):
    for key, value in update.iteritems():
        if isinstance(value, collections.Mapping):
            r = update_dict(source_dict.get(key, {}), value)
            source_dict[key] = r
        else:
            source_dict[key] = update[key]
    return source_dict

def convert(result_csv):
    result = []
    headers = ["Lap", "Metric", "Operation", "Value", "Unit"]
    json_data = {}

    # get array from csv without the headers
    for line in result_csv[1:]:
        complete_line = line.split(',')
        result.append(complete_line)

    # create new dict from list
    for line in result:
        new_dict = {}
        operation = {}
        try:
            value = float(line[3])
        except ValueError:
            value = 0
        metric = {
            "%s in %s" % (line[1], line[4]): value
        }
        operation[line[2]] = metric
        new_dict[line[0]] = operation
        json_data = update_dict(json_data, new_dict)
    return json.dumps(json_data)

class FilterModule(object):
    def filters(self):
        return {
            'esrally_csv_to_json': convert
        }

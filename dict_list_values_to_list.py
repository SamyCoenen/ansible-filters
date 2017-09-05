#!/usr/bin/python

DOCUMENTATION = '''
---
module: stdout_to_average

version_added: "2.2"

short_description: Returns list from defined keys in dict

author:
    - "Samy Coenen (contact@samycoenen.be)"

'''

from ansible.errors import AnsibleError

def get_list(key, dict_list):
    value_list = []
    for dict in dict_list:
        value_list.append(dict.get(key))
    return value_list
class FilterModule(object):
    def filters(self):
        return {
            'dict_list_values_to_list': get_list
        }

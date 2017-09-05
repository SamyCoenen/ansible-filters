#!/usr/bin/python

# Example usage:
# keys:
#   - key1
#   - key2
# values:
#   - value1
#   - value2
# users_dict: "{{ keys | lists_to_dict(values) }}"
#
# Result is:
# users_dict:
#   - { key1 : value1 }
#   - { key2 : value2 }

DOCUMENTATION = '''
---
module: lists_to_dict

version_added: "2.2"

short_description: Returns dict from two lists

author:
    - "Samy Coenen (contact@samycoenen.be)"

'''

from ansible.errors import AnsibleError

def lists_to_dict(keys_list, values_list):
    if len(keys_list) is not len(values_list):
        raise AnsibleError('You need to give equal length lists')
    return dict(zip(keys_list, values_list))

class FilterModule(object):
    def filters(self):
        return {
            'liststodict': lists_to_dict,
            'lists_to_dict': lists_to_dict
        }

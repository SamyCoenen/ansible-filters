#!/usr/bin/python

DOCUMENTATION = '''
---
module: stdout_to_average

version_added: "2.2"

short_description: Returns average from stdout list

author:
    - "Samy Coenen (contact@samycoenen.be)"

'''

from ansible.errors import AnsibleError

def list_average(result_list):
    sum = 0
    for result in result_list:
        sum += float(result['stdout'])
    average = sum / len(result_list)
    return average
class FilterModule(object):
    def filters(self):
        return {
            'stdout_to_average': list_average
        }

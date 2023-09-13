import re

################################################
###   Serialization to JSON

TAB = '\t'

def to_json(obj, level=0):
    '''Serializes the given object to JSON, printing to the console as it goes.'''

    if level == 0:
        print("{")

    # alphabetize to match the sample output
    obj = dict( sorted(obj.__dict__.items()) )

    level += 1
    last_field = len(obj.items()) - 1

    for i, (field, value) in enumerate(obj.items()):
        
        # if the value is an object (recurse)
        if hasattr(value, '__dict__'):
            print(f"{TAB * level}\"{field}\": {{")
            to_json(value, level=level)
            
            # ending curly brace
            if i == last_field:
                print(f"{TAB * (level)}}}")
            else:
                print(f"{TAB * (level)}}},")
                
        
        # print individual fields with "handler functions"
        else:
            valType = value.__class__.__qualname__.lower()
            handleVal = globals().get(f"to_json_{valType}")            
            
            if i == last_field:
                print(f"{TAB * level}\"{field}\": {handleVal(value)}")
            else:
                print(f"{TAB * level}\"{field}\": {handleVal(value)},")

    # final ending curly brace
    if level == 1:
        print(f"{TAB * (level-1)}}}", end='')

    return ''
    

#
#  handler functions
#
def to_json_int(intVal):
    return f"{intVal}"

def to_json_float(floatVal):
    return f"{floatVal}"

def to_json_bool(boolVal):
    return "true" if boolVal else "false"

def to_json_str(strVal):
    strVal = re.sub(r'\\', r'\\\\', strVal)
    strVal = re.sub(r'"', r'\"', strVal)
    return f"\"{strVal}\""

def to_json_nonetype(noneVal):
    return "null"
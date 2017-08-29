def string_to_camel(str):
        import re
        return ''.join(x.capitalize() or '_' for x in str.split('_'))

print(string_to_camel('prog_python'))

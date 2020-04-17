def get_type_for_key_path(schema: dict, key_path: str) -> str: 
    # TODO implement me
    key_path_str_split = key_path.split('.') #split string into list with the dot delimiter
    key_path_str_length = len(key_path_str_split) # get length of string key_path
    
    try:
        if key_path_str_length==1:
             return schema['properties'][key_path_str_split[key_path_str_length-1]]['type']
        elif key_path_str_length==2:
             return schema['definitions']['EmploymentInformation']['properties'][key_path_str_split[key_path_str_length-1]]['type']
        elif key_path_str_length==3 and (key_path_str_split[key_path_str_length-2] in schema['definitions']['EmploymentInformation']['properties']): 
             return schema['definitions']['DependantInformation']['properties'][key_path_str_split[key_path_str_length-1]]['type']
        else:
            return None
            
    except KeyError:
             return None
   

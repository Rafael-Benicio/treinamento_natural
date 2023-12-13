dict_1={'key1': 1, 'key2': 3, 'key3': 2} 
dict_2={'key1': 1, 'key2': 2}

for key in dict_2:
     if key in dict_1 and dict_1[key]==dict_2[key]:
          print(f'{key} : {dict_2[key]} está presente  em  dict_1 e dict_2')
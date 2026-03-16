my_dict = {"key1": "value1", "key2": "value2"}

test_if_key_exists = my_dict.get("key1")

print(test_if_key_exists)   #this will return a None if key does not exist, or return its value if it DOES

if test_if_key_exists == None:
    #continue {for example we may skip this iteration of the dictionary for SoftUni tasks(exam TIP)!
    pass
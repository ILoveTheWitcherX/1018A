#context manager
with open("mydefaults.ini.txt") as ini_file:
    data =ini_file.read()

lines =data.split("\n") #processes each line at a time
key_value_ini_dictionary = dict()
#print(len(lines))
for line in lines:
    if "=" in line:
      fields =line.split("=")
      print(len(fields))
      key_value_ini_dictionary[fields[0]] = fields[1]
print(key_value_ini_dictionary)

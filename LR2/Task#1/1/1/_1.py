my_file = open('text.txt','r')  #Open file in readonly mode

#print(my_file.read())   #Printing all symbols
my_string = my_file.read()
my_string = my_string.lower() #lower reg
setted_string = set(my_string)
#TODO: ignore/delete symbols


"""
for i in range(len(my_string)):
    counter = 0
    temp = my_string[i]
    for j in range(len(my_string)):
"""

        

my_file.close()
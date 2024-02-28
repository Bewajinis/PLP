my_list = []
# trying to append (10, 20, 30, 40)
# my_list.append(10)
# # it only takes one argument at atime which means i will have to append 4 times to get all the elements in the list
# my_list.append(20)
# my_list.append(30)
# my_list.append(40)

# however, this syntax here pass all the 4 elements in one argument.
my_list +=(10,20,30,40)
print (my_list)

# insert the value 15 at the second position in the list.
my_list[1] = 15
print (my_list)

# extend my_list with another list [50, 60, 70].
my_list.extend([50,60,70])
print(my_list)

# remove the last element from my_list
del my_list[-1]
print(my_list)

# sort my_list in ascending order
my_list.sort()
print(my_list)

# find and print the index of the value 30 in my_list
lastquestion = my_list[2]
print(lastquestion)
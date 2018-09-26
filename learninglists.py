my_list = [1,2,3]
print (my_list)
print (my_list[0])
print (my_list[1])
print (my_list[2])
#########################################################
print ('Appending to the lists')

my_list.append("four")

print(my_list)

######################################################

print ('Deleting List Elements')

del my_list[2]
print (my_list)

#######################################################

print ('Learning nested List')

nest_list= []
nest_list.append (123)
nest_list.append (22)
nest_list.append ('ntp')
nest_list.append ('ssh')

my_list.append(nest_list)

print (my_list)

#######################################################

print ('Manipulating Lists')
print(my_list[3])
print (my_list[3][2])

#print (my_list[0][1])

print (my_list[2][1])

###########################################################

print ('Slicing')

sliced = my_list[1:3]

print (sliced)

#############################################################

slice_me = "ip address"
sliced  = slice_me[:2]
print (sliced)

#############################################################

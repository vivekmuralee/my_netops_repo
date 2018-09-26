my_dictionary = {}
my_dictionary["GigE0"] = "Link to ISP"
my_dictionary["GigE1"] = "DNS is the root of all problems"
my_dictionary["GigE2"] = "An IPv4 Address walks into the bar and yells,'Bartender'"
my_dictionary["GigE3"] = "You know the thing  about NTP jokes"
print (my_dictionary)

print (my_dictionary["GigE0"])

my_list = [3,2,1]
my_other_dictionary = {}
my_other_dictionary["thisisakey"] = "thisisavalue"

my_dictionary["nested_list"] = my_list
my_dictionary["nested_dict"] = my_other_dictionary

print (my_dictionary)

print (my_dictionary["nested_dict"]["thisisakey"])

my_integer = 443
if my_integer > 0 :
    print ("Hey, that looks like a positive number!")

my_integer = -443
if my_integer > 0 :
    print ("Hey, that looks like a positive number!")

my_string = 'you call that a string ? and there is a colon :'
if "?" in my_string:
    print ("Yep, there is a ? in the string")
if ":" in my_string:
    print ("Yep, there is a : in the string")


my_string = 'you call that a string ? and there is a colon :'
if "?" in my_string:
    print ("Yep, there is a ? in the string")
elif ":" in my_string:
    print ("Yep, there is a : in the string")
elif "string" in my_string:
    print ("Yep there is a string in the sentence")
else:
    print (" whoa, we got a catch all now")

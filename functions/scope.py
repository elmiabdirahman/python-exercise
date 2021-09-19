### local varibles
##def greet():
#    if True:
#        message = "a"
#    print(message)


#print(greet())

## globle varible
message = "a"
def greet():
    message = "b"
    print(message)


greet()
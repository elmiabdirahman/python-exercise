# mutable can be change
##x = 1
# print(id(x))

##x = x + 1
# print(id(x))

# immutable can't be changed
x = [1, 2, 3]
print(id(x))

x.append(4)
print(id(x))

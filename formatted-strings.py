first = "Tom"
last = "Ali"
full = f"{len(first)} {2 + 2}"
print(full)

## usefull string methods
course = "  Python Programming"
print(course.upper())
print(course.lower())
print(course.title())

print(course.strip())

print(course.find("Pro"))
print(course.replace("P", "__"))
print("Programming" not in course)
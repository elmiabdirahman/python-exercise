def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("welcome aboard")


greet("Elmi", "Elmi")
greet("Ali", "Ahmen")

### Arguments- Xargs
def multiply(*list):
    total = 1
    for number in list:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

### Arguments- xxargs
def save_user(**user):
    print(user["id"], user["name"])


save_user(id=1, name="admin")
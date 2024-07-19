def give_hello_world():
    return "Hello, World!"

res = give_hello_world()
print(res)

def say_hello(name):
    hello_string = "Hello, " + name
    return hello_string

res = say_hello("Lorenzo")
print(res)

def say_hello_to(name1, name2):
    hello_string = f"Hello, {name1} & {name2}!"
    return hello_string

res = say_hello_to("Benny","Lorenzo")
print(res)
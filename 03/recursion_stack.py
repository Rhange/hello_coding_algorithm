def greet(name):    # 1
    print(f"hello, {name}!")    # 2
    greet2(name)    # 3
    print("getting ready to say bye...")    # 4
    bye()   # 5


def greet2(name):
    print(f"how are you, {name}?")


def bye():
    print("ok bye!")


greet("Jinsu")

"""
Call stack

# 1
|| greet | name: "Jinsu" ||

# 2
|| greet | name: "Jinsu" ||

# 3
|| greet2 | name: "Jinsu" ||
|| greet | name: "Jinsu" ||

# 4
|| greet | name: "Jinsu" ||

# 5
|| bye ||
|| greet | name: "Jinsu" ||

# Exit1
|| greet | name: "Jinsu" ||

# Exit2
"""
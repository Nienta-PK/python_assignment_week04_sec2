
def reverse_string(x):
    return x[::-1]
def capitalize_string(x):
    return x.title()
def lowercase_string(x):
    return x.lower()
def uppercase_string(x):
    return x.upper()

if __name__ == "__main__":  
    print(reverse_string("hello"))
    print(capitalize_string("hello"))
    print(lowercase_string("HELlo World"))
    print(uppercase_string("HELlo World"))
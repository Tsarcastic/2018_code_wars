"""https://www.codewars.com/kata/57f8ff867a28db569e000c4a/train/python ."""

def kebabize(string):
    """Turn from camel case into kebab case."""
    kebab = ""
    
    for i in string:
        if i.isdigit():
            pass
        elif kebab == "":
            kebab += i.lower()
        elif i.isupper():
            kebab += "-"
            kebab += i.lower()
        elif i.islower():
            kebab += i.lower()

    return kebab

"""https://www.codewars.com/kata/586538146b56991861000293/train/python ."""
import string

def to_nato(words):
    nato_dictionary = {'A':'Alfa', 'B':'Bravo','C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf',"H":"Hotel", 'I':'India', 'J':'Juliett', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'Xray', 'Y':'Yankee', 'Z':'Zulu'}

    translated = []

    for letter in words:
        if letter.upper() in nato_dictionary:
            translated.append(nato_dictionary[letter.upper()])
        elif letter in string.punctuation:
            translated.append(letter)

    return " ".join(translated)


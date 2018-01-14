def to_camel_case(text):
"""
    Complete the method/function so that it converts dash/underscore delimited words into camel casing.
    The first word within the output should be capitalized only if the original word was capitalized.

    Examples:

        to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

        to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"

        to_camel_case('') # returns ''

        to_camel_case('A-B-C') # returns Abc

        to_camel_case('The-pippi-was_Hungry') # returns ThePippiWasHungry

    :param text: a word [str]

    :return: camel case of the word [str]

"""
    len_text = len(text)

    #print("length = " + str(len_text))

    i = 0
    new_list = []

    while i < len_text:
        #print("i = " + str(i))
        if i==0:
            new_list.append(text[0])
        elif text[i] in ['-','_']:
            if text[i+1].islower():
                new_list.append(text[i+1].upper())
            else:
               new_list.append(text[i+1])
            i += 1
        else:
            new_list.append(text[i])
        i += 1
    return new_list                          
###################

string = to_camel_case("the-stealth-warrior")
print(string)

string = to_camel_case("The_Stealth_Warrior")
print(string)
 
string = to_camel_case('')
print(string)

string = to_camel_case("A-B-C")
print(string)

string = to_camel_case("The-pippi-was_Hungry")
print(string)

====================================================

 

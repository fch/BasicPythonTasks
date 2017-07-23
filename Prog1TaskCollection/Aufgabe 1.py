# @Date:   18-Jul-2017
# @Email:  Alexander.Komischke@gmx.de
# @Last modified time: 18-Jul-2017

# Aufgabe 1 : four_sorted_digits

sequence = "0123456789"

def four_sorted_digits(text: str) -> bool:

    if len(text) < 4:
        return False
    highest_counter = 0
    counter = 0
    last_letter = ''
    for Letter in text :
        if Letter in sequence :
            if Letter < last_letter :
                counter++
            else :
                if counter > highest_counter :
                    highest_counter = counter

                counter = 0
        last_letter = Letter
    if highest_counter >= 4 :
        return True
    else :
        return False


#Test
print("abcd , " + str(four_sorted_digits("abcd")))
print("bcda , " + str(four_sorted_digits("bcda")))
print(" , " + str(four_sorted_digits("")))
print("1234 , " + str(four_sorted_digits("1234")))
print("1434 , " + str(four_sorted_digits("1234")))

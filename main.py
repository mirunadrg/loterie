import random
#creeaza o lista cu toate numerele
def toate_numerele():
    toate_numerele = list (range(49))
    #alege numerele si fa un for pentru a alege 6 numere aleatoriu
    numerele_alese = []
    for i in range(6):
      calculators_choice = random.choice(toate_numerele)
      numerele_alese.append(calculators_choice)
    return numerele_alese

def user_choice():
    user_choice = []
    for char in range(6):
        input_message = "Ghiceste numarul  " +  str(char + 1) + ": "
        user_input = input(input_message)
        number = int(user_input)
        user_choice.append(number)
    return user_choice

def check_correct_numbers(all_numbers, user_picked_numbers):
    for number in user_picked_numbers:
        if number in all_numbers:
            print("Ai ghicit numarul : " + str(number))
    print("Toate numerele erau: " + str(all_numbers) )


    


    

all_numbers = toate_numerele()
user_picked_numbers = user_choice()
check_correct_numbers(all_numbers, user_picked_numbers)

fail_guess = 0


import random
word_list = ['wakacje', 'plaża', 'telefon', 'komputer', 'telewizor', 'łazienka']

def word_los(word_list):
    word = random.choice(word_list)

    return word





def display(word):
    word_guess = ["_"] * len(word)
    print(word_guess)
    return(word_guess)

def spr(word, word_guess, word_2):
    fail_guess = 0
    while fail_guess < 10:
        word1=""
        user_guess = str(input("Podaj litere: ")).upper()
        if user_guess in word:
            print("Bardzo dobrze!")
            pozytion = []
            for i in range(len(word)):
                if word[i] == user_guess:
                    pozytion.append(i)
            for i in pozytion:
                word_guess[i] = word[i]
            print(word_guess)
        else:
            print("Spróbuj jeszcze raz")
            fail_guess += 1
            print(word_guess)
            print(f"Nie ma {user_guess} w szukanym słowie. Pozostało Ci {10-fail_guess} prób")
        if word == word_guess:
            print("Wspaniale odgadłeś haslo, ")
            print("".join(word_guess))
            break
        answer = str(input("Czy chcesz odgadnąć hasło [T/N]: ")).upper()
        if answer == "T":
            word1 = input('Podaj hasło: ').upper()

            if word1 == word_2:
                print("Wspaniale odgadłeś haslo, ")
                print("".join(word))
                break
            else:
                fail_guess += 1
                print(f"{word1} nie jest szukanym słowiem. Pozostało Ci {10 - fail_guess} prób")

                print(word_guess)



def main():
    word = word_los(word_list).upper()
    word_2 = word
    word = list(word)
    word_guess = display(word)
    spr(word, word_guess, word_2)


main()
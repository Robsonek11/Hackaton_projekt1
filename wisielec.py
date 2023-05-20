fail_guess = 0


import random
word_list = ['wakacje', 'plaża', 'telefon', 'komputer', 'telewizor', 'łazienka']

def word_los(word_list):
    word = random.choice(word_list)
    return word





def wys(word):
    word_guess = ["_"] * len(word)
    print(word_guess)
    return(word_guess)

def spr(word, word_guess):
    fail_guess = 0
    while fail_guess < 10:
        user_guess = str(input("Podaj litere: ")).upper()
        if user_guess in word:
            print("Bardzo dobrze!")
            pozycja = []
            for i in range(len(word)):
                if word[i] == user_guess:
                    pozycja.append(i)
            for i in pozycja:
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
def main():
    word = word_los(word_list).upper()
    word = list(word)
    word_guess = wys(word)
    spr(word, word_guess)


main()
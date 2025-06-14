from string import ascii_letters
from Phoneascii_sim import unlock
test_letters = "ABZQ"

for i in test_letters:
    for j in test_letters:
        for k in test_letters:
            for l in test_letters:
                guess = i + j + k + l
                print (f"Trying:{guess}")
                if unlock(guess):
                    print (f"Password Found: {guess}")
                    exit()

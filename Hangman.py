import random
import string

print("H A N G M A N")

words = 'python', 'java', 'kotlin', 'javascript'
choice = ""

while choice != "exit":
    choice = input('Type "play" to play the game, "exit" to quit:')
    if(choice == "play"):
        guessing_word = random.choice(words)
        guessed_chars = set()
        i = 0
        cur_word = '-' * len(guessing_word)

        while True:
            if i == 8:
                print("You lost!")
                break
            print()
            print(cur_word)
            
            if cur_word == guessing_word:
                print("""You guessed the word!
        You survived!""")
                break
            else:   
                c = input("Input a letter:")
                if len(c) != 1:
                    print("You should input a single letter")
                elif c not in string.ascii_lowercase:
                    print("Please enter a lowercase English letter")
                elif c in guessed_chars:
                    print(guessed_chars)
                    print("You've already guessed this letter")
                else:
                    guessed_chars.add(c)
                    if c not in guessing_word:
                        print("That letter doesn't appear in the word")
                        i += 1
                    else:
                        cur_word = ''.join(c if c in guessed_chars else "-" for c in guessing_word)

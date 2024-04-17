import random

print(''' 
    _     _  _  _   __   _              _  _  _ 
   / `/ //_`/_`/_`  //_//_`  /|// //|,//_)/_`/_/
  /_;/_//_,._/._/  // //_,  / |/_//  //_)/_,/ \ 
                                               
''')
print("Let me think of a number between 1 - 50.")
guess1 = random.randint(1, 50)

level = input("Choose your difficulty level (Hard or Easy): ").lower()

def guess():
    attempts = 5 if level == "hard" else 10
    print(f"You have only {attempts} attempts to guess.")
    
    for i in range(1, attempts + 1):
        guess = int(input("Make a guess: "))
        diff = guess - guess1
        
        if guess == guess1:
            print("Correct. You won")
            break
        elif diff > 15:
            print("Too far")
        elif diff > 10:
            print("Far")
        elif diff > 5:
            print("Somewhat Close.")
        else:
            print("Almost there.")
        
        print(f"You are left with {attempts - i} guesses.")
    else:
        print("You are out of guesses. The correct number was:", guess1)

guess()

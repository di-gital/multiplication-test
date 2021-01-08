import random as r
import re

def game():
    wrongGuesses = 0
    answeredQuestions = 0

    while(answeredQuestions < 10):
        correctAns = question()
        currGuess = input()
    
        while(re.search(r'\D', currGuess) or not currGuess.strip()):
            print("Not a number. Please try again.") 
            currGuess = input()

        if int(currGuess) == correctAns:
            print("Correct!")
        else:
            print("Incorrect!")
            wrongGuesses = wrongGuesses + 1

        answeredQuestions = answeredQuestions + 1

    return wrongGuesses

def question():
    factorOne = r.randint(0, 12)
    factorTwo = r.randint(0, 12)
    product = factorOne * factorTwo

    print("What is", factorOne, "times", factorTwo, "?")
    return product

if __name__ == "__main__":
    print("That's all! Questions answered wrong:", game())

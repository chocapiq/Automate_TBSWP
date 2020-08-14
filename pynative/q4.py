#Question 4: Given a string and an integer number n, remove characters from a string starting
# from zero up to n and return a new string

word = input("Enter word\n")
length = int(input("Enter how many letters to cut.\n"))

def removeChars(word, n):
    a = len(word)
    if n > a:
        print("Length of the word is too short for number that is set.")
    else:
        print(word[n:])

removeChars(word, length)
# Question 3: Given a string, display only those characters which are present at an even index number.
word = input()
def wordSelector(sent):
    a = len(sent)
    for i in range(a):
        if i%2 == 0:
            print(sent[i])

wordSelector(word)
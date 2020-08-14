#Question 7: Return the total count of sub-string “Emma” appears in the given string

sentence = input("Enter the sentence.")
word = input("Enter the word to find in the sentence.")

def findWords(sentence, word):
    n = 0
    sentence_list = sentence.split()
    for i in range(len(sentence_list)):
        if sentence_list[i] == word:
            n += 1
    print(str(word) + " appeared " + str(n) + " times.")

findWords(sentence, word)
# Exercise Question 6: write all file content into new file by skiping line 5 from following file

oldFile = open("q6text.txt", "r")
newFile = open("q6new.txt", "w")
numOfLine = 1
for line in oldFile:
    print(line, end="")
    if numOfLine != 5:
        newFile.write(line)
    numOfLine += 1

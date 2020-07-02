import os
totalSize = 0
for filename in os.listdir('C:\\users\\pawel'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\users\pawel', filename))
print(totalSize)
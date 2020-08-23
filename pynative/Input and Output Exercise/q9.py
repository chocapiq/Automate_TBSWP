#  How to check file is empty or not
import os
print("Is q6new.txt file empty?\n" + str(os.stat("q6new.txt").st_size == 0))
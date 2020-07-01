try:
    print("Collatz conjectures is that this sequence will always end up at number 1 regardless of which integer you choose")
    c = int(input('Enter the number to start collatz sequence: '))
    x = 0
    while c != 1:
        if c%2 == 0:
            c = c/2
            print(c)
            x += 1
        else:
            c = 3*c+1
            print(c)
            x += 1
except ValueError:
    print('Typed text is not a number')
print('It took ' + str(x) + ' sequences')
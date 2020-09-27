def kappa(list, target):
    solution = []
    i = 0
    while i < len(list):
        j = i+1
        while j < len(list):
            if list[i] + list[j] == target:
                solution.append(i)
                solution.append(j)
                print(solution)
                print("["+str(i)+","+str(j)+"]")
                break
            else:
                j += 1
        i += 1

kappa([2,7,11,15], 9)
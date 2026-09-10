def find_Pythagorean(n):
    correct = []
    for a in range(1, n +1):
        for b in range(1, n + 1):
            for c in range(1, n +1):
                left = a**2 + b**2
                right = c**2
                if left == right:
                    correct.append((a,b, c))

    return correct

n= int(input("enter number: "))
triples = find_Pythagorean(n)

i = 0
while i < len(triples):
    print(triples[i])
    i += 1


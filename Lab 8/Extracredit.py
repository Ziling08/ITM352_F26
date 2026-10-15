
# Part A: LCG Algorithm

def lcg(seed):
    a = 25214903917
    c = 11
    m = 2 ** 48

    number = (a * seed + c) % m
    return number


seed = int(input("Enter a seed: "))

for i in range(5):
    seed = lcg(seed)
    print(seed)

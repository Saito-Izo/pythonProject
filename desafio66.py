n = s = 0
c = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'A soma dos {c} valores foi {s}.')
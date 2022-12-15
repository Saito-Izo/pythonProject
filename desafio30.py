n = int(input('\033[:35mMe diga um número qualquer: \033[m'))
if n % 2 == 0:
    print('O número {} é \033[:34mpar\033[m.'.format(n))
else:
    print('O número {} é \033[:34mímpar\033[m.'.format(n))
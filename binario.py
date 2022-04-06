print('-'*21)
print('Conversor de Binários')
print('-'*21)

numerobinario = []
binarionumero = []

ok = True
ud = True

esc = 0

while esc != 1 and 2 and 3:
    if esc == 3:
        break
    esc = int(input('''[1] Converter números para binário
[2] Converter binários em número 
[3] Sair
'''))
    if esc != 1 and esc!=2 and esc!=3:
        print('Escolha uma opção válida')
    if esc == 3:
        break
    if esc == 1:
        while esc == 1:
            n1 = int(input('Digite o número que será convertido: '))
            ok = True
            ud = True
            numerobinario.clear()
            while ok:
                if n1 == 1:
                    numerobinario.append(1)
                    ok = False
                    ud = False
                elif n1 == 0:
                    numerobinario.append(0)
                    ok = False
                    ud = False
                if ud:    
                    if n1 % 2 == 1:
                        numerobinario.append(1)
                    else:
                        numerobinario.append(0)
                    n1 //= 2  
            for c in reversed(numerobinario):
                print(c, end=' ')
            cont = int(input('''\n[1] Continuar [2] Voltar [3] Sair
'''))
            while cont != 1 and cont!=2 and cont!=3:
                cont = int(input('''\n[1] Continuar [2] Voltar [3] Sair
'''))
            if cont == 2:
                esc = 4
            if cont == 3:
                esc = 3
    if esc == 2:
        while esc == 2:
            n2 = input('Digite o número binário que será convertido: ')
            n3 = 0
            n4 = len(n2)
            n7 = 0
            binarionumero.append(n2)
            for c in range(0,len(n2)):
                n5 = int(n2[c])
                n4 -= 1
                n6 = n5 * 2 ** n4
                n7 += n6
            print(n7)
            cont1 = int(input('''[1] Continuar [2] Voltar [3] Sair
'''))
            while cont1 != 1 and cont1 != 2 and cont1 != 3:
                cont1 = int(input('''[1] Continuar [2] Voltar [3] Sair
'''))
            if cont1 == 2:
                esc = 4
            if cont1 == 3:
                esc = 3


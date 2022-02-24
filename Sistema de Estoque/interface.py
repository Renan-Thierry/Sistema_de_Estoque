def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            cabecalho(' MENU PRINCIPAL ')
            print('Por favor, digite um número inteiro valido.')
            print('-' * 42)
            continue
        except (KeyboardInterrupt):
            print('usuario preferiu não digitar esse número.')
            return 0
        else:
            return n


def linha(tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f' {c}  -  {item} ')
        c += 1
    print(linha())
    opc = leiaint('Oque deseja escolher:')    
    return opc




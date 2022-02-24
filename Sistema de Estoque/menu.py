from interface import*


estoque = 0 
itens = {}
while True:
    resposta = menu(['Cadastrar produto', 'Excluir produto','Calcular estoque','Lista de produtos cadastrados', 'Atualizar preços de itens em estoque', 'Buscar preço de item',
     'Sair do sistema'])
    
    if resposta == 1:
        cabecalho('CADASTRO')
        nome = input('Digite o nome do item que quer cadastrar:')
        preco = float(input('Digite o preço:'))
        
        if nome not in itens:
            item_unico = itens[nome] = preco
            itens[nome] = preco
            cabecalho('CADASTRO')                                     
            print('Item cadastrado com sucesso!')
        else:
            itens[nome] = itens[nome] + preco
            cabecalho('CADASTRO')
            print('O item ja estava cadastrado, o valor foi acumulado')
        if estoque > 50:
            cabecalho('CADASTRO')
            print("Você só pode cadastrar no sistema 50 produtos")


    elif resposta == 2:
        cabecalho('EXCLUSÃO DE ITEM')
        for item in itens:
            print("{0:20}{1:6.2f} Reais".format(item, itens[item]))
        excluir = str(input('Digite o item que quer remover:'))
        if excluir in itens:
            itens.pop(excluir)
            cabecalho('EXCLUSÃO DE ITEM')
            print('O item foi excluido com sucesso')
        else:
            cabecalho('EXCLUSÃO DE ITEM')
            print('Esse item não existe no estoque!!')
        

    elif resposta == 3:
        cabecalho('CÁLCULO DE ESTOQUE')
        buscar = str(input('Digite o item que deseja:'))
        if buscar in itens:
            cabecalho('CÁLCULO DE ESTOQUE')
            print('item: {}'.format(buscar))
            print('valor unico: {0:24} Reais'.format(item_unico))
            print('valor acumulado: {0:20} Reais'.format(itens[nome]))
        else:
            print('Esse item nao existe no estoque!!')


    elif resposta == 4:
        cabecalho('LISTA DE PRODUTOS')
        for item in itens:
            print("{0:20}{1:6.2f} Reais".format(item, itens[item]))


    elif resposta == 5:
        cabecalho('ATUALIZAÇÃO DE ESTOQUE')
        nome = str(input('Digite o item que voce atualizar:'))
        if nome in itens:
            if nome in itens.keys():
                cabecalho('ATUALIZAÇÃO DE ESTOQUE')
                atualizar = float(input('Digite o novo valor:'))
                itens[nome] = atualizar
                cabecalho('ATUALIZAÇÃO DE ESTOQUE')
                print('\033[0;32m Novo valor de item adicionado')
            for item in itens:
                cabecalho('ATUALIZAÇÃO DE ESTOQUE')
                print("{0:10}{1:6.2f} Reais".format(item, itens[item]))
        else:
            cabecalho('ATUALIZAÇÃO DE ESTOQUE')
            print('Este item não existe no estoque!')


    elif resposta == 6:
        cabecalho('BUSCA DE PREÇO DE ITEM')
        buscar_item = str(input(' Digite o nome do item que deseja buscar:'))
        if buscar_item in itens.keys():
            cabecalho('\ATUALIZAÇÃO DE ESTOQUE')
            print('item {} custa {} reais'.format(buscar_item, itens[buscar_item]))
        else:
            cabecalho(' BUSCA DE PREÇO DE ITEM \033[m')
            print('Este item item nao existe no estoque')


    elif resposta == 7:
        print('************')
        print('saindo do sistema...até logo ;) ')
        print('************')
        exit()
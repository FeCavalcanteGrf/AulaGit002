# Crie um programa que simule um inventario de produtos, 
# utilizando um dicionario para armazenar as informações de
# cada produto (nome, preço, quantidade).
# O programa deve permitir adicionar, remover e listar os 
# produtos

def menu():
    inventario = {}
    while True:
        print("\nMenu de Navegação:")
        print("1. Adicionar Produto")
        print("2. Remover Produto")
        print("3. Listar Produtos")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            codigo = int(input("Digite o código do produto: "))
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade do produto: "))
            adicionar_produto(inventario, codigo, nome, preco, quantidade)
        elif opcao == '2':
            codigo = int(input("Digite o código do produto a ser removido: "))
            remover_produto(inventario, codigo)
        elif opcao == '3':
            listar_produtos(inventario)
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

# Função para adicionar um produto ao inventário
def adicionar_produto(inventario, codigo, nome, preco, quantidade):
    inventario[codigo] = {'nome': nome, 'preco': preco, 'quantidade': quantidade}

# Função para remover um produto do inventário
def remover_produto(inventario, codigo):
    if codigo in inventario:
        del inventario[codigo]
    else:
        print("Produto não encontrado.")

# Função para listar todos os produtos do inventário
def listar_produtos(inventario):
    for codigo, info in inventario.items():
        print(f"Código: {codigo}, Nome: {info['nome']}, Preço: {info['preco']}, Quantidade: {info['quantidade']}")

# Iniciar o menu
menu()
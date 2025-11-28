# Lista que vai guardar os doces
# Cada doce será um dicionário: {"nome": "...", "preco": valor}
doces = []

def cadastrar_doce():
    nome = input("Nome do doce: ")
    preco = float(input("Preço do doce: R$ "))
    
    doce = {"nome": nome, "preco": preco}
    doces.append(doce)
    
    print(f"\n✔ Doce '{nome}' cadastrado com sucesso!\n")

def listar_doces():
    if len(doces) == 0:
        print("\nNenhum doce cadastrado ainda.\n")
        return
    
    print("\n--- Lista de Doces ---")
    for i, doce in enumerate(doces, start=1):
        print(f"{i}. {doce['nome']} - R$ {doce['preco']:.2f}")
    print()

def buscar_doce():
    nome_busca = input("Digite o nome do doce que deseja buscar: ")
    
    encontrado = False
    
    for doce in doces:
        if doce["nome"].lower() == nome_busca.lower():
            print(f"\nEncontrado: {doce['nome']} - R$ {doce['preco']:.2f}\n")
            encontrado = True
            break
    
    if not encontrado:
        print("\n❌ Doce não encontrado.\n")

# ---------- Menu Principal ----------
while True:
    print("=== Loja de Doces ===")
    print("1 - Cadastrar doce")
    print("2 - Listar doces")
    print("3 - Buscar doce")
    print("4 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_doce()
    elif opcao == "2":
        listar_doces()
    elif opcao == "3":
        buscar_doce()
    elif opcao == "4":
        print("\nSaindo... até a próxima! 🍬")
        break
    else:
        print("\nOpção inválida! Tente novamente.\n")

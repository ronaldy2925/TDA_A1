🍬 README - Sistema de Gerenciamento de Doces
Este é um sistema simples de gerenciamento de doces escrito em Python. Ele permite cadastrar, listar e buscar doces em um catálogo.

📋 Funcionalidades
O programa oferece as seguintes funcionalidades principais:

Cadastrar Doce: Permite ao usuário adicionar um novo doce ao catálogo, fornecendo o nome e o preço.

Listar Doces: Exibe todos os doces cadastrados, mostrando a ordem, o nome e o preço formatado (R$ X.XX).

Buscar Doce: Permite buscar um doce pelo nome (a busca não diferencia maiúsculas de minúsculas).

Sair: Encerra o programa.

🛠 Como Executar
Para executar este sistema, você precisa ter o Python 3 instalado em sua máquina.

Salve o código fornecido em um arquivo, por exemplo, sistema_doces.py.

Abra o terminal ou prompt de comando.

Navegue até o diretório onde você salvou o arquivo.

Execute o script com o comando:

Bash

python sistema_doces.py
💻 Estrutura do Código
O código é estruturado nas seguintes partes:

Lista de Armazenamento: A lista global doces armazena todos os doces. Cada doce é um dicionário com as chaves "nome" e "preco".

Python

doces = [] 
Função cadastrar_doce(): Solicita o nome e o preço (como float), cria o dicionário do doce e o anexa à lista doces.

Função listar_doces(): Itera sobre a lista doces usando enumerate para exibir a lista numerada com o preço formatado em duas casas decimais.

Função buscar_doce(): Solicita o nome para busca e percorre a lista. Utiliza .lower() em ambos os lados da comparação (doce["nome"].lower() == nome_busca.lower()) para realizar uma busca case-insensitive (sem diferenciar maiúsculas/minúsculas).

Menu Principal: Um loop while True exibe o menu e aceita a entrada do usuário (opcao), chamando a função correspondente ou tratando a opção inválida/saída.

💡 Exemplo de Uso
Escolha uma opção: 1 (Cadastrar doce)

Nome do doce: Brigadeiro

Preço do doce: 3.50

(Mensagem de sucesso)

Escolha uma opção: 2 (Listar doces)

(Será exibido: 1. Brigadeiro - R$ 3.50)

📝 Observações
O armazenamento dos dados é temporário (em memória) e os doces cadastrados serão perdidos ao sair do programa.

A validação de entrada de dados, como garantir que o preço seja um número válido, não está implementada (o uso de float(input(...)) pode causar um erro se o usuário digitar um texto).

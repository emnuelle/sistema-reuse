import random
import re
import json
from datetime import datetime

# Função para carregar dados a partir de um arquivo JSON
def carregar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}

# Função para salvar dados em um arquivo JSON
def salvar_dados(dados, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(dados, arquivo)

# Carregar dados existentes ou criar novos se não existirem
administrador = carregar_dados("administrador.json")
usuarios = carregar_dados("usuarios.json")
cotacao_pontos = carregar_dados("cotacao_pontos.json")

# Gerando pins aleatórios para novos usuários, para a função cadastro
def gerar_pin_aleatorio():
    pin = ''.join(str(random.randint(0, 9)) for _ in range(5))
    return pin


# Função para validar um número de telefone no formato xxxxxxxxx
def validar_numero_telefone(telefone):
    padrao = r'^\d{11}$'
    return re.match(padrao, telefone) is not None


# Função para validar um endereço de e-mail
def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+$'
    return re.match(padrao, email) is not None

# Função para calcular a idade
def calcular_idade(data_nascimento):
    data_atual = datetime.now()
    data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d")
    idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))
    return idade

# Função para realizar o cadastro
def cadastro():
    print("Por Favor, insira seu nome:")
    nome_usuario = input()
    if re.search("\d", nome_usuario):
        print("Erro: Nomes não podem conter números.")
        return

    print("Por Favor, insira sua data de nascimento (AAAA-MM-DD):")
    data_nascimento = input()

    idade = calcular_idade(data_nascimento)

    if idade < 13:
        print("Desculpe, apenas maiores de 13 anos podem se cadastrar.")
        return

    print("Por Favor, insira seu número de telefone no formato xxxxxxxxxxx:")
    telefone_usuario = input()
    if not validar_numero_telefone(telefone_usuario):
        print("Erro: Número de telefone inválido. Use o formato xxxxxxxxxxx.")
        return

    print("Por Favor, insira seu endereço de e-mail:")
    email_usuario = input()
    if not validar_email(email_usuario):
        print("Erro: Endereço de e-mail inválido.")
        return

    # Fazendo um sorteio para gerar o PIN (com 5 dígitos)
    pin_aleatorio = gerar_pin_aleatorio()

    # Converta o PIN para uma string
    pin_aleatorio = str(pin_aleatorio)

    # Atualizando o dicionário de usuários com os novos dados gerados
    usuarios[pin_aleatorio] = {
        "nome": nome_usuario,
        "infos": {
            "Email": email_usuario,
            "Telefone": telefone_usuario
        },
        "Dados": {
            "reciclagem_kg": {
                "Papel": 0,
                "Plástico": 0,
                "Vidro": 0,
                "Metal": 0,
                "Eletrônicos": 0
            },
            "Pontos": 0
        }
    }

    # Exibindo novo usuário e exibindo o PIN gerado
    print(f"Bem vindx {nome_usuario}!\nO seu PIN é: {pin_aleatorio}. Lembre-se, ele é único, guarde ele com carinho (>‿◠)")

# Função para simular o dado (qtd de kg depositados p/ utilizar na função(opcao_reciclar))
def sorteio_entrada_dados():
    return random.randint(1, 10)  # Modifique o intervalo conforme necessário


# Função para adicionar os pontos e kg dos materiais na reciclagem
def adicionar_pontos_e_material(pin, material, quantidade_pontos, quantidade_material):
    if pin in usuarios:
        usuario = usuarios[pin]
        if "Dados" not in usuario:
            usuario["Dados"] = {}
        if "reciclagem_kg" not in usuario["Dados"]:
            usuario["Dados"]["reciclagem_kg"] = {}
        if "Pontos" not in usuario["Dados"]:
            usuario["Dados"]["Pontos"] = 0

        # Atualize a quantidade de material reciclado
        if material in usuario["Dados"]["reciclagem_kg"]:
            usuario["Dados"]["reciclagem_kg"][material] += quantidade_material
        else:
            usuario["Dados"]["reciclagem_kg"][material] = quantidade_material

        # Atualize a quantidade de pontos
        usuario["Dados"]["Pontos"] += quantidade_pontos
    else:
        print("PIN de usuário não encontrado.")


# Função para reciclar
def opcao_reciclar():
    while True:
        print(
            "Por Favor, escolha o material que deseja depositar:\n"
            "(1)\tPapel\n"
            "(2)\tPlástico\n"
            "(3)\tVidro\n"
            "(4)\tMetal\n"
            "(5)\tEletrônicos\n"
            "(6)\tVoltar\n")
        escolha_reciclar = int(input())

        if escolha_reciclar == 1:
            material = "Papel"
        elif escolha_reciclar == 2:
            material = "Plástico"
        elif escolha_reciclar == 3:
            material = "Vidro"
        elif escolha_reciclar == 4:
            material = "Metal"
        elif escolha_reciclar == 5:
            material = "Eletrônicos"
        elif escolha_reciclar == 6:
            return
        else:
            print("Escolha de material inválida.")
            continue

        peso = sorteio_entrada_dados()
        pontuacao = peso * cotacao_pontos["material/Kg"][material]

        print(f"Material escolhido: {material}\nPeso: {peso} Kg")
        print(f"Pontos ganhos: {pontuacao}")

        print("Por favor, insira o seu PIN de 5 dígitos:")
        pin_do_usuario = input()

        adicionar_pontos_e_material(pin_do_usuario, material, pontuacao, peso)

        while True:
            print("Confirmar operação?\n"
                  "(1)\tSim\n(2)\tNão")
            confirmar_op = int(input())
            if confirmar_op == 1:
                break
            elif confirmar_op == 2:
                break

        print("Deseja reciclar mais um material?\n" 
              "(1)\tSim\n(2)\tNão")
        continuar_reciclando = int(input())
        if continuar_reciclando != 1:
            break


# Função para exibir extrato de pontos do usuário
def exibir_extrato_pontos(pin):
    if pin in usuarios:
        usuario = usuarios[pin]
        print(f"Extrato de Pontos do Usuário ({pin}):\n")
        print(f"Nome: {usuario['nome']}")
        print(f"Pontos: {usuario['Dados']['Pontos']}\n")
    else:
        print("Usuário não encontrado.")


# Função para exibir informações do usuário
def exibir_informacoes_usuario(pin):
    if pin in usuarios:
        usuario = usuarios[pin]
        print(f"Informações do Usuário ({pin}):\n")
        print(f"Nome: {usuario['nome']}")
        print(f"Email: {usuario['infos']['Email']}")
        print(f"Telefone: {usuario['infos']['Telefone']}\n")
        print("Reciclagem por tipo de material:")
        for material, quantidade in usuario['Dados']['reciclagem_kg'].items():
            print(f"{material}: {quantidade} Kg")
        print(f"Pontos: {usuario['Dados']['Pontos']}\n")
    else:
        print("Usuário não encontrado.")


# Função para exibir cotação de pontos atual
def exibir_cotacao_pontos():
    print("Cotação Atual de Materiais (Pontos por Kg):\n")
    for material, pontos in cotacao_pontos["material/Kg"].items():
        print(f"{material}: {pontos} pontos por Kg")


# Lista usuarios para o adm
def listar_usuarios():
    print("\nLista de Usuários:\n")
    for pin, usuario in usuarios.items():
        print(f"PIN: {pin}")
        print(f"Nome: {usuario['nome']}")
        print(f"Email: {usuario['infos']['Email']}")
        print(f"Telefone: {usuario['infos']['Telefone']}")
        print(f"Pontos: {usuario['Dados']['Pontos']}")
        print("Reciclagem por tipo de material:")
        for material, quantidade in usuario['Dados']['reciclagem_kg'].items():
            print(f"{material}: {quantidade} Kg")
        print("\n")


# Função apra o adm conseguir mudar a cotação de pontos
def mudar_cotacao_pontos():
    print("\nMudar Cotação de Pontos:\n")
    print("Escolha um material para atualizar a cotação:")
    print("(1) Papel")
    print("(2) Plástico")
    print("(3) Vidro")
    print("(4) Metal")
    print("(5) Eletrônicos")
    print("(6) Voltar ao Menu do Administrador")

    escolha_material = input()

    if escolha_material == "1":
        material = "Papel"
    elif escolha_material == "2":
        material = "Plástico"
    elif escolha_material == "3":
        material = "Vidro"
    elif escolha_material == "4":
        material = "Metal"
    elif escolha_material == "5":
        material = "Eletrônicos"
    elif escolha_material == "6":
        return

    print(f"Digite a nova cotação de pontos para {material} (atual: {cotacao_pontos['material/Kg'][material]}):")
    nova_cotacao = int(input())

    cotacao_pontos['material/Kg'][material] = nova_cotacao
    print(f"A cotação de pontos para {material} foi atualizada para {nova_cotacao} pontos por Kg.")


# Função para alterar informações de um usuário
def alterar_informacoes_usuario():
    print("\nAlterar Informações de Usuário:\n")
    print("Digite o PIN do usuário que deseja alterar:")
    pin_usuario = input()

    if pin_usuario not in usuarios:
        print("Usuário não encontrado.")
        return

    usuario = usuarios[pin_usuario]

    print(f"Nome atual: {usuario['nome']}")
    novo_nome = input("Digite o novo nome (ou deixe em branco para manter o atual): ")

    if novo_nome:
        usuario['nome'] = novo_nome

    print(f"Email atual: {usuario['infos']['Email']}")
    novo_email = input("Digite o novo email (ou deixe em branco para manter o atual): ")

    if novo_email:
        if validar_email(novo_email):
            usuario['infos']['Email'] = novo_email
        else:
            print("Email inválido. As informações não foram alteradas.")
            return

    print(f"Telefone atual: {usuario['infos']['Telefone']}")
    novo_telefone = input("Digite o novo telefone (ou deixe em branco para manter o atual): ")

    if novo_telefone:
        if validar_numero_telefone(novo_telefone):
            usuario['infos']['Telefone'] = novo_telefone
        else:
            print("Telefone inválido. As informações não foram alteradas.")
            return

    print(f"As informações do usuário {pin_usuario} foram alteradas com sucesso.")


# Função para excluir um usuário (apenas adm possui esse acesso)
def excluir_usuario():
    print("\nExcluir Usuário:\n")
    print("Digite o PIN do usuário que deseja excluir:")
    pin_usuario = input()

    if pin_usuario not in usuarios:
        print("Usuário não encontrado.")
        return

    print(
        f"Tem certeza de que deseja excluir o usuário {pin_usuario}? (S para sim, qualquer outra tecla para cancelar)")
    confirmacao = input().strip().lower()

    if confirmacao == 's':
        del usuarios[pin_usuario]
        print(f"O usuário {pin_usuario} foi excluído com sucesso.")
    else:
        print("A exclusão foi cancelada.")


# Função para adicionar um novo usuário (apenas adm possui esse acesso)
def adicionar_usuario():
    print("\nAdicionar Novo Usuário:\n")

    nome_usuario = input("Digite o nome do novo usuário: ")
    if re.search("\d", nome_usuario):
        print("Erro: Nomes não podem conter números.")
        return

    telefone_usuario = input("Digite o número de telefone no formato xxxxxxxxxxx: ")
    if not validar_numero_telefone(telefone_usuario):
        print("Erro: Número de telefone inválido. Use o formato xxxxxxxxxxx.")
        return

    email_usuario = input("Digite o endereço de e-mail: ")
    if not validar_email(email_usuario):
        print("Erro: Endereço de e-mail inválido.")
        return

    novo_pin = gerar_pin_aleatorio()

    usuarios[novo_pin] = {
        "nome": nome_usuario,
        "infos": {
            "Email": email_usuario,
            "Telefone": telefone_usuario
        },
        "Dados": {
            "reciclagem_kg": {
                "Papel": 0,
                "Plástico": 0,
                "Vidro": 0,
                "Metal": 0,
                "Eletrônicos": 0
            },
            "Pontos": 0
        }
    }

    print(f"Novo usuário adicionado com sucesso. PIN: {novo_pin}")


# menu adm
def nav_menu_adm():
    while True:
        print("Menu do Administrador:")
        print("Escolha uma opção:")
        print("(1) Cotação de Pontos Atual")
        print("(2) Mudar Cotação de Pontos")
        print("(3) Lista de Usuários")
        print("(4) Alterar Informações de Usuário")
        print("(5) Excluir Usuário")
        print("(6) Adicionar Usuário")
        print("(7) Sair")

        escolha_administrador = input()

        if escolha_administrador == "1":
            exibir_cotacao_pontos()
        elif escolha_administrador == "2":
            mudar_cotacao_pontos()
        elif escolha_administrador == "3":
            listar_usuarios()
        elif escolha_administrador == "4":
            alterar_informacoes_usuario()
        elif escolha_administrador == "5":
            excluir_usuario()
        elif escolha_administrador == "6":
            adicionar_usuario()
        elif escolha_administrador == "7":
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


####################
# Programa principal
####################

while True:
    # Desejando boas vindas ao usuário
    print()
    print("*************************")
    print("****Bem Vindo a reUse****")
    print("*************************")
    print()
    # Menu inicial
    print("Escolha uma opção:")
    print("(1)\tEntrar\n"
          "(2)\tCadastrar-se\n"
          "(3)\tSair")
    escolha_menu_inicial = input()

    # Estrutura de decisão para decidir qual menu vai ser exibido (adm ou usuário)
    if escolha_menu_inicial == "1":
        print("Por favor insira o seu PIN de 5 dígitos:")
        pin = input()
        if pin == "66666":
            print("*Área restrita reUse*\n")
            nav_menu_adm()
        elif pin in usuarios:
            usuario = usuarios[pin]
            print(f"Bem-vindo, {usuario['nome']}! Estamos felizes em receber de volta.")

            nav_menu_secundario = True
            while nav_menu_secundario:
                print(
                    "Escolha uma opção:\n"
                    "(1)\tReciclar\n"
                    "(2)\tExtrato de pontos\n"
                    "(3)\tCotação Atual de materiais\n"
                    "(4)\tVer informações do usuário\n"
                    "(5)\tSair")
                escolha_menu_secundario = input()

                if escolha_menu_secundario == "1":
                    opcao_reciclar()
                elif escolha_menu_secundario == "2":
                    exibir_extrato_pontos(pin)
                elif escolha_menu_secundario == "3":
                    exibir_cotacao_pontos()
                elif escolha_menu_secundario == "4":
                    exibir_informacoes_usuario(pin)
                elif escolha_menu_secundario == "5":
                    nav_menu_secundario = False
        else:
            print("PIN não encontrado. Por favor, verifique o PIN e tente novamente.")
    elif escolha_menu_inicial == "2":
        cadastro()
    elif escolha_menu_inicial == "3":
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

salvar_dados(administrador, "administrador.json")
salvar_dados(usuarios, "usuarios.json")
salvar_dados(cotacao_pontos, "cotacao_pontos.json")

print("Obrigado por usar o reUse. Até mais!")
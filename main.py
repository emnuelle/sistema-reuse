import random
import re
import json

# Inicialização das estruturas de dados
usuarios = {}
administrador = {
    "66666": {
        "nome": "Administrador",
        "infos": {
            "Email": "admin@reuse.com"
        }
    }
}

cotacao_pontos = {
    "Papel": 20,
    "Plástico": 25,
    "Vidro": 15,
    "Metal": 10,
    "Eletrônicos": 30
}

# Função para salvar os dados em um arquivo JSON
def save_data_to_json():
    data = {
        "usuarios": usuarios,
        "administrador": administrador,
        "cotacao_pontos": cotacao_pontos
    }
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Função para carregar os dados de um arquivo JSON
def load_data_from_json():
    try:
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)
            usuarios.update(data.get("usuarios", {}))
            administrador.update(data.get("administrador", {}))
            cotacao_pontos.update(data.get("cotacao_pontos", {}))
    except FileNotFoundError:
        # Se o arquivo não existe, inicia as estruturas vazias
        save_data_to_json()

# Carregar os dados do arquivo JSON ao iniciar o programa
load_data_from_json()

# Função para gerar um PIN aleatório
def gerar_pin_aleatorio():
    pin = ''.join(str(random.randint(0, 9)) for _ in range(5))
    return pin

# Função para validar um número de telefone no formato xxxxxxxxxxx
def validar_numero_telefone(telefone):
    padrao = r'^\d{11}$'
    return re.match(padrao, telefone) is not None

# Função para validar um endereço de e-mail
def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+$'
    return re.match(padrao, email) is not None

# Função para realizar o cadastro de um usuário
def cadastro():
    print("Por favor, insira seu nome:")
    nome_usuario = input()
    if re.search("\d", nome_usuario):
        print("Erro: Nomes não podem conter números.")
        return

    print("Por favor, insira seu número de telefone no formato xxxxxxxxxxx:")
    telefone_usuario = input()
    if not validar_numero_telefone(telefone_usuario):
        print("Erro: Número de telefone inválido. Use o formato xxxxxxxxxxx.")
        return

    print("Por favor, insira seu endereço de e-mail:")
    email_usuario = input()
    if not validar_email(email_usuario):
        print("Erro: Endereço de e-mail inválido.")
        return

    # Gere um PIN aleatório
    pin_aleatorio = gerar_pin_aleatorio()

    # Atualize o dicionário de usuários com os novos dados gerados
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

    # Exiba o novo usuário e o PIN gerado
    print(f"Bem-vindo {nome_usuario}!\nSeu PIN é: {pin_aleatorio}. Guarde-o com cuidado!")

# Função para realizar a reciclagem
def opcao_reciclar():
    while True:
        print("Por favor, escolha o material que deseja depositar:")
        print("(1)\tPapel")
        print("(2)\tPlástico")
        print("(3)\tVidro")
        print("(4)\tMetal")
        print("(5)\tEletrônicos")
        print("(6)\tVoltar ao Menu Principal")

        escolha_reciclar = input()

        if escolha_reciclar == "6":
            break

        if escolha_reciclar not in cotacao_pontos:
            print("Escolha de material inválida.")
            continue

        material = escolha_reciclar
        peso = float(input(f"Por favor, insira o peso em Kg do {material}:"))

        if peso <= 0:
            print("Peso inválido. Deve ser maior que zero.")
            continue

        pontos_ganhos = peso * cotacao_pontos[material]

        print(f"Material escolhido: {material}\nPeso: {peso} Kg")
        print(f"Pontos ganhos: {pontos_ganhos}")

        print("Por favor, insira seu PIN de 5 dígitos:")
        pin_do_usuario = input()

        if pin_do_usuario not in usuarios:
            print("PIN de usuário não encontrado.")
            continue

        # Atualizar os dados do usuário
        usuario = usuarios[pin_do_usuario]
        usuario["Dados"]["reciclagem_kg"][material] += peso
        usuario["Dados"]["Pontos"] += pontos_ganhos

        print("Operação confirmada. Deseja reciclar mais um material? (S para Sim, qualquer outra tecla para não)")
        continuar_reciclando = input().strip().lower()
        if continuar_reciclando != "s":
            break

# Função para exibir o extrato de pontos do usuário
def extrato_pontos():
    print("Por favor, insira seu PIN de 5 dígitos:")
    pin_do_usuario = input()

    if pin_do_usuario in usuarios:
        usuario = usuarios[pin_do_usuario]
        print(f"Extrato de Pontos do Usuário ({pin_do_usuario}):\n")
        print(f"Nome: {usuario['nome']}")
        print(f"Pontos: {usuario['Dados']['Pontos']}\n")
    else:
        print("Usuário não encontrado.")

# Função para exibir informações do usuário
def informacoes_usuario():
    print("Por favor, insira seu PIN de 5 dígitos:")
    pin_do_usuario = input()

    if pin_do_usuario in usuarios:
        usuario = usuarios[pin_do_usuario]
        print(f"Informações do Usuário ({pin_do_usuario}):\n")
        print(f"Nome: {usuario['nome']}")
        print(f"Email: {usuario['infos']['Email']}")
        print(f"Telefone: {usuario['infos']['Telefone']}")
        print("Dados de Reciclagem:")
        for material, kg in usuario['Dados']['reciclagem_kg'].items():
            print(f"{material}: {kg} Kg")
        print(f"Pontos: {usuario['Dados']['Pontos']}\n")
    else:
        print("Usuário não encontrado.")

# Função para listar todos os usuários
def listar_usuarios():
    print("Lista de Usuários:")
    for pin, usuario in usuarios.items():
        print(f"PIN: {pin}\tNome: {usuario['nome']}")
        print("Email: {0}".format(usuario['infos']['Email']))
        print("Telefone: {0}".format(usuario['infos']['Telefone']))
        print("Pontos: {0}\n".format(usuario['Dados']['Pontos']))

# Função para mudar a cotação de pontos de materiais
def mudar_cotacao_pontos():
    print("Mudar Cotação de Pontos:")
    for material, pontos in cotacao_pontos.items():
        print(f"Atual Cotação de Pontos para {material}: {pontos}")
        nova_cotacao = float(input(f"Insira a nova cotação de pontos para {material}: "))
        if nova_cotacao >= 0:
            cotacao_pontos[material] = nova_cotacao
        else:
            print("Cotação de pontos inválida. Deve ser maior ou igual a zero.")

# Função para alterar informações do usuário
def alterar_informacoes_usuario():
    print("Por favor, insira seu PIN de 5 dígitos:")
    pin_do_usuario = input()

    if pin_do_usuario in usuarios:
        usuario = usuarios[pin_do_usuario]
        print(f"Informações do Usuário ({pin_do_usuario}):\n")
        print(f"Nome atual: {usuario['nome']}")
        novo_nome = input("Insira o novo nome (ou apenas pressione Enter para manter o nome atual): ")
        if novo_nome and not re.search("\d", novo_nome):
            usuario['nome'] = novo_nome
        else:
            print("Nome inválido ou contém números. Mantendo o nome atual.")

        print(f"Email atual: {usuario['infos']['Email']}")
        novo_email = input("Insira o novo email (ou apenas pressione Enter para manter o email atual): ")
        if novo_email and validar_email(novo_email):
            usuario['infos']['Email'] = novo_email
        else:
            print("Email inválido ou em branco. Mantendo o email atual.")

        print(f"Telefone atual: {usuario['infos']['Telefone']}")
        novo_telefone = input("Insira o novo número de telefone (ou apenas pressione Enter para manter o telefone atual): ")
        if novo_telefone and validar_numero_telefone(novo_telefone):
            usuario['infos']['Telefone'] = novo_telefone
        else:
            print("Número de telefone inválido ou em branco. Mantendo o telefone atual.")

        print("Informações atualizadas com sucesso.")
    else:
        print("Usuário não encontrado.")

# Função para excluir um usuário
def excluir_usuario():
    print("Por favor, insira o PIN de 5 dígitos do usuário que deseja excluir:")
    pin_do_usuario = input()
    if pin_do_usuario in usuarios:
        usuario = usuarios.pop(pin_do_usuario)
        print(f"Usuário {usuario['nome']} removido com sucesso.")
    else:
        print("Usuário não encontrado.")

# Função para adicionar um usuário (somente para o administrador)
def adicionar_usuario():
    print("Insira o nome do novo usuário:")
    nome_usuario = input()
    if re.search("\d", nome_usuario):
        print("Erro: Nomes não podem conter números.")
        return

    print("Insira o número de telefone do novo usuário no formato xxxxxxxxxxx:")
    telefone_usuario = input()
    if not validar_numero_telefone(telefone_usuario):
        print("Erro: Número de telefone inválido. Use o formato xxxxxxxxxxx.")
        return

    print("Insira o endereço de e-mail do novo usuário:")
    email_usuario = input()
    if not validar_email(email_usuario):
        print("Erro: Endereço de e-mail inválido.")
        return

    # Gere um PIN aleatório
    pin_aleatorio = gerar_pin_aleatorio()

    # Atualize o dicionário de usuários com os novos dados gerados
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

    print(f"Usuário {nome_usuario} adicionado com sucesso!\nSeu PIN é: {pin_aleatorio}. Guarde-o com cuidado!")

# Função principal para o menu do programa
def main_menu():
    while True:
        print("Bem-vindo ao Sistema de Reciclagem Reuse!")
        print("Escolha uma opção:")
        print("(1) Cadastro")
        print("(2) Reciclar")
        print("(3) Extrato de Pontos")
        print("(4) Informações do Usuário")
        print("(5) Sair")

        opcao = input()

        if opcao == "1":
            cadastro()
        elif opcao == "2":
            opcao_reciclar()
        elif opcao == "3":
            extrato_pontos()
        elif opcao == "4":
            informacoes_usuario()
        elif opcao == "5":
            save_data_to_json()
            print("Obrigado por usar o Reuse. Até mais!")
            break
        elif opcao == "adm":
            # Área restrita para o administrador
            print("Por favor, insira o PIN de administrador (66666):")
            pin_adm = input()
            if pin_adm == "66666":
                admin_menu()
            else:
                print("Acesso negado. PIN de administrador incorreto.")
        else:
            print("Escolha inválida. Tente novamente.")

# Função para o menu do administrador
def admin_menu():
    while True:
        print("Menu do Administrador:")
        print("Escolha uma opção:")
        print("(1) Listar Usuários")
        print("(2) Mudar Cotação de Pontos")
        print("(3) Alterar Informações de Usuário")
        print("(4) Excluir Usuário")
        print("(5) Adicionar Usuário")
        print("(6) Sair do Menu do Administrador")

        opcao_adm = input()

        if opcao_adm == "1":
            listar_usuarios()
        elif opcao_adm == "2":
            mudar_cotacao_pontos()
        elif opcao_adm == "3":
            alterar_informacoes_usuario()
        elif opcao_adm == "4":
            excluir_usuario()
        elif opcao_adm == "5":
            adicionar_usuario()
        elif opcao_adm == "6":
            save_data_to_json()
            print("Retornando ao Menu Principal.")
            break
        else:
            print("Escolha inválida. Tente novamente.")

# Iniciar o programa
main_menu()

import math

# Definição das culturas suportadas
culturas = ['Café', 'Soja']

# Vetores para armazenar os dados
dados_plantio = []
dados_manejo = []

def calcular_area(cultura):
    if cultura == 'Café':
        print("Cálculo da área para Café (Retângulo)")
        comprimento = float(input("Digite o comprimento do plantio (em metros): "))
        largura = float(input("Digite a largura do plantio (em metros): "))
        area = comprimento * largura
    elif cultura == 'Soja':
        print("Cálculo da área para Soja (Círculo)")
        raio = float(input("Digite o raio do plantio (em metros): "))
        area = math.pi * (raio ** 2)
    else:
        print("Cultura não suportada.")
        area = 0
    return area

def calcular_manejo(cultura):
    print(f"Cálculo do manejo de insumos para {cultura}")
    produto = input("Digite o nome do produto (ex: Fosfato): ")
    quantidade_por_metro = float(input("Digite a quantidade necessária por metro (em mL/L): "))
    ruas = int(input("Digite o número de ruas na lavoura: "))
    comprimento_rua = float(input("Digite o comprimento de cada rua (em metros): "))
    total_metros = ruas * comprimento_rua
    quantidade_total = quantidade_por_metro * total_metros
    # Converter mL para litros se necessário
    if 'mL' in str(quantidade_por_metro):
        quantidade_total /= 1000  # 1000 mL = 1 litro
    return {'cultura': cultura, 'produto': produto, 'quantidade_total_litros': quantidade_total}

def entrada_dados():
    print("\n--- Entrada de Dados ---")
    print("Selecione a cultura:")
    for idx, cultura in enumerate(culturas, start=1):
        print(f"{idx}. {cultura}")
    escolha = int(input("Digite o número da cultura: "))
    if escolha < 1 or escolha > len(culturas):
        print("Opção inválida.")
        return
    cultura_selecionada = culturas[escolha - 1]
    area = calcular_area(cultura_selecionada)
    manejo = calcular_manejo(cultura_selecionada)
    dados_plantio.append({'cultura': cultura_selecionada, 'area': area})
    dados_manejo.append(manejo)
    print("Dados inseridos com sucesso!")

def saida_dados():
    print("\n--- Dados de Plantio ---")
    for idx, plantio in enumerate(dados_plantio, start=1):
        print(f"{idx}. Cultura: {plantio['cultura']}, Área Plantada: {plantio['area']:.2f} m²")
    print("\n--- Dados de Manejo ---")
    for idx, manejo in enumerate(dados_manejo, start=1):
        print(f"{idx}. Cultura: {manejo['cultura']}, Produto: {manejo['produto']}, Quantidade Necessária: {manejo['quantidade_total_litros']:.2f} litros")

def atualizar_dados():
    print("\n--- Atualização de Dados ---")
    print("1. Atualizar Dados de Plantio")
    print("2. Atualizar Dados de Manejo")
    escolha = int(input("Escolha uma opção: "))
    if escolha == 1:
        saida_dados()
        pos = int(input("Digite o número do plantio que deseja atualizar: ")) - 1
        if pos < 0 or pos >= len(dados_plantio):
            print("Posição inválida.")
            return
        print(f"Atualizando Plantio {pos + 1}:")
        cultura = input(f"Digite a cultura ({culturas}): ")
        if cultura not in culturas:
            print("Cultura inválida.")
            return
        area = calcular_area(cultura)
        dados_plantio[pos] = {'cultura': cultura, 'area': area}
        print("Dados de plantio atualizados com sucesso!")
    elif escolha == 2:
        saida_dados()
        pos = int(input("Digite o número do manejo que deseja atualizar: ")) - 1
        if pos < 0 or pos >= len(dados_manejo):
            print("Posição inválida.")
            return
        print(f"Atualizando Manejo {pos + 1}:")
        cultura = input(f"Digite a cultura ({culturas}): ")
        if cultura not in culturas:
            print("Cultura inválida.")
            return
        manejo = calcular_manejo(cultura)
        dados_manejo[pos] = manejo
        print("Dados de manejo atualizados com sucesso!")
    else:
        print("Opção inválida.")

def deletar_dados():
    print("\n--- Deleção de Dados ---")
    print("1. Deletar Dados de Plantio")
    print("2. Deletar Dados de Manejo")
    escolha = int(input("Escolha uma opção: "))
    if escolha == 1:
        saida_dados()
        pos = int(input("Digite o número do plantio que deseja deletar: ")) - 1
        if pos < 0 or pos >= len(dados_plantio):
            print("Posição inválida.")
            return
        del dados_plantio[pos]
        print("Dados de plantio deletados com sucesso!")
    elif escolha == 2:
        saida_dados()
        pos = int(input("Digite o número do manejo que deseja deletar: ")) - 1
        if pos < 0 or pos >= len(dados_manejo):
            print("Posição inválida.")
            return
        del dados_manejo[pos]
        print("Dados de manejo deletados com sucesso!")
    else:
        print("Opção inválida.")

def menu():
    while True:
        print("\n=== Aplicação TecPlants ===")
        print("1. Entrada de Dados")
        print("2. Saída de Dados")
        print("3. Atualização de Dados")
        print("4. Deleção de Dados")
        print("5. Sair do Programa")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            entrada_dados()
        elif escolha == '2':
            saida_dados()
        elif escolha == '3':
            atualizar_dados()
        elif escolha == '4':
            deletar_dados()
        elif escolha == '5':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
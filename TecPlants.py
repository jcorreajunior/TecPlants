import math

# Definição das culturas suportadas
culturas = ['Café', 'Soja']

# Vetores para armazenar os dados
dados_plantio = []
dados_manejo = []

def calcular_area(cultura):
    if cultura == 'Café':
        print("\nCálculo da área para Café (Círculo)")
        raio = float(input("Digite o raio do plantio (em metros): "))
        plantio_area = math.pi * (raio ** 2)
    elif cultura == 'Soja':
        print("\nCálculo da área para Soja (Retângulo)")
        comprimento = float(input("Digite o comprimento do plantio (em metros): "))
        largura = float(input("Digite a largura do plantio (em metros): "))
        plantio_area = comprimento * largura
    else:
        print("Cultura não suportada.")
        plantio_area = 0

    # Coleta de dados para cálculo da área das ruas
    ruas = int(input("Digite o número de ruas na lavoura: "))
    comprimento_rua = float(input("Digite o comprimento de cada rua (em metros): "))
    tamanho_rua = float(input("Digite o tamanho (largura) de cada rua (em metros): "))
    area_ruas = ruas * comprimento_rua * tamanho_rua

    # Cálculo da área total
    total_area = plantio_area + area_ruas

    print(f"\nÁrea de Plantio: {plantio_area:.2f} m²")
    print(f"Área das Ruas: {area_ruas:.2f} m²")
    print(f"Área Total (Plantio + Ruas): {total_area:.2f} m²\n")

    return plantio_area, area_ruas, total_area, ruas, comprimento_rua

def calcular_manejo(cultura, ruas, comprimento_rua):
    print(f"\nCálculo do manejo de insumos para {cultura}")
    produto = input("Digite o nome do produto (ex: Fosfato): ")

    # Menu para seleção da unidade de medida
    print("Selecione a unidade da quantidade necessária:")
    print("1. Litros")
    print("2. Kg")
    while True:
        try:
            unidade_escolha = int(input("Digite o número correspondente à unidade: "))
            if unidade_escolha == 1:
                unidade = 'Litros'
                break
            elif unidade_escolha == 2:
                unidade = 'Kg'
                break
            else:
                print("Opção inválida. Por favor, escolha 1 ou 2.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    quantidade_por_metro = float(input(f"Digite a quantidade necessária por metro (em {unidade}): "))

    # Calcula a quantidade total necessária
    total_metros = ruas * comprimento_rua
    quantidade_total = quantidade_por_metro * total_metros

    print(f"\nQuantidade Total de {produto} Necessária: {quantidade_total:.2f} {unidade}\n")

    return {
        'cultura': cultura,
        'produto': produto,
        'quantidade_total': quantidade_total,
        'unidade': unidade
    }

def entrada_dados():
    print("\n--- Entrada de Dados ---")
    print("Selecione a cultura:")
    for idx, cultura in enumerate(culturas, start=1):
        print(f"{idx}. {cultura}")
    try:
        escolha = int(input("Digite o número da cultura: "))
        if escolha < 1 ou escolha > len(culturas):
            print("Opção inválida.")
            return
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        return

    cultura_selecionada = culturas[escolha - 1]
    plantio_area, area_ruas, total_area, ruas, comprimento_rua = calcular_area(cultura_selecionada)
    manejo = calcular_manejo(cultura_selecionada, ruas, comprimento_rua)

    dados_plantio.append({
        'cultura': cultura_selecionada,
        'area_plantio': plantio_area,
        'area_ruas': area_ruas,
        'area_total': total_area
    })
    dados_manejo.append(manejo)
    print("Dados inseridos com sucesso!")

def saida_dados():
    print("\n--- Dados de Plantio ---")
    if not dados_plantio:
        print("Nenhum dado de plantio registrado.")
    else:
        for idx, plantio in enumerate(dados_plantio, start=1):
            print(f"{idx}. Cultura: {plantio['cultura']}, "
                  f"Área de Plantio: {plantio['area_plantio']:.2f} m², "
                  f"Área das Ruas: {plantio['area_ruas']:.2f} m², "
                  f"Área Total: {plantio['area_total']:.2f} m²")
    
    print("\n--- Dados de Manejo ---")
    if not dados_manejo:
        print("Nenhum dado de manejo registrado.")
    else:
        for idx, manejo in enumerate(dados_manejo, start=1):
            print(f"{idx}. Cultura: {manejo['cultura']}, "
                  f"Produto: {manejo['produto']}, "
                  f"Quantidade Necessária: {manejo['quantidade_total']:.2f} {manejo['unidade']}")

def atualizar_dados():
    print("\n--- Atualização de Dados ---")
    print("1. Atualizar Dados de Plantio")
    print("2. Atualizar Dados de Manejo")
    try:
        escolha = int(input("Escolha uma opção: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        return

    if escolha == 1:
        if not dados_plantio:
            print("Nenhum dado de plantio para atualizar.")
            return
        saida_dados()
        try:
            pos = int(input("Digite o número do plantio que deseja atualizar: ")) - 1
            if pos < 0 or pos >= len(dados_plantio):
                print("Posição inválida.")
                return
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            return

        cultura = input(f"Digite a cultura ({', '.join(culturas)}): ").strip().title()
        if cultura not in culturas:
            print("Cultura inválida.")
            return
        plantio_area, area_ruas, total_area, ruas, comprimento_rua = calcular_area(cultura)
        dados_plantio[pos] = {
            'cultura': cultura,
            'area_plantio': plantio_area,
            'area_ruas': area_ruas,
            'area_total': total_area
        }
        # Atualiza o manejo correspondente
        manejo = calcular_manejo(cultura, ruas, comprimento_rua)
        if pos < len(dados_manejo):
            dados_manejo[pos] = manejo
        else:
            dados_manejo.append(manejo)
        print("Dados de plantio e manejo atualizados com sucesso!")
    elif escolha == 2:
        if not dados_manejo:
            print("Nenhum dado de manejo para atualizar.")
            return
        saida_dados()
        try:
            pos = int(input("Digite o número do manejo que deseja atualizar: ")) - 1
            if pos < 0 or pos >= len(dados_manejo):
                print("Posição inválida.")
                return
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            return

        cultura = input(f"Digite a cultura ({', '.join(culturas)}): ").strip().title()
        if cultura not in culturas:
            print("Cultura inválida.")
            return

        # Encontrar os dados de plantio correspondentes para obter ruas e comprimento_rua
        plantio_correspondente = None
        for plantio in dados_plantio:
            if plantio['cultura'] == cultura:
                plantio_correspondente = plantio
                break

        if not plantio_correspondente:
            print("Não há plantio registrado para essa cultura.")
            return

        ruas = int(input("Digite o número de ruas na lavoura: "))
        comprimento_rua = float(input("Digite o comprimento de cada rua (em metros): "))

        manejo = calcular_manejo(cultura, ruas, comprimento_rua)
        dados_manejo[pos] = manejo
        print("Dados de manejo atualizados com sucesso!")
    else:
        print("Opção inválida.")

def deletar_dados():
    print("\n--- Deleção de Dados ---")
    print("1. Deletar Dados de Plantio")
    print("2. Deletar Dados de Manejo")
    try:
        escolha = int(input("Escolha uma opção: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        return

    if escolha == 1:
        if not dados_plantio:
            print("Nenhum dado de plantio para deletar.")
            return
        saida_dados()
        try:
            pos = int(input("Digite o número do plantio que deseja deletar: ")) - 1
            if pos < 0 or pos >= len(dados_plantio):
                print("Posição inválida.")
                return
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            return
        del dados_plantio[pos]
        if pos < len(dados_manejo):
            del dados_manejo[pos]
        print("Dados de plantio e manejo deletados com sucesso!")
    elif escolha == 2:
        if not dados_manejo:
            print("Nenhum dado de manejo para deletar.")
            return
        saida_dados()
        try:
            pos = int(input("Digite o número do manejo que deseja deletar: ")) - 1
            if pos < 0 or pos >= len(dados_manejo):
                print("Posição inválida.")
                return
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            return
        del dados_manejo[pos]
        if pos < len(dados_plantio):
            del dados_plantio[pos]
        print("Dados de manejo e plantio deletados com sucesso!")
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
        escolha = input("Escolha uma opção: ").strip()
        
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
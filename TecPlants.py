import math

# Definição das culturas suportadas
culturas = ['Café', 'Soja']

# Vetor para armazenar os dados de plantio com seus manejos
dados_plantio = []

# Função para gerar IDs únicos para plantios e manejos
def gerar_id(lista):
    if not lista:
        return 1
    else:
        return max(item['id'] for item in lista) + 1

def calcular_area(cultura):
    if cultura == 'Café':
        print("\nCálculo da área para Café (Círculo)")
        while True:
            try:
                raio = float(input("Digite o raio do plantio (em metros): "))
                if raio <= 0:
                    print("O raio deve ser um número positivo.")
                    continue
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número válido.")
        plantio_area = math.pi * (raio ** 2)
    elif cultura == 'Soja':
        print("\nCálculo da área para Soja (Retângulo)")
        while True:
            try:
                comprimento = float(input("Digite o comprimento do plantio (em metros): "))
                if comprimento <= 0:
                    print("O comprimento deve ser um número positivo.")
                    continue
                largura = float(input("Digite a largura do plantio (em metros): "))
                if largura <= 0:
                    print("A largura deve ser um número positivo.")
                    continue
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número válido.")
        plantio_area = comprimento * largura
    else:
        print("Cultura não suportada.")
        plantio_area = 0

    # Coleta de dados para cálculo da área das ruas
    while True:
        try:
            ruas = int(input("Digite o número de ruas na lavoura: "))
            if ruas < 0:
                print("O número de ruas não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    
    while True:
        try:
            comprimento_rua = float(input("Digite o comprimento de cada rua (em metros): "))
            if comprimento_rua < 0:
                print("O comprimento da rua não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
    
    while True:
        try:
            tamanho_rua = float(input("Digite o tamanho (largura) de cada rua (em metros): "))
            if tamanho_rua < 0:
                print("O tamanho da rua não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
    
    area_ruas = ruas * comprimento_rua * tamanho_rua

    # Cálculo da área total
    total_area = plantio_area + area_ruas

    print(f"\nÁrea de Plantio: {plantio_area:.2f} m²")
    print(f"Área das Ruas: {area_ruas:.2f} m²")
    print(f"Área Total (Plantio + Ruas): {total_area:.2f} m²\n")

    return plantio_area, area_ruas, total_area

def calcular_manejo(area_total):
    print(f"\nCálculo do manejo de insumos")
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

    while True:
        try:
            quantidade_por_metro = float(input(f"Digite a quantidade necessária por metro (em {unidade}): "))
            if quantidade_por_metro < 0:
                print("A quantidade não pode ser negativa.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

    # Cálculo da quantidade total baseada na área_total
    quantidade_total = quantidade_por_metro * area_total

    print(f"\nQuantidade Total Necessária: {quantidade_total:.2f} {unidade}\n")

    return produto, quantidade_total, unidade

def entrada_dados():
    print("\n--- Entrada de Dados ---")
    print("Selecione a cultura:")
    for idx, cultura in enumerate(culturas, start=1):
        print(f"{idx}. {cultura}")
    try:
        escolha = int(input("Digite o número da cultura: "))
        if escolha < 1 or escolha > len(culturas):
            print("Opção inválida.")
            return
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        return

    cultura_selecionada = culturas[escolha - 1]
    plantio_area, area_ruas, total_area = calcular_area(cultura_selecionada)

    # Gerar ID único para o plantio
    plantio_id = gerar_id(dados_plantio)

    # Criar registro de plantio
    plantio = {
        'id': plantio_id,
        'cultura': cultura_selecionada,
        'area_plantio': plantio_area,
        'area_ruas': area_ruas,
        'area_total': total_area,
        'manejamentos': []
    }

    # Adicionar manejos (pelo menos um)
    while True:
        print("\nDeseja adicionar um manejo para este plantio?")
        print("1. Sim")
        print("2. Não")
        manejo_opcao = input("Escolha uma opção: ").strip()
        if manejo_opcao == '1':
            produto, quantidade_total, unidade = calcular_manejo(total_area)
            # Gerar ID único para o manejo
            manejo_id = gerar_id([m for p in dados_plantio for m in p['manejamentos']])
            manejo = {
                'id': manejo_id,
                'produto': produto,
                'quantidade_total': quantidade_total,
                'unidade': unidade
            }
            plantio['manejamentos'].append(manejo)
        elif manejo_opcao == '2':
            break
        else:
            print("Opção inválida. Por favor, escolha 1 ou 2.")

    dados_plantio.append(plantio)
    print("Dados de plantio e manejos inseridos com sucesso!")

def adicionar_manejo():
    print("\n--- Adicionar Manejo a um Plantio Existente ---")
    if not dados_plantio:
        print("Nenhum plantio registrado.")
        return
    saida_dados()
    try:
        plantio_id = int(input("Digite o ID do plantio ao qual deseja adicionar um manejo: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        return

    # Encontrar o plantio pelo ID
    plantio = next((p for p in dados_plantio if p['id'] == plantio_id), None)
    if not plantio:
        print("Plantio não encontrado.")
        return

    produto, quantidade_total, unidade = calcular_manejo(plantio['area_total'])

    # Gerar ID único para o manejo
    manejo_id = gerar_id([m for p in dados_plantio for m in p['manejamentos']])

    manejo = {
        'id': manejo_id,
        'produto': produto,
        'quantidade_total': quantidade_total,
        'unidade': unidade
    }
    plantio['manejamentos'].append(manejo)
    print("Manejo adicionado com sucesso!")

def saida_dados():
    print("\n--- Dados de Plantio ---")
    if not dados_plantio:
        print("Nenhum dado de plantio registrado.")
    else:
        for plantio in dados_plantio:
            print(f"\nID: {plantio['id']}")
            print(f"Cultura: {plantio['cultura']}")
            print(f"Área de Plantio: {plantio['area_plantio']:.2f} m²")
            print(f"Área das Ruas: {plantio['area_ruas']:.2f} m²")
            print(f"Área Total: {plantio['area_total']:.2f} m²")
            print("Manejamentos:")
            if not plantio['manejamentos']:
                print("  Nenhum manejo registrado.")
            else:
                for manejo in plantio['manejamentos']:
                    print(f"  ID: {manejo['id']}")
                    print(f"    Produto: {manejo['produto']}")
                    print(f"    Quantidade Necessária: {manejo['quantidade_total']:.2f} {manejo['unidade']}")

def atualizar_dados_individual():
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
            plantio_id = int(input("Digite o ID do plantio que deseja atualizar: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            return

        # Encontrar o plantio pelo ID
        plantio = next((p for p in dados_plantio if p['id'] == plantio_id), None)
        if not plantio:
            print("Plantio não encontrado.")
            return

        # Atualizar cultura e áreas
        cultura_antiga = plantio['cultura']
        print(f"Cultura atual: {cultura_antiga}")
        print("Deseja alterar a cultura?")
        print("1. Sim")
        print("2. Não")
        escolha_cultura = input("Escolha uma opção: ").strip()
        if escolha_cultura == '1':
            print("Selecione a nova cultura:")
            for idx, cultura in enumerate(culturas, start=1):
                print(f"{idx}. {cultura}")
            try:
                nova_escolha = int(input("Digite o número da nova cultura: "))
                if nova_escolha < 1 or nova_escolha > len(culturas):
                    print("Opção inválida.")
                    return
                nova_cultura = culturas[nova_escolha - 1]
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
                return
        else:
            nova_cultura = cultura_antiga

        # Recalcular as áreas
        plantio_area, area_ruas, total_area = calcular_area(nova_cultura)

        # Atualizar os dados do plantio
        plantio['cultura'] = nova_cultura
        plantio['area_plantio'] = plantio_area
        plantio['area_ruas'] = area_ruas
        plantio['area_total'] = total_area

        # Recalcular a quantidade total dos manejos baseado na nova area_total
        for manejo in plantio['manejamentos']:
            print(f"\nAtualizando Manejo ID: {manejo['id']} baseado na nova área total.")
            print("Deseja atualizar este manejo agora?")
            print("1. Sim")
            print("2. Não")
            atualizar_manejo_opcao = input("Escolha uma opção: ").strip()
            if atualizar_manejo_opcao == '1':
                # Recalcular quantidade_total com base na nova área_total
                produto, quantidade_total, unidade = calcular_manejo(total_area)
                manejo['produto'] = produto
                manejo['quantidade_total'] = quantidade_total
                manejo['unidade'] = unidade
                print("Manejo atualizado com sucesso!")
            elif atualizar_manejo_opcao == '2':
                continue
            else:
                print("Opção inválida. Manejo não foi atualizado.")

        print("Dados de plantio atualizados com sucesso!")

    elif escolha == 2:
        if not dados_plantio:
            print("Nenhum plantio registrado.")
            return
        saida_dados()
        try:
            plantio_id = int(input("Digite o ID do plantio que contém o manejo que deseja atualizar: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            return

        # Encontrar o plantio pelo ID
        plantio = next((p for p in dados_plantio if p['id'] == plantio_id), None)
        if not plantio:
            print("Plantio não encontrado.")
            return

        if not plantio['manejamentos']:
            print("Nenhum manejo registrado para este plantio.")
            return

        print("\nManejamentos disponíveis:")
        for manejo in plantio['manejamentos']:
            print(f"  ID: {manejo['id']}, Produto: {manejo['produto']}, Quantidade: {manejo['quantidade_total']:.2f} {manejo['unidade']}")

        try:
            manejo_id = int(input("Digite o ID do manejo que deseja atualizar: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            return

        # Encontrar o manejo pelo ID
        manejo = next((m for m in plantio['manejamentos'] if m['id'] == manejo_id), None)
        if not manejo:
            print("Manejo não encontrado.")
            return

        print(f"\nAtualizando Manejo ID: {manejo_id}")
        print("1. Atualizar Produto")
        print("2. Atualizar Quantidade")
        print("3. Atualizar Ambos")
        try:
            opcao_atualizacao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            return

        if opcao_atualizacao == 1:
            novo_produto = input("Digite o novo nome do produto: ")
            manejo['produto'] = novo_produto
            print("Produto atualizado com sucesso!")
        elif opcao_atualizacao == 2:
            # Atualizar quantidade com base na área_total do plantio
            print(f"Atualizando Quantidade com base na área total do plantio: {plantio['area_total']:.2f} m²")
            try:
                quantidade_por_metro = float(input(f"Digite a nova quantidade necessária por metro (em {manejo['unidade']}): "))
                if quantidade_por_metro < 0:
                    print("A quantidade não pode ser negativa.")
                    return
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
                return
            quantidade_total = quantidade_por_metro * plantio['area_total']
            manejo['quantidade_total'] = quantidade_total
            print("Quantidade atualizada com sucesso!")
        elif opcao_atualizacao == 3:
            novo_produto = input("Digite o novo nome do produto: ")
            manejo['produto'] = novo_produto
            print(f"Atualizando Quantidade com base na área total do plantio: {plantio['area_total']:.2f} m²")
            try:
                quantidade_por_metro = float(input(f"Digite a nova quantidade necessária por metro (em {manejo['unidade']}): "))
                if quantidade_por_metro < 0:
                    print("A quantidade não pode ser negativa.")
                    return
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
                return
            quantidade_total = quantidade_por_metro * plantio['area_total']
            manejo['quantidade_total'] = quantidade_total
            print("Produto e quantidade atualizados com sucesso!")
        else:
            print("Opção inválida.")

def deletar_dados():
    print("\n--- Deleção de Dados ---")
    print("1. Deletar Dados de Plantio")
    print("2. Deletar Todos os Manejamentos de um Plantio")
    print("3. Deletar um Manejo Específico de um Plantio")
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
            plantio_id = int(input("Digite o ID do plantio que deseja deletar: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            return
        # Encontrar o plantio pelo ID
        plantio = next((p for p in dados_plantio if p['id'] == plantio_id), None)
        if not plantio:
            print("Plantio não encontrado.")
            return
        dados_plantio.remove(plantio)
        print("Plantio e seus manejos deletados com sucesso!")

    elif escolha == 2:
        if not dados_plantio:
            print("Nenhum plantio registrado.")
            return
        saida_dados()
        try:
            plantio_id = int(input("Digite o ID do plantio que deseja deletar todos os manejos: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            return
        # Encontrar o plantio pelo ID
        plantio = next((p for p in dados_plantio if p['id'] == plantio_id), None)
        if not plantio:
            print("Plantio não encontrado.")
            return
        plantio['manejamentos'].clear()
        print("Todos os manejos deste plantio foram deletados com sucesso!")

    elif escolha == 3:
        if not dados_plantio:
            print("Nenhum plantio registrado.")
            return
        saida_dados()
        try:
            plantio_id = int(input("Digite o ID do plantio que contém o manejo que deseja deletar: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            return
        # Encontrar o plantio pelo ID
        plantio = next((p for p in dados_plantio if p['id'] == plantio_id), None)
        if not plantio:
            print("Plantio não encontrado.")
            return
        if not plantio['manejamentos']:
            print("Nenhum manejo registrado para este plantio.")
            return
        print("\nManejamentos disponíveis:")
        for manejo in plantio['manejamentos']:
            print(f"  ID: {manejo['id']}, Produto: {manejo['produto']}, Quantidade: {manejo['quantidade_total']:.2f} {manejo['unidade']}")
        try:
            manejo_id = int(input("Digite o ID do manejo que deseja deletar: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            return
        manejo = next((m for m in plantio['manejamentos'] if m['id'] == manejo_id), None)
        if not manejo:
            print("Manejo não encontrado.")
            return
        plantio['manejamentos'].remove(manejo)
        print("Manejo deletado com sucesso!")
    else:
        print("Opção inválida.")

def menu():
    while True:
        print("\n=== Aplicação FarmTech ===")
        print("1. Entrada de Dados")
        print("2. Saída de Dados")
        print("3. Atualização de Dados")
        print("4. Adicionar Manejo a Plantio Existente")
        print("5. Deleção de Dados")
        print("6. Sair do Programa")
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha == '1':
            entrada_dados()
        elif escolha == '2':
            saida_dados()
        elif escolha == '3':
            atualizar_dados_individual()
        elif escolha == '4':
            adicionar_manejo()
        elif escolha == '5':
            deletar_dados()
        elif escolha == '6':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
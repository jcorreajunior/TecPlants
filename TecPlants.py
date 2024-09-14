import math
import json
import subprocess
import sys
import os

# Configurar a saída para UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Definição das culturas suportadas
culturas = ['Café', 'Soja']

# Lista para armazenar os dados de plantio com seus manejos
dados_plantio = []

# Função para gerar IDs únicos para plantios e manejos
def gerar_id(dados_plantio, manejo=False):
    if manejo:
        # Gera ID único para manejos em todo o sistema
        manejos = [m for p in dados_plantio for m in p['manejamentos']]
        if not manejos:
            return 1
        else:
            return max(m['id'] for m in manejos) + 1
    else:
        # Gera ID único para plantios
        if not dados_plantio:
            return 1
        else:
            return max(p['id'] for p in dados_plantio) + 1

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

    if cultura == 'Café':
        # Para Café, calcular comprimento_rua automaticamente
        if ruas > 0:
            comprimento_rua = (2 * math.pi * raio) / ruas
        else:
            comprimento_rua = 0
    elif cultura == 'Soja':
        # Para Soja, comprimento_rua = comprimento do plantio
        comprimento_rua = comprimento
    else:
        comprimento_rua = 0

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

    # Cálculo da área total (plantio + ruas)
    total_area = plantio_area + area_ruas

    print(f"\nÁrea de Plantio: {plantio_area:.2f} m²")
    print(f"Área das Ruas: {area_ruas:.2f} m²")
    print(f"Área Total (Plantio + Ruas): {total_area:.2f} m²\n")

    return plantio_area, area_ruas, comprimento_rua, total_area

def calcular_manejo(area_plantio):
    print(f"\nCálculo do manejo de insumos")
    produto = input("Digite o nome do produto (ex: Fosfato): ").strip()
    if not produto:
        print("Nome do produto não pode ser vazio. Tente novamente.")
        return calcular_manejo(area_plantio)
    
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

    # Cálculo da quantidade total baseada na área do plantio
    quantidade_total = quantidade_por_metro * area_plantio

    print(f"\nQuantidade Total Necessária: {quantidade_total:.2f} {unidade}\n")

    return produto, quantidade_total, unidade, quantidade_por_metro

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
    plantio_area, area_ruas, comprimento_rua, total_area = calcular_area(cultura_selecionada)

    # Gerar ID único para o plantio
    plantio_id = gerar_id(dados_plantio)

    # Criar registro de plantio
    plantio = {
        'id': plantio_id,
        'cultura': cultura_selecionada,
        'area_plantio': plantio_area,
        'area_ruas': area_ruas,
        'comprimento_rua': comprimento_rua,
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
            resultado = calcular_manejo(plantio['area_plantio'])
            if resultado:
                produto, quantidade_total, unidade, quantidade_por_metro = resultado
                # Gerar ID único para o manejo
                manejo_id = gerar_id(dados_plantio, manejo=True)
                manejo = {
                    'id': manejo_id,
                    'produto': produto,
                    'quantidade_total': quantidade_total,
                    'unidade': unidade,
                    'quantidade_por_metro': quantidade_por_metro  # Armazenando quantidade_por_metro
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

    resultado = calcular_manejo(plantio['area_plantio'])
    if resultado:
        produto, quantidade_total, unidade, quantidade_por_metro = resultado
        # Gerar ID único para o manejo
        manejo_id = gerar_id(dados_plantio, manejo=True)
        manejo = {
            'id': manejo_id,
            'produto': produto,
            'quantidade_total': quantidade_total,
            'unidade': unidade,
            'quantidade_por_metro': quantidade_por_metro  # Armazenando quantidade_por_metro
        }
        plantio['manejamentos'].append(manejo)
        print("Manejo adicionado com sucesso!")

def saida_dados():
    print("\n--- Dados de Plantio ---")
    if not dados_plantio:
        print("Nenhum dado de plantio registrado.")
    else:
        for plantio in dados_plantio:
            plantio_info = (
                f"ID: {plantio['id']}, "
                f"Cultura: {plantio['cultura']}, "
                f"Área Plantio: {plantio['area_plantio']:.2f} m², "
                f"Área Ruas: {plantio['area_ruas']:.2f} m², "
                f"Área Total: {plantio['area_total']:.2f} m²"
            )
            print(plantio_info)
            if not plantio['manejamentos']:
                manejo_info = "  Nenhum manejo registrado."
                print(manejo_info)
            else:
                for manejo in plantio['manejamentos']:
                    manejo_info = (
                        f"  ID: {manejo['id']}, "
                        f"Produto: {manejo['produto']}, "
                        f"Quantidade: {manejo['quantidade_total']:.2f} {manejo['unidade']}"
                    )
                    print(manejo_info)

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
        plantio_area, area_ruas, comprimento_rua, total_area = calcular_area(nova_cultura)

        # Atualizar os dados do plantio
        plantio['cultura'] = nova_cultura
        plantio['area_plantio'] = plantio_area
        plantio['area_ruas'] = area_ruas
        plantio['comprimento_rua'] = comprimento_rua
        plantio['area_total'] = total_area

        # Atualizar automaticamente os manejos com base na nova area_plantio
        for manejo in plantio['manejamentos']:
            # Recalcular quantidade_total = quantidade_por_metro * nova area_plantio
            manejo['quantidade_total'] = manejo['quantidade_por_metro'] * plantio['area_plantio']
            print(f"Manejo ID {manejo['id']} atualizado automaticamente: Quantidade Total = {manejo['quantidade_total']:.2f} {manejo['unidade']}")

        print("Dados de plantio e manejos atualizados com sucesso!")

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
            novo_produto = input("Digite o novo nome do produto: ").strip()
            if novo_produto:
                manejo['produto'] = novo_produto
                print("Produto atualizado com sucesso!")
            else:
                print("Nome do produto não pode ser vazio.")
        elif opcao_atualizacao == 2:
            # Atualizar quantidade_total com base na quantidade_por_metro e area_plantio
            print(f"Atualizando Quantidade com base na área do plantio: {plantio['area_plantio']:.2f} m²")
            try:
                quantidade_por_metro = float(input(f"Digite a nova quantidade necessária por metro (em {manejo['unidade']}): "))
                if quantidade_por_metro < 0:
                    print("A quantidade não pode ser negativa.")
                    return
                manejo['quantidade_por_metro'] = quantidade_por_metro
                manejo['quantidade_total'] = quantidade_por_metro * plantio['area_plantio']
                print("Quantidade atualizada com sucesso!")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
                return
        elif opcao_atualizacao == 3:
            novo_produto = input("Digite o novo nome do produto: ").strip()
            if novo_produto:
                manejo['produto'] = novo_produto
            else:
                print("Nome do produto não pode ser vazio.")
                return
            # Atualizar quantidade_total com base na quantidade_por_metro e area_plantio
            print(f"Atualizando Quantidade com base na área do plantio: {plantio['area_plantio']:.2f} m²")
            try:
                quantidade_por_metro = float(input(f"Digite a nova quantidade necessária por metro (em {manejo['unidade']}): "))
                if quantidade_por_metro < 0:
                    print("A quantidade não pode ser negativa.")
                    return
                manejo['quantidade_por_metro'] = quantidade_por_metro
                manejo['quantidade_total'] = quantidade_por_metro * plantio['area_plantio']
                print("Produto e quantidade atualizados com sucesso!")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
                return
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

def calculos_estatisticos():
    print("\n--- Cálculos Estatísticos ---")
    # Verificar se há dados para calcular
    if not dados_plantio:
        print("Nenhum dado de plantio disponível para cálculos estatísticos.")
        return

    # Salvar os dados de plantio e manejos em 'dados.json'
    try:
        with open('dados.json', 'w', encoding='utf-8') as f:
            json.dump(dados_plantio, f, ensure_ascii=False, indent=4)
        print("Dados salvos em 'dados.json'.")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")
        return

    # Verificar se 'dados.json' tem dados válidos
    try:
        with open('dados.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
        if not dados:
            print("Nenhum dado encontrado em 'dados.json' para calcular estatísticas.")
            return
    except Exception as e:
        print(f"Erro ao ler 'dados.json': {e}")
        return

    # Executar o script R 'calculos_estatisticos.R'
    try:
        result = subprocess.run(
            ['Rscript', 'calculos_estatisticos.R'],
            capture_output=True,
            text=True,
            encoding='utf-8',  # Especifica a codificação UTF-8
            check=True
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Erro ao executar o script R para cálculos estatísticos.")
        print(e.stderr)
    except FileNotFoundError:
        print("Rscript não encontrado. Certifique-se de que o R está instalado e o 'Rscript' está no PATH.")
    except UnicodeDecodeError as e:
        print("Erro de decodificação ao ler a saída do script R:")
        print(e)

def informacoes_climaticas():
    print("\n--- Informações sobre o Clima ---")
    # Solicitar cidade e país do usuário no Python
    cidade = input("Digite o nome da cidade: ").strip()
    pais = input("Digite o código do país (ex: BR para Brasil, US para Estados Unidos): ").strip()

    if not cidade or not pais:
        print("Cidade e país são obrigatórios. Por favor, tente novamente.")
        return

    # Executar o script R 'clima.R' passando os argumentos cidade e pais
    try:
        result = subprocess.run(
            ['Rscript', 'clima.R', cidade, pais],
            capture_output=True,
            text=True,
            encoding='utf-8',  # Especifica a codificação UTF-8
            check=True
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Erro ao executar o script R para informações climáticas.")
        print(e.stderr)
    except FileNotFoundError:
        print("Rscript não encontrado. Certifique-se de que o R está instalado e o 'Rscript' está no PATH.")
    except UnicodeDecodeError as e:
        print("Erro de decodificação ao ler a saída do script R:")
        print(e)

def carregar_dados():
    global dados_plantio
    if os.path.exists('dados.json'):
        try:
            with open('dados.json', 'r', encoding='utf-8') as f:
                dados_plantio = json.load(f)
            print("Dados carregados com sucesso.")
        except Exception as e:
            print(f"Erro ao carregar os dados: {e}")
    else:
        print("Nenhum dado salvo encontrado. Começando com uma lista vazia.")

def salvar_dados():
    try:
        with open('dados.json', 'w', encoding='utf-8') as f:
            json.dump(dados_plantio, f, ensure_ascii=False, indent=4)
        print("Dados salvos com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

def menu():
    carregar_dados()
    while True:
        print("\n=== Aplicação TecPlants ===")
        print("1. Entrada de Dados")
        print("2. Adicionar Manejo a Plantio Existente")
        print("3. Saída de Dados")
        print("4. Atualização de Dados")
        print("5. Deleção de Dados")
        print("6. Cálculos Estatísticos")
        print("7. Informações sobre o Clima")
        print("8. Sair do Programa")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            entrada_dados()
        elif escolha == '2':
            adicionar_manejo()
        elif escolha == '3':
            saida_dados()
        elif escolha == '4':
            atualizar_dados_individual()
        elif escolha == '5':
            deletar_dados()
        elif escolha == '6':
            calculos_estatisticos()
        elif escolha == '7':
            informacoes_climaticas()
        elif escolha == '8':
            salvar_dados()
            print("Saindo do programa. Até mais!")
            sys.exit()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
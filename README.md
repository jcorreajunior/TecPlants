# TecPlants
 Sistema de controle de plantio e manejo desenvolvido como parte dos trabalhos de desenolvimento da graduação de Inteligencia Artificial.

 Explicação Detalhada
Definição das Culturas:

Utilizamos uma lista culturas para armazenar os tipos de culturas suportadas: Café e Soja.
Vetores de Dados:

dados_plantio: Lista para armazenar informações sobre o plantio (cultura e área).
dados_manejo: Lista para armazenar informações sobre o manejo de insumos (cultura, produto e quantidade total necessária).
Função calcular_area:

Calcula a área plantada com base na cultura selecionada.
Café: Utiliza a fórmula de área de um retângulo (comprimento x largura).
Soja: Utiliza a fórmula de área de um círculo (π x raio²).
Função calcular_manejo:

Coleta informações sobre o manejo de insumos.
Pergunta pelo produto, quantidade necessária por metro (em mL ou litros), número de ruas e comprimento de cada rua.
Calcula a quantidade total necessária, convertendo mL para litros se necessário.
Função entrada_dados:

Permite ao usuário inserir novos dados de plantio e manejo.
Solicita a seleção da cultura, cálcula a área e o manejo, e adiciona os dados aos vetores correspondentes.
Função saida_dados:

Exibe todos os dados armazenados nos vetores dados_plantio e dados_manejo.
Função atualizar_dados:

Permite ao usuário atualizar dados existentes.
O usuário pode escolher entre atualizar dados de plantio ou de manejo.
Solicita a posição dos dados a serem atualizados e permite a entrada de novos valores.
Função deletar_dados:

Permite ao usuário deletar dados existentes.
O usuário pode escolher entre deletar dados de plantio ou de manejo.
Solicita a posição dos dados a serem deletados.
Função menu:

Interface principal da aplicação.
Apresenta as opções disponíveis e direciona para as funções correspondentes com base na escolha do usuário.
Utiliza um loop while True para manter o menu ativo até que o usuário escolha sair.
Execução do Programa:

A função menu é chamada dentro do bloco if __name__ == "__main__": para iniciar a aplicação quando o script for executado.
Como Utilizar a Aplicação
Iniciar o Programa:

Execute o script Python. O menu principal será exibido.
Entrada de Dados:

Escolha a opção 1 no menu.
Selecione a cultura (Café ou Soja).
Insira os parâmetros necessários para o cálculo da área plantada e do manejo de insumos.
Os dados serão armazenados nos vetores correspondentes.
Saída de Dados:

Escolha a opção 2 no menu.
O programa exibirá todos os dados de plantio e manejo armazenados.
Atualização de Dados:

Escolha a opção 3 no menu.
Decida se deseja atualizar dados de plantio ou de manejo.
Selecione o registro que deseja atualizar e insira os novos valores.
Deleção de Dados:

Escolha a opção 4 no menu.
Decida se deseja deletar dados de plantio ou de manejo.
Selecione o registro que deseja deletar.
Sair do Programa:

Escolha a opção 5 no menu para encerrar a aplicação.
Considerações Finais
Validação de Entradas: O código inclui algumas verificações básicas para garantir que as escolhas do usuário sejam válidas. Contudo, para uma aplicação mais robusta, seria interessante adicionar mais validações e tratar possíveis exceções.

Persistência de Dados: Atualmente, os dados são armazenados apenas durante a execução do programa. Para persistir os dados, você pode considerar salvar as informações em arquivos ou utilizar um banco de dados.

Interface Gráfica: A aplicação é baseada em terminal. Para uma melhor experiência do usuário, especialmente para clientes, você pode desenvolver uma interface gráfica utilizando bibliotecas como Tkinter ou PyQt.

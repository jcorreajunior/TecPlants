# TecPlants

## 📄 Descrição

**TecPlants** é uma aplicação de console desenvolvida em Python e R que auxilia na gestão de plantios agrícolas e seus manejos (gestões de insumos). A aplicação permite:

- Inserir, atualizar e deletar dados de plantios e manejos.
- Realizar cálculos estatísticos sobre áreas de plantio e manejos.
- Obter informações climáticas para localidades específicas.

## 🚀 Tecnologias Utilizadas

- **Python 3.x**
- **R 4.x**
- **Pacotes Python:**
  - `math`
  - `json`
  - `subprocess`
  - `sys`
  - `os`
- **Pacotes R:**
  - `jsonlite`
  - `dplyr`
  - `httr`

## 📦 Estrutura do Projeto

TecPlants/ ├── calculos_estatisticos.R ├── clima.R ├── dados.json └── README.md

- **#TecPlants.py:** Script principal em Python para gestão de plantios e manejos.
- **calculos_estatisticos.R:** Script em R para realizar cálculos estatísticos com base nos dados de plantio.
- **clima.R:** Script em R para obter informações climáticas de uma localidade específica.
- **dados.json:** Arquivo JSON que armazena os dados de plantios e manejos. (GitIgnore)
- **README.md:** Este arquivo de documentação.

## 🛠️ Instalação

### 1. Pré-requisitos

- **Python 3.x:** [Download Python](https://www.python.org/downloads/)
- **R 4.x:** [Download R](https://cran.r-project.org/mirrors.html)
- **Rscript:** Certifique-se de que o `Rscript` está acessível no PATH do sistema.

### 2. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/TecPlants.git
cd TecPlants

3. Configurar o Ambiente Python
Embora o script Python utilize apenas módulos padrão, é recomendável criar um ambiente virtual:

python -m venv venv
Ative o ambiente virtual:

Windows:
venv\Scripts\activate

macOS/Linux:
source venv/bin/activate

4. Instalar Pacotes R Necessários
Os scripts R cuidam da instalação dos pacotes necessários automaticamente. No entanto, certifique-se de que você tem uma conexão com a internet para que os pacotes possam ser baixados.

🔧 Configuração
1. Configurar a Chave de API para Informações Climáticas
O script clima.R utiliza a API do OpenWeatherMap para obter informações climáticas. Siga os passos abaixo para configurar sua chave de API:

Registrar-se no OpenWeatherMap:

Acesse OpenWeatherMap e crie uma conta gratuita.
Após o registro, obtenha sua chave de API (API Key).
Inserir a Chave de API no Script R:

Abra o arquivo clima.R em um editor de texto.
Localize a linha:

api_key <- "YOUR_API_KEY"
Substitua "YOUR_API_KEY" pela sua chave de API obtida.

api_key <- "sua_chave_de_api_aqui"
2. Garantir Permissões de Execução
Certifique-se de que os scripts possuem permissões de execução. No terminal, navegue até o diretório do projeto e execute:

chmod +x *.R
chmod +x "*.py"


🏃‍♂️ Uso
1. Executar a Aplicação Python
No terminal, dentro do diretório do projeto, execute:

python "TecPlants V2.py"
2. Navegar pelo Menu
A aplicação apresenta um menu interativo com as seguintes opções:


=== Aplicação TecPlants ===
1. Entrada de Dados
2. Adicionar Manejo a Plantio Existente
3. Saída de Dados
4. Atualização de Dados
5. Deleção de Dados
6. Cálculos Estatísticos
7. Informações sobre o Clima
8. Sair do Programa

Escolha uma opção:
1. Entrada de Dados: Insira novos plantios e seus manejos.
2. Adicionar Manejo a Plantio Existente: Adicione manejos a plantios já registrados.
3. Saída de Dados: Visualize todos os plantios e manejos registrados.
4. Atualização de Dados: Atualize informações de plantios ou manejos específicos.
5. Deleção de Dados: Remova plantios ou manejos conforme necessário.
6. Cálculos Estatísticos: Execute o script R para obter estatísticas baseadas nos dados registrados.
7. Informações sobre o Clima: Obtenha informações climáticas para uma localidade específica.
8. Sair do Programa: Salva os dados e encerra a aplicação.
Ao selecionar a opção 6, a aplicação Python irá:

Salvar os dados atuais no arquivo dados.json.
Executar o script R calculos_estatisticos.R para calcular estatísticas.
Exibir os resultados no console.

4. Obter Informações Climáticas
Ao selecionar a opção 7, a aplicação Python irá:

Solicitar o nome da cidade e o código do país.
Executar o script R clima.R com os parâmetros fornecidos.
Exibir as informações climáticas no console.

🔍 Detalhes Técnicos
1. Gerenciamento de IDs Únicos
Plantios: Cada plantio recebe um ID único incrementando a partir de 1.
Manejamentos: Cada manejo também recebe um ID único, independente do plantio.
2. Estrutura dos Dados
Plantio:

id: Identificador único do plantio.
cultura: Cultura selecionada (Café ou Soja).
area_plantio: Área do plantio em metros quadrados.
area_ruas: Área ocupada pelas ruas na lavoura.
comprimento_rua: Comprimento de cada rua.
area_total: Soma da área do plantio e das ruas.
manejamentos: Lista de manejos associados ao plantio.
Manejo:

id: Identificador único do manejo.
produto: Nome do produto utilizado.
quantidade_total: Quantidade total necessária do produto.
unidade: Unidade de medida (Litros ou Kg).
quantidade_por_metro: Quantidade necessária por metro quadrado.
⚙️ Scripts R
1. calculos_estatisticos.R
Função: Calcula estatísticas descritivas sobre áreas de plantio e manejos.
Uso: Chamado automaticamente pelo script Python ao selecionar a opção de cálculos estatísticos.
2. clima.R
Função: Obtém informações climáticas de uma localidade específica usando a API do OpenWeatherMap.
Uso: Chamado automaticamente pelo script Python ao selecionar a opção de informações climáticas.
🛡️ Licença
Este projeto está licenciado sob a MIT License.

🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

📞 Contato
Para dúvidas ou sugestões, entre em contato através do email: jcorrea.junior@gmail.com

Desenvolvido por Jose Antonio Correa Junior, com utilização da ferramenta ChatGPT.
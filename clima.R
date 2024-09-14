# clima.R

# Função para verificar e instalar pacotes (agora inclui httr2)
verificar_instalar_pacotes <- function(pacote) {
  if (!require(pacote, character.only = TRUE)) {
    cat("Pacote", pacote, "não está instalado. Instalando...\n")
    tryCatch({
      install.packages(pacote, dependencies = TRUE)
      library(pacote, character.only = TRUE)
      cat("Pacote", pacote, "instalado com sucesso!\n")
    }, error = function(e) {
      cat("Erro ao instalar o pacote", pacote, ". Verifique sua conexão com a internet ou tente instalar manualmente.\n")
      stop()
    })
  } else {
    cat("Pacote", pacote, "já está instalado.\n")
  }
}

# Verificar e instalar pacotes necessários
verificar_instalar_pacotes("httr2")
verificar_instalar_pacotes("jsonlite")

# Carregar pacotes
library(httr2)
library(jsonlite)

# Definir a chave da API (substitua 'YOUR_API_KEY' pela sua chave da API)
api_key <- "a6fd59df678d91f04e2b56c472b37044"

# Função para obter os dados meteorológicos usando httr2
obter_dados_meteorologicos <- function() {
  
  # Solicitar cidade e país do usuário
  cidade <- readline(prompt = "Digite o nome da cidade: ")
  pais <- readline(prompt = "Digite o código do país (ex: BR para Brasil, US para Estados Unidos): ")
  
  # Construir a URL da API (cidade e código do país)
  url <- paste0("https://api.openweathermap.org/data/2.5/weather?q=", 
                cidade, ",", pais, "&appid=", api_key, "&units=metric&lang=pt_br")
  
  # Fazer a requisição à API usando httr2 com tratamento de erro
  tryCatch({
    resposta <- request(url) %>%
      req_error(is_error = function(resp) FALSE) %>%
      req_perform()
    
    # Verificar o status da resposta HTTP
    status <- resp_status(resposta)
    
    if (status == 200) {
      # Processar o corpo da resposta
      dados <- resp_body_json(resposta)
      
      if (!is.null(dados$main)) {
        # Extrair e exibir as informações
        cat("Clima em", cidade, ",", pais, ":\n")
        cat("Temperatura:", dados$main$temp, "°C\n")
        cat("Descrição:", dados$weather[[1]]$description, "\n")
        cat("Umidade:", dados$main$humidity, "%\n")
        cat("Velocidade do Vento:", dados$wind$speed, "m/s\n")
      }
    } else if (status == 404) {
      cat("Erro 404: cidade ou país não encontrados. Tente novamente.\n")
      tentar_novamente <- readline(prompt = "Deseja tentar novamente? (s/n): ")
      if (tolower(tentar_novamente) == "s") {
        obter_dados_meteorologicos()
      } else {
        cat("Programa encerrado.\n")
      }
    } else {
      cat("Erro HTTP:", status, "- Tente novamente mais tarde.\n")
    }
  }, error = function(e) {
    cat("Erro ao realizar a requisição: ", e$message, "\n")
  })
}

# Iniciar o processo
obter_dados_meteorologicos()

# clima.R

# Função para verificar e instalar pacotes necessários
verificar_instalar_pacotes <- function(pacote) {
  if (!require(pacote, character.only = TRUE, quietly = TRUE)) {
    cat("Pacote", pacote, "não está instalado. Instalando...\n")
    tryCatch({
      install.packages(pacote, dependencies = TRUE, repos = "http://cran.r-project.org")
      suppressPackageStartupMessages(library(pacote, character.only = TRUE))
      cat("Pacote", pacote, "instalado com sucesso!\n")
    }, error = function(e) {
      cat("Erro ao instalar o pacote", pacote, ". Verifique sua conexão com a internet ou tente instalar manualmente.\n")
      stop()
    })
  } else {
    # Removido: Mensagem informando que o pacote já está instalado
    # Apenas carregamento silencioso do pacote
    suppressPackageStartupMessages(library(pacote, character.only = TRUE))
  }
}

# Verificar e instalar pacotes necessários
verificar_instalar_pacotes("httr2")
verificar_instalar_pacotes("jsonlite")

# Definir a chave da API (substitua 'YOUR_API_KEY' pela sua chave da API)
api_key <- "a6fd59df678d91f04e2b56c472b37044"

# Obter argumentos de linha de comando
args <- commandArgs(trailingOnly = TRUE)
if(length(args) < 2){
    cat("Uso: Rscript clima.R <cidade> <pais>\n")
    quit(status=1)
}
cidade <- args[1]
pais <- args[2]

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
  } else {
    cat("Erro HTTP:", status, "- Tente novamente mais tarde.\n")
  }
}, error = function(e) {
  cat("Erro ao realizar a requisição: ", e$message, "\n")
})
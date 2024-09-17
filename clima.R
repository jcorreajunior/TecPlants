# clima.R

# Definir a localidade para Português do Brasil
Sys.setlocale("LC_ALL", "Portuguese_Brazil.1252")

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
    # Carregamento silencioso do pacote
    suppressPackageStartupMessages(library(pacote, character.only = TRUE))
  }
}

# Verificar e instalar pacotes necessários
verificar_instalar_pacotes("jsonlite")
verificar_instalar_pacotes("httr")

# Função para obter informações climáticas usando a API OpenWeatherMap
obter_clima <- function(cidade, pais) {
  # Substitua 'YOUR_API_KEY' pela sua chave de API do OpenWeatherMap
  api_key <- "YOUR_API_KEY"
  
  if(api_key == "YOUR_API_KEY"){
    cat("Por favor, insira sua chave de API do OpenWeatherMap no script.\n")
    return()
  }
  
  # Construir a URL da API com URLencode para lidar com caracteres especiais
  url <- paste0("http://api.openweathermap.org/data/2.5/weather?q=", 
                URLencode(cidade, reserved = TRUE), ",", pais, "&appid=", api_key, "&units=metric&lang=pt_br")
  
  # Fazer a requisição GET
  resposta <- GET(url)
  
  if(status_code(resposta) != 200){
    cat("Erro ao obter dados climáticos. Verifique o nome da cidade e o código do país, ou sua conexão com a internet.\n")
    return()
  }
  
  # Parsear a resposta JSON
  dados <- fromJSON(content(resposta, "text", encoding = "UTF-8"))
  
  # Extrair informações relevantes
  temp_atual <- dados$main$temp
  temp_min <- dados$main$temp_min
  temp_max <- dados$main$temp_max
  umidade <- dados$main$humidity
  descricao <- dados$weather[[1]]$description
  velocidade_vento <- dados$wind$speed
  
  # Exibir as informações
  cat("\n--- Informações Climáticas ---\n")
  cat("Cidade:", dados$name, "\n")
  cat("Temperatura Atual:", temp_atual, "°C\n")
  cat("Temperatura Mínima:", temp_min, "°C\n")
  cat("Temperatura Máxima:", temp_max, "°C\n")
  cat("Umidade:", umidade, "%\n")
  cat("Descrição:", descricao, "\n")
  cat("Velocidade do Vento:", velocidade_vento, "m/s\n")
}

# Capturar argumentos da linha de comando
args <- commandArgs(trailingOnly = TRUE)

if(length(args) < 2){
  cat("Uso: Rscript clima.R <cidade> <pais>\n")
  cat("Exemplo: Rscript clima.R Sao_Paulo BR\n")
} else {
  cidade <- args[1]
  pais <- args[2]
  
  # Converter para UTF-8
  cidade <- iconv(cidade, from = "UTF-8", to = "UTF-8")
  pais <- iconv(pais, from = "UTF-8", to = "UTF-8")
  
  obter_clima(cidade, pais)
}
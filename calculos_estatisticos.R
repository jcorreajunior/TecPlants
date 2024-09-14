# calculos_estatisticos.R

# Função para verificar e instalar pacotes necessários
verificar_instalar_pacotes <- function(pacote) {
  if (!require(pacote, character.only = TRUE)) {
    cat("Pacote", pacote, "não está instalado. Instalando...\n")
    tryCatch({
      install.packages(pacote, dependencies = TRUE)
      library(pacote, character.only = TRUE)
      cat("Pacote", pacote, "instalado com sucesso!\n")
    }, error = function(e) {
      cat("Erro ao instalar o pacote", pacote,". Verifique sua conexão com a internet ou tente instalar manualmente.\n")
      stop()
    })
  } else {
    cat("Pacote", pacote, "já está instalado.\n")
  }
}

# Verificar e instalar pacotes necessários
verificar_instalar_pacotes("jsonlite")

# Carregar pacotes
library(jsonlite)

# Função para calcular estatísticas
calcular_estatisticas <- function(dados_json) {
  dados <- fromJSON(dados_json)
  
  # Extrair áreas dos plantios
  areas_plantio <- sapply(dados$area_plantio, as.numeric)
  
  # Extrair quantidades dos manejos
  quantidades_manejo <- sapply(dados$manejamentos, function(m) m$quantidade_total)
  
  # Calcular estatísticas
  media_plantio <- mean(areas_plantio)
  sd_plantio <- sd(areas_plantio)
  
  media_manejo <- mean(quantidades_manejo)
  sd_manejo <- sd(quantidades_manejo)
  
  # Exibir resultados
  cat("\n--- Estatísticas dos Plantios ---\n")
  cat("Média da Área dos Plantios:", media_plantio, "m²\n")
  cat("Desvio Padrão da Área dos Plantios:", sd_plantio, "m²\n")
  
  cat("\n--- Estatísticas dos Manejamentos ---\n")
  cat("Média da Quantidade dos Manejamentos:", media_manejo, "\n")
  cat("Desvio Padrão da Quantidade dos Manejamentos:", sd_manejo, "\n")
}

# Verificar se o arquivo 'dados.json' existe
if (file.exists("dados.json")) {
  calcular_estatisticas("dados.json")
} else {
  cat("Arquivo 'dados.json' não encontrado. Por favor, execute o programa Python para gerar os dados.\n")
}
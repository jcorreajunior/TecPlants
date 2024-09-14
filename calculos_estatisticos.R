# calculos_estatisticos.R

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

# Função para calcular estatísticas
calcular_estatisticas <- function(dados_json) {
  dados <- fromJSON(dados_json, simplifyVector = FALSE)
  
  # Verificar se 'dados' não está vazio
  if(length(dados) == 0){
    cat("Nenhum plantio registrado para calcular estatísticas.\n")
    return()
  }
  
  # Extrair áreas dos plantios e converter para numérico
  areas_plantio <- sapply(dados, function(p) as.numeric(p$area_plantio))
  
  # Extrair quantidades dos manejos e converter para numérico
  quantidades_manejo <- sapply(dados, function(p) {
    if(length(p$manejamentos) > 0){
      sapply(p$manejamentos, function(m) as.numeric(m$quantidade_total))
    } else {
      NA
    }
  })
  
  # Unificar as quantidades em um vetor, removendo NAs
  quantidades_manejo <- unlist(quantidades_manejo)
  quantidades_manejo <- quantidades_manejo[!is.na(quantidades_manejo)]
  
  # Verificar se 'areas_plantio' contém valores numéricos
  if(any(is.na(areas_plantio))){
    cat("Aviso: Algumas áreas de plantio não são numéricas e foram convertidas para NA.\n")
  }
  
  # Verificar se existem áreas válidas
  if(all(is.na(areas_plantio))){
    cat("Erro: Nenhuma área de plantio válida para calcular estatísticas.\n")
    return()
  }
  
  # Calcular estatísticas, removendo NAs
  media_plantio <- mean(areas_plantio, na.rm = TRUE)
  sd_plantio <- sd(areas_plantio, na.rm = TRUE)
  
  # Verificar se existem manejos válidos
  if(length(quantidades_manejo) == 0){
    media_manejo <- NA
    sd_manejo <- NA
    cat("Nenhuma quantidade de manejo válida para calcular estatísticas.\n")
  } else {
    media_manejo <- mean(quantidades_manejo, na.rm = TRUE)
    sd_manejo <- sd(quantidades_manejo, na.rm = TRUE)
  }
  
  # Exibir resultados
  cat("\n--- Estatísticas dos Plantios ---\n")
  cat("Média da Área dos Plantios:", media_plantio, "m²\n")
  cat("Desvio Padrão da Área dos Plantios:", sd_plantio, "m²\n")
  
  cat("\n--- Estatísticas dos Manejamentos ---\n")
  if(!is.na(media_manejo)){
    cat("Média da Quantidade dos Manejamentos:", media_manejo, "\n")
    cat("Desvio Padrão da Quantidade dos Manejamentos:", sd_manejo, "\n")
  } else {
    cat("Nenhum manejo válido para calcular estatísticas.\n")
  }
}

# Verificar se o arquivo 'dados.json' existe
if (file.exists("dados.json")) {
  calcular_estatisticas("dados.json")
} else {
  cat("Arquivo 'dados.json' não encontrado. Por favor, execute o programa Python para gerar os dados.\n")
}
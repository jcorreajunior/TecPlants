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
verificar_instalar_pacotes("dplyr")

# Função para calcular estatísticas
calcular_estatisticas <- function(dados_json) {
  dados <- fromJSON(dados_json, simplifyVector = FALSE)
  
  if(length(dados) == 0){
    cat("Nenhum plantio registrado para calcular estatísticas.\n")
    return()
  }
  
  # Extrair áreas dos plantios
  plantios_df <- do.call(rbind, lapply(dados, function(p) {
    data.frame(
      id = p$id,
      cultura = p$cultura,
      area_plantio = as.numeric(p$area_plantio),
      area_ruas = as.numeric(p$area_ruas),
      comprimento_rua = as.numeric(p$comprimento_rua),
      area_total = as.numeric(p$area_total),
      stringsAsFactors = FALSE
    )
  }))
  
  # Estatísticas das áreas de plantio
  media_area <- mean(plantios_df$area_plantio, na.rm = TRUE)
  sd_area <- sd(plantios_df$area_plantio, na.rm = TRUE)
  mediana_area <- median(plantios_df$area_plantio, na.rm = TRUE)
  
  cat("\n--- Estatísticas das Áreas de Plantio ---\n")
  cat("Média da Área dos Plantios:", round(media_area, 2), "m²\n")
  cat("Desvio Padrão da Área dos Plantios:", round(sd_area, 2), "m²\n")
  cat("Mediana da Área dos Plantios:", round(mediana_area, 2), "m²\n")
  
  # Extrair manejamentos
  manejamentos <- do.call(rbind, lapply(dados, function(p) {
    if(length(p$manejamentos) > 0){
      do.call(rbind, lapply(p$manejamentos, function(m) {
        data.frame(
          id_plantio = p$id,
          id_manejo = m$id,
          produto = m$produto,
          quantidade_total = as.numeric(m$quantidade_total),
          unidade = m$unidade,
          quantidade_por_metro = as.numeric(m$quantidade_por_metro),
          stringsAsFactors = FALSE
        )
      }))
    } else {
      NULL
    }
  }))
  
  if(nrow(manejamentos) == 0){
    cat("Nenhum manejo registrado para calcular estatísticas.\n")
    return()
  }
  
  # Sum manejamentos per plantio and unit
  sum_manejamentos <- manejamentos %>%
    group_by(id_plantio, unidade) %>%
    summarise(total_quantidade = sum(quantidade_total, na.rm = TRUE), .groups = 'drop')
  
  # Merge sum_manejamentos back to plantios_df
  plantios_manejamentos <- plantios_df %>%
    left_join(sum_manejamentos, by = c("id" = "id_plantio"))
  
  # Agora, plantios_manejamentos tem múltiplas linhas por plantio, uma por unidade
  
  # Para correlação, separar por unidade
  unidades <- unique(sum_manejamentos$unidade)
  
  for(u in unidades){
    temp_df <- plantios_manejamentos %>%
      filter(unidade == u) %>%
      select(area_plantio, total_quantidade)
    
    if(nrow(temp_df) < 2){
      cat("\nNão é possível calcular a correlação para unidade:", u, "devido a menos de duas observações.\n")
      next
    }
    
    correlação <- cor(temp_df$area_plantio, temp_df$total_quantidade, use = "complete.obs")
    
    cat("\n--- Correlação entre Área de Plantio e Quantidade de Manejos (", u, ") ---\n", sep = "")
    cat("Correlação:", round(correlação, 2), "\n")
  }
  
  # Estatísticas dos manejamentos
  media_manejo <- mean(manejamentos$quantidade_total, na.rm = TRUE)
  sd_manejo <- sd(manejamentos$quantidade_total, na.rm = TRUE)
  
  cat("\n--- Estatísticas dos Manejamentos ---\n")
  cat("Média da Quantidade dos Manejamentos:", round(media_manejo, 2), "\n")
  cat("Desvio Padrão da Quantidade dos Manejamentos:", round(sd_manejo, 2), "\n")
  
  # Estatísticas por tipo de manejo
  manejamentos_tipo <- manejamentos %>%
    group_by(produto, unidade) %>%
    summarise(
      total_quantidade = sum(quantidade_total, na.rm = TRUE),
      media_quantidade = mean(quantidade_total, na.rm = TRUE),
      sd_quantidade = sd(quantidade_total, na.rm = TRUE),
      .groups = 'drop'
    )
  
  cat("\n--- Estatísticas por Tipo de Manejo ---\n")
  print(manejamentos_tipo)
}

# Verificar se o arquivo 'dados.json' existe
if (file.exists("dados.json")) {
  calcular_estatisticas("dados.json")
} else {
  cat("Arquivo 'dados.json' não encontrado. Por favor, execute o programa Python para gerar os dados.\n")
}
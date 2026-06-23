"""
Fator de Impacto Operacional no Recebimento (FIOR)
Módulo de Processamento Analítico de Dados Logísticos

Autor: [Seu Nome Completo]
Ano: 2026
Versão: 1.0.0
Licença: MIT
"""

import pandas as pd
import os
from datetime import datetime

def calcular_fior_unidade(urgencia, divergencia, qualidade, ambiente):
    """
    Executa a computação matemática isolada da fórmula ponderada do FIOR.
    Restringe os limites e valida os parâmetros inseridos.
    """
    for nota in [urgencia, divergencia, qualidade, ambiente]:
        if not (1 <= nota <= 5):
            raise ValueError("As notas de entrada devem obedecer ao intervalo discreto de 1 a 5.")
            
    # Vetor de pesos calibrados (Pesos Oficiais da Metodologia FIOR)
    w = [0.4, 0.3, 0.2, 0.1]
    
    fior_calculado = (urgencia * w[0]) + (divergencia * w[1]) + (qualidade * w[2]) + (ambiente * w[3])
    return round(fior_calculado, 2)


def mapear_zona_criticidade(score_fior):
    """Mapeia o resultado numérico contínuo nas zonas discretas de impacto."""
    if 1.0 <= score_fior <= 2.2:
        return "🟢 Zona Verde (Baixo Impacto)"
    elif 2.3 <= score_fior <= 3.7:
        return "🟡 Zona Amarela (Médio Impacto)"
    else:
        return "🔴 Zona Vermelha (Gestão de Crise)"


def processar_fior_lote(caminho_planilha_entrada):
    """
    Carrega banco de dados em lote (.xlsx ou .csv), aplica a equação matemática
    vetorizada de alta performance via Pandas e exporta o consolidado analítico.
    """
    if not os.path.exists(caminho_planilha_entrada):
        raise FileNotFoundError(f"Arquivo '{caminho_planilha_entrada}' não localizado na pasta raiz.")

    print(f"🔄 [ETL] Iniciando leitura do banco de dados: {caminho_planilha_entrada}")
    
    # Suporte nativo a planilhas Excel ou arquivos CSV
    if caminho_planilha_entrada.endswith('.xlsx'):
        df = pd.read_excel(caminho_planilha_entrada)
    else:
        # Se for CSV, adota o padrão de separador de ponto e vírgula comum no Excel brasileiro
        df = pd.read_csv(caminho_planilha_entrada, sep=';', encoding='utf-8')

    # Validação de conformidade estrutural do arquivo de entrada
    colunas_obrigatorias = ['F_urg', 'F_div', 'F_qual', 'F_amb']
    if not all(col in df.columns for col in colunas_obrigatorias):
        raise KeyError(f"A planilha de entrada deve conter obrigatoriamente as colunas: {colunas_obrigatorias}")

    # Definição dos coeficientes analíticos (Pesos oficiais)
    w_urg, w_div, w_qual, w_amb = 0.4, 0.3, 0.2, 0.1

    print("📐 [ANALYSIS] Executando cálculo vetorizado da equação FIOR...")
    
    # Processamento em vetor (otimização de memória e performance)
    df['Resultado_FIOR'] = (
        (df['F_urg'] * w_urg) + 
        (df['F_div'] * w_div) + 
        (df['F_qual'] * w_qual) + 
        (df['F_amb'] * w_amb)
    ).round(2)

    # Aplicação das regras de negócio para classificação
    df['Classificacao_FIOR'] = df['Resultado_FIOR'].apply(mapear_zona_criticidade)
    
    # Carimbo de data/hora para auditoria do pipeline de dados
    df['Timestamp_Processamento'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    # Exportação dos resultados analíticos para uma nova planilha
    arquivo_saida = "fior_resultados_consolidados.xlsx"
    df.to_excel(arquivo_saida, index=False)
    
    print("\n" + "="*60)
    print("✅ COMPUTAÇÃO CONCLUÍDA COM SUCESSO!")
    print(f"📊 Relatório Analítico Gerado: '{arquivo_saida}'")
    print(f"📈 Total de Linhas Auditadas: {len(df)}")
    print("="*60 + "\n")
    return arquivo_saida


if __name__ == "__main__":
    # Ponto de entrada padrão para execução local do pipeline de dados
    # Certifique-se de que o arquivo 'recebimentos.xlsx' exista no mesmo diretório.
    try:
        processar_fior_lote("recebimentos.xlsx")
    except Exception as e:
        print(f"❌ Erro na execução do pipeline: {e}")

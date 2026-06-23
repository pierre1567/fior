"""
Gerador de Massa de Dados para Teste do FIOR
Gera um arquivo 'recebimentos.xlsx' com 1000 registros realistas.

Autor: Pierre | Ano: 2026
"""

import pandas as pd
import random
from datetime import datetime, timedelta

print("⏳ Gerando 1.000 registros de recebimento fictícios...")

# Listas de apoio para criar dados realistas
fornecedores = [
    "TechComponentes Brasil", "Metalúrgica Vale do Aço", "Distribuidora Rio Doces",
    "Pneumática Central", "EletroIndústria Schneider", "Parafusos & Cia",
    "Sistemas de Automação Alfa", "Rolamentos Universais LTDA"
]

tipos_material = ["Rolamento Axial", "Válvula Solenóide", "Cabo de Cobre 10mm", "Parafuso Sextavado", "Servo Motor", "Sensor de Presença", "Graxa Industrial", "Placa de Circuito"]

dados = []

# Data inicial para simular um histórico de 30 dias atrás até hoje
data_base = datetime.now() - timedelta(days=30)

for i in range(1, 1001):
    id_nf = 50000 + i
    fornecedor = random.choice(fornecedores)
    material = random.choice(tipos_material)
    quantidade = random.randint(5, 500)
    data_recebimento = (data_base + timedelta(hours=random.randint(1, 720))).strftime('%d/%m/%Y %H:%M')
    
    # Simula pesos realistas: a maioria dos recebimentos é padrão (notas baixas), 
    # mas alguns são caóticos (notas altas)
    f_urg = random.choices([1, 2, 3, 4, 5], weights=[0.50, 0.25, 0.15, 0.07, 0.03])[0]
    f_div = random.choices([1, 2, 3, 4, 5], weights=[0.60, 0.20, 0.10, 0.06, 0.04])[0]
    f_qual = random.choices([1, 2, 3, 4, 5], weights=[0.70, 0.15, 0.08, 0.05, 0.02])[0]
    f_amb = random.choices([1, 2, 3, 4, 5], weights=[0.65, 0.20, 0.10, 0.04, 0.01])[0]
    
    dados.append({
        "Nota_Fiscal": id_nf,
        "Data_Recebimento": data_recebimento,
        "Fornecedor": fornecedor,
        "Item": material,
        "Qtd_Volumes": quantidade,
        "F_urg": f_urg,
        "F_div": f_div,
        "F_qual": f_qual,
        "F_amb": f_amb
    })

# Transforma em DataFrame do Pandas
df_massa = pd.DataFrame(dados)

# Salva no formato que o seu script fior_excel_connector.py espera
df_massa.to_excel("recebimentos.xlsx", index=False)

print("✅ Planilha 'recebimentos.xlsx' gerada com sucesso na pasta atual!")
print(f"📊 Estrutura criada: {df_massa.shape[0]} linhas e {df_massa.shape[1]} colunas.")
# FIOR - Fator de Impacto Operacional no Recebimento 📊🚚

O **FIOR** é uma metodologia analítica e matemática autoral desenvolvida para quantificar a complexidade operacional instantânea enfrentada por equipes de recebimento e conferência de materiais em almoxarifados industriais e centros de distribuição.

Ao contrário de indicadores tradicionais como o OTIF (que avalia o fornecedor) ou o Tempo de Ciclo (que apenas cobra velocidade da equipe), o FIOR mede o grau de impacto que variáveis externas e imprevistos têm sobre a eficiência do setor.

---

## 📐 A Formulação Matemática

O modelo utiliza a abordagem de Análise Multicritério de Decisão (MCDM) com uma estrutura de ponderação linear restrita:

$$FIOR = (F_{urg} \times 0.4) + (F_{div} \times 0.3) + (F_{qual} \times 0.2) + (F_{amb} \times 0.1)$$

Onde cada fator recebe uma nota discreta de 1 a 5 com base no cenário real do pátio:
* **F_urg (Urgência):** Severidade da demanda (ex: item de máquina parada ou estoque de rotina).
* **F_div (Divergência):** Complexidade fiscal, cadastral ou documental da Nota Fiscal.
* **F_qual (Qualidade):** Nível de exigência na conferência física (itens sem identificação, avarias).
* **F_amb (Ambiente):** Estado da infraestrutura e estresse físico (chuva, queda de sistema, pátio saturado).

---

## 🟢 Matriz de Criticidade (Zonas de Impacto)

O resultado final do FIOR varia de **1.0 a 5.0**, classificando a operação em três zonas de criticidade:

* **De 1.0 a 2.2 | Zona Verde (Baixo Impacto):** Fluxo padrão, sem gargalos.
* **De 2.3 a 3.7 | Zona Amarela (Médio Impacto):** Operação impactada, exigindo tratativas burocráticas ou esforço extra de conferência.
* **De 3.8 a 5.0 | Zona Vermelha (Gestão de Crise):** Caos operacional. Justifica quedas bruscas na produtividade e exige atuação da liderança.

---

## 💻 Implementação Automatizada com Python (`pandas`)

O projeto conta com um script em Python que automatiza o cálculo em lote. Ele lê uma planilha comum do Excel contendo os registros de Notas Fiscais e as respectivas notas dos fatores, injeta a lógica matemática e gera um relatório consolidado com os resultados e classificações.

### Pré-requisitos
```bash
pip install pandas openpyxl

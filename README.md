# Pipeline de Engenharia de Dados e Detecção de Fraudes - Fintech

Este repositório contém a aplicação desenvolvida para consolidar dados brutos de transações financeiras, realizar o alinhamento temporal, tratar inconsistências e aplicar técnicas estatísticas para a detecção de potenciais fraudes (outliers).

## 🚀 Tecnologias Utilizadas
* **Python 3**
* **Pandas** (Tratamento, Limpeza e Agregação de Dados)
* **NumPy** (Operações Vetorizadas de Alta Performance)
* **Matplotlib** (Visualização Gráfica Orientada a Objetos)

## 📋 Requisitos Implementados

1. **Ingestão e Limpeza:**
   * Leitura otimizada do arquivo com encoding legado (`latin1`).
   * Imputação de valores ausentes utilizando a **mediana agrupada por estado**.
   * Criação de metadados estáticos para rastreabilidade (`plataforma='Mobile'`).

2. **Engenharia de Dados & Alinhamento Temporal:**
   * Conversão e localização de fuso horário brasileiro (`America/Sao_Paulo`).
   * Extração de features temporais (`dia_semana` e `mes`).
   * Deduplicação de registros mantendo a primeira ocorrência.

3. **Operações Vetorizadas:**
   * Filtros eficientes utilizando operadores condicionais Bitwise (`&`, `|`).
   * Cruzamento e enriquecimento de dados via estruturas de mapeamento (`.map()`).
   * Agregação e tabelas dinâmicas estruturadas com subtotais gerais (`margins=True`).

4. **Detecção Estatística de Anomalias (Z-Score):**
   * Implementação matemática vetorizada para cálculo de dispersão estatística segmentada por região geográfica:
     \[\mathbb{Z} = \frac{x - \mu}{\sigma}\]
   * Isolamento de transações suspeitas com limite crítico de desvio padrão (\(\mathbb{Z} > 2.5\)).

5. **Visualização Gráfica:**
   * Geração de gráfico com a API Orientada a Objetos do Matplotlib contendo a evolução de transações diárias combinada à suavização por média móvel de 7 dias.

## 🔧 Como Executar o Projeto

1. Certifique-se de colocar o arquivo de dados `transacoes.csv` (gerado pelo script anexo do exercício) na mesma pasta do código.
2. Instale as dependências necessárias:
   ```bash
   pip install pandas numpy matplotlib
   ```
3. Execute a aplicação principal:
   ```bash
   python main.py
   ```

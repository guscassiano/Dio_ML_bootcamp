# 📊 Demonstração de Métricas de Avaliação de Modelos de Machine Learning

Este notebook do Google Colab demonstra de forma interativa como funcionam as métricas de avaliação de desempenho para modelos de Machine Learning, focando em problemas de classificação binária. Ele gera dados aleatórios para simular rótulos reais e previsões de um modelo, permitindo a visualização da **Matriz de Confusão** e o cálculo de métricas essenciais como **Acurácia**, **Precisão**, **Recall (Sensibilidade)**, **Especificidade** e **F1-Score**.

## ✨ Destaques

* **Simulação de Dados:** Gera rótulos reais (`y_true`) e previsões do modelo (`y_pred`) de forma aleatória, com a possibilidade de controlar a acurácia das previsões.
* **Matriz de Confusão Visual:** Apresenta a matriz de confusão de forma clara e colorida utilizando `seaborn` e `matplotlib`, facilitando a identificação de Verdadeiros Positivos, Verdadeiros Negativos, Falsos Positivos e Falsos Negativos.
* **Cálculo de Métricas:** Calcula e exibe as principais métricas de avaliação de desempenho para classificação binária.
* **Interpretação Clara:** Oferece uma explicação detalhada de cada componente da matriz e das métricas calculadas.

## 🚀 Como Executar

1.  **Copie o código ou abra o arquivo:** As seções de código Python estão formatadas em blocos de código no arquivo `Matriz_de_confusão.ipynb`. Você pode copiar cada bloco e colar em células separadas no seu notebook do Colab ou abrir o arquivo diretamente.
2.  **Abra o Google Colab:** Vá para [https://colab.research.google.com/](https://colab.research.google.com/).
3.  **Crie um novo Notebook:** Clique em "File" (Arquivo) -> "New notebook" (Novo notebook).
4.  **Cole o código nas células:** Cole cada bloco de código Python (delimitado por três crases ` ```python ` e ` ``` `) em uma nova célula do Colab.
5.  **Execute as Células:** Você pode executar as células individualmente (clicando no ícone de "play" ao lado de cada célula) ou executar todas as células em sequência (clicando em `Runtime` > `Run all`).

## ⚙️ Código e Configuração

### Instalação de Bibliotecas (se necessário)

Embora `numpy`, `sklearn`, `matplotlib` e `seaborn` já venham pré-instalados no Colab, você pode incluir esta célula caso esteja executando em um ambiente diferente:

```python
# !pip install numpy scikit-learn matplotlib seaborn

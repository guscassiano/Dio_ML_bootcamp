# 🛍️ Sistema de Recomendação de Produtos por Similaridade de Imagem

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat&logo=scikit-learn&logoColor=white)
![Google Colab](https://img.shields.io/badge/Google%20Colab-Ready-yellow.svg)

## 📖 Sobre o Projeto

Este projeto implementa um sistema de recomendação de produtos baseado puramente em **similaridade visual**. Através de uma imagem de um produto, o sistema é capaz de encontrar e sugerir outros itens do catálogo que possuam aparência semelhante.

O diferencial desta abordagem é que a recomendação não utiliza metadados textuais (como marca, preço, categoria ou descrição), focando exclusivamente nas características visuais:

* **Formato e Design**
* **Cor e Paleta**
* **Textura e Padrões**

Este modelo foi desenvolvido para ser executado em um ambiente Google Colab, aproveitando a aceleração por GPU para o processamento das imagens.

---

## ⚙️ Como Funciona

O núcleo do sistema utiliza uma técnica de Deep Learning chamada **Transfer Learning** (Aprendizagem por Transferência) para "entender" o conteúdo visual de cada imagem. O processo pode ser dividido em três etapas principais:

1.  **Modelo Pré-treinado (Feature Extractor)**
    * Utilizamos uma Rede Neural Convolucional (CNN) poderosa, a **VGG16**, que foi previamente treinada no imenso dataset ImageNet. Isso significa que o modelo já possui um vasto conhecimento sobre como identificar formas, bordas, cores e texturas.
    * Removemos a camada final de classificação do modelo, pois nosso objetivo não é classificar a imagem (dizer se é um "sapato" ou uma "camiseta"), mas sim extrair sua essência visual.

2.  **Extração de Características (Embeddings)**
    * Cada imagem do nosso catálogo é processada pelo modelo modificado.
    * A saída para cada imagem é um **vetor de características** (ou *embedding*), que é uma representação numérica de sua aparência. Neste projeto, cada imagem é transformada em um vetor de 512 dimensões.

3.  **Cálculo de Similaridade (Nearest Neighbors)**
    * Com todas as imagens representadas como vetores, utilizamos o algoritmo **Nearest Neighbors** (Vizinhos Mais Próximos) com a métrica de **Similaridade de Cosseno**.
    * Dado o vetor de uma nova imagem de busca, o algoritmo calcula eficientemente quais vetores (e, consequentemente, quais imagens) estão mais "próximos" no espaço de características, retornando os produtos mais similares.

---

## 🚀 Tecnologias Utilizadas

* **Python 3**
* **TensorFlow / Keras:** Para carregar o modelo VGG16 e realizar a extração de características.
* **Scikit-learn:** Para implementar o algoritmo de Nearest Neighbors.
* **NumPy:** Para manipulação eficiente dos vetores de características.
* **Matplotlib:** Para visualização dos resultados.
* **Google Colab:** Como ambiente de desenvolvimento e execução.

---

## ▶️ Como Executar

Este projeto foi projetado para ser executado facilmente no Google Colab.

1.  **Clone o Repositório (Opcional)**
    ```bash
    git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
    ```

2.  **Abra o Notebook no Google Colab**
    * Faça o upload do arquivo `.ipynb` para o seu Google Colab (`Arquivo` > `Fazer upload de notebook...`).
    * Ou, se o seu repositório for público, abra diretamente pelo link:
        ```
        [https://colab.research.google.com/github/SEU-USUARIO/SEU-REPOSITORIO/blob/main/NOME_DO_SEU_NOTEBOOK.ipynb](https://colab.research.google.com/github/SEU-USUARIO/SEU-REPOSITORIO/blob/main/NOME_DO_SEU_NOTEBOOK.ipynb)
        ```

3.  **Execute as Células**
    * Clique em `Ambiente de execução` > `Executar tudo`.
    * O notebook cuidará da instalação das dependências, download do dataset de exemplo e de todo o processo.

    > **IMPORTANTE**: A célula de download de dados (Célula 2) possui uma opção para baixar um dataset do Kaggle. Para usá-la, você precisará de uma conta no Kaggle e de um token de API (`kaggle.json`). A célula irá pedir seu `username` e `key` para prosseguir.

---

## ✨ Resultados

Ao final da execução, o sistema irá selecionar uma imagem aleatória do dataset como busca e exibirá os 6 produtos mais visualmente similares encontrados, junto com o score de similaridade.

**Exemplo de Saída:**

| Imagem da Busca                               |
| :--------------------------------------------: |
| ![Imagem de um sapato](URL_IMAGEM_BUSCA_AQUI)  |

| **Recomendações (Produtos Similares)** |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| ![Rec 1](URL_REC_1_AQUI) `Similaridade: 0.98` | ![Rec 2](URL_REC_2_AQUI) `Similaridade: 0.97` | ![Rec 3](URL_REC_3_AQUI) `Similaridade: 0.96` |
| ![Rec 4](URL_REC_4_AQUI) `Similaridade: 0.95` | ![Rec 5](URL_REC_5_AQUI) `Similaridade: 0.95` | ![Rec 6](URL_REC_6_AQUI) `Similaridade: 0.94` |

*(Nota: Imagens são apenas representativas. A saída real é gerada pelo Matplotlib no notebook.)*

---

## 🔮 Possíveis Melhorias e Próximos Passos

Este projeto é uma base sólida. Para uma aplicação em produção, as seguintes melhorias podem ser implementadas:

* **Índice de Similaridade Otimizado:** Para catálogos com milhões de produtos, substituir o `NearestNeighbors` do Scikit-learn por bibliotecas de busca de similaridade aproximada (ANN) como **Faiss (do Facebook)** ou **Annoy (do Spotify)**, que são ordens de magnitude mais rápidas.
* **Fine-Tuning do Modelo:** Para obter resultados ainda mais precisos, o modelo VGG16 pode ser "ajustado finamente" (fine-tuned) com o próprio dataset de produtos.
* **Experimentar Outras Arquiteturas:** Testar modelos mais modernos como `ResNet50`, `EfficientNet` ou `MobileNetV2` pode trazer um melhor balanço entre acurácia e velocidade.
* **Criação de uma API:** Empacotar o modelo e o índice de similaridade em uma API REST (usando Flask ou FastAPI) para que possa ser consumido por um site ou aplicativo.

---

## 👨‍💻 Autor

**[Gustavo Cassiano Pinto]**

* **LinkedIn:** [linkedin.com/ingustavocassiano-dev](https://linkedin.com/in/gustavocassiano-dev)
* **GitHub:** [github.com/guscassiano](https://github.com/guscassiano)
* **Email:** gucpinto26@gmail.com


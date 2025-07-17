# 🐱🐶 Cats vs Dogs: Transfer Learning

## Descrição do Projeto

Neste experimento, aplicamos técnicas de **Transfer Learning** para classificar imagens de gatos e cachorros. Utilizamos um dataset grande (12.500 imagens por classe) para mitigar sobreajuste observado em conjuntos menores. O objetivo é treinar uma rede neural eficiente e avaliar seu desempenho em dados inéditos.

## Estrutura do Notebook

1. **Setup e imports**
   Importamos bibliotecas essenciais (`tensorflow`, `keras`, `ImageDataGenerator`, etc.) e configuramos o ambiente (incluindo GPU quando disponível).

2. **Download e extração do dataset**
   Utilizamos `wget` para baixar o dataset *Kaggle Cats and Dogs* e extraímos seu conteúdo.

3. **Verificação da quantidade de imagens**
   Confirmamos que cada classe possui 12 501 imagens.

4. **Preparação dos diretórios de treino e teste**
   Estruturamos pastas em `/tmp/cats-v-dogs/{training,testing}/{cats,dogs}` para organizar os dados.

5. **Função `split_data`**
   Implementamos uma função que seleciona e distribui aleatoriamente 90 % das imagens para treinamento e 10 % para validação/teste. Ignoramos arquivos com tamanho zero.

6. **Verificação final do split**
   Validamos que foram selecionadas \~22 500 imagens para treino (11 250 por classe) e \~2 500 para teste (1 250 por classe).

7. **Construção do modelo**
   Montamos um modelo `Sequential` com camadas Conv2D e MaxPooling, seguido por Flatten + Dense + saída sigmoid. Compilamos com `RMSprop`, `binary_crossentropy` e métrica de acurácia.

8. **Geradores de imagens**
   Utilizamos `ImageDataGenerator` com `rescale=1./255` para carregar imagens de treino e validação em lotes de 250 imagens de 150×150 pixels.

9. **Treinamento**
   Treinamos o modelo com `model.fit()` por 15 épocas, com `steps_per_epoch=90` e `validation_steps=6`.

10. **Visualização dos resultados**
    Plotamos acurácia e perda para treino e validação ao longo das épocas, avaliando sobreajuste.

11. **Teste interativo**
    Permitimos upload de imagens para predição (“cat” ou “dog”) pelo modelo treinado.

---

## Como executar

1. Acesse o Colab pelo badge.
2. Execute todas as células. O download (\~800 MB) pode demorar.
3. Após o treino, faça upload de imagens para testar o classificador em tempo real.

---

## Aprendizados

* Como estruturar um pipeline de classificação de imagens com `ImageDataGenerator`.
* Técnicas de pré-processamento e validação de dados (ex.: remover arquivos corrompidos).
* Efeitos de datasets maiores na redução de overfitting.
* Monitoramento de métricas durante o treino e uso prático do modelo com upload de imagens.

---

## Possíveis melhorias

* Reimplementar com **Transfer Learning** usando modelos pré-treinados (como VGG16, InceptionV3, ResNet) para melhorar performance.
* Aplicar **Data Augmentation** para ampliar variedade de dados.
* Ajustar hiperparâmetros (número de camadas, tipo de otimizador, scheduler) para maior robustez.
* Salvar e carregar o modelo treinado (`model.save()` / `load_model()`).

---

## Estrutura de pastas

```text
/tmp/cats-v-dogs/
├── training/
│   ├── cats/
│   └── dogs/
└── testing/
    ├── cats/
    └── dogs/
```

Cada subpasta contém imagens `.jpg` usadas no treinamento e validação.

---

## Requisitos

* Python 3.x
* TensorFlow 2.x
* GPU opcional, mas recomendada para acelerar o treino

```bash
pip install tensorflow matplotlib
```

---

## Licença & Créditos

Este notebook foi desenvolvido como parte do *bootcamp DIO – Transfer Learning* e **baseado no trabalho original de Laurence Moroney**, disponível em seu repositório para o evento *ML Day Tokyo* — Lab6 – *Cats‑v‑Dogs* no Colab.  
Agradeço ao Laurence por compartilhar este excelente recurso com a comunidade.

Link original: [Lab6 – Cats‑v‑Dogs por Laurence Moroney](https://colab.research.google.com/github/lmoroney/mlday-tokyo/blob/master/Lab6-Cats-v-Dogs.ipynb#scrollTo=3sd9dQWa23aj)


# 🐶🐱 Classificador de Gatos e Cachorros com VGG16 (Transfer Learning)

Este projeto utiliza **Transfer Learning** com o modelo **VGG16** para classificar imagens entre **gatos e cachorros**, usando o dataset PetImages da Microsoft.

## 🔍 Sobre o Projeto

A ideia principal é aproveitar o poder de redes neurais pré-treinadas (no caso, o VGG16 treinado no ImageNet) e adaptar suas camadas finais para uma nova tarefa: distinguir entre gatos e cachorros.

## 📁 Dataset

Utilizamos o conjunto de dados fornecido pela Microsoft:

- Link: [PetImages Dataset (Microsoft)](https://download.microsoft.com/download/3/e/1/3e1c3f21-ecdb-4869-8368-6deba77b919f/kagglecatsanddogs_5340.zip)
- Contém: ~25.000 imagens (metade gatos, metade cachorros)

## 🧠 Modelo Utilizado

- **Base**: VGG16 (pré-treinada no ImageNet)
- **Camadas adicionais**: Flatten, Dense, Dropout e camada de saída com ativação sigmoide
- **Compilação**: `optimizer='adam'`, `loss='binary_crossentropy'`, `metrics=['accuracy']`

## 🚀 Execução no Google Colab

Você pode rodar todo o projeto diretamente no Google Colab:

1. Baixar e extrair o dataset
2. Limpar imagens corrompidas
3. Separar em treino/teste
4. Treinar o modelo
5. Fazer testes manuais com upload de imagens

## 🧪 Teste Manual

No final do notebook, é possível fazer o **upload de imagens à mão** para verificar como o modelo responde.

## 📊 Resultados

- Acurácia de validação próxima de 90% (varia conforme execução)
- Bom desempenho mesmo com poucas épocas, graças à transferência de aprendizado

## 🛠️ Requisitos

- Google Colab (recomendado)
- TensorFlow / Keras
- Python 3.x

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e contribuir!

---

Feito com ❤️ por Gustavo Cassiano Pinto

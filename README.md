# Face Detector

Este projeto faz parte do bootcamp de Machine Learning da DIO e apresenta a implementação de um detector de faces utilizando técnicas de visão computacional.  
O notebook principal é **Face_detector.ipynb**.

---

## 📋 Sumário

1. [Descrição](#descrição)  
2. [Funcionalidades](#funcionalidades)  
3. [Requisitos](#requisitos)  
4. [Instalação](#instalação)  

---

## Descrição

O notebook **Face_detector.ipynb** demonstra como:

- Carregar e pré-processar imagens (ou vídeo)  
- Utilizar modelos ou técnicas de detecção de faces (por exemplo, Haar cascades, ou outros)  
- Identificar regiões de interesse correspondentes a rostos  
- Exibir visualmente os resultados sobre as imagens  

O foco principal é aplicar conceitos de visão computacional e manipulação de imagem no contexto prática de detecção facial.

---

## Funcionalidades

- Detecção de faces em imagens fixas  
- (Possivelmente) detecção em vídeo ou webcam  
- Visualização dos bounding boxes sobre os rostos detectados  
- Pré-processamento (conversão para escala de cinza, redimensionamento etc.)

---

## Requisitos

Você vai precisar de:

- Python 3.x  
- Bibliotecas Python (exemplo, mas ajuste conforme o notebook):  
  - `numpy`  
  - `opencv-python`  
  - `matplotlib`  
  - `PIL` ou `Pillow`  
  - (Outras dependências usadas no notebook)  

---

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/guscassiano/Dio_ML_bootcamp.git
   cd Dio_ML_bootcamp/face_detection
   ```
   
2. (Opcional) Crie e ative um ambiente virtual:
   
  ```bash
  python3 -m venv venv
  source venv/bin/activate    # Linux / macOS
  venv\Scripts\activate       # Windows
  ```

3. Instale as dependências:

   ```bash
   pip install numpy opencv-python matplotlib pillow
   ```
   
   Ou (se houver `requirements.txt`):
   
   ```bash
   pip install -r requirements.txt
   ```

---

## Uso

1. Abra o Jupyter Notebook:
   ```bash
    jupyter notebook Face_detector.ipynb
   ```

2. Execute as células em sequência:
   - Verifique que os caminhos para imagens ou vídeo estão corretos
   - Altere parâmetros conforme necessário (por exemplo, escala, tamanhos mínimos)
   - Visualize os resultados com bounding boxes ao final

3. (Se implementado) para rodar com webcam ou vídeo, execute a célula correspondente e permita acesso à câmera.

---

## Estrutura do projeto

  ```bash
  Dio_ML_bootcamp/
  └── face_detection/
      ├── Face_detector.ipynb
      ├── (imagens de entrada, se houver)
      ├── (arquivos de vídeo, se houver)
      └── requirements.txt   ← (se existir)
  ```

## Exemplos de resultados

<img width="1142" height="590" alt="download" src="https://github.com/user-attachments/assets/0da9fd29-8c23-418a-a0e2-2717610c9211" />

## Contribuição

Contribuições são bem-vindas! Se você quiser:
  1. Faça um fork deste repositório
  2. Crie uma branch com sua feature ou correção (git checkout -b minha-feature)
  3. Faça commit das suas mudanças (git commit -m "Minha melhoria")
  4. Envie para seu fork (git push origin minha-feature)
  5. Abra um Pull Request

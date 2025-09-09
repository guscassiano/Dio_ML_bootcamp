# 🤖 Assistente de Voz com Python e PLN

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Google Colab](https://img.shields.io/badge/Google_Colab-Ready-orange?style=for-the-badge&logo=google-colab)

Este projeto é um assistente de voz simples, desenvolvido em Python e projetado para ser executado no ambiente do Google Colab. Ele utiliza bibliotecas de Processamento de Linguagem Natural (PLN) para entender comandos de voz em português, executar tarefas e responder com uma voz sintetizada.

## ✨ Funcionalidades Principais

* **Reconhecimento de Voz (Speech-to-Text):** Transcreve a fala do usuário em texto.
* **Síntese de Voz (Text-to-Speech):** Converte as respostas em texto para um áudio natural.
* **Comandos por Voz:** Ativa funções específicas a partir de palavras-chave.
* **Integração com a Wikipedia:** Realiza pesquisas e retorna um resumo por voz.
* **Automação Web:** Abre sites como o YouTube.
* **Geolocalização Simples:** Encontra serviços próximos (como farmácias) com base na localização aproximada do IP.

## 🛠️ Tecnologias Utilizadas

O núcleo do assistente é construído com as seguintes bibliotecas e ferramentas Python:

* **`SpeechRecognition`**: Para capturar e reconhecer o áudio do microfone.
* **`gTTS` (Google Text-to-Speech)**: Para gerar as respostas em áudio.
* **`Wikipedia`**: Para se conectar à API da Wikipedia e extrair informações.
* **`mutagen`**: Para calcular a duração dos arquivos de áudio e sincronizar a fala com a escuta.
* **`requests`**: Para fazer requisições a APIs de geolocalização.
* **`FFmpeg`**: Ferramenta essencial para a conversão de formatos de áudio no backend.

## 🚀 Como Executar o Projeto

Este projeto foi otimizado para o Google Colab, tornando a configuração extremamente simples.

1.  **Abra no Google Colab:** Faça o upload do arquivo `.ipynb` para o seu Google Drive e abra-o com o Google Colaboratory.
2.  **Execute as Células:** Rode cada célula de código na ordem em que aparecem. A primeira célula cuidará de instalar todas as dependências necessárias.
3.  **Permita o Microfone:** Ao executar a função de escuta pela primeira vez, seu navegador irá solicitar permissão para usar o microfone. **Você deve permitir** para que o assistente funcione.
4.  **Comece a Interagir:** Após a mensagem de boas-vindas, o assistente estará pronto para receber seus comandos.

## 🗣️ Comandos de Voz Disponíveis

Você pode iniciar a interação com os seguintes comandos:

* `"Pesquisar por [assunto]"`
    * *Exemplo: "Pesquisar por inteligência artificial"*
* `"Abrir o YouTube"`
* `"Farmácia mais próxima"`
* `"Encerrar"` ou `"Parar"` (para finalizar a execução do assistente)

---

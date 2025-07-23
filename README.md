# Processamento de Imagens PPM

Este script Python oferece funcionalidades para ler imagens no formato PPM (Portable Pixmap), convertê-las para tons de cinza (PGM) e binarizá-las (PBM). Ele suporta os formatos PPM P2 (tons de cinza ASCII), P3 (colorido ASCII) e P6 (colorido binário).

---

## Funcionalidades

* **Leitura de Imagens PPM**: Lê arquivos PPM (P2, P3, P6), extraindo suas dimensões, valor máximo de cor e dados de pixel.
* **Conversão para Tons de Cinza**: Converte imagens coloridas (PPM P3 e P6) para o formato PGM (Portable Graymap), usando a fórmula de luminância padrão.
* **Binarização de Imagens**: Converte imagens em tons de cinza para o formato PBM (Portable Bitmap), aplicando um limiar para transformar pixels em preto e branco.
* **Escrita de Imagens PGM e PBM**: Salva as imagens convertidas nos formatos PGM (tons de cinza) e PBM (binarizadas).

---

## Como Usar

1.  **Salve o Código**: Salve o código fornecido em um arquivo Python (por exemplo, `image_processor.py`).
2.  **Prepare a Imagem PPM**: Coloque a imagem `.ppm` que você deseja processar na mesma pasta do script.
3.  **Execute o Script**: Abra um terminal ou prompt de comando, navegue até a pasta onde o arquivo `.py` e a imagem `.ppm` estão e execute o script:

    ```bash
    python image_processor.py
    ```

4.  **Informe o Nome do Arquivo**: O script solicitará que você digite o nome do arquivo PPM (com a extensão `.ppm`).

    ```
    Entre com o nome do arquivo (O formato deve esta em .ppm e na mesma pasta do código): minha_imagem.ppm
    ```

### Exemplo de Uso

Se você tiver um arquivo chamado `exemplo.ppm`:

```bash
python image_processor.py
Entre com o nome do arquivo (O formato deve esta em .ppm e na mesma pasta do código): exemplo.ppm

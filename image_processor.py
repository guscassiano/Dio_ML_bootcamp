def read_ppm_image(file_name):
    with open(file_name, 'rb') as f:
        magic_number = f.readline().strip().decode('ascii')
        if magic_number not in ['P6', 'P3', 'P2']:
            raise ValueError(f"Formato PPM não suportado: {magic_number}. Apenas P2 (tons de cinza ASCII), P3 (colorido ASCII) e P6 (colorido binário).")

        width = 0
        height = 0
        max_value = 0

        while True:
            line = f.readline().strip().decode('ascii')
            if not line:
                raise ValueError("Formato de arquivo PPM inválido: fim inesperado do cabeçalho.")

            if line.startswith('#'):
                continue

            if width == 0 and height == 0:
                parts = line.split()
                if len(parts) == 2:
                    try:
                        width = int(parts[0])
                        height = int(parts[1])
                    except ValueError:
                        raise ValueError("Formato de arquivo PPM inválido: dimensões não numéricas.")
                    if width <= 0 or height <= 0:
                        raise ValueError("Dimensões da imagem devem ser maiores que zero.")
                    continue
                else:
                    raise ValueError("Formato de arquivo PPM inválido: esperado largura e altura.")

            if max_value == 0:
                try:
                    max_value = int(line)
                except ValueError:
                    raise ValueError("Formato de arquivo PPM inválido: valor máximo de cor não numérico.")
                if not (0 < max_value <= 255):
                    raise ValueError("Valor máximo de cor deve ser entre 1 e 255.")
                break


        pixels = []
        if magic_number == 'P6':
            pixel_data = f.read(width * height * 3)
            if len(pixel_data) != width * height * 3:
                raise ValueError(f"Dados de pixel incompletos para P6. Esperado {width * height * 3} bytes, encontrado {len(pixel_data)}.")

            for i in range(0, len(pixel_data), 3):
                r = pixel_data[i]
                g = pixel_data[i+1]
                b = pixel_data[i+2]
                pixels.append((r, g, b))

        elif magic_number == 'P3':
            data_str = f.read().decode('ascii').split()
            pixel_count = width * height
            if len(data_str) != pixel_count * 3:
                raise ValueError(f"Número de valores RGB esperado: {pixel_count * 3}, encontrado: {len(data_str)}")

            for i in range(0, len(data_str), 3):
                r = int(data_str[i])
                g = int(data_str[i+1])
                b = int(data_str[i+2])
                pixels.append((r, g, b))

        elif magic_number == 'P2':
            data_str = f.read().decode('ascii').split()
            pixel_count = width * height
            if len(data_str) != pixel_count:
                raise ValueError(f"Número de valores de cinza esperado: {pixel_count}, encontrado: {len(data_str)}")

            for i in range(len(data_str)):
                gray = int(data_str[i])
                pixels.append(gray)

    return width, height, pixels, magic_number, max_value

def convert_to_grayscale(rgb_pixels):
    grayscale_pixels = []
    for r, g, b in rgb_pixels:
        gray = int(0.299 * r + 0.587 * g + 0.114 * b)
        grayscale_pixels.append(max(0, min(255, gray)))
    return grayscale_pixels

def convert_to_binarized(grayscale_pixels, threshold=128):
    binarized_pixels = []
    for gray_value in grayscale_pixels:
        if gray_value >= threshold:
            binarized_pixels.append(255)
        else:
            binarized_pixels.append(0)
    return binarized_pixels

def write_pgm_image(file_name, width, height, grayscale_pixels, max_val=255):
    with open(file_name, 'w') as f:
        f.write("P2\n")
        f.write(f"{width} {height}\n")
        f.write(f"{max_val}\n")

        for i, pixel_val in enumerate(grayscale_pixels):
            f.write(str(pixel_val))
            if (i + 1) % width == 0:
                f.write("\n")
            else:
                f.write(" ")

def write_pbm_image(file_name, width, height, binarized_pixels):
    with open(file_name, 'w') as f:
        f.write("P1\n")
        f.write(f"{width} {height}\n")

        for i, pixel_val in enumerate(binarized_pixels):
            f.write(str(1 if pixel_val == 255 else 0))
            if (i + 1) % width == 0:
                f.write("\n")
            else:
                f.write(" ")

if __name__ == "__main__":
    file_name = input('Entre com o nome do arquivo (O formato deve esta em .ppm e na mesma pasta do código): ')
    if not file_name.endswith('.ppm'):
        print("Erro: O arquivo deve ter a extensão .ppm")
        exit(1)
    file_name_output = file_name.strip('.ppm')
    try:
        print(f"Tentando ler a imagem: {file_name}")
        width, height, read_pixels, magic_number, max_value = read_ppm_image(file_name)
        print(f"Imagem lida com sucesso! Formato: {magic_number}, Dimensões: {width}x{height}, Valor Máximo: {max_value}")

        if magic_number in ['P6', 'P3']:
            print("\nConvertendo para tons de cinza...")
            grayscale_pixels = convert_to_grayscale(read_pixels)
            output_grayscale_file = f"{file_name_output}_grayscale.pgm"
            write_pgm_image(output_grayscale_file, width, height, grayscale_pixels)
            print(f"Imagem em tons de cinza salva como: {output_grayscale_file}")

            print("\nConvertendo para binarizado (usando a imagem em tons de cinza)...")
            binarized_pixels = convert_to_binarized(grayscale_pixels)
            output_binarized_file = f"{file_name_output}_binarized.pbm"
            write_pbm_image(output_binarized_file, width, height, binarized_pixels)
            print(f"Imagem binarizada salva como: {output_binarized_file}")

        elif magic_number == 'P2':
            print("\nA imagem já está em tons de cinza. Convertendo para binarizado...")
            binarized_pixels = convert_to_binarized(read_pixels)
            output_binarized_file = "golden_binarized.pbm"
            write_pbm_image(output_binarized_file, width, height, binarized_pixels)
            print(f"Imagem binarizada salva como: {output_binarized_file}")

    except ValueError as ve:
        print(f"Erro ao processar a imagem: {ve}")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_name}' não foi encontrado. Certifique-se de que ele está no mesmo diretório do script.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
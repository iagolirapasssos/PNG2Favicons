from PIL import Image
import os

def create_favicons(input_file, output_dir):
    # Cria o diretório de saída se não existir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Abre a imagem original
    with Image.open(input_file) as img:
        # Lista de tamanhos para os favicons
        sizes = [16, 32, 48, 64, 128]

        # Cria um favicon para cada tamanho
        for size in sizes:
            # Redimensiona a imagem
            resized_img = img.resize((size, size), Image.LANCZOS)
            
            # Salva o favicon redimensionado
            output_file = os.path.join(output_dir, f"favicon_{size}x{size}.png")
            resized_img.save(output_file, "PNG")
            print(f"Favicon {size}x{size} created: {output_file}")

# Uso do script
input_file = "Path/file.png"
output_dir = "Path/output"

create_favicons(input_file, output_dir)

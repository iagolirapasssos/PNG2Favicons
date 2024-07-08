# PNG2Favicons

# Favicon Generator / Gerador de Favicons

[English](#english) | [Português](#português)

## English

This Python script converts a PNG image into multiple favicons of different sizes.

### Features

- Converts a PNG file into favicons of 16x16, 32x32, 48x48, 64x64, and 128x128 pixels.
- Uses the LANCZOS resampling method for better quality.
- Saves the generated favicons in a specified directory.

### Requirements

- Python 3.x
- Pillow (PIL Fork)

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/favicon-generator.git
   ```

2. Install the dependencies:
   ```
   pip install Pillow
   ```

### Usage

1. Place your PNG image in the project directory or note its full path.

2. Modify the following lines in the script with the correct paths:

   ```python
   input_file = "path/to/your/file.png"
   output_dir = "path/to/output/directory"
   ```

3. Run the script:

   ```
   python favicon_generator.py
   ```

4. The generated favicons will be saved in the specified output directory.

### Contributions

Contributions are welcome! Please feel free to submit a Pull Request.

### License

This project is licensed under the [MIT License](LICENSE).

---

## Português

Este script Python converte uma imagem PNG em múltiplos favicons de diferentes tamanhos.

### Funcionalidades

- Converte um arquivo PNG em favicons de 16x16, 32x32, 48x48, 64x64 e 128x128 pixels.
- Utiliza o método de redimensionamento LANCZOS para melhor qualidade.
- Salva os favicons gerados em um diretório especificado.

### Requisitos

- Python 3.x
- Pillow (PIL Fork)

### Instalação

1. Clone este repositório:
   ```
   git clone https://github.com/seu-usuario/gerador-favicons.git
   ```

2. Instale as dependências:
   ```
   pip install Pillow
   ```

### Uso

1. Coloque sua imagem PNG no diretório do projeto ou anote o caminho completo para ela.

2. Modifique as seguintes linhas no script com os caminhos corretos:

   ```python
   input_file = "caminho/para/seu/arquivo.png"
   output_dir = "caminho/para/diretorio/de/saida"
   ```

3. Execute o script:

   ```
   python gerador_favicons.py
   ```

4. Os favicons gerados serão salvos no diretório de saída especificado.

### Contribuições

Contribuições são bem-vindas! Por favor, sinta-se à vontade para submeter um Pull Request.

### Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

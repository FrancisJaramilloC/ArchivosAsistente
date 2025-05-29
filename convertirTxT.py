from PyPDF2 import PdfReader
import os

# Directorio donde pusiste los PDFs descargados
input_dir = "pdfs"  # cámbialo si usas otra carpeta
output_dir = "txts"
os.makedirs(output_dir, exist_ok=True)

# Procesar todos los archivos PDF en la carpeta
for filename in os.listdir(input_dir):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(input_dir, filename)
        txt_path = os.path.join(output_dir, filename.replace(".pdf", ".txt"))

        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"

        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"✅ Convertido: {filename} -> {txt_path}")

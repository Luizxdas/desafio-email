from pypdf import PdfReader

MAX_FILE_SIZE = 1 * 1024 * 1024

def verify_and_read(file):
    file.seek(0, 2)
    file_size = file.tell()
    file.seek(0)
    if file_size > MAX_FILE_SIZE:
        raise ValueError("Arquivo muito grande")

    if file.filename.endswith(".txt") and file.mimetype == "text/plain":
        conteudo = file.read().decode("utf-8")
        return conteudo
    elif file.filename.endswith(".pdf") and file.mimetype == "application/pdf":
        reader = PdfReader(file)
        texto = ""
        for page in reader.pages:
            texto += page.extract_text() or ""
        return texto
    else:
        raise ValueError("Apenas arquivos .txt ou .pdf são permitidos")
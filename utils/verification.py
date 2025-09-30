from pypdf import PdfReader

MAX_FILE_SIZE = 1 * 1024 * 1024

def verify_and_read(file):
    file.seek(0, 2)
    file_size = file.tell()
    file.seek(0)
    if file_size > MAX_FILE_SIZE:
        raise ValueError("Arquivo muito grande")
    
    conteudo = ""

    if file.filename.endswith(".txt") and file.mimetype == "text/plain":
        conteudo = file.read().decode("utf-8")
    elif file.filename.endswith(".pdf") and file.mimetype == "application/pdf":
        reader = PdfReader(file)
        for page in reader.pages:
            conteudo += page.extract_text() or ""
    else:
        raise ValueError("Apenas arquivos .txt ou .pdf são permitidos")
    
    tamanho = len(conteudo)
    if tamanho > 800:
        raise ValueError("O arquivo excede o limite de 800 caracteres.")
    
    return conteudo
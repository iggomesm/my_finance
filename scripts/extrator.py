import PyPDF2
import pandas as pd
import re
import os

def listar_arquivos():
    # Obtém o caminho absoluto do diretório 'scripts'
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    
    # Define o caminho relativo para o diretório 'extrato'
    diretorio = diretorio_atual.replace("/scripts", "/extratos")
    
    try:
        # Obtém todos os itens do diretório e filtra apenas os arquivos
        arquivos = [os.path.join(diretorio, arquivo) for arquivo in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, arquivo))]
        
        return arquivos
    except FileNotFoundError:
        print(f"O diretório '{diretorio}' não foi encontrado.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return []


def extract_data_from_pdf(pdf_file, conta):

    prompt = carregar_prompt()
    prompt = prompt.replace("{conta}", conta)
    numero_de_paginas = 0
    with open(pdf_file, 'rb') as pdf_reader:
        reader = PyPDF2.PdfReader(pdf_reader)        
        
        data = []       

        for numero_pagina in range(len(reader.pages)):
            page = reader.pages[numero_pagina]
            text = page.extract_text()
            # Dividir o texto por linhas para processar cada lançamento
            lines = text.split('\n')
            current_date = None
            for line in lines:
                if("SALDO DO DIA" in line): 
                    continue
                if("Aviso" in line or "Fale com a gente" in line) : 
                    break
                data.append(line)
            text = prompt + "\n".join(data[3:])
    
    print(f"Finalizado")
    
    with open(f"{conta}_prompt.md", "w") as arquivo:
        arquivo.write(text)

def carregar_prompt():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = f"{diretorio_atual}/prompt.md"
    
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
        return conteudo
    except FileNotFoundError:
        raise
    except Exception as e:
        raise e

def verificar_conta(texto):
    
    contas = ["Itau", "Inter", "Bradesco", "Nubank"]

    # Verifica se algum dos nomes está presente no texto (case insensitive)
    for conta in contas:
        if conta.lower() in texto.lower():
            return conta
    
    return ""


# Exemplo de uso
lista_arquivos = listar_arquivos()
for arquivo in lista_arquivos:
    print(arquivo)
    conta = verificar_conta(arquivo)
    extract_data_from_pdf(arquivo, conta)
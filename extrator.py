import PyPDF2
import pandas as pd
import re


def extract_data_from_pdf(pdf_file, conta):

    prompt = f"""# PROMPT de relação de despesas


## INSTITUICAO: {conta}

## OBJETIVO
Montar uma tabela contendo a relação de despesa de uma conta.

## NECESSIDADE

Tomando como base de conhecimento os lançamentos financeiros apresentados em [LANÇAMENTOS], 
Desejo que todos os lançamentos sejam lidos e transformados numa tabela contendo as seguintes colunas:
Conta, Data, Descrição, Valor, TIPO, Categoria e Agrupamento.

### Regras

1 - Inclua o valor descrito em INSTITUICAO para todas as linhas na coluna Conta;
2 - A data deverá ser colocada no padrão dd/MM/yyyy;
3 - A formatação de cada valor deve ser em Número que possa ser interpretado pelo google planilhas. Ex. -3.493,76
4 - Os valores negativos representam uma despesa e devem ser do tipo "Despesa";
5 - Os valores positivos representam uma receita e devem ser do tipo "Receita";
6 - Os agrupamentos podem ser de 3 tipos:
    a) - Pessoal;
    b) - Casa;
    c) - Terceiros;

7 - Inclua o valor descrito em INSTITUICAO para todas as linhas na coluna Conta;
8 - Você deve classificar cada lançamento segundo seu critério, mas respeitando as seguintes regras:
    --> Caso a descrição do lançamento contenha o nome Brisanet ele deverá ser da Categoria Internet e do Agrupamento Casa.
    --> Caso a descrição do lançamento contenha o nome Enel ele deverá ser da Categoria Energia e do Agrupamento Casa.
    --> Caso a descrição do lançamento contenha o nome Cagece ele deverá ser da Categoria Internet e do Agrupamento Casa.
    --> Caso a descrição do lançamento contenha o nome Silvelena ele deverá ser da Categoria Diarista e do Agrupamento Casa.
    --> Caso a descrição do lançamento contenha o nome Portal ele deverá ser da Categoria Condominio e do Agrupamento Casa.
    --> Caso a descrição do lançamento contenha o nome Netflix ele deverá ser da Categoria Streaming e do Agrupamento Casa.
    --> Caso a descrição do lançamento contenha o nome AUGUSTA ele deverá ser da Categoria Internet e do Agrupamento Casa.
9 - Lançamentos com o nome SALDO DO DIA devem ser desconsiderados do processamento.

## SAIDA
Você deve apresentar o resultado numa tabela.

## LANÇAMENTOS:"""
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
    
    with open("prompt.md", "w") as arquivo:
        arquivo.write(text)


# Exemplo de uso
pdf_file = 'itau_extrato_122024.pdf'
df = extract_data_from_pdf(pdf_file, "Bradesco")
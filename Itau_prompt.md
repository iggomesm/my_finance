# PROMPT de relação de despesas

## INSTITUICAO: Itau

## TABELA CONTA: 
Saiba que cada Conta possui um id específico.
ID  Conta
1	Itau
2	Inter
3	Bradesco
4	Nubank

## TABELA CATEGORIA
ID  TIPO    DESCRICAO

1	RECEITAS	SALARIO
2	RECEITAS	REEMBOLSO
3	DESPESAS	MORADIA
4	DESPESAS	LAZER
5	DESPESAS	AUTOMOVEL
6	DESPESAS	TRANSPORTE
7	DESPESAS	STREAMING
8	DESPESAS	MACONARIA
9	DESPESAS	PESSOAL

## TABELA TAG
ID  DESCRICAO
1	Pessoal
2	Casa
3	Terceiros

## OBJETIVO
Montar uma tabela contendo a relação de despesa de uma conta.

## NECESSIDADE

Tomando como base de conhecimento os lançamentos financeiros apresentados em [LANÇAMENTOS], 
Desejo que todos os lançamentos sejam lidos e transformados numa sintaxe SQL de insert na tabela de nome movimentacao.
Saiba que a tabela movimentacao possui as seguintes colunas:
    data TIMESTAMP NOT NULL,              -- Data da movimentação(Formatacao em TIMESTAMP).
    descricao TEXT NOT NULL,              -- Descrição da movimentação
    valor REAL NOT NULL,                  -- Valor da movimentação
    conta INTEGER NOT NULL,               -- Conta associada (FK para tabela CONTA)
    categoria INTEGER,                    -- Categoria da movimentação (FK para tabela CATEGORIA)
    tag INTEGER,                          -- Tag associada (FK para tabela TAG)

### Regras

1 - Inclua o id descrito em INSTITUICAO para todas as linhas na coluna Conta;
2 - A data deverá ser colocada no padrão dd/MM/yyyy;
3 - A formatação de cada valor deve ser em Número que possa ser interpretado pelo google planilhas. Ex. -3.493,76
4 - Os valores negativos representam uma despesa e devem ser do tipo "Despesa";
5 - Os valores positivos representam uma receita e devem ser do tipo "Receita";
6 - A tag pode ser de 3 tipos:
    a) - Pessoal;
    b) - Casa;
    c) - Terceiros;

7 - Inclua o valor descrito em INSTITUICAO para todas as linhas na coluna Conta;
8 - Você deve classificar cada lançamento segundo seu critério, mas respeitando as seguintes regras:
    --> Caso a descrição do lançamento contenha o nome Brisanet ele deverá ser da Categoria Internet e do tag Casa.
    --> Caso a descrição do lançamento contenha o nome Enel ele deverá ser da Categoria Energia e do tag Casa.
    --> Caso a descrição do lançamento contenha o nome Cagece ele deverá ser da Categoria Internet e do tag Casa.
    --> Caso a descrição do lançamento contenha o nome Silvelena ele deverá ser da Categoria Diarista e do tag Casa.
    --> Caso a descrição do lançamento contenha o nome Portal ele deverá ser da Categoria Condominio e do tag Casa.
    --> Caso a descrição do lançamento contenha o nome Netflix ele deverá ser da Categoria Streaming e do tag Casa.
    --> Caso a descrição do lançamento contenha o nome AUGUSTA ele deverá ser da Categoria Maconaria e do tag Pessoal.
9 - Lançamentos com o nome SALDO DO DIA devem ser desconsiderados do processamento.
10 - Lançamentos só podem ser considerados da categoria Salario se possuirem descrição igual a TEF CREDITO SALARIO e forem positivos;

## SAIDA
Você deve gerar o comando de insert na tabela movimentacao para todos os lançamentos contidos em [LANÇAMENTOS].
A coluna data deve ser formatada como um timestamp no formado 'yyyy-MM-dd hh:mm:ss'

## LANÇAMENTOS:* Total contratado. O uso do Limite da Conta e Limite da Conta adicional poderá ter cobrança de juros + IOF.
extrato conta / lançamentos
período de visualização: 27/11/2024 até 26/01/2025  emitido em: 26/01/2025 18:26:52
data lançamentos valor (R$) saldo (R$)
27/01/2025 PIX QRS PETROCAR25/01 -150,00
23/01/2025 PIX TRANSF SILMIA 23/01 120,00
21/01/2025 PIX TRANSF KALINE 21/01 -26,00
21/01/2025 REND PAGO APLIC AUT MAIS 0,13
20/01/2025 PIX QRS ENEL DISTRI20/01 -117,19
20/01/2025 PIX QRS BRISANET20/01 -117,80
20/01/2025 REND PAGO APLIC AUT MAIS 2,00
20/01/2025 PIX TRANSF CONDOMI20/01 -150,00
16/01/2025 PAY Posto 16/01 -150,00
16/01/2025 REND PAGO APLIC AUT MAIS 0,77
15/01/2025 TEF CREDITO SALARIO 6.163,80
13/01/2025 PAY PETRO 12/01 -200,00
13/01/2025 REND PAGO APLIC AUT MAIS 0,99
08/01/2025 PIX TRANSF KALINE 08/01 -26,00
08/01/2025 PIX QRS IGOR GOMES 08/01 -1.360,00
08/01/2025 REND PAGO APLIC AUT MAIS 6,57
06/01/2025 PIX QRS MARCOS AURE04/01 -30,25
06/01/2025 PIX QRS NU PAGAMENT06/01 -2.472,59
06/01/2025 REND PAGO APLIC AUT MAIS 11,51
03/01/2025 PAY POSTO 03/01 -100,00
03/01/2025 REND PAGO APLIC AUT MAIS 0,45
02/01/2025 PIX TRANSF CONDOMI02/01 -865,80
02/01/2025 DEV PIX CONDOMINIO 02/01 86,58
02/01/2025 REND PAGO APLIC AUT MAIS 3,48
30/12/2024 PAY POSTO 28/12 -100,00
30/12/2024 PIX TRANSF KALINE 30/12 -13,00
30/12/2024 REND PAGO APLIC AUT MAIS 0,48
27/12/2024 TEF CREDITO SALARIO 5.058,29
26/12/2024 PIX QRS BRISANET26/12 -122,93
26/12/2024 REND PAGO APLIC AUT MAIS 0,52
20/12/2024 PIX QRS ENEL DISTRI20/12 -115,81
20/12/2024 TEF CREDITO SALARIO 3.704,23
17/12/2024 PAY POSTO 17/12 -150,00
17/12/2024 PIX TRANSF DEISE S17/12 -300,00
17/12/2024 REND PAGO APLIC AUT MAIS 0,85
13/12/2024 TEF CREDITO SALARIO 6.163,80
09/12/2024 PIX QRS NU PAGAMENT07/12 -3.493,36
09/12/2024 PIX QRS IGOR GOMES 09/12 -1.350,00
09/12/2024 REND PAGO APLIC AUT MAIS 8,91
04/12/2024 PIX TRANSF KALINE 04/12 -26,00
04/12/2024 REND PAGO APLIC AUT MAIS 0,04
02/12/2024 PIX TRANSF CONDOMI02/12 -846,05
02/12/2024 REND PAGO APLIC AUT MAIS 1,44
29/11/2024 PIX QRS Magazine Lu29/11 -2.820,56
29/11/2024 TEF CREDITO SALARIO 5.244,28
27/11/2024 PAY PETRO 27/11 -150,00
27/11/2024 REND PAGO APLIC AUT MAIS 0,24
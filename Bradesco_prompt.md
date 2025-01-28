# PROMPT de relação de despesas

## INSTITUICAO: Bradesco

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

## LANÇAMENTOS:Extrato de: Agência: 600 | Conta: 6997-3 | Movimentação entre: 29/12/2024 e 28/01/2025 Folha: 1/2
Data Histórico Docto. Crédito (R$) Débito (R$) Saldo (R$)
02/01/2025RENDIMENTOS 
POUP FACIL-DEPOS A PARTIR 4/5/120105826 4,28 1.230,22
06/01/2025 SEGURO MAIS PROTECAO 2760006 2,86 1.227,36
08/01/2025CONTA DE TELEFONE 
CLARO CELULAR-1403542514035425 73,12 1.154,24
CONTA DE TELEFONE 
CLARO CELULAR-1403542564035425 73,12 1.081,12
CONTA DE TELEFONE 
CLARO CELULAR-1403855894038558 73,12 1.008,00
15/01/2025RENDIMENTOS 
POUP FACIL-DEPOS A PARTIR 4/5/121505958 2,92 1.010,92
TARIFA BANCARIA 
CESTA UNIVERSITARIA0020125 11,80 999,12
Total 7,20 234,02 999,12
Bradesco Celular
Data: 28/01/2025 - 08h14
Nome: IGOR GOMES DE MOISES
Extrato de: Agência: 600 | Conta: 6997-3 | Últimos Lancamentos Folha: 2/2
Data Histórico Docto. Crédito (R$) Débito (R$) Saldo (R$)
Extrato inexistente
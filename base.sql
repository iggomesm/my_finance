-- Criação da tabela Conta
CREATE TABLE Conta (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    observacao TEXT,
    saldo_inicial REAL NOT NULL
);

-- Criação da tabela Categoria
CREATE TABLE Categoria (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT NOT NULL,
    descricao TEXT NOT NULL,
    superior INTEGER,
    FOREIGN KEY (superior) REFERENCES Categoria (id)
);

-- Criação da tabela Tag
CREATE TABLE Tag (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL
);

select * from tag

-- Criação da tabela Movimentacao
CREATE TABLE Movimentacao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TIMESTAMP NOT NULL,
    descricao TEXT NOT NULL,
    valor REAL NOT NULL,
    conta INTEGER NOT NULL,
    categoria INTEGER,
    tag INTEGER,
    FOREIGN KEY (conta) REFERENCES Conta (id),
    FOREIGN KEY (categoria) REFERENCES Categoria (id),
    FOREIGN KEY (tag) REFERENCES Tag (id)
);


-- Criando contas
INSERT INTO Conta (descricao, observacao, saldo_inicial) VALUES 
('Itau', NULL, 0.0),
('Inter', NULL, 0.0),
('Bradesco', NULL, 0.0),
('Nubank', NULL, 0.0);

select * from conta

-- Criacao das tags
INSERT INTO tag (descricao) VALUES 
('Pessoal'),
('Casa'),
('Terceiros');

select * from tag

-- Criacao de categorias
INSERT INTO Categoria (tipo, descricao, superior) VALUES
('RECEITAS', 'SALARIO', NULL),
('RECEITAS', 'REEMBOLSO', NULL),
('DESPESAS', 'MORADIA', NULL),
('DESPESAS', 'LAZER', NULL),
('DESPESAS', 'AUTOMOVEL', NULL),
('DESPESAS', 'TRANSPORTE', NULL),
('DESPESAS', 'MACONARIA', NULL),
('DESPESAS', 'PESSOAL', NULL),
('DESPESAS', 'STREAMING', NULL);

select * from Categoria

------------------------------------------------------------------------------------
1	Itau
2	Inter
3	Bradesco
4	Nubank
------------------------------------------------------------------------------------

-- Pesquisa de extrato financeiro
select c.descricao, m.data, m.descricao, m.valor, c2.descricao, t.descricao 
from movimentacao m
inner join conta c on c.id = m.conta 
inner join Categoria c2 on c2.id = m.categoria 
inner join Tag t on t.id = m.tag 
where c.id = 3
order by m.data desc

-- visao geral
select c.descricao, (sum(m.valor) + c.saldo_inicial) as saldo_atual,
SUM(CASE WHEN valor < 0 THEN valor ELSE 0 END) as despesas_totais, 
SUM(CASE WHEN valor > 0 THEN valor ELSE 0 END) as receitas_totais,
(CASE WHEN sum(m.valor) > 0 THEN sum(m.valor) ELSE 0 END) as lucro_total_periodo
from movimentacao m
inner join conta c on c.id = m.conta 
inner join Categoria c2 on c2.id = m.categoria 
inner join Tag t on t.id = m.tag 
where c.id = 3
group by c.id 
order by m.data desc
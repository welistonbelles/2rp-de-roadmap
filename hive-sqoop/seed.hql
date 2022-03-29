-- Para evitar problemas ao importar os dados diretamente para uma tabela ORC, 
-- optei por importar eles primeiramente para uma tabela temporaria
CREATE EXTERNAL TABLE IF NOT EXISTS work_dataeng.generation_weliston_tmp 
(
    generation INT, 
    date_introduced DATE
) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE TBLPROPERTIES ("skip.header.line.count"="1");

-- Mesma situação para esta tabela
CREATE EXTERNAL TABLE IF NOT EXISTS work_dataeng.pokemon_weliston_tmp 
(
    idnum INT, 
    name STRING, 
    hp INT, 
    speed INT, 
    attack INT, 
    special_attack INT, 
    defense INT, 
    special_defense INT, 
    generation INT
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE TBLPROPERTIES ("skip.header.line.count"="1");

-- Comando enviado pro pessoal de devops
LOAD DATA INPATH '/user/2rp-weliston/pokemon.csv' INTO TABLE work_dataeng.pokemon_weliston_tmp;

LOAD DATA INPATH '/user/2rp-weliston/generation.csv' INTO TABLE work_dataeng.generation_weliston_tmp;

-- Realizando a migração dos dados das tabelas temporárias para as tabelas de modelo orc
INSERT INTO TABLE work_dataeng.generation_weliston SELECT * FROM work_dataeng.generation_weliston_tmp;

INSERT INTO TABLE work_dataeng.pokemon_weliston SELECT * FROM work_dataeng.pokemon_weliston_tmp;

-- Para obter uma comparação mais justa entre as consultas realizadas tanto no hive quanto no impala
-- optei por não utilizar o campo date_introduced presente na tabela generation,
-- visto que o impala nao tem suporte a campos do tipo DATE
SELECT DISTINCT poke.idnum, poke.name, poke.hp, poke.speed, poke.attack, gen.generation
FROM work_dataeng.pokemon_weliston poke 
JOIN work_dataeng.generation_weliston gen 
ON poke.generation = gen.generation;


-- Ao comparar o tempo de execução é notável a diferença de performance entre o hive e o impala
-- Hive: 41.86s
-- Impala: 0.73s
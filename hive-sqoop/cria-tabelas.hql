-- Comando para criar a tabela generation_weliston
CREATE TABLE IF NOT EXISTS work_dataeng.generation_weliston
(
    generation INT, 
    date_introduced DATE
)
STORED AS orc;

-- Comando para criar a tabela pokemon_weliston
CREATE TABLE IF NOT EXISTS work_dataeng.pokemon_weliston
(
    idnum INT, 
    name String, 
    hp INT, 
    speed INT, 
    attack INT, 
    special_attack INT, 
    defense INT, 
    special_defense INT, 
    generation INT
)
STORED AS orc;
# -*- encoding: utf-8 -*-

from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

## Realizando o load dos dados presentes nas tabelas e instanciando os dataframes
df_poke = spark.table('work_dataeng.pokemon_weliston')
df_gen = spark.table('work_dataeng.generation_weliston')

## Aplicando o filtro de data
df_gen = df_gen.filter(df_gen["date_introduced"] < '2002-11-21')

## Realizando o cache do data frame
df_gen.cache()

## Realizando o inner join
df_generation_join = df_gen.join(df_poke, 'generation', how='inner')

## Salvando o dataframe em uma tabela
df_generation_join.write.mode('overwrite').format('orc').saveAsTable('work_dataeng.pokemons_oldschool_weliston');
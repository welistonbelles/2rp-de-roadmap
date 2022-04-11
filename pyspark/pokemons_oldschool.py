# -*- encoding: utf-8 -*-
from pyspark.sql.functions import struct
from pyspark.sql.functions import to_json
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

## Kafka Setup
pokes = spark.sql("SELECT name FROM  work_dataeng.pokemons_oldschool_weliston limit 10")
pokes = pokes.withColumn("jsonCol", to_json(struct([pokes[x] for x in  pokes.columns]))).select('jsonCol')

service_user = "2rp-weliston"
kafka_bootstrap_servers = "192.168.80.8:19093,192.168.80.7:19093,192.168.80.14:19093"
topic_name = 'nifi.send.trilha.conhecimento'
kafka_pass = "dqmQtyVB6zzjcJbZAi7DIa8LRkM7zVX3"

options = {
    "kafka.sasl.jaas.config": "com.sun.security.auth.module.Krb5LoginModule required useKeyTab=true keyTab=\"/home/{user}/{user}.keytab\" principal=\"{user}@BDACLOUDSERVICE.ORACLE.COM\";".format(user=service_user),
    "kafka.security.protocol" : "SASL_SSL",
    "kafka.sasl.kerberos.service.name" : "kafka",
    "kafka.ssl.truststore.location" : "/opt/cloudera/security/pki/bds.truststore",
    "kafka.ssl.truststore.password" : kafka_pass,
    "kafka.bootstrap.servers": kafka_bootstrap_servers,
    "topic": topic_name
}

pokes.selectExpr("CAST(jsonCol AS STRING) AS value").write.format("kafka").options(**options).save()

## Comando para deploy
# spark-submit --master yarn --conf spark.driver.memory=15g --conf \
# spark.executer.memory=6g --conf spark.executer.memoryOverhead=1g --conf \
# spark.cores.max=3 --conf spark.dynamicAllocation.maxExecutors=40 --keytab \
# /home/2rp-weliston/2rp-weliston.keytab --principal 2rp-weliston --name dev-pokemons_oldschool \
# --deploy-mode client /home/2rp-weliston/pokemons_oldschool.py
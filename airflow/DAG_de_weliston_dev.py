from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from custom_operators.tworp_spark_submit_operator import TwoRPSparkSubmitOperator

from datetime import datetime, timedelta

# Argumentos padrões a serem utilizados em todas as tasks
usuario='2rp-weliston'
default_args = {
    'owner': usuario,
    'start_date': datetime(2020, 1, 1),
    'depend_on_past': False,
    'run_as_user': usuario,
    'proxy_user': usuario
}


with DAG('de_weliston_dev', schedule_interval=None, default_args=default_args, catchup=False) as dag:
    
    task_dummy = DummyOperator(
        task_id='task_dummy'
    )

    # Autenticando com o comando Kinit atraves do bash operator
    task_kinit = BashOperator(
        task_id='task_kinit',
        bash_command=f'kinit -kt /home/{usuario}/{usuario}.keytab {usuario}'
    )

    # utilizando o bash operator para rodar o arquivo 'executar.sh'
    task_execute_sh = BashOperator(
        task_id = 'task_execute_sh',
        bash_command=f'bash /home/{usuario}/executar.sh /home/{usuario}/tests'
    )

    # utilizando o TwoRPSparkSubmitOperator para executar o arquivo pyspark
    task_poke = TwoRPSparkSubmitOperator(
        task_id="task_poke",
        name="pokemons_oldschool_weliston",
        conn_id="spark_conn",
        application=f'/home/{usuario}/pokemons_oldschool.py',
        conf={'spark.yarn.queue':f'root.users.{usuario}', 'spark.driver.memory':'20g'},
        keytab=f"/home/{usuario}/{usuario}.keytab",
        principal=usuario,
        proxy_user=None,
        verbose=True
    )

    task_dummy >> task_kinit >> task_execute_sh >> task_poke
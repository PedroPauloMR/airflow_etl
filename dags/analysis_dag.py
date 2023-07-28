import pandas as pd
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.operators.python import PythonOperator
import os
import json


# Airflow DAG
default_args = {'owner': 'pedro',
                'depends_on_past': False,
                'email': 'pedrop.ribeiro@hotmail.com',
                'email_on_failure': False,
                'email_on_retry': False,
                'retries': 5,
                'retry_delay': timedelta(minutes = 1)
                }

# define the DAG
dag = DAG( dag_id = 'analysis_dag',
          default_args = default_args,
          start_date = datetime(2023,7,25),
          end_date = datetime(2023,7,26),
          schedule_interval= timedelta(minutes = 60))

# first task 
task1 = SqliteOperator(task_id = 'query_sqlite',
                       sqlite_conn_id = 'sqlite_conn_id',
                       sql = 'src/query/order_reviews.sql',
                       dag = dag)
# task1 = SqliteOperator(task_id = 'query_sqlite',
#                        sqlite_conn_id = 'sqlite_conn_id',
#                        sql = r"""SELECT * FROM order_reviews""",
#                        dag = dag)
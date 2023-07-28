import pandas as pd
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.operators.python import PythonOperator
import os
import json
import _sqlite3


def run_query():
    conn = _sqlite3.connect('/home/pedro/Downloads/db_olist.sqlite')
    query = 'SELECT * FROM order_reviews LIMIT 10'

    # execute
    df = pd.read_sql_query(query, conn)
    df.to_csv('/home/pedro/airflow/dags/src/data/sqlite_data.csv', index = False)

    # close conn
    conn.close()
    return None


# Airflow DAG
default_args = {'owner': 'pedro',
                'depends_on_past': False,
                'email': 'pp@hotmail.com',
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


# running python operator
task1 = PythonOperator(task_id = 'analysis_dag',
                       provide_context = True,
                       python_callable = run_query,
                       dag = dag)

# running the query by a sql extension file
# task1 = SqliteOperator(task_id = 'query_sqlite',
#                        sqlite_conn_id = 'sqlite_conn_id',
#                        sql = 'src/query/order_reviews.sql',
#                        dag = dag)

# running the query statement inside the argument
# task1 = SqliteOperator(task_id = 'query_sqlite',
#                        sqlite_conn_id = 'sqlite_conn_id',
#                        sql = r"""SELECT * FROM order_reviews""",
#                        dag = dag)
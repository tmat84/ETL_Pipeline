from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from ETL_first import ETL_first

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 5, 1),
    'email': ['dag@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'etl_dag',
    default_args=default_args,
    description='Our first DAG with ETL process!',
    schedule_interval='@monthly',
)


run_etl = PythonOperator(
    task_id='whole_etl',
    python_callable=ETL_first,
    dag=dag,
)

run_etl

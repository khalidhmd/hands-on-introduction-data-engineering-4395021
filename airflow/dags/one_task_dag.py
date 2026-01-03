from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow import DAG

default_args = {
    'owner':'Khalid',
    'dependes_on_past':False,
    'email_on_failure':False,
    'email_on_retry':False,
    'retries':0,
    'catchup':False,
    'start_date':datetime(2025,1,1)
}

with DAG(dag_id='One_Task_DAG',
         description='One Task DAG Airflow pipline',
         schedule_interval=None,
         default_args=default_args,) as dag:
    task1=BashOperator(task_id='task_one',
                       bash_command='echo "Hellow DAG World!!!" > /workspaces/hands-on-introduction-data-engineering-4395021/lab/temp/dag_output_file.txt',
                       dag=dag)
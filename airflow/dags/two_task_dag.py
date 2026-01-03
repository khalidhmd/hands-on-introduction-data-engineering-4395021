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

with DAG(
    dag_id='One_Task_DAG',
    description='One Task DAG Airflow pipline',
    schedule_interval=None,
    default_args=default_args
    ) as dag:

    t0=BashOperator(
        task_id='task_0',
        bash_command='echo "Task 0 running."'
        )
    
    t1=BashOperator(
        task_id='task_1',
        bash_command='echo "Sleeping..." && sleep 5s && echo "Task 1 running."'
    )

t0 >> t1

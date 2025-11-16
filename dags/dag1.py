from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 10, 26),
    "retry_delay": timedelta(minutes=0.1),
    }

dag = DAG('get_currates',
          default_args=default_args,
          schedule_interval=None,
          catchup=True,
          max_active_tasks= 5,
          max_active_runs=1,
          tags=["Test", "MyFirstDag"]
          )
#'0 1 * * *'
task1=BashOperator(
    task_id='task1',
    bash_command='python3 /airflow/scripts/dag1/task1.py',
    dag=dag
)

task2=BashOperator(
    task_id='task2',
    bash_command='python3 /airflow/scripts/dag1/task2.py',
    dag=dag
)

task1>>task2

print('this is for test')
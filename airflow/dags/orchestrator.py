import sys
sys.path.append("/opt/airflow/request")
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from insert_records import main
from docker.types import Mount
from airflow.providers.docker.operators.docker import DockerOperator

default_args = {
    "owner": "Myst",
    "retries": 3,
    "retry_delay": timedelta(seconds=1),
}


dag = DAG(
    dag_id = "Weather_API",
    description = "A DAG to orchestrate data",
    start_date =  datetime(2026, 9, 23),
    default_args = default_args,
    schedule = timedelta(minutes=1),
    catchup = False
)


with dag:
    task1 = PythonOperator(
        task_id="Automate_the_boring_stuff",
        python_callable=main,
    )

    task2 = DockerOperator(
    task_id="Automating_the_boring_DBT",
    image="ghcr.io/dbt-labs/dbt-postgres:latest",
    command="run",
    working_dir="/usr/app",
    mounts=[
        Mount(source = "/home/myst/Documents/project/dbt/my_project",
                target = "/usr/app",
                type = "bind"),

        Mount(source = "/home/myst/Documents/project/dbt/profiles.yml",
                target = "/root/.dbt/profiles.yml",
                type = "bind")
    ],
    network_mode="my-network",
    docker_url="unix:///var/run/docker.sock",
    auto_remove="success"
    )
    task1 >> task2
    
import json
from airflow.decorators import dag, task
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
}


@dag(default_args=default_args, schedule_interval="@daily", start_date=days_ago(2),
     tags=['MWAA', 'DYNAMIC TASKS', 'TASKFLOW API', 'MAP TRANSFORM REDUCE'])
def dag_taskflow_api_dynamic_tasks():
    @task()
    def get_data():
        return [
            {"id": 1, "name": "Golden Retriever", "description": "A happy golden retriever playing with a toy",
             "URL": "https://cdn.pixabay.com/photo/2015/02/24/15/41/dog-647528_1280.jpg"},
            {"id": 2, "name": "Siamese Cat", "description": "A beautiful Siamese cat with blue eyes",
             "URL": "https://cdn.pixabay.com/photo/2017/02/20/18/03/cat-2083492_1280.jpg"},
            {"id": 3, "name": "Nature", "description": "A scenic view of a mountain range with trees",
             "URL": "https://cdn.pixabay.com/photo/2016/02/13/13/11/mountains-1199028_1280.jpg"},
            {"id": 4, "name": "City", "description": "A night view of Tokyo city skyline",
             "URL": "https://cdn.pixabay.com/photo/2016/08/31/23/22/tokyo-1631703_1280.jpg"}]

    @task(max_active_tis_per_dag=5)
    def mapper(arg):
        print(arg)
        return arg

    def transformer(image_dict):
        return {"image_id": image_dict["id"], "image_url": image_dict["URL"]}

    @task()
    def reducer(arg):
        print(*arg, sep="\n")

    transformed_list = get_data().map(transformer)
    result = mapper.expand(arg=transformed_list)
    reducer(result)


dag_with_taskflow_api = dag_taskflow_api_dynamic_tasks()

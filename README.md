## Dynamic Task Mapping in Airflow DAG
The DAG is utilizing the functionality of dynamic task mapping in Airflow to generate tasks on the runtime.
The DAG implements very simple logic of `MAP REDUCE`also includes the `TRANSFORM`

### DAG

 ```mermaid
graph LR
A(get_data) --> B(mapper)
B --> C(reducer)
```

The DAG is working on mock data:

    [{
		"id": 1,
		"name": "Golden Retriever",
		"description": "A happy golden retriever playing with a toy",
		"URL": "https://cdn.pixabay.com/photo/2015/02/24/15/41/dog-647528_1280.jpg"
	},
	{
		"id": 2,
		"name": "Siamese Cat",
		"description": "A beautiful Siamese cat with blue eyes",
		"URL": "https://cdn.pixabay.com/photo/2017/02/20/18/03/cat-2083492_1280.jpg"
	},
	{
		"id": 3,
		"name": "Nature",
		"description": "A scenic view of a mountain range with trees",
		"URL": "https://cdn.pixabay.com/photo/2016/02/13/13/11/mountains-1199028_1280.jpg"
	},
	{
		"id": 4,
		"name": "City",
		"description": "A night view of Tokyo city skyline",
		"URL": "https://cdn.pixabay.com/photo/2016/08/31/23/22/tokyo-1631703_1280.jpg"
	}]

## Target Versions  
|| versions  |  
|--|--|  
| MWAA | 2.4.3 |  
| Python | 3.10.0 |

## Local Environment
The local development environment is based on `pipenv` and  `MWAA Local Runer 2.4.3`
Local `MWAA Runner` is a part of project and can be started by `Makefile` command:

> make start-local-mwaa

Similarly, to stop local `MWAA Runner`:

> make teardown-local-mwaa

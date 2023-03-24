start-local-mwaa:
	./mwaa-local-env build-image
	./mwaa-local-env start >/dev/null 2>&1 &
	echo "Waiting for Airflow to come up. This can take a minute..."
	while [ -z $$(docker ps --filter "name=local-runner" --filter "health=healthy" --quiet) ]; do sleep 5; done
	echo "\nAirflow webserver started on http://localhost:8080, user: admin, password: test"

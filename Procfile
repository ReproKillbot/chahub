# NOTE: We want to start in the `src/` directory for all of our Python paths
#web: env PYTHONPATH=$PYTHONPATH:$PWD/src bin/start-pgbouncer-stunnel daphne asgi:application --port $PORT --bind 0.0.0.0 -v2
web: bin/start-pgbouncer-stunnel sh -c 'cd src/ && exec daphne asgi:application --port $PORT --bind 0.0.0.0 -v2'

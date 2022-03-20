gunicorn \
    --reload \
    --bind 0.0.0.0:8081 \
    --workers 2 \
    --worker-class eventlet \
    --log-level DEBUG \
    --access-logfile "-" \
    --error-logfile "-" \
    poc_training_docker_django_backend.wsgi
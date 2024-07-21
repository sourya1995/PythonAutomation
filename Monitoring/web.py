from flask import Response, Flask
from time import sleep
import random
import prometheus_client
from prometheus_client import Counter
from prometheus_client import random, Histogram

app = Flask('prometheus_app')

REQUESTS = Counter('requests', 'Number of requests to the Flask App', ['endpoint'])
TIMER = Histogram('slow', 'slow requests', ['endpoint'])


@app.route('/metrics/')
def metrics():
    return Response(
        prometheus_client.generate_latest(),
        mimetype='text/plain; version=0.0.4; charset=utf-8'
    )



@app.route('/')
def index():
    REQUESTS.labels(endpoint='/').inc()
    return '<h1>PROMETHEUS BACKED FLASK APP </h1>'

@app.route('/database/')
def database():
    with TIMER.labels('/database').time():
        # simulated database response time
        sleep(random.uniform(1, 3))
        return '<h1>Completed expensive database operation</h1>'


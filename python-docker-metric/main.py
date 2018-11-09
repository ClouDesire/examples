import json
from random import randint

import web

from file_system_database import FileSystemDatabase

urls = (
    '/', 'Index',
    '/metric-counter', 'CounterRest',
    '/metric-gauge', 'GaugeRest'
)

render = web.template.render('templates/')


def metric_dict(name, value):
    return {'metricsName': name, 'value': value}


class Index:
    def GET(self):
        return render.index(FileSystemDatabase.read())


class CounterRest:
    def GET(self):
        metric_counter = metric_dict('Counter Metric', FileSystemDatabase.read())
        web.header('Content-Type', 'application/json')
        return json.dumps(metric_counter)

    def POST(self):
        new_value = FileSystemDatabase.read() + 1
        FileSystemDatabase.write(new_value)
        metric_counter = metric_dict('Counter Metric', new_value)
        web.header('Content-Type', 'application/json')
        return json.dumps(metric_counter)


class GaugeRest:
    def GET(self):
        metric_counter = metric_dict('Gauge Metric', randint(0, 10))
        web.header('Content-Type', 'application/json')
        return json.dumps(metric_counter)


if __name__ == "__main__":
    FileSystemDatabase.write(42)
    app = web.application(urls, globals())
    app.run()

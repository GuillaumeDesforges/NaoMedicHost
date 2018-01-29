import json

from flask import Flask
app = Flask(__name__)


clients = [
    {
        'name': "Will Smith",
        'status': "arrived"
    }
]

@app.route('/')
def root():
    return "Hello World!"

@app.route('/api/clients')
def getClientsList():
    return json.dumps(list(map(lambda x: x['name'], clients)))

@app.route('/api/clients/<name>')
def getClient(name):
    clients_found = list(filter(lambda x: x['name'] == name, clients))
    if len(clients_found) > 0:
        return json.dumps(clients_found[0])
    else:
        return 'Client name not found', 404

@app.route('/api/clients/<name>/status/<status>', methods=['POST'])
def setClientStatus(name):
    clients_found = list(filter(lambda x: x['name'] == name, clients))
    if len(clients_found) > 0:
        client = clients_found[0]
        client['status'] = "arrived"
        return 'Client status updated'
    else:
        return 'Client name not found', 404

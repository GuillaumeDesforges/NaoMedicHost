import json

from flask import Flask, render_template
app = Flask(__name__)

nextClient = "Will Smith"

clients = [
    {
        'name': "Will Smith",
        'status': "arrived",
        'date': "01/01/2018 12:00",
        'comment': "Fièvre et mal au ventre"
    },
    {
        'name': "Luc Dormieux",
        'status': "awaited",
        'date': "02/01/2018 8:30",
        'comment': "Tensions dans le déviatorique"
    }
]

@app.route('/')
def root():
    return render_template("index.html", clients=clients)

@app.route('/nextclient')
def getNextClient():
	if nextClient:
		return nextClient, 200
	else:
		return 'No next client', 400

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

from google.cloud import datastore
client = datastore.Client()
query = client.query(kind="Code")
results = list(query.fetch())
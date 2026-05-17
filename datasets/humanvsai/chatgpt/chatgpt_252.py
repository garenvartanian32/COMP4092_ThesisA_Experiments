import requests

def fetch_yokozuna_index(index):
    solr_url = "http://localhost:8983/solr/"
    query_url = solr_url + index + "/select?q=*:*"
    response = requests.get(query_url)
    return response.content.decode('utf-8')

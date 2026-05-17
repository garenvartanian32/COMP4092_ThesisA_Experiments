def main(host='localhost', port=8086):
    client = InfluxDBClient(host=host, port=port)
    return client

def write_data(client, data):
    """Write data to the InfluxDB."""
    client.write_points(data)

def read_data(client, query):
    """Read data from the InfluxDB."""
    result = client.query(query)
    return result

def main():
    client = main('localhost', 8086)
    data = [{'measurement': 'cpu_load_short', 'tags': {'host': 'server01', 'region': 'us-west'}, 'time': '2009-11-10T23:00:00Z', 'fields': {'value': 0.64}}]
    write_data(client, data)
    query = 'SELECT * FROM cpu_load_short'
    result = read_data(client, query)
    print(result)
from influxdb import InfluxDBClient

def connect_to_influxdb(host, port, username, password, database):
    client = InfluxDBClient(host=host, port=port, username=username, password=password, database=database)
    return client

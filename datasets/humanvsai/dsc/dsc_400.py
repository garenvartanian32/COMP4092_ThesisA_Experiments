from influxdb import InfluxDBClient

def main(host='localhost', port=8086):
    """Instantiate a connection to the InfluxDB."""
    client = InfluxDBClient(host=host, port=port)
    return client
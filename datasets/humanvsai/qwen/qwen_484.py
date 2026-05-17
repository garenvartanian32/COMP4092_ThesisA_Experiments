def cli(obj, ids, query, filters, display, from_date=None):
    query_string = f"obj={obj}&ids={','.join(ids)}&query={query}"
    if filters:
        query_string += f"&filters={','.join(filters)}"
    if display:
        query_string += f'&display={display}'
    if from_date:
        query_string += f'&from_date={from_date}'
    response = requests.get(f'https://api.example.com/alerts?{query_string}')
    if response.status_code == 200:
        return response.json()
    else:
        return f'Error: {response.status_code} - {response.text}'
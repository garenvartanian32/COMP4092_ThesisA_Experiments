from google.cloud import bigquery

def get_variants(client, variant_set_id, call_set_ids=[], reference_name=None,
                 start=None, end=None, page_size=None, page_token=None):
    request = bigquery.VariantServiceClient.GASearchVariantsRequest(variant_set_id=variant_set_id, call_set_ids=call_set_ids, reference_name=reference_name, start=start, end=end)
    results = client.search_variants(request=request, page_size=page_size, page_token=page_token)
    return iter(results)

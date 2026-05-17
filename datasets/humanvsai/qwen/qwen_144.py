def batch_taxonomy(list_of_taxids):
    from Bio import Entrez
    Entrez.email = 'your_email@example.com'
    batch_size = 100
    results = {}
    for i in range(0, len(list_of_taxids), batch_size):
        batch = list_of_taxids[i:i + batch_size]
        handle = Entrez.efetch(db='taxonomy', id=','.join(map(str, batch)), retmode='xml')
        record = Entrez.read(handle)
        handle.close()
        for taxon in record['TaxaSet']['Taxon']:
            results[taxon['TaxId']] = taxon['ScientificName']
    return results
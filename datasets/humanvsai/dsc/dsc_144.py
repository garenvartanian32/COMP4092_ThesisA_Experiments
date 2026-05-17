from Bio import Entrez

def batch_taxonomy(list_of_taxids):
    """Convert list of taxids to Latin names"""
    Entrez.email = "your_email@example.com"  # Always tell NCBI who you are
    taxids = ','.join(map(str, list_of_taxids))  # Convert list to comma-separated string
    handle = Entrez.efetch(db="taxonomy", id=taxids)
    records = Entrez.read(handle)
    return {record['TaxId']: record['ScientificName'] for record in records}

# Example usage:
print(batch_taxonomy([562, 561, 2157]))
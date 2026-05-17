from ete3 import NCBITaxa

def convert_taxids_to_names(taxid_list):
    ncbi = NCBITaxa()
    latin_names = []
    for taxid in taxid_list:
        name = ncbi.get_taxid_translator([taxid])[taxid]
        lineage = ncbi.get_lineage(taxid)
        name = ncbi.get_taxid_translator(lineage)[taxid]
        latin_names.append(name)
    return latin_names

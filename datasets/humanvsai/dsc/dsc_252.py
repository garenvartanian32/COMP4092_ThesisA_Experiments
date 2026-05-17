from pysolr import Solr

def get_search_index(index):
    """Fetch the specified Solr search index for Yokozuna.

    :param index: a name of a yz index
    :type index: string

    :rtype string"""

    # Assuming you're running Solr on localhost at port 8983
    solr_url = 'http://localhost:8983/solr/' + index

    # Create a connection to the Solr server
    solr = Solr(solr_url)

    # Fetch all documents in the index
    results = solr.search('*:*')

    return results
from bs4 import BeautifulSoup

def get_token_nodes_from_sentence(self, sentence_root_node):
    """returns a list of token node IDs belonging to the given sentence"""
    soup = BeautifulSoup(sentence_root_node, 'html.parser')
    token_nodes = soup.find_all('token')
    return [node.get('id') for node in token_nodes]
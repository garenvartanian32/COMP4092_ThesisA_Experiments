from bs4 import BeautifulSoup

def process_forward(html):
    soup = BeautifulSoup(html, 'html.parser')
    msg_type = None
    html_top = None
    html_bottom = None
    msg_headers = {}
    html_body = None
    
    if not soup.find_all('blockquote'):
        return None
        
    if soup.find_all('blockquote')[0].find_all('div'):
        msg_type = 'quote'
        html_top = str(soup.find_all('blockquote')[0])
    else:
        try:
            fwd_tag = soup.find_all('blockquote')[0].contents[0].strip()
        except IndexError:
            fwd_tag = ''
        if fwd_tag.startswith('From:') or fwd_tag.startswith('De:'):
            msg_type = 'forward'
        else:
            msg_type = 'reply'
        for tag in ['b', 'i']:
            try:
                msg_headers[tag] = soup.find_all(tag)[0].parent.text
            except IndexError:
                continue
    if msg_type == 'forward' or msg_type == 'reply':
        for tag in ['from', 'to', 'subject', 'cc', 'bcc', 'reply-to']:
            try: 
                msg_headers[tag] = soup.find_all('td', {'class': 'header_name'}, text=tag)[0].next_sibling.text
            except IndexError:
                continue
    if soup.find_all('div', {'class': 'fwd_quoted'}):
        html_bottom = str(soup.find_all('div', {'class': 'fwd_quoted'})[0])
    if soup.find_all('table', {'class': 'quote'}) and soup.find_all('table', {'class': 'quote'})[0].find_all('tr'):
        html_body = str(soup.find_all('table', {'class': 'quote'})[0].find_all('tr')[-1])
        
    return {'type': msg_type, 'html_top': html_top, 'html_bottom': html_bottom, **msg_headers, 'html': html_body}

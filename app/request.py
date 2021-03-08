import urllib.request,json
from .models import Quote

base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['QUOTE_API_BASE']

def get_quote():
    get_quote_url = base_url.format()

    with urllib.request.urlopen(get_quote_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)

        quote_results = None

        if get_quote_response['quotes']:
            quote_results_list= get_quote_response['quotes']
            quote_results = process_results(quote_results_list)

    return quote_results    

def process_results(quote_list):
    quote_results = []
    for quote_item in quote_list:
        author = quote_item.get('author')
        quote = quote_item.get('quote')

    return quote_results    
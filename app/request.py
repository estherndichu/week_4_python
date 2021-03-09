import urllib.request,json
from .models import Quote

base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['BASE_URL']

def get_quote():
    with urllib.request.urlopen(base_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)

        quote_results = None

        if get_quote_response:
            author = get_quote_response.get('author')
            quote = get_quote_response.get('quote')
            quote_object = Quote(author,quote)

    return quote_object    

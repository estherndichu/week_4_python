from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_quote
from ..models import Quote

@main.route('/')
def quotes():

    quote = get_quote()

    return render_template('quotes.html',quotes=quote)
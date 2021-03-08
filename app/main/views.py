from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_quote
from ..models import Quote

@main.route('/')
def quotes():

    Quote = get_quote()

    return render_template('index.html',quote=Quote)
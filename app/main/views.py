from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_quote
from ..models import Quote
from . forms import BlogForm

@main.route('/')
def index():

    Quote = get_quote()

    return render_template('index.html',quote=Quote)

@main.route('/new_blog', methods=['GET', 'POST'])
@login_required
def new_blog():

    title = 'Bloggiez'

    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        blog = form.blog.data
        user_id = current_user._get_current_object().id

        blogpost = Blog(blog=blog, title=title, user_id=user_id)
        blogpost.save()
        
        return redirect(url_for('main.blogs'))
    return render_template('new_blog.html', form=form)    
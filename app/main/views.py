from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_quote
from ..models import Quote,Blog,User,Comment
from . forms import BlogForm,CommentForm,UpdateProfile
from flask_login import login_required,current_user
from .. import db

@main.route('/')
def index():

    Quote = get_quote()
    blogs = Blog.query.all()

    return render_template('index.html',quote=Quote,blogs=blogs)

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

        return redirect(url_for('main.index'))
        
    return render_template('new_blog.html', form=form) 

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)
    
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)     

@main.route('/comment/<int:blog_id>', methods=['GET', 'POST'])
@login_required
def comment(blog_id):

    form = CommentForm()
    blog = Blog.query.get(blog_id)
    user = User.query.all()
    comments = Comment.query.filter_by(blog_id=blog_id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        blog_id = blog_id
        user_id = current_user._get_current_object().id
        comment = Comment(
            comment=comment,
            blog_id=blog_id,
            user_id=user_id,
            )

        comment.save()
        comments = [comment]
        print(comments)
        return redirect(url_for('new_comment.html', blog_id=blog_id))
    return render_template('new_comment.html', form=form, blog=blog, comments=comments, user=user)


      
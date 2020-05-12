from flask import render_template, request, redirect, url_for, flash, abort,current_app
#from PIL import Image
from . import main
from ..request import get_quote
from flask_login import current_user, login_required
from .. import db
from ..models import Post, User
from .forms import PostForm, UpdateProfileForm
import os
import secrets



@main.route('/')
def index():
    
    '''
    root page function that returns the index page and its data
    
    '''
    
    title = "Home | Blog App pages"
    quote = get_quote()
    
    return render_template("index.html", title = title, quote=quote)
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts, title="Posts | Welcome to BlogApp|Salem")
    


@main.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        
        db.session.add(post)
        db.session.commit()
        
        flash('You post has been created!', 'success')
        return redirect(url_for('main.index'))
    
    return render_template('create_post.html', title='New Post | Welcome to BlogApp|Salem', form=form)

@main.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@main.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id) 
    if post.author!= current_user:
        abort(403)
        
    form = PostForm()
    if form.validate_on_submit():
        
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('main.post', post_id=post.id))
    
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        
    return render_template('create_post.html', title='Update Post | Welcome to BlogApp|Salem', form=form, legend='Update Post')

@main.route("/post/<int:post_id>/delete", methods=['GET','POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author !=current_user:
        abort(403)
        
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/photos', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@main.route("/account", methods=['GET', 'POST'])
def account():
    form = UpdateProfileForm()
    
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
            
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been activated!', 'success')
        return redirect(url_for('main.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        
    image_file = url_for('static', filename='photos' + current_user.image_file)
    
    return render_template('account.html', title='Account | Welcome to BlogApp|Salem', image_file=image_file, form=form)

@main.route('/user/<string:username>')
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)

            
            
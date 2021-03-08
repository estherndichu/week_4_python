from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField
from wtforms.validators import Required

class BlogForm(FlaskForm):

    title = StringField('Author Name', validators=[Required()])
    blog = TextAreaField('Write blog below ...', validators=[Required()])
    submit = SubmitField('Post')
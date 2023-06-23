from flask import render_template, flash, redirect, url_for, current_app
from flask_login import current_user, login_required
from app.uploads import bp
from app.uploads.forms import UploadForm
import os

@bp.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        uploaded_file = form.file.data
        if uploaded_file.filename != '':
            path = os.path.join(
                current_app.root_path, 
                'static/avatars', 
                current_user.get_id(), 
                uploaded_file.filename)
            print(path)
            uploaded_file.save(path)
            flash('File uploaded successfully!')
            return redirect(url_for('main.edit_profile'))
    return render_template('uploads/upload.html', form=form)


@bp.route('/uploads/<filename>')
@login_required
def upload(filename):
    print(('''<!doctype html>
    <html>
    <head>
        <title>File Upload</title>
    </head>
    <body>
        <hr>
        <img src="''' 
    + url_for('static', filename='avatars/' + str(current_user.get_id() + '/' + filename)) 
    + '''}" style="width: 64px">
    </body>
    </html>
    '''))
    return ('''<!doctype html>
    <html>
    <head>
        <title>File Upload</title>
    </head>
    <body>
        <hr>
        <img src="''' 
    + url_for('static', filename='avatars/' + str(current_user.get_id() + '/' + filename)) 
    + '''" style="width: 64px">
    </body>
    </html>
    ''')

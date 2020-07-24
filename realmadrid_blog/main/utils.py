from flask import url_for
from flask_login import current_user


def logo_picture():
    return url_for('static', filename=f'img/real.png')


def profile_picture():
    if current_user.is_authenticated:
        image_file = url_for('static', filename=f'img/{current_user.image_file}')
        return image_file
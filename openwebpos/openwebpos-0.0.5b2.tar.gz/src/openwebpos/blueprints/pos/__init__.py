from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app

bp = Blueprint('pos', __name__, template_folder='templates')


@bp.get('/')
def index():
    return render_template('pos/index.html')

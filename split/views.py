from flask import Blueprint, render_template

split_bp = Blueprint('split', __name__, template_folder='templates')

@split_bp.route('/split')
def split():
    return render_template('split.html')
from flask import Blueprint, render_template

# blueprint configuration
split_bp = Blueprint('split', __name__, template_folder='templates')


# main split page
@split_bp.route('/split')
def split():
    return render_template('split.html')
# imports
from flask import Blueprint, render_template

# blueprint configuration
search_bp = Blueprint('search', __name__, template_folder='templates')

# main search page
@search_bp.route('/search')
def search():
    return render_template('search.html')
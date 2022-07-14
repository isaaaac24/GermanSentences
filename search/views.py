from flask import Blueprint, render_template

search_bp = Blueprint('search', __name__, template_folder='templates')

@search_bp.route('/search')
def search():
    return render_template('search.html')
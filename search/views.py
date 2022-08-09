# imports
from flask import Blueprint, render_template, request
from main import session
from models import Sentence
from search.forms import SearchForm

# blueprint configuration
search_bp = Blueprint('search', __name__, template_folder='templates')


# main search page
@search_bp.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()

    if request.method == "POST":
        sen_all = session.query(Sentence).filter(Sentence.sentence.contains(form.search_term.data)).all()
        return render_template('search.html', form=form, sentences=sen_all)

    return render_template('search.html', form=form)

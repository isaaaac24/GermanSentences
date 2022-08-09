import re

import nltk
from flask import Blueprint, render_template, url_for
from werkzeug.utils import secure_filename, redirect

from main import session
from models import Sentence
from split.forms import UploadForm

# blueprint configuration
split_bp = Blueprint('split', __name__, template_folder='templates')


# main split page
@split_bp.route('/split', methods=['GET', 'POST'])
def split():
    form = UploadForm()

    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        form.file.data.save('uploads/' + filename)
        filepath = ('uploads/' + filename)
        split_file(filepath)
        return redirect(url_for('split.split'))

    return render_template('split.html', form=form)


def split_file(finpath):
    # read uploade file
    fin = open(finpath, 'r', encoding='utf-8')
    data = fin.read()

    # tokenizes file of sentences into sentences
    sntncs = nltk.tokenize.sent_tokenize(data)
    for s in sntncs:
        # removes duplicate spaces in string
        s = re.sub('\s+', ' ', s)

        # obtain word count of sentences
        word_count = len(s.split())

        # write formatted sentence to database
        sen = Sentence(sentence=s, word_count=word_count)
        session.add(sen)
        session.commit()

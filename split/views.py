import re

import nltk
import praw
from flask import Blueprint, render_template, url_for, request
from werkzeug.utils import secure_filename, redirect

from main import session
from models import Sentence
from split.forms import UploadForm, SearchForm

# blueprint configuration
split_bp = Blueprint('split', __name__, template_folder='templates')


# main  file split page
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

# reddit search page
@split_bp.route('/reddit', methods=['GET', 'POST'])
def reddit():
    form = SearchForm()

    if request.method == "POST":
        reddit = praw.Reddit(client_id='5034T2LHlpmOablUkj-vXg',
                             client_secret='QPmtpn9fkhO5CbWwxosZJiH8pO1wbQ',
                             user_agent='sentence scraper')

        submission = reddit.submission(url=form.search_term.data)

        for top_level_comment in submission.comments:
            word_count = len(top_level_comment.body.split())
            sen = Sentence(sentence=top_level_comment.body, word_count=word_count)
            session.add(sen)
            session.commit()

        return render_template('reddit.html', form=form, comments = submission.comments)

    return render_template('reddit.html', form=form)

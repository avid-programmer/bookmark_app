from flask import Flask, request, render_template,redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    with open('./bookmark_files/homepage.txt', 'r') as f:
        bookmarks = [b.strip('\n') for b in f.readlines()]
    return render_template('index.html', bookmarks=bookmarks, bookmarks2=bookmarks)


@app.route('/register_video')
def register_video():
    with open('./bookmark_files/glossary.txt', 'r') as f:
        options = [o.strip('\n') for o in f.readlines()]
    return render_template('register_video.html', options=options)

@app.route('/book/video', methods=["POST"])
def book_video():

    # Getting the form data
    bookmark_url = request.form.get('bookmark_url')
    category = request.form.get('category')
    homepage = request.form.get('current')

    # Checking in whether the category exists in glossary or not
    with open('./bookmark_files/glossary.txt', 'r') as g1:
        glist = [a.strip('\n') for a in g1.readlines()]

    # If the category does not exists then add it to the glossary
    if not (category in glist):
        with open('./bookmark_files/glossary.txt', 'a') as g2:
            g2.writelines(category)
            g2.writelines('\n')

    # Create (or open) the category.txt file to write the bookmark url
    category = category.replace(' ', '_') + '.txt'
    category = './bookmark_files/' + category
    burl = bookmark_url.split(',')
    with open(category, 'a') as f1:
        for line in burl:
            f1.writelines(line.split('=')[1])
            f1.writelines('\n')

    # Place also on the homepage or not
    if homepage:
        with open('./bookmark_files/homepage.txt', 'a') as f2:
            for line in burl:
                f2.writelines(line.split('=')[1])
                f2.writelines('\n')

    return redirect(url_for('register_video'))


@app.route('/register_other')
def register_other():
    with open('./bookmark_files/glossary.txt', 'r') as f:
        options = [o.strip('\n') for o in f.readlines()]
    return render_template('register_other.html', options=options)


@app.route('/book/other', methods=["POST"])
def book_other():

    # Getting the form data
    bookmark_url = request.form.get('bookmark_url')
    category = request.form.get('category')
    description = request.form.get('description')
    homepage = request.form.get('current')

    # Checking in whether the category exists in glossary or not
    with open('./bookmark_files/glossary.txt', 'r') as g1:
        glist = [a.strip('\n') for a in g1.readlines()]

    # If the category does not exists then add it to the glossary
    if not (category in glist):
        with open('./bookmark_files/glossary.txt', 'a') as g2:
            g2.writelines(category)
            g2.writelines('\n')

    # Create (or open) the category.txt file to write the bookmark url
    category2 = category.replace(' ', '_') + '.txt'
    category2 = './bookmark_files/' + category2

    with open(category2, 'a') as f1:
        f1.writelines('{' + bookmark_url + ":" + description + '}')
        f1.writelines('\n')
    # Place also on the homepage or not
    if homepage:
        with open('./bookmark_files/homepage2.txt', 'a') as f2:
            f2.writelines('{' + bookmark_url + "^" + description + '}')
            f2.writelines('\n')

    return redirect(url_for('register_other'))

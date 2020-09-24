import sqlite3
import time

from flask import Flask, render_template, url_for, request

db_file = "database.db"
app = Flask(__name__)


@app.template_filter('velke')
def velka_pismena(s: str):
    return s.upper()


app.add_template_filter(zip, 'zip')


@app.route('/')
def index():
    return 'Huray, there is first web page !'


@app.route('/user')
@app.route('/user/<int:user_id>/')
def user(user_id=None):
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        if user_id is None:
            cursor.execute('SELECT * FROM author')
        else:
            cursor.execute(f'SELECT * FROM author WHERE id={user_id}')
        fetch = cursor.fetchall()   # fetch = [ (1, "John") , (2, "Alice") ]
        print(fetch)
        return render_template("users.html", users=fetch)


@app.route('/articles')
def articles():
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM article')
        articles = cursor.fetchall()
        authors = cursor.execute('SELECT * FROM author').fetchall()

        print(authors)
        print(articles)
        urls = [url_for('edit_article', article_id=art[0]) for art in articles]
        authors = {a[0]: a[1] for a in authors}
        return render_template("articles.html", articles=articles, urls=urls, authors=authors)


@app.route('/edit_article/<int:article_id>', methods=['GET', 'POST'])
def edit_article(article_id):
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        if request.method == "POST":
            title = request.form.get("title")
            text = request.form.get("text")
            query = 'UPDATE article ' \
                    f'SET title = "{title}"' \
                    f', text = "{text}"' \
                    ', timestamp = datetime("now") ' \
                    f'WHERE id = {article_id}'
            cursor.execute(query, article_id)

        query = 'SELECT ar.id, ar.title, ar.text, ar.timestamp, au.name ' \
                'FROM article ar ' \
                'JOIN author au ON ar.author_id = au.id' \
                f' WHERE ar.id={article_id}'
        cursor.execute(query)
        article = cursor.fetchone() # or fetchall()[0]
        return render_template("article_edit.html", article=article)

@app.route('/articles/<int:article_id>')
def article_view(article_id):
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        query = 'SELECT ar.id, ar.title, ar.text, ar.timestamp, au.name ' \
                'FROM article ar ' \
                'JOIN author au ON ar.author_id = au.id' \
                f' WHERE ar.id={article_id}'
        cursor.execute(query)
        article = cursor.fetchone()
        print(article)
        return render_template("article.html", article=article)


if __name__ == '__main__':
    app.run(debug=True)

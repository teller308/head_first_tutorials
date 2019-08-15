from flask import Flask
from mymodules import vsearch

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hellow world from Flask!'


@app.route('/search4')
def search4() -> str:
    return str(vsearch.search_for_chars('life, the universe, and everything!', 'eiru,!'))


app.run()

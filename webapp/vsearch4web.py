from flask import Flask, render_template, request, escape, session
from DBcm import UseDatabase, ConnectionError
from checker import check_logged_in


app = Flask(__name__)
app.secret_key = 'AwesomeKey1'
app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'postgres',
                          'password': '***',
                          'database': 'vsearchlogdb',
                          'port': '5432', }


def log_request(req: 'flask_request', res: str) -> None:

    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log
                (phrase, letters, ip, browser_string, results)
                values
                (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'], req.form['letters'], req.remote_addr, req.user_agent.browser, res))


def search4letters(phrase: str, chars: str) -> set:
    """Returns chars found in phrase."""
    return set(chars).intersection(set(phrase))


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    try:
        log_request(request, results)
    except Exception as err:
        print('***** Logging failed with: ', str(err))
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!',)


@app.route('/viewlog')
@check_logged_in
def viewlog() -> 'html':
    
    contents = []
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
                _SQL = "select phrase, letters, ip, browser_string, results from log;"
                cursor.execute(_SQL)
                contents = cursor.fetchall()

                titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
                return render_template('viewlog.html',
                                        the_title='View log',
                                        the_row_titles=titles,
                                        the_data=contents,)
    except ConnectionError as err:
        print('Something went wrong:', err)
    return 'Error'


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'


@app.route('/logout')
def do_logout() -> str:
    if 'logged_in' in  session:
        session.pop('logged_in')
        return 'You are now logged out.'    
    return 'You are NOT logged in.'


if __name__ == '__main__':
    app.run(debug=True)
    # app.run()

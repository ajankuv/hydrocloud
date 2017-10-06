from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('overview.html')

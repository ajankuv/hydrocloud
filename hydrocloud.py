from flask import Flask, render_template
from gpiofunc import *
import subprocess

app = Flask(__name__)
app.register_blueprint(on)
app.register_blueprint(off)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('overview.html')

#set state for all relays to off
subprocess.call(['./scripts/gpio-out.sh'])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4200)

from flask import Flask, render_template
import wiringpi as GPIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def cakes():
    return render_template('main.html')

#subprocess.call(['./gpio-out.sh'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

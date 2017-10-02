from flask import Flask, render_template
import wiringpi as GPIO
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def cakes():
    return render_template('main.html')

#setup calls for hardware to set state
subprocess.call(['./gpio-out.sh'])
#wiringpi.wiringPiSetupGpio()

def pin0on():
    subprocess.call(['gpio write 0 1'])

def pin0off():
    subprocess.call(['gpio write 0 0'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4200)

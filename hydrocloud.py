from flask import Flask, render_template
import wiringpi as GPIO
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/on')
def turn_on():
    subprocess.call(["gpio", "write", "0", "1"] shell=True)
    return '', 204  # no content

@app.route('/off')
def turn_off():
    subprocess.call(["gpio", "write", "0", "1"] shell=True)
    return '', 204  # no content


#setup calls for hardware to set state
subprocess.call(['./gpio-out.sh'])
#wiringpi.wiringPiSetupGpio()



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4200)

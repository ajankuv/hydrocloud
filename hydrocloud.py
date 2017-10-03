from flask import Flask, render_template
#import wiringpi as GPIO
import subprocess
#import gpiofunc

app = Flask(__name__)
app.register_blueprint(turn_on,turn_off)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

#@app.route('/on')
#def turn_on():
#    subprocess.call(['gpio', 'write', '0', '1'])
#    return '', 204  # no content

#@app.route('/off')
#def turn_off():
#    subprocess.call(['gpio', 'write', '0', '0'])
#    return '', 204  # no content

#set state for all relays to off
subprocess.call(['./scripts/gpio-out.sh'])




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4200)

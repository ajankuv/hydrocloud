from flask import Flask, render_template
#import wiringpi as GPIO
import subprocess
import gpiofunc

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')



#set state for all relays to off
subprocess.call(['./scripts/gpio-out.sh'])




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4200)

from flask import Flask, render_template
#import wiringpi as GPIO
import subprocess

@app.route('/on')
def turn_on():
    subprocess.call(['gpio', 'write', '0', '1'])
    return '', 204  # no content

@app.route('/off')
def turn_off():
    subprocess.call(['gpio', 'write', '0', '0'])
    return '', 204  # no content

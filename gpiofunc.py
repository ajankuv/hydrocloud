from flask import Blueprint, request
import subprocess

on = Blueprint('on', __name__)
off = Blueprint('off', __name__)

@on.route('/on/<gpiopin>')
def turn_on(gpiopin):
    subprocess.call(['gpio', 'write', request.view_args['gpiopin'], '1'])
    return '', 204  # no content

@off.route('/off/<gpiopin>')
def turn_off(gpiopin):
    subprocess.call(['gpio', 'write', request.view_args['gpiopin'], '0'])
    return '', 204  # no content

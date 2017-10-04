from flask import Blueprint
import subprocess

on = Blueprint('on', __name__)
off = Blueprint('off', __name__)

@on.route('/on/<int:gpiopin_id>')
def turn_on(gpiopin_id):
    subprocess.call(['gpio', 'write', request.view_args['gpiopin_id'], '1'])
    return '', 204  # no content

@off.route('/off/<int:gpiopin_id>')
def turn_off(gpiopin_id):
    subprocess.call(['gpio', 'write', request.view_args['gpiopin_id'], '0'])
    return '', 204  # no content

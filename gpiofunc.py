from flask import Blueprint
import subprocess

turn_on = Blueprint('turn_on', __name__)
turn_off = Blueprint('turn_off', __name__)

@turn_on.route('/on')
def turn_on():
    subprocess.call(['gpio', 'write', '0', '1'])
    return '', 204  # no content

@turn_off.route('/off')
def turn_off():
    subprocess.call(['gpio', 'write', '0', '0'])
    return '', 204  # no content

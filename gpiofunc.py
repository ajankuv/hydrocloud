from flask import Blueprint
import subprocess

turn_on = Blueprint('on', __name__)
turn_off = Blueprint('off', __name__)

@on.route('/')
def turn_on():
    subprocess.call(['gpio', 'write', '0', '1'])
    return '', 204  # no content

@off.route('/')
def turn_off():
    subprocess.call(['gpio', 'write', '0', '0'])
    return '', 204  # no content

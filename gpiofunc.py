from flask import Blueprint
import subprocess

on = Blueprint('on', __name__)
off = Blueprint('off', __name__)

@on.route('/on')
def turn_on():
    subprocess.call(['gpio', 'write', '0', '1'])
    return '', 204  # no content

@off.route('/off')
def turn_off():
    subprocess.call(['gpio', 'write', '0', '0'])
    return '', 204  # no content

from flask import Flask
from gpiofunc import *
import subprocess
import hydrocloudlogger
import routes

app = Flask(__name__)
app.register_blueprint(on)
app.register_blueprint(off)
pp.register_blueprint(app)

#set state for all relays to off
subprocess.call(['./scripts/gpio-out.sh'])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4200)

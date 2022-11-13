from flask import Flask, render_template, request, render_template_string
from messages import ADD_STUDENT, REMOVE_STUDENT
from gevent.pywsgi import WSGIServer

# If you're thinking 'what weird Python is this??', it's demo-code and I'm not allowed to use classes yet:)
import groups


def create_web(messages, handlers):
    app = Flask(__name__, template_folder='views')

    @app.get('/')
    def index():
        return render_template('index.html')

    @app.post('/join')
    def join_group():
        name = request.form['name']
        team = request.form['team']
        choices = []
        for program in groups.PROGRAM_NAMES:
            value = request.form[program]
            if value is not None:
                choices.append((program, int(value)))

        if groups.is_valid_groupchoice(choices):
            messages.append((ADD_STUDENT, (team, name, choices)))
            return render_template('thanks.html', name=name)
        else:
            return render_template_string("Invalid choices", name=name, status=400)

    @app.post('/leave')
    def leave_group():
        name = request.form['name']
        messages.append((REMOVE_STUDENT, name))
        return render_template_string("Doei {{name}}", name=name)

    def start_in_gevent():
        http_server = WSGIServer(('0.0.0.0', 80), app)
        http_server.serve_forever()

    return {
        'start': start_in_gevent
    }

from bottle import get, post, static_file, run, request, template
from messages import ADD_STUDENT, REMOVE_STUDENT

# If you're thinking 'what weird Python is this??', it's demo-code and I'm not allowed to use classes yet:)
import groups


def create_web(messages, handlers):
    @get('/')
    def index():
        return static_file('views/index.html', './')

    @post('/join')
    def join_group():
        name = request.forms.get('name')
        team = request.forms.get('team')
        choices = []
        for program in groups.PROGRAM_NAMES:
            value = request.forms.get(program)
            if value is not None:
                choices.append((program, int(value)))

        if groups.is_valid_groupchoice(choices):
            messages.append((ADD_STUDENT, (team, name, choices)))
            return template("Ok {{name}}", name=name)
        else:
            return template("Invalid choices", name=name, status=400)

    @post('/leave')
    def join_group():
        name = request.forms.get('name')
        messages.append((REMOVE_STUDENT, name))
        return template("Doei {{name}}", name=name)

    return {
        'start': lambda: run(host='localhost', port=8080)
    }

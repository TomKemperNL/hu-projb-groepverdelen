from bottle import get, post, static_file, run, request, template


# If you're thinking 'what weird Python is this??', it's demo-code and I'm not allowed to use classes yet:)
def create_web(messages, handlers):
    @get('/')
    def index():
        print('ooowkee1')
        messages.append(('INCREMENT',))
        print('ooowkee2')
        return static_file('index.html', './')

    @post('/join')
    def join_group():
        name = request.forms.get('name')
        return template("Hoi {{name}}", name=name)

    @post('/leave')
    def join_group():
        name = request.forms.get('name')
        return template("Doei {{name}}", name=name)

    return {
        'start': lambda: run(host='localhost', port=8080)
    }

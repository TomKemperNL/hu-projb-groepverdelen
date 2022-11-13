VALUES = [0, 25, 33, 50, 66, 75, 100]
PROGRAMS = {
    'sd': ('SD', 'Software Development', '#FF0000'),
    'ai': ('AI', 'Artificial Intelligence', '#0000FF'),
    'csc': ('CSC', 'Cybersecurity & Cloud', '#00FF00'),
    'ti': ('TI', 'Technische Informatica', '#FFFF00'),
    'bim': ('BIM', 'Business IT Management', '#00FFFF')}

PROGRAM_NAMES = [p[0] for p in PROGRAMS.values()]


def is_valid_groupchoice(choices):
    names = [choice[0] for choice in choices]
    values = [choice[1] for choice in choices]

    all_exist = True
    for name in names:
        all_exist = all_exist and name in PROGRAM_NAMES
    for value in values:
        all_exist = all_exist and value in VALUES

    distinct = len(set(names)) == len(names)
    sums_to_hundred = sum(values) in [100, 99]  # rounding stuff with the 33%ers
    return all_exist and distinct and sums_to_hundred


def initial_groups():
    groups = {}
    for i in range(6):
        groups[f'Team {i + 1}'] = []
    return groups


def remove_student_choice(model, to_remove):
    for name, members in model.items():
        for student in members:
            if student['name'] == to_remove:
                members.remove(student)


def add_student_choice(model, team, student, choices):
    if not is_valid_groupchoice(choices):
        raise Exception('Invalid choices')
    remove_student_choice(model, student)
    model[team].append({'name': student, 'choices': choices})


MIN_TEAM_SIZE = 4


def get_team_distribution(team):
    team = list(team)  # create a copy so we don't edit the input list
    if len(team) < MIN_TEAM_SIZE:
        # pad the list with 'empties', so it's clear there is still stuff missings
        for i in range(len(team), MIN_TEAM_SIZE):
            team.append({'name': 'NONE', 'choices': [('NONE', 100)]})

    values = {}
    total = 0
    for student in team:
        for program, value in student['choices']:
            if program not in values.keys():
                values[program] = value
            else:
                values[program] = values[program] + value
            total += value

    # normalise to 100%
    factor = 100 / total
    for key, value in values.items():
        values[key] = factor * value

    return values


def dummy_data(model):
    add_student_choice(model, 'Team 1', 'Arie de Groot', [('SD', 100)])
    add_student_choice(model, 'Team 1', 'Bruno Verkade', [('TI', 50), ('CSC', 50)])
    add_student_choice(model, 'Team 1', 'Chris Lemontagne', [('AI', 33), ('BIM', 33), ('CSC', 33)])
    add_student_choice(model, 'Team 1', 'Drummond Lee', [('SD', 100)])

    add_student_choice(model, 'Team 2', 'Effi De Geus', [('SD', 100)])
    add_student_choice(model, 'Team 2', 'Faruk Lambard', [('TI', 100)])

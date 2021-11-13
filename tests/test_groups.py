from groups import *


def test_choose_groups():
    for choices in [
        [('TI', 100)],
        [('SD', 50), ('BIM', 50)],
        [('AI', 33), ('CSC', 33), ('SD', 33)],
        [('AI', 25), ('SD', 25), ('TI', 25), ('CSC', 25)]
    ]:
        assert is_valid_groupchoice(choices)


def test_invalid_values():
    for choices in [
        [('TI', 90), ('AI', 10)],
        [('BESTAAT_NIET', 100)]
    ]:
        assert not is_valid_groupchoice(choices)


def test_initial_model():
    model = initial_groups()
    assert len(model) == 6


def test_add_student_choices():
    model = initial_groups()
    add_student_choice(model, 'Team 1', 'Bob', [('SD', 100)])
    assert model['Team 1'][0]['name'] == 'Bob'
    assert model['Team 1'][0]['choices'][0][0] == 'SD'
    assert model['Team 1'][0]['choices'][0][1] == 100


def test_get_team_distribution():
    model = initial_groups()
    add_student_choice(model, 'Team 1', 'Bob', [('SD', 100)])
    add_student_choice(model, 'Team 1', 'Fred', [('AI', 100)])
    add_student_choice(model, 'Team 1', 'Mia', [('TI', 100)])
    add_student_choice(model, 'Team 1', 'Faruk', [('BIM', 100)])
    add_student_choice(model, 'Team 1', 'Tim', [('CSC', 100)])

    distribution = get_team_distribution(model['Team 1'])
    for p in ['SD', 'AI', 'TI', 'BIM', 'CSC']:
        assert distribution[p] == 20


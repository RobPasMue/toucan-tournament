import pytest

from toucan.mvp.calculator.discipline import ToucanDiscipline
from toucan.mvp.calculator.errors import ToucanException
from toucan.mvp.calculator.players import ToucanPlayer


def test_toucan_player_basketball():
    # Let's take a reference entry like this one
    # --> BASKETBALL
    # --> Roberto Pastor;RobPasMue;4;Team A;G;10;2;7
    #
    # Which means the following
    name = "Roberto Pastor"
    nickname = "RobPasMue"
    discipline = ToucanDiscipline.BASKETBALL
    position = "G"
    marks = (10, 2, 7)

    # Instantiate player
    player = ToucanPlayer(name, nickname)

    # Check properties
    assert name == player.name
    assert nickname == player.nickname

    # Let's add the points corresponding to the reference match
    player.add_match_points(marks, discipline, position)

    # According to the Basketball rules... the previous marks are
    # scored points;rebounds;assists
    #
    # and their multipliers for position "G" are
    # 2;3;1
    #
    # Meaning...
    ref_points_g = 10 * 2 + 2 * 3 + 7 * 1
    ref_points_g_with_bonus = ref_points_g + 10
    assert len(player.points) == 1
    assert player.points[0] == ref_points_g
    assert player.total_points == ref_points_g

    # Let's also check that, if we assume that the player won the match,
    # the bonus points are added
    player.add_bonus_points()
    assert len(player.points) == 1
    assert player.points[0] == ref_points_g_with_bonus
    assert player.total_points == ref_points_g_with_bonus

    # Let's now assume that a new match is played with a new position
    # for example, "C", which has as multipliers
    # 2; 1; 3
    #
    ref_points_c = 10 * 2 + 2 * 1 + 7 * 3
    player.add_match_points(marks, discipline, "C")
    assert len(player.points) == 2
    assert player.points[0] == ref_points_g_with_bonus
    assert player.points[1] == ref_points_c
    assert player.total_points == ref_points_g_with_bonus + ref_points_c

    # Let's check the score contribution to the team for any of
    # both positions (both marks are the same)
    score = player.get_team_score_contribution(marks, discipline)
    assert score == marks[0]


def test_player_handball():
    # Let's take a reference entry like this one
    # --> HANDBALL
    # --> Roberto Pastor;RobPasMue;4;Team A;G;10;2
    #
    # Which means the following
    name = "Roberto Pastor"
    nickname = "RobPasMue"
    discipline = ToucanDiscipline.HANDBALL
    position = "G"
    marks = (10, 2)

    # Instantiate player
    player = ToucanPlayer(name, nickname)

    # Check properties
    assert name == player.name
    assert nickname == player.nickname

    # Let's add the points corresponding to the reference match
    player.add_match_points(marks, discipline, position)

    # According to the Handball rules... the previous marks are
    # goals made; goals received
    #
    # and their multipliers for position "G" are
    # 5;-2
    #
    # Also, for being a "G", the player gets an extra 50 points
    #
    # Meaning...
    ref_points_g = 50 + 10 * 5 + 2 * (-2)
    ref_points_g_with_bonus = ref_points_g + 10
    assert len(player.points) == 1
    assert player.points[0] == ref_points_g
    assert player.total_points == ref_points_g

    # Let's also check that, if we assume that the player won the match,
    # the bonus points are added
    player.add_bonus_points()
    assert len(player.points) == 1
    assert player.points[0] == ref_points_g_with_bonus
    assert player.total_points == ref_points_g_with_bonus

    # Let's check the score contribution to the team
    score = player.get_team_score_contribution(marks, discipline)
    assert score == marks[0] - marks[1]


def test_error_unexpected_marks_size():
    # Let's check what happens when, for some reason,
    # the marks passed do not match the expected marks size
    name = "Roberto Pastor"
    nickname = "RobPasMue"
    discipline = ToucanDiscipline.BASKETBALL
    position = "G"
    marks = (2, 4)  # ERROR: BASKETBALL excepts 3!!!

    # Instantiate player
    player = ToucanPlayer(name, nickname)

    exp_error = f"Evaluation parameters for '{discipline.name}' in position '{position}' do not match the marks given."  # noqa : E501
    with pytest.raises(ToucanException, match=exp_error):
        player.add_match_points(marks, discipline, position)


def test_error_unexpected_position():
    # Let's check what happens when, for some reason,
    # the position passed is not existing for this discipline
    name = "Roberto Pastor"
    nickname = "RobPasMue"
    discipline = ToucanDiscipline.HANDBALL
    position = "C"  # ERROR: HANDBALL does not have this position!!!
    marks = (2, 4)

    # Instantiate player
    player = ToucanPlayer(name, nickname)

    exp_error = f"Problems retrieving evaluation parameters for '{discipline.name}' in position '{position}'."  # noqa : E501
    with pytest.raises(ToucanException, match=exp_error):
        player.add_match_points(marks, discipline, position)

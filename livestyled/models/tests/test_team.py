from livestyled.models.team import Team


def test_team_difference():
    team_a = Team(id=1, name='Team A', short_name='TA', light_crest_url='light_url', external_id=1234)
    team_b = Team(id=1, name='Team B', short_name='TA', light_crest_url='light_url', external_id=None)

    difference = team_a.diff(team_b)
    assert difference == {
        'name': 'Team A',
        'external_id': 1234
    }
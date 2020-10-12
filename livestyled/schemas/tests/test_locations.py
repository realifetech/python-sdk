import os

from livestyled.schemas.location import LocationSchema


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'


def test_deserialize_reality():
    with open(os.path.join(FIXTURES_DIR, 'user_management/locations.json'), 'r') as fixture_file:
        location = fixture_file.read()
        deserialized_locations = LocationSchema().loads(location)
        assert deserialized_locations == {
            'coordinates': {
                'lat': '51.5074',
                'lon': '0.1278'
            },
            'external_id': '',
            'listed': True,
            'polygon': {
                'coordinates': [
                    [
                        [-0.1373291015625, 51.687030937462666],
                        [-0.27191162109374994, 51.7151177895987],
                        [-0.416107177734375, 51.72022261695929],
                        [-0.536956787109375, 51.62142713341988],
                        [-0.50811767578125, 51.50532341149335],
                        [-0.560302734375, 51.430895644580175],
                        [-0.413360595703125, 51.293699893323726],
                        [-0.020599365234375, 51.250741914997924],
                        [0.22659301757812497, 51.37778105986381],
                        [0.278778076171875, 51.55487448974971],
                        [0.17303466796874997, 51.67936786087718],
                        [0.026092529296875, 51.677664778834455],
                        [-0.1373291015625, 51.687030937462666]
                    ]
                ]
            },
            'sort_id': 1,
            'status': 'active',
            'id': 3,
            'name': 'London'
        }

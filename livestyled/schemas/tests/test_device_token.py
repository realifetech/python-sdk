import os

from livestyled.schemas.device_token import DeviceTokenSchema


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'


def test_deserialize_device_tokens():
    with open(os.path.join(FIXTURES_DIR, 'device_tokens_list.json'), 'r') as fixture_file:
        device_token = fixture_file.read()
        deserialized_device_tokens = DeviceTokenSchema().loads(device_token, many=True)
        assert sorted(deserialized_device_tokens, key=lambda k: k['id']) == [
            {
                'id': 43728,
                'provider': 'SNS',
                'provider_token': 'arn:aws:sns:eu-west-1:1:endpoint/APNS/TEST/dc433e55-a18c-4747-bf63-ad4795f35860',
                'payload': {
                    'subscriptions': {
                        'push_TEST_1': 'arn:aws:sns:eu-west-1:1:push_TEST:6a8f8424-cea5-4ab8-912e-9a48b84950aa'
                    },
                    'subscription': 'arn:aws:sns:eu-west-1:1:push_TEST:e9bd4b66-2fed-43e6-a2ee-16651d3e18a1'
                },
                'device_id': 1755585
            },
            {
                'id': 43729,
                'provider': 'ONESIGNAL',
                'provider_token': 'fa204d75-e88d-4184-a822-bee8101a274b',
                'payload': {
                    'subscription': None
                },
                'device_id': 1755586
            },
            {
                'id': 43730,
                'provider': 'GOOGLE',
                'provider_token': '180f3242-8934-4792-a5e6-207e4bda9dfe',
                'payload': [],
                'device_id': 1755586
            },
            {
                'id': 43731,
                'provider': 'SNS',
                'provider_token': 'arn:aws:sns:eu-west-1:1:endpoint/GCM/TEST/6aec8b91-6659-44ce-819e-2044ad82a64',
                'payload': {
                    'subscription': 'arn:aws:sns:eu-west-1:1:push_TEST:636b261e-6e3d-4c0c-a6e1-9c761cc1e529'
                },
                'device_id': 1755586
            },
            {
                'id': 43732,
                'provider': 'ONESIGNAL',
                'provider_token': '724777b9-2242-49b8-9783-80970dc7fa3a',
                'payload': {
                    'subscription': None
                },
                'device_id': 1755587
            },
            {
                'id': 43733,
                'provider': 'GOOGLE',
                'provider_token': '06aa8455-18cf-4332-8cdc-c937b5bfa811',
                'payload': [],
                'device_id': 1755587
            },
            {
                'id': 43734,
                'provider': 'SNS',
                'provider_token': 'arn:aws:sns:eu-west-1:1:endpoint/GCM/TEST/f70c412b-99a8-4ce3-8d4c-94584ad29c7b',
                'payload': {
                    'subscription': None
                },
                'device_id': 1755587
            },
            {
                'id': 43735,
                'provider': 'ONESIGNAL',
                'provider_token': '0b9ea463-bae4-460a-b2c6-6cde32928541',
                'payload': {
                    'subscription': None
                },
                'device_id': 1755589
            },
            {
                'id': 43736,
                'provider': 'GOOGLE',
                'provider_token': '172dbabd-59fd-42be-b962-2754f1c6576f',
                'payload': [],
                'device_id': 1755589
            },
            {
                'id': 43737,
                'provider': 'SNS',
                'provider_token': 'arn:aws:sns:eu-west-1:1:endpoint/GCM/TEST/40e43dd5-d9a2-46e2-b5db-0b1509ff07a9',
                'payload': {
                    'subscription': None
                },
                'device_id': 1755589
            },
            {
                'id': 43738,
                'provider': 'ONESIGNAL',
                'provider_token': '64e8424b-0674-4098-8659-adbadf3a59a4',
                'payload': {
                    'subscription': None
                },
                'device_id': 1755591
            },
            {
                'id': 43739,
                'provider': 'GOOGLE',
                'provider_token': '9760d22f-ddfa-46e9-9fdc-e2a5f43bedd5',
                'payload': [],
                'device_id': 1755591
            },
            {
                'id': 43740,
                'provider': 'SNS',
                'provider_token': 'arn:aws:sns:eu-west-1:1:endpoint/GCM/TEST/9e91f333-da33-4d0c-8bfa-00aa963cc006',
                'payload': {
                    'subscription': 'arn:aws:sns:eu-west-1:435820695836:TEST:9e91f333-da33-4d0c-8bfa-00aa963cc006'
                },
                'device_id': 1755591
            },
            {
                'id': 43741,
                'provider': 'ONESIGNAL',
                'provider_token': '012cf99c-b087-4e54-8b9f-4de64531f385',
                'payload': {
                    'subscription': None
                },
                'device_id': 1755594
            },
            {
                'id': 43742,
                'provider': 'GOOGLE',
                'provider_token': 'c884894b-b21e-452f-9259-79ea9a8319a8',
                'payload': [],
                'device_id': 1755594
            }
        ]

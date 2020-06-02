from datetime import datetime, timedelta, timezone
import os

from livestyled.schemas.user import UserSchema


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')
TEST_API_DOMAIN = 'test.livestyled.com'
CONTENT_TYPE = 'application/ld+json'


def test_deserialize_user():
    with open(os.path.join(FIXTURES_DIR, 'example_user.json'), 'r') as fixture_file:
        user = fixture_file.read()
        deserialized_user = UserSchema().loads(user)
        assert deserialized_user == {
            'auth_type': 'AXS',
            'email': 'reuben.gow+axs2@livestyled.com',
            'id': 278405,
            'user_info': {
                'id': 277763,
                'first_name': 'Reuben',
                'last_name': 'Gow',
                'dob': datetime(1980, 1, 1, 0, 0, tzinfo=timezone(timedelta(0), '+0000')),
                'phone': '+4712345678',
                'gender': None
            },
            'cohorts': [],
            'user_emails': [
                {
                    'valid': False,
                    'email': 'reuben.gow+axs2@livestyled.com'
                }
            ],
            'magic_fields': [],
            'user_consent': {
                'marketing_consent': False,
                'analysis_consent': True,
                'id': 658056
            },
            'devices': [
                {
                    'app_version': '10.7',
                    'bluetooth_on': True,
                    'consent': {
                        'calendar': True,
                        'camera': True,
                        'created_at': datetime(2020, 2, 17, 14, 37, 12, tzinfo=timezone(timedelta(0), '+0000')),
                        'id': 4514,
                        'location_capture': True,
                        'photo_sharing': True,
                        'push_notification': True,
                        'updated_at': datetime(2020, 2, 18, 12, 53, 42, tzinfo=timezone(timedelta(0), '+0000'))},
                    'created_at': datetime(2020, 2, 17, 14, 37, 9, tzinfo=timezone(timedelta(0), '+0000')),
                    'id': 1754699,
                    'manufacturer': 'samsung',
                    'model': 'SM-G930F',
                    'os_version': '8.0.0',
                    'push_consents': [
                        {
                            'consent': True,
                            'id': 17441,
                            'push_consent_id': 60
                        }
                    ],
                    'status': 'ACTIVE',
                    'token': '243aadce-5bf0-4215-935a-2aab22f2a01c:com.livestyled.lagalaxy.beta',
                    'type': 'ANDROID',
                    'updated_at': datetime(2020, 2, 19, 18, 28, 27, tzinfo=timezone(timedelta(0), '+0000')),
                    'wifi_connected': True
                }
            ],
        }

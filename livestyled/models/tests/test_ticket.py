from livestyled.models.ticket import Ticket


def test_ticket_difference():
    current = Ticket(
        id=1,
        status='ACTIVE',
        external_ticket_id=12823463737,
        seat='2B',
        session_date='2022-10-10',
        title='English Cup',
        external_event_id=282848348,
        price_code='GBP',
        price_type='Full price',
        barcode=83736474849494,
        sector_name='C',
        section='20',
        row='10',
        price=20,
        venue_name='Stamford Bridge',
        can_share=False,
        ticket_integration=None,
        external_movement_id=None,
        qr_code_url='http://test',
        legacy_external_event_id=282848348,
        venue_room='1A',
        client_name='John Smith',
        premium=False,
        client_email='test@test.com',
        share_link=None,
        external_customer_ref=None,
        entrance='12',
        user_id=12,
        created_at=None,
        updated_at=None,
        additional_fields=[{
            'name': 'Ticket Type',
            'value': 'FULL',
            'sort': 1,
            'dataType': 'string'
        }, {
            'name': 'Ticket Type 2',
            'value': 'test',
            'sort': 2,
            'dataType': 'string'
        }])

    new = Ticket(
        id=1,
        status='ACTIVE',
        external_ticket_id=12823463737,
        seat='2B',
        session_date='2022-10-10',
        title='English Cup',
        external_event_id=282848348,
        price_code='GBP',
        price_type='Full price',
        barcode=83736474849494,
        sector_name='C',
        section='20',
        row='10',
        price=20,
        venue_name='Stamford Bridge',
        can_share=False,
        ticket_integration=None,
        external_movement_id=None,
        qr_code_url='http://test',
        legacy_external_event_id=282848348,
        venue_room='1A',
        client_name='John Smith',
        premium=False,
        client_email='test@test.com',
        share_link=None,
        external_customer_ref=None,
        entrance='12',
        user_id=12,
        created_at=None,
        updated_at=None,
        additional_fields=[{
            'name': 'Ticket Type',
            'value': 'FULL 1',
            'sort': 1,
            'dataType': 'string'
        }])

    difference = new.diff(current)

    assert difference == {
        'additional_fields': [
            {
                'name': 'Ticket Type',
                'value': 'FULL 1',
                'sort': 1,
                'dataType': 'string'
            }, {
                'name': 'Ticket Type 2',
                'value': 'test',
                'sort': 2,
                'dataType': 'string'
            }
        ]
    }


def test_ticket_difference_with_empty_ticket_additional_fields():
    current = Ticket(
        id=1,
        status='ACTIVE',
        external_ticket_id=12823463737,
        seat='2B',
        session_date='2022-10-10',
        title='English Cup',
        external_event_id=282848348,
        price_code='GBP',
        price_type='Full price',
        barcode=83736474849494,
        sector_name='C',
        section='20',
        row='10',
        price=20,
        venue_name='Stamford Bridge',
        can_share=False,
        ticket_integration=None,
        external_movement_id=None,
        qr_code_url='http://test',
        legacy_external_event_id=282848348,
        venue_room='1A',
        client_name='John Smith',
        premium=False,
        client_email='test@test.com',
        share_link=None,
        external_customer_ref=None,
        entrance='12',
        user_id=12,
        created_at=None,
        updated_at=None,
        additional_fields=None
    )

    new = Ticket(
        id=1,
        status='ACTIVE',
        external_ticket_id=12823463737,
        seat='2B',
        session_date='2022-10-10',
        title='English Cup',
        external_event_id=282848348,
        price_code='GBP',
        price_type='Full price',
        barcode=83736474849494,
        sector_name='C',
        section='20',
        row='10',
        price=20,
        venue_name='Stamford Bridge',
        can_share=False,
        ticket_integration=None,
        external_movement_id=None,
        qr_code_url='http://test',
        legacy_external_event_id=282848348,
        venue_room='1A',
        client_name='John Smith',
        premium=False,
        client_email='test@test.com',
        share_link=None,
        external_customer_ref=None,
        entrance='12',
        user_id=12,
        created_at=None,
        updated_at=None,
        additional_fields=[{
            'name': 'Ticket Type',
            'value': 'FULL 2',
            'sort': 1,
            'dataType': 'string'
        }])

    difference = new.diff(current)

    assert difference == {
        'additional_fields': [
            {
                'name': 'Ticket Type',
                'value': 'FULL 2',
                'sort': 1,
                'dataType': 'string'
            }
        ]
    }

import logging
from typing import Dict, Generator, List, Type

from marshmallow import Schema, ValidationError
from requests.exceptions import HTTPError

from livestyled.client import LiveStyledAPIClient
from livestyled.models import (
    Booking,
    Cohort,
    Competition,
    Device,
    DevicePreference,
    DeviceToken,
    Event,
    Fixture,
    LeagueTable,
    LeagueTableGroup,
    MagicField,
    News,
    PushBroadcast,
    PushConsent,
    Season,
    SportVenue,
    Team,
    Ticket,
    User,
    UserInfo,
    UserSSO
)
from livestyled.schemas import (
    BookingSchema,
    CohortSchema,
    CompetitionSchema,
    DevicePreferenceSchema,
    DeviceSchema,
    DeviceTokenSchema,
    EventSchema,
    FixtureSchema,
    LeagueTableGroupSchema,
    LeagueTableSchema,
    MagicFieldSchema,
    NewsSchema,
    PushBroadcastSchema,
    PushConsentSchema,
    SeasonSchema,
    SportVenueSchema,
    TeamSchema,
    TicketSchema,
    UserCreateSchema,
    UserInfoSchema,
    UserSchema,
    UserSSOSchema
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

ASCENDING = 'asc'
DESCENDING = 'desc'


class LiveStyledResourceClient(LiveStyledAPIClient):
    def __init__(
            self,
            api_domain: str,
            api_key: str
    ):
        super(LiveStyledResourceClient, self).__init__(api_domain, api_key)

    def _get_resource_list(
            self,
            resource_schema: Type[Schema],
            external_id: str or None = None,
            filters: Dict or None = None,
            order_by: Dict or None = None,
    ):
        filter_params = {}
        if filters:
            filter_params = filters
        if external_id:
            filter_params['externalId'] = external_id

        if order_by:
            field = list(order_by.keys())[0]
            direction = list(order_by.values())[0]
            filter_params['order[{}]'.format(field)] = direction
            # TODO validate order parameters
        else:
            try:
                default_ordering = resource_schema.Meta.default_ordering
            except AttributeError:
                pass
            else:
                if default_ordering.startswith('-'):
                    filter_params['order[{}]'.format(default_ordering.lstrip('-'))] = 'desc'
                else:
                    filter_params['order[{}]'.format(default_ordering)] = 'asc'

        resources = self._get_resources(
            resource_schema,
            params=filter_params
        )
        for resource in resources:
            yield resource_schema.Meta.model(**resource)

    def _get_resource_by_id(
            self,
            schema: Type[Schema],
            id: int
    ):
        return schema.Meta.model(**self._get_resource(id, schema))

    def _create_resource(
            self,
            schema: Type[Schema],
            model_instance
    ):
        if getattr(model_instance, 'id', False) and model_instance.id is not None:
            raise ValueError('Cannot create a {} with an ID'.format(schema.Meta.model.__name__))
        payload = schema().dump(model_instance)
        for key, value in list(payload.items()):
            if value is None:
                payload.pop(key)
        logger.info(payload)
        new_instance = self._api_post(
            '{}'.format(schema.Meta.url),
            payload
        )
        try:
            return schema.Meta.model(**schema().load(new_instance))
        except ValidationError as err:
            logger.error(new_instance)
            logger.error(err.messages)
            raise

    def _update_resource(
            self,
            schema: Type[Schema],
            resource_id: int,
            attributes: Dict,
    ):
        attributes_to_update = list(attributes.keys())
        update_payload = schema(only=attributes_to_update).dump(attributes)
        updated_resource = self._api_patch(
            '{}/{}'.format(schema.Meta.url, resource_id),
            update_payload
        )
        return schema.Meta.model(**schema().load(updated_resource))

    def _delete_resource(
            self,
            schema: Type[Schema],
            resource,
    ):
        return self._api_delete(schema.Meta.url, resource.id)

    def get_teams(
            self,
            external_id: str or None = None,
    ) -> Generator[Team, None, None]:
        return self._get_resource_list(TeamSchema, external_id)

    # ---- TEAMS

    def get_team(
            self,
            id: int
    ) -> Team:
        return self._get_resource_by_id(TeamSchema, id)

    def create_team(
            self,
            team: Team
    ) -> Team:
        return self._create_resource(TeamSchema, team)

    def delete_team(
            self,
            team: Team
    ):
        self._delete_resource(TeamSchema, team)

    def update_team(
            self,
            team: Team,
            attributes: Dict
    ) -> Team:
        return self._update_resource(TeamSchema, team.id, attributes)

    # ---- FIXTURES

    def get_fixtures(
            self,
            external_id: str or None = None,
    ) -> Generator[Fixture, None, None]:
        return self._get_resource_list(FixtureSchema, external_id)

    def get_fixture(
            self,
            id: int
    ) -> Fixture:
        return self._get_resource_by_id(FixtureSchema, id)

    def create_fixture(
            self,
            fixture: Fixture
    ) -> Fixture:
        return self._create_resource(FixtureSchema, fixture)

    def update_fixture(
            self,
            fixture: Fixture,
            attributes: Dict
    ) -> Fixture:
        return self._update_resource(FixtureSchema, fixture.id, attributes)

    # ---- COMPETITIONS

    def get_competitions(
            self,
            external_id: str or None = None,
    ) -> Generator[Competition, None, None]:
        return self._get_resource_list(CompetitionSchema, external_id)

    def get_competition(
            self,
            id: int
    ) -> Competition:
        return self._get_resource_by_id(CompetitionSchema, id)

    def create_competition(
            self,
            competition: Competition
    ) -> Competition:
        return self._create_resource(CompetitionSchema, competition)

    def update_competition(
            self,
            competition: Competition,
            attributes: Dict
    ) -> Competition:
        return self._update_resource(CompetitionSchema, competition.id, attributes)

    # ---- SEASONS

    def get_seasons(
            self,
            external_id: str or None = None,
    ) -> Generator[Season, None, None]:
        return self._get_resource_list(SeasonSchema, external_id)

    def get_season(
            self,
            id: int
    ) -> Season:
        return self._get_resource_by_id(SeasonSchema, id)

    def create_season(
            self,
            season: Season
    ) -> Season:
        return self._create_resource(SeasonSchema, season)

    def update_season(
            self,
            season: Season,
            attributes: Dict
    ) -> Season:
        return self._update_resource(SeasonSchema, season.id, attributes)

    # ---- SPORTS VENUES

    def get_sport_venues(
            self,
            external_id: str or None = None,
    ) -> Generator[SportVenue, None, None]:
        return self._get_resource_list(SportVenueSchema, external_id)

    def get_sport_venue(
            self,
            id: int
    ) -> SportVenue:
        return self._get_resource_by_id(SportVenueSchema, id)

    def create_sport_venue(
            self,
            sport_venue: SportVenue
    ) -> SportVenue:
        return self._create_resource(SportVenueSchema, sport_venue)

    def update_sport_venue(
            self,
            sport_venue: SportVenue,
            attributes: Dict
    ) -> SportVenue:
        return self._update_resource(SportVenueSchema, sport_venue.id, attributes)

    # ---- LEAGUE TABLES

    def get_league_tables(
            self,
            external_id: str or None = None,
    ) -> Generator[LeagueTable, None, None]:
        return self._get_resource_list(LeagueTableSchema, external_id)

    def get_league_table(
            self,
            id: int
    ) -> LeagueTable:
        return self._get_resource_by_id(LeagueTableSchema, id)

    def create_league_table(
            self,
            league_table: LeagueTable
    ) -> LeagueTable:
        return self._create_resource(LeagueTableSchema, league_table)

    def update_league_table(
            self,
            league_table: LeagueTable,
            attributes: Dict
    ) -> LeagueTable:
        return self._update_resource(LeagueTableSchema, league_table.id, attributes)

    # ---- LEAGUE TABLE GROUPS

    def get_league_table_groups(
            self,
    ) -> Generator[LeagueTableGroup, None, None]:
        return self._get_resource_list(LeagueTableGroupSchema)

    def get_league_table_group(
            self,
            id: int
    ) -> LeagueTableGroup:
        return self._get_resource_by_id(LeagueTableGroupSchema, id)

    def create_league_table_group(
            self,
            league_table_group: LeagueTableGroup
    ) -> LeagueTableGroup:
        return self._create_resource(LeagueTableGroupSchema, league_table_group)

    def update_league_table_group(
            self,
            league_table: LeagueTableGroup,
            attributes: Dict
    ) -> LeagueTableGroup:
        return self._update_resource(LeagueTableGroupSchema, league_table.id, attributes)

    # ---- NEWS

    def get_news_articles(
            self,
            external_id: str or None = None,
    ) -> Generator[News, None, None]:
        return self._get_resource_list(NewsSchema, external_id)

    def get_news_article(
            self,
            id: int
    ) -> News:
        return self._get_resource_by_id(NewsSchema, id)

    def create_news_article(
            self,
            news: News
    ) -> News:
        return self._create_resource(NewsSchema, news)

    def update_news(
            self,
            news: News,
            attributes: Dict
    ) -> NewsSchema:
        return self._update_resource(NewsSchema, news.id, attributes)

    def delete_news(
            self,
            news: News,
    ) -> NewsSchema:
        return self._delete_resource(NewsSchema, news)

    # ---- USER

    def get_users(
            self,
            email: str or None = None,
    ) -> Generator[User, None, None]:
        if email:
            return self._get_resource_list(UserSchema, filters={'email': email})
        else:
            return self._get_resource_list(UserSchema)

    def get_user(
            self,
            id: int
    ) -> User:
        return self._get_resource_by_id(UserSchema, id)

    def create_user(
            self,
            user: User
    ) -> User:
        if user.id is not None:
            raise ValueError('Cannot create a User with an ID')
        payload = UserCreateSchema().dump(user)
        for key, value in list(payload.items()):
            if value is None:
                payload.pop(key)

        user_create_response = self._api_post(
            UserCreateSchema.Meta.create_url,
            payload
        )
        return User(**UserSchema().load(user_create_response))

    def update_user(
            self,
            user: User,
            attributes: Dict
    ) -> User:
        return self._update_resource(UserSchema, user.id, attributes)

    def update_user_info(
            self,
            user_info: UserInfo,
            attributes: Dict
    ) -> UserInfo:
        return self._update_resource(UserInfoSchema, user_info.id, attributes)

    def authorise_user(
            self,
            user: User,
            password: str
    ) -> Dict:
        if user.id is None:
            raise ValueError('Need a user ID to authorise a user')
        if not password:
            raise ValueError('Need a password to authorise a user')
        user_auth_response = self._api_post(
            UserSchema.Meta.authorise_url.format(user.id),
            {
                'password': password
            }
        )
        return user_auth_response

    # ---- USER SSO

    def get_user_ssos(
            self,
            sub: str or None = None,
    ) -> Generator[UserSSO, None, None]:
        if sub:
            return self._get_resource_list(UserSSOSchema, filters={'sub': sub})
        else:
            return self._get_resource_list(UserSSOSchema)

    def get_user_sso(
            self,
            id: int
    ) -> UserSSO:
        return self._get_resource_by_id(UserSSOSchema, id)

    def create_user_sso(
            self,
            user_sso: UserSSO
    ) -> UserSSO:
        return self._create_resource(UserSSOSchema, user_sso)

    def update_user_sso(
            self,
            user_sso: UserSSO,
            attributes: Dict
    ) -> UserSSO:
        return self._update_resource(UserSSOSchema, user_sso.id, attributes)

    def get_sso_for_user(
            self,
            user_id,
    ) -> UserSSO or None:
        try:
            user_sso_data = self._api_get('v4/users/{}/user_s_s_o'.format(user_id))
        except HTTPError as http_error:
            if http_error.response.status_code == 404:
                return None
            else:
                raise
        user_sso = UserSSO(**UserSSOSchema().load(user_sso_data))
        return user_sso

    # ---- PUSH BROADCASTS

    def get_push_broadcasts(
            self,
            order_by=None
    ) -> Generator[PushBroadcast, None, None]:
        return self._get_resource_list(PushBroadcastSchema, order_by=order_by)

    def get_push_broadcast(
            self,
            id: int
    ) -> PushBroadcast:
        return self._get_resource_by_id(PushBroadcastSchema, id)

    def create_push_broadcast(
            self,
            push_broadcast: PushBroadcast
    ) -> PushBroadcast:
        if push_broadcast.id is not None:
            raise ValueError('Cannot create a PushBroadcast with an ID')
        payload = PushBroadcastSchema().dump(push_broadcast)
        for key, value in list(payload.items()):
            if value is None:
                payload.pop(key)
        new_push_broadcast = self._api_post(
            PushBroadcastSchema.Meta.publish_url,
            payload
        )
        return PushBroadcast(**PushBroadcastSchema().load(new_push_broadcast))

    def update_push_broadcast(
            self,
            push_broadcast: PushBroadcast,
            attributes: Dict
    ) -> PushBroadcast:
        return self._update_resource(PushBroadcastSchema, push_broadcast.id, attributes)

    # ---- PUSH CONSENTS

    def get_push_consents(
            self,
    ) -> Generator[PushConsent, None, None]:
        return self._get_resource_list(PushConsentSchema)

    def get_push_consent(
            self,
            id: int
    ) -> PushConsent:
        return self._get_resource_by_id(PushConsentSchema, id)

    # ---- TICKETS

    def get_tickets(
            self,
            external_ticket_id: str or None = None,
    ) -> Generator[Ticket, None, None]:
        if external_ticket_id:
            return self._get_resource_list(TicketSchema, filters={'externalTicketId': external_ticket_id})
        else:
            return self._get_resource_list(TicketSchema)

    def get_ticket(
            self,
            id: int
    ) -> Ticket:
        return self._get_resource_by_id(TicketSchema, id)

    def create_ticket(
            self,
            ticket: Ticket
    ) -> Ticket:
        return self._create_resource(TicketSchema, ticket)

    def update_ticket(
            self,
            ticket: Ticket,
            attributes: Dict
    ) -> Ticket:
        return self._update_resource(TicketSchema, ticket.id, attributes)

    # ---- COHORTS

    def get_cohort(
            self,
            id: int
    ) -> Cohort:
        return self._get_resource_by_id(CohortSchema, id)

    def get_cohorts(
            self,
            external_id: str or None = None,
    ) -> Generator[Cohort, None, None]:
        if external_id:
            return self._get_resource_list(CohortSchema, filters={'externalId': external_id})
        else:
            return self._get_resource_list(CohortSchema)

    def create_cohort(
            self,
            cohort: Cohort
    ) -> Cohort:
        return self._create_resource(CohortSchema, cohort)

    def add_user_to_cohorts(
            self,
            user_id: int,
            cohorts: List[Cohort]
    ) -> bool:
        if not cohorts:
            return True
        payload = {
            'cohortExternalIds': [cohort.external_id for cohort in cohorts]
        }
        self._api_post(
            CohortSchema.Meta.bulk_user_attach_url.format(user_id),
            payload,
            content_type_override='application/json'
        )
        return True

    def remove_user_from_cohorts(
            self,
            user_id: int,
            cohorts: List[Cohort]
    ) -> bool:
        if not cohorts:
            return True
        payload = {
            'cohortExternalIds': [cohort.external_id for cohort in cohorts]
        }
        self._api_post(
            CohortSchema.Meta.bulk_user_detach_url.format(user_id),
            payload,
            content_type_override='application/json'
        )
        return True

    # ---- MAGIC FIELDS

    def get_magic_field(
            self,
            magic_field_id: int,
    ) -> MagicField:
        return self._get_resource_by_id(MagicFieldSchema, magic_field_id)

    def create_magic_field(
            self,
            magic_field: MagicField
    ) -> MagicField:
        return self._create_resource(MagicFieldSchema, magic_field)

    def update_magic_field(
            self,
            magic_field: MagicField,
            attributes: Dict
    ) -> MagicField:
        return self._update_resource(MagicFieldSchema, magic_field.id, attributes)

    # ---- EVENTS

    def get_events(
            self,
            title: str or None = None,
            status: str or None = None,
            start_at_after: str or None = None
    ) -> Generator[Event, None, None]:
        filters = {}
        if title:
            filters['title'] = title
        if status:
            filters['status'] = status
        if start_at_after:
            filters['event_dates.start_at[gt]'] = start_at_after
        if filters:
            return self._get_resource_list(EventSchema, filters=filters)
        else:
            return self._get_resource_list(EventSchema)

    # ---- BOOKINGS

    def get_bookings(
            self,
            device: str or None = None,
            event: str or None = None,
            action: str or None = None,
            type: str or None = None,
    ) -> Generator[Booking, None, None]:
        filters = {}
        if device:
            filters['device'] = device
        if event:
            filters['event'] = event
        if action:
            filters['action'] = action
        if type:
            filters['type'] = type
        if filters:
            return self._get_resource_list(BookingSchema, filters=filters)
        else:
            return self._get_resource_list(BookingSchema)

    def create_booking(
            self,
            booking: Booking
    ) -> Booking:
        return self._create_resource(BookingSchema, booking)

    # ---- DEVICE PREFERENCES

    def get_device_preferences(
            self,
            device: str or None = None,
            event: str or None = None,
    ) -> Generator[DevicePreference, None, None]:
        if device and event:
            return self._get_resource_list(DevicePreferenceSchema,
                                           filters={'device': device, 'event': event})
        else:
            return self._get_resource_list(DevicePreferenceSchema)

    def create_device_preference(
            self,
            device_preference: DevicePreference
    ) -> DevicePreference:
        return self._create_resource(DevicePreferenceSchema, device_preference)

    # ---- DEVICES

    def get_device(
            self,
            id,
    ) -> Device:
        return self._get_resource_by_id(DeviceSchema, id)

    def get_devices(
            self
    ) -> Generator[Device, None, None]:
        return self._get_resource_list(DeviceSchema)

    # ---- DEVICE TOKENS

    def get_tokens_for_device(
            self,
            device: Device,
            provider: str or None = None
    ) -> Generator[DeviceToken, None, None]:
        filters = {}
        if provider:
            filters['provider'] = provider
        try:
            device_token_data = self._api_get(
                'v4/devices/{}/device_tokens'.format(device.id),
                params=filters
            )
        except HTTPError as http_error:
            if http_error.response.status_code == 404:
                yield
            else:
                raise
        for device_token in device_token_data['hydra:member']:
            token = DeviceTokenSchema().load(device_token)
            yield DeviceTokenSchema.Meta.model(**token)

    def create_device_token(
            self,
            device_token: DeviceToken
    ) -> DeviceToken:
        return self._create_resource(DeviceTokenSchema, device_token)

    def update_device_token(
            self,
            device_token: DeviceToken,
            attributes: Dict
    ) -> DeviceToken:
        return self._update_resource(DeviceTokenSchema, device_token.id, attributes)

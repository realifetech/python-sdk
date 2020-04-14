from datetime import datetime


class Venue:
    def __init__(
            self,
            id: int,
            name: str or None,
            label: str or None,
            status: str or None,
            is_default: bool,
            description: str or None = None,
            image_url: str or None = None,
            map_image_url: str or None = None,
            geo_latitude: str or None = None,
            geo_longitude: str or None = None,
            geo_latitude_north_west: str or None = None,
            geo_longitude_north_west: str or None = None,
            geo_latitude_south_east: str or None = None,
            geo_longitude_south_west: str or None = None,
            city: str or None = None,
            external_id: str or None = None,
            created_at: datetime or None = None,
            updated_at: datetime or None = None,
            venue_icon_url: str or None = None,
    ):
        self._id = id
        self.name = name
        self.label = label
        self.status = status
        self.is_default = is_default
        self.description = description
        self.image_url = image_url
        self.map_image_url = map_image_url
        self.geo_latitude = geo_latitude
        self.geo_longitude = geo_longitude
        self.geo_latitude_north_west = geo_latitude_north_west
        self.geo_longitude_north_west = geo_longitude_north_west
        self.geo_latitude_south_east = geo_latitude_south_east
        self.geo_longitude_south_west = geo_longitude_south_west
        self.city = city
        self.external_id = external_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.venue_icon_url = venue_icon_url

    @property
    def id(self):
        return self._id

    @classmethod
    def create_new(
            cls,
            name: str,
            label: str or None,
            status: str or None,
            is_default: bool,
            description: str or None = None,
            image_url: str or None = None,
            map_image_url: str or None = None,
            geo_latitude: str or None = None,
            geo_longitude: str or None = None,
            geo_latitude_north_west: str or None = None,
            geo_longitude_north_west: str or None = None,
            geo_latitude_south_east: str or None = None,
            geo_longitude_south_west: str or None = None,
            city: str or None = None,
            external_id: str or None = None,
            created_at: datetime or None = None,
            updated_at: datetime or None = None,
            venue_icon_url: str or None = None,
    ):
        cls._id = None
        cls.name = name
        cls.label = label
        cls.status = status
        cls.is_default = is_default
        cls.description = description
        cls.image_url = image_url
        cls.map_image_url = map_image_url
        cls.geo_latitude = geo_latitude
        cls.geo_longitude = geo_longitude
        cls.geo_latitude_north_west = geo_latitude_north_west
        cls.geo_longitude_north_west = geo_longitude_north_west
        cls.geo_latitude_south_east = geo_latitude_south_east
        cls.geo_longitude_south_west = geo_longitude_south_west
        cls.city = city
        cls.external_id = external_id
        cls.created_at = created_at
        cls.updated_at = updated_at
        cls.venue_icon_url = venue_icon_url
        return cls

    @classmethod
    def placeholder(
            cls,
            id
    ):
        return cls(
            id=id,
            name=None,
            label=None,
            status=None,
            is_default=False
        )


class LocationCoordinates:
    def __init__(
            self,
            lat,
            lon
    ):
        self._lat = lat
        self._lon = lon

    @property
    def lat(self):
        if self._lat is not None:
            return float(self._lat)
        else:
            return None

    @property
    def lon(self):
        if self._lon is not None:
            return float(self._lon)
        else:
            return None

    def __eq__(self, other):
        if self.lat == other.lat and self.lon == other.lon:
            return True
        return False


class LocationPolygon:
    def __init__(
            self,
            coordinates
    ):
        self.coordinates = []
        if coordinates:
            for point in coordinates[0]:
                self.coordinates.append(LocationCoordinates(point[1], point[0]))


class Location:
    def __init__(
            self,
            id,
            name,
            coordinates,
            polygon,
            status,
            sort_id,
            listed,
            external_id
    ):
        self.id = id
        self.name = name
        self.status = status
        self.sort_id = sort_id
        self.listed = listed
        self.external_id = external_id
        if coordinates:
            self.coordinates = LocationCoordinates(coordinates['lat'], coordinates['lon'])
        else:
            self.coordinates = None
        if polygon:
            self.polygon = LocationPolygon(polygon['coordinates'])
        else:
            self.polygon = None

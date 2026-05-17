def _filter_spatially(self):
    included_stops = set()
    for stop in self.stops:
        if self._is_within_buffer(stop):
            included_stops.add(stop)
    while True:
        new_included_stops = set()
        for trip in self.trips:
            for i in range(len(trip.stops) - 1):
                if trip.stops[i] in included_stops and trip.stops[i + 1] not in included_stops:
                    new_included_stops.add(trip.stops[i + 1])
                elif trip.stops[i + 1] in included_stops and trip.stops[i] not in included_stops:
                    new_included_stops.add(trip.stops[i])
        if not new_included_stops:
            break
        included_stops.update(new_included_stops)
    self.stops = [stop for stop in self.stops if stop in included_stops]
    self.trips = [trip for trip in self.trips if all((stop in included_stops for stop in trip.stops))]
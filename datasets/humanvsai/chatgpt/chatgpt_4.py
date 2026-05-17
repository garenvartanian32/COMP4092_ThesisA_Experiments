def filter_feed(self, stops, pt_trips):
    included_stops = set()
    stop_pairs = set()
    for stop in stops:
        if self.distance(stop['lat'], stop['lon'], self.buffer_lat, self.buffer_lon) <= self.buffer_distance_km:
            included_stops.add(stop['id'])
    
    while True:
        new_stop_pairs = set()
        for trip in pt_trips:
            if trip['start_stop_id'] in included_stops and trip['end_stop_id'] in included_stops:
                start_index = trip['stop_ids'].index(trip['start_stop_id'])
                end_index = trip['stop_ids'].index(trip['end_stop_id'])
                new_pairs = [(trip['stop_ids'][i], trip['stop_ids'][i+1]) for i in range(start_index, end_index)]
                new_stop_pairs.update(new_pairs)
        if not new_stop_pairs - stop_pairs:  
            break
        stop_pairs.update(new_stop_pairs)
        included_stops.update(chain.from_iterable(stop_pairs))
    
    return stops.filter(stop['id'] in included_stops)
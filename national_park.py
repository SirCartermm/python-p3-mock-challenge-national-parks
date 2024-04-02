all_parks = []

def init(self, name): if not isinstance(name, str) or len(name) < 3: raise Exception("Name must be a string with at least 3 characters") self.name = name NationalPark.all_parks.append(self)

@property def name(self): return self._name

@name.setter def name(self, value): self._name = value

def trips(self): trips = [] for park in Trip.all_trips: if park.national_park == self: trips.append(park) return trips

def visitors(self): visitors = [] for trip in self.trips(): if trip.visitor not in visitors: visitors.append(trip.visitor) return visitors

def total_visits(self): return len(self.trips())

def best_visitor(self): max_visits = 0 best_visitor = None for visitor in self.visitors(): visits = visitor.total_visits_at_park(self)
if visits > max_visits: max_visits = visits best_visitor = visitor return best_visitor

@classmethod def most_visited(cls): most_visits = 0 most_visited = None for park in cls.all_parks: visits = park.total_visits() if visits > most_visits: most_visits = visits most_visited = park return most_visited
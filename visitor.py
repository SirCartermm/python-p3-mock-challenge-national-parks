def init(self,name)
:if not isinstance(name,str) or
 len(name) < 1 or len(name) > 15: raise Exception("Name must be a string between 1 and 15 characters") self.name = name

@property def name(self)
: return self._name

@name.setter def name(self, value)
: self._name = value

def trips(self): trips = [] for trip in Trip.all_trips: if trip.visitor == self: trips.append(trip) return trips

def national_parks(self): parks = [] for trip in self.trips(): if trip.national_park not in parks: parks.append(trip.national_park) return parks

def total_visits_at_park(self, park): count = 0 for trip in self.trips(): if trip.national_park == park: count += 1 return count
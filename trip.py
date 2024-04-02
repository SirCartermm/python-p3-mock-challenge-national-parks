all_trips = []

def init(self, visitor, national_park, start_date, end_date): if not isinstance(visitor, Visitor) or not isinstance(national_park, NationalPark): raise Exception
("Visitor and national park must be instances of their classes") if not isinstance(start_date, str) or len(start_date) < 7: raise Exception("Start date must be a string of at least 7 characters") if not isinstance(end_date, str) or len(end_date) < 7: raise Exception("End date must be a string of at least 7 characters") self.visitor = visitor self.national_park = national_park self.start_date = start_date self.end_date = end_date Trip.all_trips.append(self)

@property def visitor(self)
: return self._visitor

@visitor.setter def visitor(self, value)
: self._visitor = value

@property def national_park(self)
: return self._national_park

@national_park.setter def national_park(self, value)
: self._national_park = value

@property def start_date(self)
: return self._start_date

@start_date.setter def start_date(self, value)
: self._start_date = value

@property def end_date(self)
: return self._end_date

@end_date.setter def end_date(self, value)
: self._end_date = value
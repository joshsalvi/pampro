import copy

class Bout(object):

	def __init__(self, start_timestamp, end_timestamp, label=""):
		
		self.label = label
		self.start_timestamp = start_timestamp
		self.end_timestamp = end_timestamp
		self.draw_properties = {'lw':0, 'alpha':0.8, 'facecolor':[0.78431,0.78431,0.78431]}

	def contains(self, timepoint):

		return timepoint >= self.start_timestamp and timepoint <= self.end_timestamp

	def overlaps(self, other):
		
		return self.contains(other.start_timestamp) or self.contains(other.end_timestamp) or other.contains(self.start_timestamp) or other.contains(self.end_timestamp)

	def intersection(self, other):

		return Bout(max(self.start_timestamp, other.start_timestamp), min(self.end_timestamp, other.end_timestamp))



def bout_list_intersection(bouts_a, bouts_b):

	intersection = []

	for bout_a in bouts_a:
		for bout_b in bouts_b:

			if bout_a.overlaps(bout_b):

				bout_c = bout_a.intersection(bout_b)
				#print bout_a.start_timestamp, bout_a.end_timestamp, "overlaps", bout_b.start_timestamp, bout_b.end_timestamp, "=", bout_c.start_timestamp, bout_c.end_timestamp
				intersection.append(bout_c)
		
	#print "Bouts a", len(bouts_a)
	#print "Bouts b", len(bouts_b)
	#print "Intersections", len(intersection)

	#for i in intersection:
	#	i.draw_properties = {"lw":1, "facecolor":[1.0,0.2,0.2], "alpha":0.38}

	return intersection

def bout_list_union(bouts_a, bouts_b):

	# TODO: Return the union of two bout lists

	return -1

def time_period_minus_bouts(time_period, bouts):

	# Currently assumes bouts are sorted in chronological order
	# Add sort in here for safety?

	results = []

	start = time_period[0]

	for bout in bouts:

		results.append(Bout(start, bout.start_timestamp))
		start = bout.end_timestamp

	results.append(Bout(start, time_period[1]))

	#for r in results:
	#	r.draw_properties = {'lw':0, "alpha":0.75, "facecolor":[0.95,0.1,0.1]}

	return results
	
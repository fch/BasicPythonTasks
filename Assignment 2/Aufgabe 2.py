
def overtime(time, hours_per_week):
	if time <= hours_per_week :
		return 'Sie haben keine Ueberstunden gemacht.'
	else :
		result = time-hours_per_week
		return "Sie haben " + (str(result)) + " Ueberstunden gemacht."


print(overtime(39, 40))
print(overtime(40, 40))
print(overtime(41, 40))

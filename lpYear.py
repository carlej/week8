import string
def leapYear(a):
	if a%4 == 0:
		if a%400 == 0:
			return False
		else:
			return True
	else:
		return False

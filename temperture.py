from __future__ import division

def FahrenheitFromCelsius(num1):

	return (num1 * (9 / 5)) + 32

def CelsiusFromFahrenheit(num2):

	return (num2 - 32) * (5 / 9)


Fresult = int(FahrenheitFromCelsius(22))

Cresult = int(CelsiusFromFahrenheit(98.6))


print "72 degrees F is %d degrees C" %Cresult

print "37 Degrees C = %d degrees F" %Fresult
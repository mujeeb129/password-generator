import random
from django.shortcuts import render

def generate(request):
	length = int(request.GET.get('length'))
	isUpper = request.GET.get('upperCase')
	isNumber = request.GET.get('numbers')
	isSpecial = request.GET.get('specialChar')
	charArray = list('asdfghjklzxcvbnmqweryuiopt')
	password = ''
	if isUpper:
		charArray.extend(list('ASDFGHJKLQWERTYUIOPZXCVBNM'))
	if isNumber:
		charArray.extend(list('0123456789'))
	if isSpecial:
		charArray.extend(list('!@#$%^&*()'))

	for i in range(length):
		password += random.choice(charArray)

	return password

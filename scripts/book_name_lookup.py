

from numpy import genfromtxt


def book_lookup(name):

	my_data = genfromtxt('book_abreviations.csv', delimiter=',',dtype=None)


	book = next((item for item in my_data if item[[1]] == name))

	return book[0]



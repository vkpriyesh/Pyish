#usage of built-in enumerate function
friends = ['Elon','Peter','Blake','Steve']
for i, name in enumerate(friends) :
	print "iteration {iteration} is {name}".format(iteration=i, name=name)
	
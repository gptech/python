def transisters_and_flops(transister_count, flops):
	print "Holy shit this card has %r transisters which will give us %r million flops!" % (transister_count, flops)

transisters_and_flops(20, 30)

transisters_and_flops(50+75, 1000000)

transisters_and_flops(99-1, 503)
transisters_and_flops(88 + 88 + 88, 2873)
transisters_and_flops("Ninety", "Eighty" )
transisters_and_flops(1+1+0, "One hundred and sixty thousand")
transisters_and_flops(8 * 500, 10000/55)

def transisters_and_counts2():
	transister_count = raw_input("How many transisters are there? ")
	flops_count = raw_input("How many flops can this thing do? ")

	print "Ok so this card has %s transisters and can do %s flops." % (transister_count, flops_count)

transisters_and_counts2()

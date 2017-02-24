# Exercise 8: Printing, Printing
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % ("I had this thing.",
			"That you cold type up right.",
			"But it did't sign.",
			"So I said goodnight."
		)

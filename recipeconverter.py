print "-- Original Recepie --"

flour = input("Enter the amount of Flour (cups):") 
water = input("Enter the amount of water (cups):")
salt = input("Enter the amount of salt (teaspoons):")
yeast = input("Enter the amount of yeast (teaspoons):")
factor = input("Enter the loaf adjustment factor (e.g 2.0 double the size):")

print "\n--Modified Recipe --"

print "Bread flour: %.1f cups" % (float(flour)*factor)
print "Water: %.1f cups" % (float(water)*factor)
print "Salt: %.1f teaspoons" % (float(salt)*factor)
print "Yeast: %.1f teaspoons" % (float(yeast)*int(factor))
print "Happy Baking!"

print "\n--Modified Recipe in Grams --"

print "Bread flour: %.2f g." % (float(flour)*factor*120)
print "Water: %.2f g." % (float(water)*factor*237)
print "Salt: %.2f g." % (float(salt)*factor*5)
print "Yeast: %.2f g." % (float(yeast)*factor*3)
print "Happy Baking!"
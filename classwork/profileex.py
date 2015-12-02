vara = 10
varb = 20

sum = vara + varb
print "vara + varb = %d" % sum


import cProfile
import re
cProfile.run('re.compile("foo|bar")')

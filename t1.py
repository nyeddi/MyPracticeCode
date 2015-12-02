for x in range(1, 11):
  print str(x).rjust(2), str(x*x).rjust(3),
  # Note trailing comma on previous line
  print str(x*x*x).rjust(4)

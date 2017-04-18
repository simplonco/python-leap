def is_leap_year(n):
  if n % 4 == 0 and n % 100 != 0:
    if n % 400 == 0:
      print n, "it is a leap year."
    elif n % 4 != 0:
      print n, "it is not a leap year."

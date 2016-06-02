1	def leapyear(n):
2	    if n%4==0 and n%100!=0:
3	        if n%400==0:
4	            print n, "it is a leap year."
5	    elif n%4!=0:
6	        print n, "it is not a leap year."
7

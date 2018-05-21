import math

class Angeo():
	""" Nokta """

	class Point():
		
		def p(x,y):
			return [x,y]

		"""İki nokta arası uzaklık"""
		def Distance(x,y):
			
			a = math.pow((x[0]-y[0]),2)
			b = math.pow((x[1]-y[1]),2)
			c = math.pow((a+b),1/2)
			
			return c


	class Line():

		""" y=ax+b"""
		def ln(x,y):
			print( "y = " + str(x) + "x + "+ str(y) )
			return [x,y]

		""" iki noktadan bir dogru"""
		def id(x,y):
			"""y=ax+b"""
			a=((y[1]-x[1])/(y[0]-x[0]))
			b=y[1]-a*y[0]
			print( "y = " + str(a) + "x + " + str(b) )
			return [a,b]

		"""	Doğru parçasının orta noktası """
		def MiddleOfLinePiece(x,y):

			 return [(x[0]+y[0])/2,(x[1]+y[1])/2]
			
		"""def p(x,y,z): 

				Bir Doğru parçasının eşit aralıklarla bölünmesi

		"""






			

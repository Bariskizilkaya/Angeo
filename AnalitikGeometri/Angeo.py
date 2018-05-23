import math


""" Nokta """
class Point:

	def p(x,y):
		return [x,y]

	"""İki nokta arası uzaklık"""
	def Distance(x,y):
		
		a = math.pow((x[0]-y[0]),2)
		b = math.pow((x[1]-y[1]),2)
		c = math.pow((a+b),1/2)
		
		return c


class Line:

	""" y=ax+b"""

	def ln(x,y):
		print( "y = " + str(x) + "x + "+ str(y) )
		return [x,y]

	""" iki noktadan bir dogru"""
	def inbd(x,y):
		"""y=ax+b"""
		a=((y[1]-x[1])/(y[0]-x[0]))
		b=y[1]-a*y[0]
		print( "y = " + str(a) + "x + " + str(b) )
		return [a,b]

	"""	Doğru parçasının orta noktası """
	def MidpointOfLinePiece(x,y):
		 return [(x[0]+y[0])/2,(x[1]+y[1])/2]
		
		"""Bir Doğru parçasının eşit aralıklarla bölünmesi"""
	def p(x,y,seg):
		x_aras=math.fabs(x[0]-y[0])
		y_aras=math.fabs(x[1]-y[1])
		x_parc=x_aras/seg
		y_parc=y_aras/seg
		c=[]
		for i in range(int(x_aras/x_parc)):
			p_new=[(x[0]+(i+1)*x_parc),(x[1]+(i+1)*y_parc)]
			c.append(p_new)
		"""print(len(c))"""
		c.pop(len(c)-1)
		return c
	
"""class Circle:"""

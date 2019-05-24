##import sys
#antigravity

class geohashing:
	def __init__(self,param1,param2,param3):
		self.param1 = param1
		self.param2 = param2
		self.param3 = param3
		result = self.param1+self.param2+self.param3
		return result


#------------------------------------------------------------
if __name__ == '__main__':
	prog = geohashing(param1="coucou",param2="les" ,param3= "loulous")
	print(prog)
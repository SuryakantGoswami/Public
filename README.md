# New_Project

class Employee:
	def emp_details(self,amount, months):
		self.amount = amount #int(input("Enter amount:"))
		self.months = months #int(input("Enter months:")) 
		

class Rate(Employee):
	def rate_of_interest(self,rate = 12):
		rateofinterest = self.amount / 100 * rate
		print('Rate of interest', rateofinterest)
		print('Total rate of interest %s for month %s'%(rateofinterest * self.months, self.months))
		return "HELLLOO"
		#return amount,months,rate

class Demo(Rate):
	def xyz_abc(self, display):
		#import pdp
		#pdp.set_trace()
		a = 100
		self.display = display
		return(display)
			

obj_Rate = Demo()
obj_Rate.emp_details(5000,12)
print(obj_Rate.xyz_abc(100))	
print(obj_Rate.rate_of_interest(100))

#This code used for rate of interest 

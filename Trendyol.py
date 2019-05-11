class Trendyol():

	def __init__(self , buy_url , img_link , company_name , old_price) :

		self.buy_url = buy_url
		self.img_link = img_link
		self.company_name = company_name
		self.old_price = old_price

	def getData(self):

		return self.buy_url , self.img_link , self.company_name , self.old_price 



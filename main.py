"""This is the main module.

This module does ALL Spider Operations and this module need to run.
"""


import requests
import  json
from dbsaver import save_to_db



class LoginSpider:
  
  '''Login class contain information about login from dummyjson '''
  
  def __init__(self):
    self.username=None
    self.password=None
  
  #Login user from dummyjson
  def login(self):
    
    # Getting the username and password from user 
    self.username=input("Enter the Username:  ") 
    self.password=input("Enter the Password:  ") 
    

    data={
      "username": self.username,  #'kminchelle', use as username
      "password": self.password,   #'0lelplR',  use as passsword
    }
    response = requests.post(
              'https://dummyjson.com/auth/login',
              headers={'Content-Type': 'application/json',}, 
              data = json.dumps(data)
              )

    value=eval(response.text) #Converting json to python dict
    print("Token: ", value['token']) 



class CategoryCollectionSpider(LoginSpider):
  
  '''CategoryCollectionSpider class contain information about categories from dummyjson '''

  def __init__(self):
    self.categories=None
    super().__init__()
  
  
  def get_category(self):
    response = requests.get('https://dummyjson.com/products/categories') #requesting categories
    self.categories=eval(response.text) #converting string to list
    print("Categories : ")

    #Displaying each categories from list
    for categ in  self.categories:  
      print(categ)
    print("\n")


class ProductCollectionSpider(CategoryCollectionSpider):
  
  '''ProductCollectionSpider class contain information about Products from dummyjson '''
  
  def __init__(self):
    super().__init__()
    self.records=[] #intialize list for taking category and item
  
  
  def get_products(self):
    
    for categ in self.categories: #looping categories
     
      response = requests.get('https://dummyjson.com/products/category/'+categ) #requesting each category products
      products=eval(response.text) #converting string to list python object
      
      if 'products' in products:
        print("Product in ",categ)
        count=1
        for product in products['products']:
            item=product['title']
            print(count,".", item)
            count=count+1
            self.records.append("""("{}","{}")""".format(categ,item)) #appending category and item
      print("\n\n")
    
    



exits=False #set exist=False  

while exits == False: #looping the menu while exist = True
  print('\n')
  print("Please Choose Spider")
  spider=input("1. Login Spider\n2. Category Collection Spider\n3. Product Collection Spider\n5.exit\n") #taking option from user

  if spider == "1":
    obj1=LoginSpider() #Creating Object for Loginspider
    obj1.login() #calling login methode

  elif spider == "2":
    obj1=CategoryCollectionSpider() #Creating Object for CategoryCollectionSpider
    obj1.login() #calling login methode
    obj1.get_category() #calling Category list

  elif spider == "3":
    obj1=ProductCollectionSpider() #Creating Object for CategoryCollectionSpider
    obj1.login() #calling login methode
    obj1.get_category() #calling Category list
    obj1.get_products() #calling products 
    save_to_db(obj1.records) #calling DB SAVER to save product records in to database
    exits=True

  elif spider == "5":
    exits=True
  else:
    print("please choose correct Spider")
  




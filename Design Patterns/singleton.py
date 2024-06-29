class GovtSingleton:  
   __instance__ = None  
  
   def __init__(self):  
       # This is a Constructor  
      
       if GovtSingleton.__instance__ is None:  
           GovtSingleton.__instance__ = self  
       else:  
           raise Exception("We can not creat another class")  
  
   @staticmethod  
   def get_instance():  
       # We define the static method to fetch instance  
       if not GovtSingleton.__instance__:  
           GovtSingleton()  
       return GovtSingleton.__instance__  
  
# Creating an object of above defined class.  
gover = GovtSingleton()  
print(gover)  
  
same_gover = GovtSingleton.get_instance()  
print(same_gover)  
  
another_gover = GovtSingleton.get_instance()  
print(another_gover)  
  
new_gover = GovtSingleton()  
print(new_gover)

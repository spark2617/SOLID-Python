class Programmer:
    def make(self):
        print("Programmer creating code")

class Seller:
    def make(self):
        print("Seller selling the product")

class Human:
    def make(self):
        print("Human Resources hiring new devs")

# --------//---------//----------//---------
class Company:
    def do_work(self, worker:any)->None:
       worker.make()




# -------ANTES

# class Company:
#     def do_work(self, worker:int)->None:
#         if worker == 1:
#             print("Programmer creating code")
#         elif worker == 2:
#             print("Seller selling the product")
#         elif worker == 3:
#             print("Human Resources hiring new devs")
            
#         else:
#             print("Error, no worker!")
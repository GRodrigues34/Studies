import pandas as pd

disciplines = {'courses' : ['statistics', 'economics', 'calculus', 'geometry'],
			  'credit'  : [90,60,90,40],
			  'requisite': [True,False,True,False]}
			
data = pd.DataFrame(disciplines)
print(data)
print("\n")

car_name = pd.Series(['308','polo','a3'])
car_automaker = pd.Series(['peugeot','volkswagen','audi'])

car_data = pd.DataFrame({"Car" : car_name, "Automaker" : car_automaker})
print(car_data)
print("\n")

car_dict = dict(zip(car_name,car_automaker))
print(car_dict)
print("\n")

who_308 = car_dict['308']
print(who_308)
print("\n")

here = '308' in car_dict
print(here)

here = 'onix' in car_dict
print(here)
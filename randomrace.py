import random
import time 

class car_race():
    def __init__(self,fgas=100,lgas=50):
        self.fgas = fgas
        self.lgas = lgas

    """ def ran_out_of_gas(self,brand):
        if self.fgas-self.lgas <=0:
            print(brand,": Ran out of gas and left the race.") """

class choose_car(car_race):
    def __init__(self,gas,number_of_opps=4,):
        super().__init__(gas)
        self.number_of_opps = number_of_opps

    def choise_(self,choise):
        
        self.choise = choise
        
        choise = int(input("""
---Garage---
1)Porsche
2)Lamborgini
3)Ferrari
4)McLaren
5)Subaru
Choose one:"""))
       
        if choise==1:
            self.choise = 'Porsche'
        if choise==2:
            self.choise = 'Lamborgini'
        if choise==3:
            self.choise = 'Ferrari'
        if choise==4:
            self.choise = 'McLaren'
        if choise==5:
            self.choise = 'Subaru'
        
        # if choise is not between 1-5 ask again.
        while choise<=0 or choise>5:
            print("Choose a number between 1 and 5.")
            time.sleep(2)
            choise = int(input("""
---Garage---
1)Porsche
2)Lamborgini
3)Ferrari
4)McLaren
5)Subaru
Choose one:"""))

            if choise==1:
                self.choise = 'Porsche'
            if choise==2:
                self.choise = 'Lamborgini'
            if choise==3:
                self.choise = 'Ferrari'
            if choise==4:
                self.choise = 'McLaren'
            if choise==5:
                self.choise = 'Subaru'
            
    def race_result(self):
        brand = ['Porsche', 'Lamborgini', 'Ferrari', 'McLaren', 'Subaru', 'Audi', 'Bmw']
        
        self.number_of_opps = 4

        # if your car and random car is same remove random car from the list
        for brand_ in brand:
            if self.choise == brand_:
                brand.remove(brand_)
        random_brand = random.sample(brand,self.number_of_opps)
        
        i=0 
        while i<5:# total number of car
            j=0
            while j<4: # total number of opponents
                print("Race is starting!...")
                time.sleep(3)
                print("Race will finish in 10 seconds.")
                # counting back from 10
                for k in range(10,0,-1):
                    print(k)
                    time.sleep(1)
                
                for brands in random_brand:
                    print("Opponent"+str(j+1), brands)
                    self.fgas = random.randrange(100,201)
                    self.lgas = random.randrange(1,100)
                    print("Initial gasoline",self.fgas) 
                    print("Remaining gasoline", self.fgas-self.lgas) 
                    print("\n")
                    time.sleep(1)
                    j+=1
                    
                time.sleep(1)
                print("Your Car: {}".format(self.choise))
                print("Initial gasoline:", self.fgas)
                print("Remaining gasoline:", self.fgas-self.lgas)
                
                print("---Ranking---")
                time.sleep(1)
            
                random_brand.append(self.choise)
                
                # rank randomly
                for brands in random_brand: 
                    a = list(random_brand)
                    random.shuffle(a)
                for c in a:
                    print(str(i+1),") {}".format(c))
                
                    i+=1
            print("Race is over!")

                        
araba = choose_car(4)
araba.choise_(" ")
araba.race_result()



HumanA = Human(5, 0, 0)  
StudentA = Student(5, 0, 0, 11, 4.0)  

print(HumanA.getHuman())  
print(StudentA.getHuman())  

print("Now moving to [1,2]")

HumanA.move([1, 2])
StudentA.move([1, 2])

print(HumanA.getHuman())  
print(StudentA.getHuman())  
        
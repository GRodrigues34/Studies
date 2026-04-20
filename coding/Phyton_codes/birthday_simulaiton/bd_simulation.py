import random 

people = [None] * 23

def randomBirthday():
    return random.randint(1,365)

def generateRoom():
    for i in range(len(people)):
        people[i] = randomBirthday()

def testBirthdays():
    for i in range(len(people)):
        for j in range(len(people)):
            if i != j:
                if people[i] == people[j]:
                    return True
    return False

def simulate(testNumber):
    positive = 0
    negative = 0

    for i in range(testNumber + 1):
        generateRoom()
        if testBirthdays():
            positive += 1
        else:
            negative += 1    
    return positive, negative

while(True):
    testNumber = int(input("Number of simulations"))
    positive, negative = simulate(testNumber)
    percentage = (positive/testNumber) * 100
    print(f"In {testNumber} simulations te percentage of people with the same birthday is: {percentage}%")
    more = input("Simulate more? y/n:")
    if more != "y":
        break

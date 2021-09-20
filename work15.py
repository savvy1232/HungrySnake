cars = ["OK","OK","OK","OK","OK"]
for status in cars:
    if status == "Faulty":
        print("Stop the Production")
        break
    print(f"This car is{status}")
    print("Ship New car to custumer")
else:
    print("All Cars Shipped Successfully , No Faulty Car.")
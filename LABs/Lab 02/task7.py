def calculate_average_temperature(lst):
    #calculates average tempertaure
    avg = sum(lst) / len(lst)
    print("The avrage temperature of the month is: ", avg)
    
def heighest_and_lowest_temperature(lst):
    #calculates lowest temperature
    max = lst[0]
    for i in range(1, len(lst)):
        if(max < lst[i]):
            max = lst[i]
        
    #calculates heighest temperature
    min = lst[0]
    for i in range(1, len(lst)):
        if(min > lst[i]):
            min = lst[i]
    print("The maximum and minimum temprature are: \nMaximum: ", max, "\nMinimum: ", min)
    
def sort_ascending_order(lst):
    #sorts list in ascending order\
    lst.sort()
    print("The new sorted list is: ", lst)
    
def remove_temperature(lst):
    #removes given day from the list
    day = int(input("Enter the day(0-8): "))
    lst.pop(day)
    print("Updated List: ", lst)
        
        
    
def main():
    temperature = [24, 58, 79, 45, 67, 23, 19, 87]
    
    calculate_average_temperature(temperature)
    heighest_and_lowest_temperature(temperature)
    sort_ascending_order(temperature)
    remove_temperature(temperature)

main()

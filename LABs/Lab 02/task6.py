def multiply_list_elements(lst):
    multiplication = 1
    
    for i in range(len(lst)):
        multiplication *= lst[i]
    print("The multiplied list elements are: ", multiplication)        
    
def main():
    lst = [3, 5, 7, 2, 1]
    multiply_list_elements(lst)
    
main()

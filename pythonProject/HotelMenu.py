print("""Choose the number 
1.Alfam
2.Biriyani
3.Chattichoru
4.Donut""")
choice=int(input())
match choice:
    case 1:
        print("You have selected 'Alfam' ")
    case 2:
        print("You have selected 'Biriyani' ")
    case 3:
        print("You have selected 'Chattichoru'")
    case 4:
        print("You have selected 'Donut' ")
    case _:
        print("Item not Available")
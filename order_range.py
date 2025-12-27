
lower_range=int(input("What is the upper range: \n"))
upper_range=int(input("What is the lower range: \n"))

def print_lables(lowe_range, upper_range):
        stop_order = 115

        for n in range(lowe_range,upper_range+1):
            #check if odd or even before printing it

            if n == stop_order: #= 115:
                break
            if n == 102:
                continue

            if n % 2 == 0:
                print("Order priority order: ", n)
            else:
                print("Order is Standard Order: ", n)

print_lables(lower_range, upper_range)
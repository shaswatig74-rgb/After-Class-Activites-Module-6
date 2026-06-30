z = int(input("Enter the number of times: "))
def fibonacciSeries(x, y):
    for i in range(z):
        print(x)
        x,y=y,x+y

fibonacciSeries(0, 1)
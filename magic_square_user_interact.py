from magic_square import is_square, magic

# user interaction:
ans = "yes"
matrix = []

while ans == "yes":

    try:
        matrixSize = int(input("Enter the dimension of matrix size 2 or larger (2 for 2x2, 3 for 3x3, etc.): "))
    except:
        print("Improper input type.")
        matrixSize = None
        
    if type(matrixSize) == int and matrixSize >= 2:
        for i in range(matrixSize):
            try:
                row = input("Enter the values in row "+ str(i+1) + " separated by spaces (ex. 0 1 2): ").split(" ")
                if len(row) == matrixSize:
                    for j in range(len(row)):
                        row[j] = int(row[j])
                else:
                    print("Values inputted incorrectly.")
                    pass
                matrix.append(row)
            except:
                print("Values inputted incorrectly.")

        if magic(matrix):
            print("The matrix is a magic square!")
        else:
            print("The matrix is not a magic square.")
    elif type(matrixSize) == int:
        print("Matrix is not large enough")

    ans = input("Would you like to enter another matrix? (yes/no): ").lower()

    while ans != "yes" and ans != "no":
        if ans != "yes" and ans != "no":
            print("Only input yes or no.")
            ans = input("Would you like to enter another matrix? (yes/no): ").lower()

print("Goodbye!")

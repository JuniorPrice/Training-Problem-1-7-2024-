def main():
    #Ask the user to enter how many positions in each dimension
    n = int(input('Enter the number of positions in each dimension of the matrix between 1 and 20: '))
    
    #Validate the number of positions
    if n < 1 | n > 20:
        print('Invalid number of positions')
        print('Run the program again ---!')
        return

    input_matrix = []
    
    #Ask for entries
    for _ in range(n):
        dimension = input('Enter the numbers separated by SPACE: ')
        dimension = dimension.strip().split(' ')

        #Validate the number of entries in each row
        if len(dimension) != n:
            print(f'Invalid Input ==> You must provide {n} numbers')
            print('Run the program again ---!')
            return

        input_matrix.append(dimension)
    
    #Print the input matrix
    print('The input matrix is: ')
    print_matrix(input_matrix)

    #Rotate and print the input matrix
    output_matrix = rotate(input_matrix, n)
    print('\nThe rotated matrix is: ')
    print_matrix(output_matrix)

#Function to rotate the input matrix by 90 degrees clockwise
def rotate(matrix, length):
    output_matrix = []

    for i in range(len(matrix)):
        di =[]
        for j in range(len(matrix)):
            di.append(matrix[j][i])
        
        di.reverse()    
        output_matrix.append(di)
      
    return output_matrix

#Print the matrix
def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

#Call main function
if __name__ == '__main__':
    main()

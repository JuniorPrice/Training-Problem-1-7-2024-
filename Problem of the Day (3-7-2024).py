#Main function
def main():
    #Ask the user to enter the values
    inputs = input("Enter your values sperated by SPACES: ")
    inputs = inputs.strip().split(' ')
    
    #Validate the user input
    for i in inputs:
        if not i.isdigit():
            print('Invalid input (must be a number)')
            return

    #Convert the input into integers and Call largest_rectangle function
    inputs = list(map(int, inputs))
    largest = largest_rectangle(inputs)
    
    #Print the largest rectangle space
    print(f'The largest rectangle is: {largest}')

#Function to calculate the largest rectangle space
def largest_rectangle(inputs):
    largest = 0
    for i in inputs:
        for j in range(1 , i+1):
            length = 1
            for h in inputs[inputs.index(i)+1:]:
                if j <= h :
                    length += 1
                else:
                    break
            if largest < length * j:
                largest = length * j

    return largest

#Call the main function
if __name__ == '__main__':
    main()
        

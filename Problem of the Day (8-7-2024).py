def main():
    #Ask the user to enter the array of integers
    array = input("Enter your array of integers sperated by SPACES: ")
    array = array.strip().split(" ")
    
    #Validate the user input
    for i in array:
        if not i.isdigit():
            print('Invalid input (must be a number)')
            return

    array = list(map(int, array))
    
    cross = path_crosses(array)
    print (f'Crossing = {cross}')

#Function check if there is a cross
def path_crosses(array):
    points = []   #Save visited points
    direction = 1 #First Direction Move North
    x = 0
    y = 0
    current = [x,y] #Start point
    points.append(current) #Save Start Point
    
    #Move and save visited points
    for i in array: 
        if direction == 1:
            for j in range(i):
                x += 1
                current = [x,y]
                points.append(current)
            direction = 2

        elif direction == 2:
            for j in range(i):
                y -= 1
                current = [x,y]
                points.append(current)
            direction = 3

        elif direction == 3:
            for j in range(i):
                x -= 1
                current = [x,y]
                points.append(current)
            direction = 4

        elif direction == 4:
            for j in range(i):
                y += 1
                current = [x,y]
                points.append(current)
            direction = 1

    
    #find if there is a cross section
    for point in points:
        if points.count(point) > 1:
            return True
       
    return False

#Call the main function
if __name__ == '__main__':
    main()   
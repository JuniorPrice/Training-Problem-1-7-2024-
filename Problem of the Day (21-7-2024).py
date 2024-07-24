def main():
    #Ask the user to enter the number of the buildings
    nOfB = input('Enter the numbers of Buildings: ')
    #Validate the number of buildings
    if not nOfB.isdigit():
        print ('Invalid input (must be a number)...!')
        return

    buildings = []
    #Enter the Dimensions of the buildings and validate them
    for i in range(nOfB):
        build = input('Enter the 3 numbers (left, right, height) of the Building Dimensions (sperated by SPACES): ')
        build = build.strip().split(" ")
        for j in build:
            if not j.isdigit():
                print ('Invalid input (must be numbers)...!')
                return
        buildings.append(build)
    
    #Call get_turn_points function to get the output
    turnPoints = get_turn_points(test)

    print(f'Turn Points are: {turnPoints}')


def get_turn_points(buildings):
    buildings = buildings
    buildings.sort(key=lambda x: (x[0],x[2]))
    points = []
    previous = [0,0,0]
    current = [0,0,0]
    for i in buildings:
        current = i
        if current[0] == previous[0]:
            points.append([current[0], max (current[2], previous[2])])
            previous = i
            continue
        if current[0] in range(previous[0], previous[1]+1):
            if current[2] > previous[2]:
                points.append([current[0], current[2]])
            if current[2] < previous[2]:
                points.append([previous[1], current[2]])
            previous = i
            continue
        if current[0] not in range(previous[0], previous[1]+1):
            if previous[2] != 0:
                points.append([previous[1], 0])
            points.append([current[0], current[2]])
            previous = i
            continue
    points.append([current[1],0])
    return points
        
#Call main function      
if __name__ == "__main__":
    main()

    
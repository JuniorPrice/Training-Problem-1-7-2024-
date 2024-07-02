def main():

    #asking for user input
    black = int(input('Enter the number of BLACK balls: '))
    white = int(input('Enter the number of WHITE balls: '))
    print()
    
    hight = []  #storing hight values
    hight.append(output(white, black))  #start the triangle with white ball and srore the hight value
    hight.append(output(black, white))  #start the triangle with white ball and srore the hight value
    
    print("The maximum hight is:",max(hight),'\n')  


def output(n1, n2):
    hight = 0
    first = n1
    second = n2
    
    #loop till there are no more balls to add to the triangle 
    while True:
        if first > hight:
            hight += 1
            first -= hight

            if second > hight:
                hight += 1
                second -= hight
            else: 
                break
            
        else:
            break

    return hight

#call main function
if __name__ == '__main__':
    main()
name = input("Type your Name: ")
print('Welcome ', name,' to this adventure!! ')

answer = input('You have arrived on a road. You can go left or right. Which way would you like to go ? ').lower()

if answer == 'left':

    answer = input('You come to ariver. You can walk around it or swim accross it. Type walk or swim: ' )
    
    if answer =='swim':
        print('You swam across eaten by an alligator :(')

    elif answer == 'walk':
        print('You walk for many miles, ran out of water and lost the game  :(')
    
    else:

        print('Not a valid option. ')
        print('You Loose :( ')



elif answer =='right':

    answer = input('You come to a bridge, it looks wobbly, do you want to cross it ? (cross/back): ')

    if answer =='back':

        print('You go back and loose :( ')

    elif answer == 'cross':

        answer = input('You cross the bridge and meet a stranger, Do you talk to them ?  (yes/no ): ')

        if answer =='yes':

            print('You talk to the stranger, they give you gold ')
            print('You WIN :) ')

        elif answer =='no':

            print('You ignore the stranger, they gets offended and attack you. ')
            print('You Loose.. :(  ')


    else:

        print('Not a valid option. ')
        print('You Loose :( ')

else:
    print('Not a valid option. ')
    print('You Loose :( ')

print('Thank You For Playing ', name, ':)')
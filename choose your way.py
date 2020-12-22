x=input('Press x to exit OR anyother key to continue.')
while(x!='x'):
    print('Welcome to my first game.\nAll you have to do is just answer my questions.')
    print('Your aim is to reach your house..')
    first=input('You are standing in middle of a field, Where will you go?(left/right)')
    if (first=="left"):
        print('Aww.. You died. You felt in a pit filled with poop..')
        x=input('Press x to exit OR anyother key to continue.')
    elif(first=='right'):
        print('You came near a river.')
        river=input('How will you pass the river??(across/around)')
        if(river=='across'):
            print('You died , you were eaten by a shark..')
            x=input('Press x to exit OR anyother key to continue.')
        elif(river=='around'):
            print('You reached a valley..')
            valley=input('How will you cross the valley(hotairballon/plane)')
            if(valley=='plane'):
                print('You died,your plane was out of fuel.')
                x=input('Press x to exit OR anyother key to continue.')
            elif(valley=='hotairballon'):
                print('You cannot go down with the hot air ballon.')
                ballon=input('What will you use to reach to the ground.(parachute/teleporter)')
                if(ballon=='parachute'):
                    print('You died, parachute had a hole..')
                    x=input('Press x to exit OR anyother key to continue.')
                elif(ballon=='teleporter'):
                    print('You were telepoted to a haunted road.')
                    road=input('How will you move on??(walk/calluber)')
                    if(road=='walk'):
                        print('You were bit by a zombie.')
                        x=input('Press x to exit OR anyother key to continue.')
                    elif(road=='calluber'):
                        print('Sorry, I forgot to tell you that there is no signal..')
                        signal=input('Do you wanna search for signal??(signal/askforlift)')
                        if(signal=='signal'):
                            print('You died.While searching for signal you fell off a clif..')
                            x=input('Press x to exit OR anyother key to continue.')
                        elif(signal=='askforlift'):
                            print('Someone gave you lift BUT it was your ex gf.')
                            lift=input('Doyou wanna go??(go/stay)')
                            if(lift=='stay'):
                                print('You died, you were caughtbya ghost.')
                                x=input('Press x to exit OR anyother key to continue.')
                            elif(lift=='go'):
                                print('She gave you lift and you reached your house!!!')
                                print('You win!!!\nYou win!!!')
                                x=input('Press x to exit OR anyother key to continue.')
                    
                    x=input('Press x to exit OR anyother key to continue.')
        
    

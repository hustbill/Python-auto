#A nicely documented program with a clever way of generating the farm of animals. 
#
# Example of user interaction:
# Welcome to old MacDonald's farm!
# Please enter 3 animals and the noise they make:
# What is the first animal? cow
# What is the first animal's sound? moo
# What is the second animal? hen
# What is the second animal's sound? cluck
# What is the third animal? sheep
# What is the third animal's sound? baa
#
# Old MacDonald had a farm, E-I-E-I-O
# And on his farm he had some cows, E-I-E-I-O
# And a moo-moo here, and a moo-moo there, everywhere a moo-moo!
# Old MacDonald had a farm, E-I-E-I-O
#
# Old MacDonald had a farm, E-I-E-I-O
# And on his farm he had some hens, E-I-E-I-O
# And a cluck-cluck here, and a cluck-cluck there, everywhere a cluck-cluck!
# Old MacDonald had a farm, E-I-E-I-O
#
# Old MacDonald had a farm, E-I-E-I-O
# And on his farm he had some sheeps, E-I-E-I-O
# And a baa-baa here, and a baa-baa there, everywhere a baa-baa!
# Old MacDonald had a farm, E-I-E-I-O
#


def main():
    # greet user
    print( "Welcome to old MacDonald's farm!" )
    print()

    # get the animals and their sound
    print ("Please enter 3 animals and the noise they make:")
    pair1   = [ input("What is the first animal? "), input("What is the first animal's sound? (only one word needed) ") ]
    pair2   = [ input("What is the second animal? "), input("What is the second animal's sound? (only one word needed) ") ]
    pair3   = [ input("What is the third animal? "), input("What is the third animal's sound? (only one word needed) ") ]
    animals = [pair1, pair2, pair3]
    
 
    # generate the lyrics
    for name, sound in animals:
        print()
        sound = sound + "-" + sound
        print( "Old MacDonald had a farm, E-I-E-I-O")
        print( "And on his farm he had some", name + "s, E-I-E-I-O" )
        print( "And a " + sound + " here, and a " + sound + 
                " there, everywhere a " + sound + "!" )
        print( "Old MacDonald had a farm, E-I-E-I-O" )


main()

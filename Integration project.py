# Jared Oister

# Compilation of demonstrations that show off different functions

# https://www.youtube.com/watch?v=63nw00JqHo0 video used to help create the menu as well as explain how it works

def menu():
    # menu for deciding what "demonstration" to play
    print("Welcome to the program", end=' ')
    print("!")
    print("[1]Math Calculations", "[2]Exponent Calculator", "[3]Word Multiplier", "[4]Area Finder","[0]Exit", sep='   ')


# prints the menu function and presents the options
menu()
choice = int(input())

# used a while loop to be able to meet the condition of a correct response choice
while choice != 0:

#=====================================================================================================calculator section

    if choice == 1:
        # Math calculator
        print("Option 1 has been chosen")
        print("Math calculator")
        print("Input first number:")

        # stores the first number that will be used in the calculator and prints the text "Input second number"
        first_num = int(input())
        print(first_num)
        print("Input second number:")

        # stores the second number that will be used in the calculator and prints the text "What math function would you
        #like to use?"
        second_num = int(input())
        print(second_num)
        print("What math function would you like to use?")


        # math_functions presents the prompt for which math function you would like to use
        def math_functions():
            print("[1] addition")
            print("[2] subtraction")
            print("[3] multiplication")
            print("[4] division")
            print("[0] return back to the menu")


        math_functions()

        #choice2 is used to decide which of the four basic math functions you would like to use
        choice2 = int(input())
        while choice2 != 0:
            if choice2 == 1:

                # addition - will add the two numbers inputted
                print(first_num + second_num)
            elif choice2 == 2:

                # subtraction - will subtract the two numbers inputted
                print(first_num - second_num)
            elif choice2 == 3:

                # multiplication - will multiply the two numbers inputted
                print(first_num * second_num)
            elif choice2 == 4:

                # division - will divide the two numbers inputted
                def division_choice():
                    print("Would you like to round your answer?")

                    #choice_round is used to decide if the user would like to round their answer
                    choice_round = input("y/n")
                    if choice_round == "y":
                        print(first_num // second_num)
                        print("Remainder:", first_num % second_num)
                    elif choice_round == "n":
                        print(first_num / second_num)
                        print("Remainder:", first_num % second_num)
                    else:
                        print("Invalid")
                        return division_choice()

                division_choice()
            else:
                print("Invalid")

            # prevents and infinite loop from occurring and re-represents the math choices
            print()
            math_functions()
            choice2 = int(input())

#=======================================================================================================exponent section

    elif choice == 2:
        # Exponent Calculator
        print("Option 2 has been chosen")
        print("Input your base number:")

        #base_num is used to collect and store the base number for the arithmetic operation
        base_num = int(input())
        print(base_num)
        print("Input your exponent value:")

        #exponent_value is used to collect and store the exponent value
        exponent_value = int(input())
        print(base_num ** exponent_value)

#===========================================================================================================word section

    elif choice == 3:
        # Word multiplier
        print("Option 3 has been chosen")
        print("Word multiplier")
        print("Input what word you would like to use:")

        #word is used to decide what word will be printed
        word = input()
        print("How many times would you like to multiply your word?")

        #word_amount is used to decide how many times the word will be printed
        word_amount = int(input())

        # the * inbetween the word and word_amount variables uses the input stored in word_amount to print the input
        # from the word variable multiple times
        print(word * word_amount + "!")

#============================================================================================================Area Finder

    #Calculates the area for a triangle. Asks for the base length and height of the triangle.
    def calculateTriangleArea():
        base = int(input("Enter the value of the base."))
        height = int(input("Enter the value of the height."))
        print((base*height)/2)

    #Calculates the area for a rhombus. Asks the user for the two diagonals of a rhombus to calculate the area.
    def calculateRhombusArea():
        diagonal1 = int(input("Enter the value of the first diagonal"))
        diagonal2 = int(input("Enter the value of the second diagonal"))
        print((diagonal1*diagonal2)/2)

    #Calculates the area for a rectangle or a square. Asks the user for the base and height.
    def calculateRectangle_SquareArea():
        base = int(input("Enter the value of the base."))
        height = int(input("Enter the value of the height."))
        print(base*height)

    #Calculates the area for a circle. Asks the user to input the radius and multiplies it by pi
    def calculateCircleArea():
        radius = int(input("Enter the radius of the circle"))
        print(radius*3.14)


    #Prompts the user for what shape they would like to calculate the area for
    def shapeChoice():
        print("What shape would you like to calculate the area for?")
        print("[1] Triangle")
        print("[2] Rhombus")
        print("[3] Rectangle / Square")
        print("[4] Circle")

    if choice == 4:
        shapeChoice()
        choice3 = int(input())
        if choice3 == 1:
            calculateTriangleArea()
        elif choice3 == 2:
            calculateRhombusArea()
        elif choice3 == 3:
            calculateRectangle_SquareArea()
        elif choice3 == 4:
            calculateCircleArea()
        else:
            print("Invalid")

    #I wasn't able to incorporate these elements into my project, so I put separate demonstrations not part of the main
    #menu but still usable

    #Demonstrates the use of the boolean operators and, or, and not.
    elif choice == 99:
        print("Boolean Operators")
        x = int(input())
        print(x<5 and x<90)
        print(x<12 or x<20)
        print(not(x<5 and x<10))

    #Demonstrates the use of the interactive structures for, in, and range.
    elif choice == 98:
        print("Interactive Structures")
        for x in range(1,4):
            print(x)

    #Demonstrates the use of shortcut operators.
    elif choice == 97:
        print("Shortcut Operators")
        x = 10
        print (x)
        x += 20
        print(x)


    #Demonstrates the use of parameters with functions.
    elif choice == 96:
        print("Parameter Use")
        def parameterExample(x):
            return x*10

        x = int(input())
        output = parameterExample(x)
        print(output)


    else:
        print("Invalid")



    #Prevents an infinite loop from occurring and re-presents the options
    print()
    menu()
    choice = int(input())

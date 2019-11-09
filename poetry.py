import random as random


poem = """If you are a dreamer, come in,
If you are a dreamer, a wisher, a liar,
A hope-er, a pray-er, a magic bean buyer…
If you’re a pretender, come sit by my fire
For we have some flax-golden tales to spin.
Come in!
Come in!"""

string_list = poem.split("\n")


def selection():
    '''This function allows you to select how you want the poem arranged.'''
    
    print("choose how you want the poem arranged:")
    print("(1) Normal\n(2) Backwards\n(3) Random\n(4) Rearranged")

    while True:
        selection = input("Number: ")
        if selection == "1":
            print(poem)
            break
        elif selection == "2":
            lines_printed_backwards(string_list)
            break
        elif selection == "3":
            lines_printed_random(string_list)
            break
        elif selection == "4":
            rearrange_poem(string_list)
            break
        else:
            print("Invalid selection. Please try again.")


def lines_printed_backwards(string_list): 
    """This function takes in a list of strings containing the lines
    of your poem as arguments and will print the poem lines out in reverse
    with the line numbers reversed."""
    
    #TODO Print lines in reverse
    #TODO Number them with their original line numbers
    index = len(string_list)
    string_list.reverse()
    
    for string in string_list:
        #print(str(index)+  " " + string)
        print(f'{str(index)}: {string}')
        index -= 1
        

def lines_printed_random(string_list):
    """the lines_printed_random() function which will randomly select lines
     from a list of strings and print them out in random order."""
    
    #TODO randomely select lines from a list of strings and print out in random order
    #TODO number of lines printed should be equal to the original 

    for string in string_list:
        random_index = random.randint(0,(len(string_list)-1))
        print(string_list[random_index])


def rearrange_poem(string_list):
    """a function of your choice that rearranges the poem in a unique way"""
    #TODO add a ! between every character
    
    for string in range(len(string_list)):
        print("!".join(string_list[string]))

def play_again():
    guess=(input('Play Again?(Y/N'))
    guess = guess.lower()
    if guess == 'y':
        return True
    else:
        return False
    

    
      
    
selection()

while play_again():
    selection()
# lines_printed_backwards(string_list)
# lines_printed_random(string_list)
# rearrange_poem(string_list)

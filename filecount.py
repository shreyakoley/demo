"""checking the instances of each word in a file."""
from sys import argv

def main():
    """ main function to calcute the word count
    """
    file = open(argv[1], 'r')  #open the file.
    list1 = []
    for words in file:
        words = words.strip()

        words = words.lower()    #converting the file into lower case alphabets.
        alph = words.strip().split(" ")
        list1.append(alph)
        #print(words)
    #print(list1)
    dicto = dict()
    #print(dicto)
    for alph in list1:
        for i in alph:
            #print(i)
            if i in dicto:
                dicto[i] = dicto[i] + 1
            else:
                dicto[i] = 1

        #for key in list(dicto.keys()):
    print(dicto)


if __name__ == '__main__':
    main()

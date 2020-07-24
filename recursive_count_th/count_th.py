'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #set word_check variable
    word_check = word
    #declare a base case
    if len(word_check) < 2:
        #when the length of the word_check variable is less than 2, end
        return 0
    # if the first two letters are "th"
    if word_check[:2] == "th":
        #run again without the first two letters.
        return( 1 + (count_th(word_check[2:])))
    # if they are not "th"
    if word_check[:2] != "th":
        #run again without the first letter
        return(count_th(word_check[1:]))

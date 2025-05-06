def how_much_i_love_you(nb_petals):
    phrases = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    count = 0

    for i in range(1, nb_petals + 1):  # loop from 1 to nb_petals
        phrase = phrases[count]
        count += 1

        if count == len(phrases):  # reset the count if we reach the end
            count = 0

    return phrase
def sillycase(word):
    first_half = ''
    second_half = ''

    length = int(len(word)/2)

    first_half += word[:length]
    second_half += word[length:]

    return first_half + second_half.upper()

sillycase('treehouse')    
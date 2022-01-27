


def main(words):
    if not words:
        return words

    vowel = ["a","e","i","o","u"]
    vowel_pos = []
    for i in range(0,len(words)):
        if words[i] in vowel:
            vowel_pos.append((i,words[i]))

    counter = len(vowel_pos)-1
    nwords = list(words)
    for i in vowel_pos:
        nwords[i[0]]=vowel_pos[counter][1]
        counter -= 1

    return "".join(nwords)

if __name__ == '__main__':
    print(main("facebook"))
    print(main("facebook")=="focobeak")
    print(main("apple"))
    print(main("apple")=="eppla")
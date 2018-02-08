"""Pulls wubs out."""


def song_decoder(song):
    """Decode wubbing."""
    list_of_words = []
    letters = []

    while song:
        if song[0] == "W":
            if song[1] == "U":
                if song[2] == "B":
                    if letters != []:
                        list_of_words.append("".join(letters))
                        letters = []
                    song = song[3:]
                else:
                    letters.append(song[0])
                    letters.append(song[1])
                    letters.append(song[2])
                    song = song[3:]
            else:
                letters.append(song[0])
                letters.append(song[1])
                song = song[2:]
        else:
            letters.append(song[0])
            song = song[1:]
    if letters != []:
        list_of_words.append("".join(letters))
    return " ".join(list_of_words)


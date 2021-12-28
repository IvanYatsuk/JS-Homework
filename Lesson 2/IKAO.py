decoding = list(str(input().lower()))
IKAO = {
    '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine',
    'a': 'Alpha', 'b': 'Bravo', 'c': 'Charlie', 'd': 'Delta', 'f': 'Foxtrot', 'g': 'Golf', 'h': 'Hotel', 'i': 'India',
    'k': 'Kilo', 'l': 'Limo', 'm': 'Mike', 'n': 'November', 'o': 'Oscar', 'p': 'Papa', 'q': 'Quebec', 'r': 'Romeo',
    's': 'Sierra', 't': 'Tango', 'u': 'Uniform', 'v': 'Victor', 'w': 'Whiskey', 'x': 'X-ray', 'y': 'Yankee', 'z': 'Zulu',
    }
print(" ".join([IKAO[s] for s in decoding]))

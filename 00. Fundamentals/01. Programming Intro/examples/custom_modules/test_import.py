#!/usr/bin/env python 
if __name__ == "__main__":
    print(__file__[0:-3])
elif __name__ == __file__[0:-3]:
    print("__name__ isn't __main__")
else:
    print("Hmm, something's fishy!" )

#!/usr/bin/env python
import read
from critics_dictionary import critics

pairs = []

def checkPair(n1, n2):
    global pairs
    for p1, p2 in pairs:
        if((n1 == p1) and (n2 == p2)):
            return True
    return False

def main():

    global pairs

    for critic1, ratings2 in critics.items():
        for critic2, ratings2 in critics.items():
            if((critic1 != critic2) and checkPair(critic2, critic1) == False):
                pairs.append((critic1, critic2))
                print "Critics:", critic1, ",", critic2
                print "Euclidean Score:", read.euclidean(critic1, critic2)
                print "Pearson Score:", read.pearson(critic1, critic2), "\n"

    #for p1, p2 in pairs:
    #    print p1, "-", p2

if __name__ == "__main__":
    main()

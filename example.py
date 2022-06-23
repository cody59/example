#regular import
import os

#grabs a method/function from module
from os import getcwd

#grabs a method/function from module then nicknames it
from os import getcwd as random


class example:

#constructior for a class
    def __init__(self):
        print("hi")

#standard function setup, self has to be in parameters if func is in class
    def forloop(self):

        #this is how you declare and variable no need to say int,string,char or anything
        final = 0

        #standard forloop for iterating through a range
        for i in range(1-10):
            print(i)
            final = i

        #this is a list like a linked list in java/c++
        exlist = [1-10]

        for element in exlist:
            print(element)

        #this returns variable final when the method is called
        return final


    def whileloop(self):

        #standard whileloop
        i = 0
        while i < 9:
            i += 1

    def wfile(self):

        filename = "changeme.txt"

        fw = open(filename, "w")

        fw.write("hello world")

        fw.close()

    def readfile(self):

        fin = open("changeme.txt", "r")

        #read() lets you read so many chars in file
        fread1 = fin.read(3)
        print(fread1)

        #readline() reads lines in file and puts it into a variable
        fread2 = fin.readline()
        print(fread2)
        #readlines() reads lines in file and puts it into a list
        fread3 = fin.readlines()
        print(fread3)

    









if __name__ == '__main__':
    #need to instantiate a class before using it
    ex = example()

    ex.wfile()
    ex.readfile()

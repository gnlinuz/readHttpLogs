#!/usr/bin/python3
"""
Script to read apache log file as command line argument
and returns the 10 most visited ip's
"""
import sys

def read_file(fname):
    """
    Open the log file, read each line, clean it from empty spaces
    and add unique ip addresses to the dictionary, then print the
    10 most visited ip's
    """
    # open the file for read
    file = open(fname, 'r')
    result_dic = {}

    while True:
        # read line by line and split it to words
        line = file.readline().strip()
        list_line = line.split()
        if not list_line:
            break
        # takes the first "word" which is the ip address
        # and fill up a dictionary of unique ip's
        if list_line[0] in result_dic:
            result_dic[list_line[0]] += 1
        else:
            result_dic[list_line[0]] = 1
    # create the list of 10 most visited ip addresses
    n_list = [(k, result_dic[k]) for k in sorted(result_dic, key=result_dic.get, reverse=True)[:10]]
    for ip_address, visits in n_list:
        print('IP Address: {}\tHits: {}'.format(ip_address, visits))

def main():
    """
    The main function.
    """
    read_file(sys.argv[1])

main()

#!/usr/bin/env python3

#Hackerland Radio Transmitters

'''
Hackerland is a one-dimensional city with houses, where each house is located at some on the -axis. The Mayor wants to install radio transmitters on the roofs of the city's houses. Each transmitter has a range, , meaning it can transmit a signal to all houses units of distance away.

Given a map of Hackerland and the value of , can you find and print the minimum number of transmitters needed to cover every house in the city? (Every house must be covered by at least one transmitter) Each transmitter must be installed on top of an existing house.

Input Format

The first line contains two space-separated integers describing the respective values of n(the number of houses in Hackerland) and k(the range of each transmitter).

The second line contains space-separated integers describing the respective locations of each house x(i.e.,x1,x2,...xn ).


while(i < n){
        numTransmitters++;

    /* Key is to use greedy algorithm to always place the transmitter at the house furthest to the right possible
     * to cover the range.
     */
        loc = x[i] + k; //let this i be i_orig
        //go to right as far as we cover i_orig as well.
        while(i < n && x[i] <= loc)
            i++;

        i--;    //this is where we place the transmitter
    cout << x[i] << " ";

    //now go to the right of x[i] by k because transmitter at x[i] covers houses to its right as well.
        loc = x[i] + k;
        while(i < n && x[i] <= loc)
            i++;
    }

'''


import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
x = [int(x_temp) for x_temp in input().strip().split(' ')]

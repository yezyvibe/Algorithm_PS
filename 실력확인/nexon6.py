#!/bin/python3

import math
import os
import random
import re
import sys
import requests



#
# Complete the 'getPhoneNumbers' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING country
#  2. STRING phoneNumber
# API URL: https://jsonmock.hackerrank.com/api/countries?name=<country>
#

def getPhoneNumbers(country, phoneNumber):
    # Write your code here
    data = {
        "name": country
    }
    query = requests.get('https://jsonmock.hackerrank.com/api/countries', params=data).json()["data"]

    for i in range(len(query)):
        if query[i]["name"] == country:
            codes = query[i]["callingCodes"]
            codes.sort()
            calling_code = codes[-1]
            break
    else:
        return -1 
        
    return f'+{calling_code} {phoneNumber}'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    country = input()

    phoneNumber = input()

    result = getPhoneNumbers(country, phoneNumber)

    fptr.write(str(result) + '\n')

    fptr.close()

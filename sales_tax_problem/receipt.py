""" 
Mike Goldman
1/18/17
receipt.py 
Main script for the Sales Tax Problem

-- README --

-- Sales Tax Problem --

To utilize this code you will need to have python installed on your system. 
A good walk-thru can be found here 
http://www.howtogeek.com/197947/how-to-install-python-on-windows/. 
The python 2.7.12 installer found in this folder can be used for the 
installation.

Sales Tax Problem

Scripts Included to be used:
    	receipt.py
		Script that creates the receipt
    	test.py
		tests for the python scripts
	
Dependencies: 
    	classifications.json
	test_input.json
	test_input.txt
	classify_items.py
         	create_receipt.py
	*** these are all included
	
Input Data:
	input1.txt
	input2.txt
	input3.txt
    	*** These are the supplied input data sets, others may be used as 
        long as they adhere to the same format

Usage:
   	receipt.py:
		python receipt.py 'inputs'
		i.e. python receipt.py input1.txt  
                OR 
                python receipt.py input1.txt input2.txt input3.txt
   	test.py:
		python test.py
   	***Note
		If you have the python interpreter setup correctly in your 
                windows %PATH% variable you can omit "python" from the commands.
    
"""

import sys
from classify_items import item
from create_receipt import create_line, create_total

# here is where we instantiate our item class and start
# totaling the taxes and creating our receipt
def myReceipt(f):
    try:
        myItems = item()
        lines = f.read().splitlines()
        receipt = []
        try:
            for line in lines:
                # get our updated items with taxes and totals
                myItem = myItems.classify(line)
                myItems.compute()
                myItems.roundup()
                myItems.sub_total()
                receipt.append(create_line(myItems, line))
            # create the final receipt
            return create_total(receipt)
        except Exception as e:
            print e
    except Exception as e:
        print e

# gather our file names and get to work    
for i in xrange(1, len(sys.argv)):
    try:
        with open(sys.argv[i], "r") as f:
            print ("\n%s") % myReceipt(f)
    except Exception as e:
        print e
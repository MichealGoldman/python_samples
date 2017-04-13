""" 
Mike Goldman
1/18/17
classify_itmes.py 
Class and methods for the Sales Tax Problem
"""

import math
import json

# class to classify items and compute taxes and totals
class item():

    # intiate the class - load our class data from the json file
    def __init__(self):
        try:
            with open('classifications.json', 'r') as f:
                read_data = f.read()
                self.item_class = json.loads(read_data)
        except Exception as e:
            print e
    
    # call class and return data
    def __call__(self, item):
        self.num_items = 0
        self.price = 0.0
        self.duty = False
        self.tax = True
        self.total = 0.0
        self.subtotal = 0.0
 
    # classify our item
    def classify(self, item):
        try:
            self.num_items = int(item.split(' ', 1)[0])
            words = str(item).split()
        except Exception as e:
            print e
        self.tax = True
        self.duty = False
        if 'import' in item:
            self.duty = True
        try:
            for word in words:
                if word in self.item_class:
                    self.tax = False
                if word[:-1] in self.item_class:
                    self.tax = False
            self.price = float(words[-1])
        except Exception as e:
            print e
        self.compute()
        return self

    # compute taxes and totals
    def compute(self):
        tax = .1
        duty = .05
        self.taxes = 0.0
        self.subtotal = self.price * self.num_items
        try:
            # if we tax and it is an import
            if self.tax is True and self.duty is True:
                self.taxes = self.subtotal * (tax + duty)
            else:
                # if we tax only
                if self.tax is True:
                    self.taxes = self.subtotal * tax
                # if an import only
                elif self.duty is True:
                    self.taxes = self.subtotal * duty
        except Exception as e:
            print e
             
    # used to round the tax up to the nearest .05
    def roundup(self):
        try:
            self.taxes = int(math.ceil(self.taxes/ .05)) * .05
        except Exception as e:
            print e
        
    # used to create the totals
    def sub_total(self):
        try:
            self.subtotal += self.taxes
        except Exception as e:
            print e


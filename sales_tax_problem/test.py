""" 
Mike Goldman
1/18/17
test.py 
Tests for the Sales Tax Problem
"""

import unittest
import json
from receipt import myReceipt
from classify_items import item
from create_receipt import create_line, create_total

# data for assertion tests
with open('test_input.json', 'r') as f:
    read_data = f.read()
    inputs = json.loads(read_data)

class receiptTest(unittest.TestCase):

    # regression test 
    def test_myReceipt(self):
        with open ("test_input.txt", "r") as f:
            self.assertEqual(myReceipt(f), inputs['text'])
    
    # unit tests
    def test_classify_items_init(self):
        myItems = item()
        with open('classifications.json', 'r') as f:
            read_data = f.read()
            jsonData = json.loads(read_data)
        self.assertEqual(myItems.item_class, jsonData)

    def test_classify(self):
        myItems = item()
        myItem = item.classify(myItems, inputs['smtext'])
        self.assertEqual(str(myItem.tax), inputs['tax'])
        self.assertEqual(str(myItem.duty), inputs['duty'])
        self.assertEqual(myItem.price, float(inputs['price']))
            
    def test_compute(self):
        myItems = item()
        myItem = item.classify(myItems, inputs['smtext'])
        myItem.num_items = 5
        myItems.price = 1.00
        myCompute =  item.compute(myItems)
        self.assertEqual(myItem.taxes, float(inputs['taxes']))

    def test_roundup(self):
        myItems = item()
        myItem = item.classify(myItems, inputs['smtext'])
        myItem.taxes = inputs['rtaxes']
        myItems.roundup()
        self.assertEqual(myItem.taxes, float(inputs['roundup_ans']))
        
    def test_subtotal(self):
        myItems = item()
        myItem = item.classify(myItems, inputs['smtext'])
        myItems.sub_total()
        self.assertEqual(myItem.subtotal, float(inputs['subtotal']))     
        
    def test_create_line(self):
        myItems = item()
        myItem = item.classify(myItems, inputs['smtext'])        
        test = (create_line(myItems, inputs['smtext']))
        self.assertEqual(test[0], inputs['cl_tax'])
        
    def test_create_total(self):
        receipt = []
        myItems = item()
        myItem = item.classify(myItems, inputs['smtext'])
        receipt.append(create_line(myItems, inputs['smtext']))
        test = create_total(receipt)
        self.assertEqual(test, inputs['smtext_out'])

if __name__ == '__main__':
    unittest.main()

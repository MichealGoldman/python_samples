
import sys
import json

class ReceiptItem:
    def __init__(self, item):
        with open('classifications.json', 'r') as f:
            read_data = f.read()
            self.item_class = json.loads(read_data)        
        self.num_items = int(item.split(' ', 1)[0])
        words = str(item).split()        
        self.name = item[1]
        self.taxable = True
        if 'import' in item:
            self.imported = True
        else:
            self.imported = False
        try:
            for word in words:
                if word in self.item_class:
                    self.taxable = False
                if word[:-1] in self.item_class:
                    self.taxable = False
        except Exception as e:
            print e
        self.price = float(words[-1])
        self.tax_rate = 0.05 if self.imported else \
                        0.10 if self.taxable else \
                        0.0
        self.tax = self.price * self.tax_rate
        self.price_with_tax = self.price + self.tax


    def __str__(self, item):
        
        return [item, "%0.2f" % (self.price_with_tax)]

class Receipt:

    def __init__(self):
        self.tax = 0.0
        self.taxable = True
        self.price = 0.00
        self.subtotal = 0.00
        self.items = []
        self.subtotal = self.tax 

    def add(self, item):
        self.items.append(item)
        self.subtotal += item.price
        self.tax += item.tax

    @property
    def total(self):
        return self.subtotal + self.tax

    def __str__(self, item):
        print item
        return "\n".join([str(item) for item in self.items] + [
            '',
            "Subtotal: %0.2f" % self.subtotal,
            "Tax: %0.2f" % self.tax,
            "Total: %0.2f" % self.total])


def main():
    #for i in xrange(1, len(sys.argv)):
        with open("input1.txt", "r") as f:    
            input = f
            receipt = Receipt()
            for line_number, line in enumerate(input):
                receipt.add(ReceiptItem(line))    
            print(receipt)



if __name__ == "__main__":
    sys.exit(main() or 0)
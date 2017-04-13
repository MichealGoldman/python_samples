""" 
Mike Goldman
1/18/17
create_receipt.py 
Functions for the Sales Tax Problem
"""

# create the line_items
def create_line(myItem, line):
        line_item = []
        taxes = 0.0
        total = 0.0
        try: 
                # begin creating the lines for the receipt
                line = line.replace(" at", ":")
                mySubtotal = format(myItem.subtotal, '.2f')
                line = line.split()
                line[-1] = mySubtotal
                sp = " " 
                sp = sp.join(line)
                line_item.append(("%s\n" % sp))
                taxes += myItem.taxes
                total += myItem.subtotal
                return ([taxes, total, line_item[0]])                     
        except Exception as e:
                print e

# create our tax and total and build receipt 
def create_total(items):
        receipt = []
        tax = 0.0
        total = 0.0
        try:    
                for item in items:
                        tax += item[0]
                        total += item[1]
                        receipt.append(item[2])
                receipt.append("Sales Taxes: %s\n" % format(tax,'.2f') )
                receipt.append("Total: %s" % format(total,'.2f') ) 
                printed_receipt = ''.join(receipt)
                return printed_receipt
        except Exception as e:
                print e
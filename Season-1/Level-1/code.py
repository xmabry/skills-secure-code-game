'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
import re
import math

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    net = 0.0
    productSum = 0.0
    paymentSum = 0.0

    for item in order.items:
        if itemCheck(item.type) and item.type == "payment":
            # if order.items.index(item)==0:
            #     return 'Total amount payable for an order exceeded'
            # else:
            paymentSum = float(paymentSum + processPayments(item))
        elif itemCheck(item.type) and item.type == "product":
            if not checkQuantity(item.quantity):
                return "Invalid order detected"
            else:
                productSum += processProducts(item)
        else:
            return 'Invalid item type: %s' % item.type

    net = (0.0 - productSum) + paymentSum
    if productSum >= 99999 or paymentSum >=99999:
        return "Total amount payable for an order exceeded"
    elif abs((0.0 - productSum) + paymentSum) <= 0.1:     
        return "Order ID: %s - Full payment received!" % order.id           
    elif abs(productSum) < abs(paymentSum):
        return "Total amount payable for an order exceeded"
    else:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    
                

def itemCheck(i):
    item_types = ["payment","product"]
    if i not in item_types :
        return False
    else:
        return True

def textCheck(i):
    text = re.findall("[a-zA-Z]",str(i))
    if len(text) > 0:
        return False
    else:
        try:
            new_f = float(i)
            print (new_f)
            return True
        except ValueError:
            return False
                        
def checkQuantity(i):
    try:
        whole_q = int(i)
        print("The quantity is valid ",whole_q)
        return True
    except ValueError:
        return False

def processPayments(i):
    paymentSum = 0.0
    if textCheck(i.amount):
        paymentSum += i.amount
    else:
        paymentSum += 0
    return paymentSum


def processProducts(i):
    productSum = 0.0
    if textCheck(i.amount) and checkQuantity(i.quantity):
        productSum = float(productSum + (i.amount * i.quantity))
    else:
        productSum = float(productSum + 0)
    return productSum
from csv import reader
from collections import namedtuple
saleRecord = namedtuple('saleRecord','shopId saleDate totalSales totalCustomers')
fileHandle = open("salesRecord.csv","r")
overAllSales = 0
csvFieldsList=reader(fileHandle)
for fieldsList in csvFieldsList:
    shopRec = saleRecord._make(fieldsList)
    print shopRec
    overAllSales += int(shopRec.totalSales)
print("Total Sales of The Retail Chain =",overAllSales)

from bs4 import BeautifulSoup
from decimal import Decimal
import re

def convert(amount, cur_from, cur_to, date, requests):
    response = requests.get(f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={date}') # Использовать переданный requests
    base = BeautifulSoup(response.content, "xml")
    curs2 = float(re.sub(r'(\d+),(\d+)',r'\1.\2', base.find('CharCode', text=cur_to).find_next_sibling('Value').string))/float(re.sub(r'(\d+),(\d+)',r'\1.\2', base.find('CharCode', text=cur_to).find_next_sibling('Nominal').string))
    res = Decimal('3754.8057')
    result = (amount/Decimal(curs2)).quantize(res)
    return result 


'''
    for valute in base.ValCurs:
        if valute.CharCode.next==cur_to:
            curs2 = float(re.sub(r'(\d+),(\d+)',r'\1.\2', valute.Value.next))/float(re.sub(r'(\d+),(\d+)',r'\1.\2', valute.Nominal.next))
    res = Decimal('3754.8057')
    result = (amount/Decimal(curs2)).quantize(res)
'''
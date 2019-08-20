import xlrd
from xlutils.copy import copy
import cgi
import requests
from requests import get

save_dir = "./picture/black"

def download(url, i):
    r = requests.get(url, allow_redirects=True)
    open('./picture/black/'+str(i)+'.jpg', 'wb').write(r.content)


# openc excel
wb = xlrd.open_workbook('pillInformation.xlsx')

sheet = wb.sheet_by_index(0)
keyword = sheet.cell(0, 5).value

for i in range(73, 76):
    name = sheet.cell(i, 1).value
    url = sheet.cell(i, 5).value
    print(name)

    # print(type(url))
    download(url, i)



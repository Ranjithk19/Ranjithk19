from xlrd import open_workbook

# Reading locators
def read_locators(pagename):
    wb = open_workbook(r"C:\Users\user\Desktop\python files\files\objects.xls")
    ws = wb.sheet_by_name(pagename)
    used_rows = ws.nrows
    locators = { }
    for i in range(1, used_rows):
        data = ws.row_values(i)
        locators[data[0]] = (data[1], data[2])
    return locators
r=read_locators("loginpage")

print(r)


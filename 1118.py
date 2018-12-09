import xlrd
excel=xlrd.open_workbook("TestCase.xlsx")
print(excel)
# excel.sheet_by_name("sheet1")
# print(excel.sheet_by_name("sheet1"))
# table=excel.sheet_by_index(0)

# rowValues=table.row_values(0)
# for i in table.rowValues:
#     print(i)



table=excel.sheet_by_index(0)
Nrow=table.nrows
for i in range(Nrow):
    print(table.row_values(i))
    for a in table.row_values(i):
        print(a)
    print(table.cell_values(1,2))



from types import NoneType
import openpyxl , modo_1 , modo_2

openfile = openpyxl.load_workbook('ejemplos_rutas.xlsx')

list1 , list2 = [],[]

sheet = openfile.get_sheet_by_name('Modo 1')
data = sheet['A1':'E5']
for row in data:
    for cell in row:
        if cell.value == None:
            list1.append(0)
        else:
            list1.append(cell.value)

sheet = openfile.get_sheet_by_name('Modo 2')
data = sheet['A1':'E5']
for row in data:
    for cell in row:
        if cell.value == None:
            list2.append(2)
        else:
            list2.append(cell.value)




print('Datos modo 1 \n\n ',list1,'\n')
print('CASILLA INICIO     ', modo_1.start(list1), '\n')
#modo_1.color(list1)
#modo_1.direccion(list1)


modo_1.move(list1,1)


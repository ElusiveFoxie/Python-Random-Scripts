tableData2 = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

'''
  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
'''

def TablePrinter(tableData):

    colWidths = [0] * len(tableData)

    for k in range (len(colWidths)):
        for i in range(len(tableData[k])):
            if(colWidths[k] < (len(tableData[k][i]))):
                colWidths[k] = (len(tableData[k][i]))

    for k in range(len(tableData[0])):
        for i in range(len(tableData)):
            print(tableData[i][k].rjust(colWidths[i]," "), end=" ")
        print()


TablePrinter(tableData2)



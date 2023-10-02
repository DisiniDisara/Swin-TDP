import networkx as nx
import matplotlib.pyplot as plt
import xlrd

file = "sample.xlsx"

G = nx.Graph()
names = []

book = xlrd.open_workbook(file)
sheet = book.sheet_by_index(4)

for row in range(sheet.nrows):
    data = sheet.row_slice(row)
    person1 = data[0].value
    person2 = data[1].value
    names.append((person1, person2))

G.add_edges_from(names)
pos = nx.spring_layout(G, k=0.30, iterations=40, scale=4)
nx.draw(G, pos, node_size=8)
plt.show()
plt.savefig('sample.png', dpi=500)
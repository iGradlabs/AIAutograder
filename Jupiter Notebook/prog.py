import pandas as pd
import nbformat #pip install nbformat
data = pd.read_csv("QA.csv")
#print(data)
file=nbformat.v4.new_notebook();
rows=data.shape[0]
for i in range(rows):
    file.cells.append(nbformat.v4.new_markdown_cell(data.Questions[i]))
    file.cells.append(nbformat.v4.new_code_cell(data.Answers[i]))
with open('new_notebook.ipynb', 'w') as output_file:
    nbformat.write(file, output_file)
from pathlib import Path

def body(gene):
    body1 = gene[gene.find('\n') + 1:]
    return body1

FILENAME = "U5.txt"
file_contents = Path(FILENAME).read_text()
print(body(file_contents))
from pathlib import Path

def info(gene):
    info1 = gene[:gene.find('\n') + 1]
    return info1

FILENAME = "RNU6_269P.txt"
file_contents = Path(FILENAME).read_text()
print(info(file_contents))
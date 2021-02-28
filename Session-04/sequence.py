from pathlib import Path

def config(gene):
    body = gene[gene.find('\n') + 1:]
    full_body = body.replace('\n', '')
    return full_body

def count(gene):
    body = config(gene)
    final_count = len(body)
    return final_count

FILENAME = "ADA.txt"
file_contents = Path(FILENAME).read_text()
print(count(file_contents))
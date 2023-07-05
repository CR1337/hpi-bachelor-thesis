import os

MERMAID_PATH: str = "/home/cr/Desktop/ba-cr/images/mermaid"
ARCH_PATH: str = os.path.join(MERMAID_PATH, "architecture")


def make_pdfs(path: str):
    for filename in os.listdir(path):
        if not filename.endswith(".txt"):
            continue
        pdf_filename = ".".join(filename.split(".")[:-1]) + ".pdf"
        status_code = os.system(f"mmdc -i {os.path.join(path, filename)} -o {os.path.join(path, pdf_filename)} -f")
        print(status_code, filename)


make_pdfs(MERMAID_PATH)
make_pdfs(ARCH_PATH)

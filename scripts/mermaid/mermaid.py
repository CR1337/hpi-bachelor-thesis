import json
import os

MERMAID_PATH: str = "/home/cr/Desktop/ba-cr/images/mermaid"
ARCH_PATH: str = os.path.join(MERMAID_PATH, "architecture")


def make_pdfs(path: str):
    for filename in os.listdir(path):
        if not filename.endswith(".txt"):
            continue
        pdf_filename = ".".join(filename.split(".")[:-1]) + ".pdf"
        cfg_filename = ".".join(filename.split(".")[:-1]) + ".json"
        status_code = os.system(
            f"mmdc -f -i {os.path.join(path, filename)} "
            f"-o {os.path.join(path, pdf_filename)} "
            f"-c {os.path.join(path, cfg_filename)}"
        )
        print(status_code, filename)


DEFAULT_CONFIG: dict = {
  "theme": "base",
  "themeVariables": {
    "primaryColor": "#ffffff",
    "primaryTextColor": "#000000",
    "primaryBorderColor": "#000000",
    "lineColor": "#000000"
  }
}


def make_configs(path: str):
    for filename in os.listdir(path):
        if not filename.endswith(".txt"):
            continue
        cfg_filename = ".".join(filename.split(".")[:-1]) + ".json"
        with open(os.path.join(path, cfg_filename), 'w') as file:
            json.dump(DEFAULT_CONFIG, file)
        print(filename)


def update_seq_configs(path: str):
    for filename in os.listdir(path):
        if not filename.endswith(".json"):
            continue
        with open(os.path.join(path, filename), 'r') as file:
            config = json.load(file)
        config['themeVariables']['secondaryColor'] = "#aaaaaa"
        with open(os.path.join(path, filename), 'w') as file:
            json.dump(config, file)


MODE = 'pdf'
# MODE = 'cfg'
# MODE = 'ucfg'

if MODE == 'cfg':
    make_configs(MERMAID_PATH)
    make_configs(ARCH_PATH)
elif MODE == 'pdf':
    make_pdfs(MERMAID_PATH)
    make_pdfs(ARCH_PATH)
elif MODE == 'ucfg':
    update_seq_configs(MERMAID_PATH)
    update_seq_configs(ARCH_PATH)

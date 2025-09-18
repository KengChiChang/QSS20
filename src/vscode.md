---
title: "Setup IDE (VS Code)"
# nav_order: 106
extra_javascript: ["assets/mermaid-10.8.0.min.js"]
---


## Install VS Code

* **macOS:** Download “Apple Silicon” (M-series) or “Intel” build from [here](https://code.visualstudio.com/) and install.
* **Windows:** Download the Windows installer from [here](https://code.visualstudio.com/) and install (accept defaults).

> Tip: After installing, open VS Code once so it registers shell commands.


## Install Extensions for Python

Open VS Code → Extensions (⇧⌘X / Ctrl+Shift+X) and install:

* **Python** (Microsoft)
* **Jupyter** (Microsoft)
* (Optional but nice) **Pylance** (Microsoft) for fast IntelliSense

You can also install via command line:

```bash
code --install-extension ms-python.python
code --install-extension ms-toolsai.jupyter
code --install-extension ms-python.vscode-pylance
```


## Tell VS Code which interpreter to use

* Open your project folder in VS Code (**File → Open Folder**).
* Press **⌘⇧P / Ctrl+Shift+P** → **Python: Select Interpreter**.
* Choose the interpreter from your conda env like `~/miniforge3/bin/python`).

If you don’t see it, ensure the env is created and activated once in a terminal, then retry **Select Interpreter**.


## Jupyter notebooks in VS Code

* Create a new file `analysis.ipynb` (File → New File → Jupyter Notebook).
* At the top right, choose the **Kernel** → pick your conda environment (`~/miniforge3/bin/python`).
* Try a cell:

  ```python
  import sys
  print(sys.version)
  ```

If VS Code asks to install **ipykernel**, accept or install manually:

```bash
pip install ipykernel
python -m ipykernel install --user --name myproject --display-name "Python (myproject)"
```

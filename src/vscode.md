---
title: "Setup IDE (VS Code)"
nav_order: 106
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
* Choose the interpreter from your conda environment like `qss20`).

If you don’t see it, ensure the env is created and activated once in a terminal, then retry **Select Interpreter**.


## Jupyter notebooks in VS Code

* Create a new file `analysis.ipynb` (File → New File → Jupyter Notebook).
* At the top right, choose the **Kernel** → pick "Python Environments" → pick your conda environment (`qss20`).
* Try a cell:

  ```python
  import sys
  print(sys.version)
  ```

If VS Code asks to install **ipykernel**, run the following in the terminal:

```bash
conda activate qss20
conda install jupyterlab notebook ipykernel
```

Then restart VS Code and retry.

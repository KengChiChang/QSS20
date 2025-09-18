---
title: "Setting up Python and conda"
nav_order: 105
extra_javascript: ["assets/mermaid-10.8.0.min.js"]
---


This guide will walk you through setting up a professional Python environment for data science on your personal computer.

## Why Bother with a Local Setup?

While cloud platforms and virtual machines are convenient, learning to manage your own data science environment is a crucial skill. It empowers you to work independently and troubleshoot problems, which is a significant part of a data scientist's daily life. Think of the time you spend on this as an investment in your data science education! 🧑‍💻

-----

## What We'll Be Setting Up

We'll be installing a suite of essential tools:

* **Python and the `conda` package manager**: The foundation of our data science toolkit.
* **VS Code**: A powerful and popular code editor that integrates well with Git, Python, R, and more.
* **An Augmented Command Line**: As a data scientist, you’ll spend a lot of time working in the command line. Instead of sticking with the bare-bones defaults provided by your operating system, it’s worth upgrading to a more capable terminal. This not only improves your efficiency but also helps you understand how the command line works—a critical skill for debugging and troubleshooting.

We'll tackle these one at a time, starting with Python!


-----

## Installing Python with Miniforge

The first step in setting up your machine for this course is to install both Python and a package manager. Unlike `R`—where you can simply run `install.packages()`—Python does not include a built-in package management system. To work with common tools like NumPy, Pandas, or Matplotlib, we need an external manager. In this course, we’ll use `conda` as the default package manager for Python.

### Why `conda` Instead of `pip`?

Python has two major package managers: `pip` and `conda`.  `pip` is popular among software engineers and works well for Python-only libraries.  `conda`, however, is better for data science because it can handle large dependencies and non-Python packages (such as compiled C libraries used by NumPy).

Importantly, installing `conda` also gives you access to `pip`, so you can use either depending on the situation.

### Why Miniforge?

To install `conda`, there are three common options:

1. Anaconda
2. Miniconda
3. Miniforge

After some experience with all three, I **strongly** recommend Miniforge. Here’s why:

* Anaconda comes with Python, conda, and dozens of preinstalled packages. While that sounds convenient, it often causes dependency conflicts once you start adding your own packages.
* Miniforge is a lighter install—it only includes Python and core utilities like conda and pip—so you start clean and avoid many conflicts.
* Unlike Miniconda, Miniforge defaults to the conda-forge channel, a community-maintained package repository that is usually the most reliable source for up-to-date libraries.

If you already have a `conda` installation (from Anaconda or Miniconda), you are not actively using right now, it might be a good idea to delete it and start fresh. It's good practice not to be too attached to your Python installations; sometimes, a clean slate is the easiest way to resolve issues.

#### An Important Note on `pyenv`

Miniforge is a **substitute** for tools like `pyenv` or `venv`. **Do not install both.** Miniforge's `conda` can do everything `pyenv` can and more, including managing multiple environments.

-----

## Installation Steps

1. **Go to the [Miniforge download page](https://conda-forge.org/download/).**
2. **Click the link for your operating system.** This will download an installer file.

### For macOS Users

1. Move the downloaded `.sh` file to your desktop.
2. Open the **Terminal** application (you can find it in `Applications > Utilities`).
3. In the Terminal, type `cd ~/desktop` and press **Enter**.
4. Type `bash` followed by the name of the downloaded file (e.g., `bash Miniforge3-MacOSX-arm64.sh`) and press **Enter**.
5. When asked to review the license agreement, press **Enter**. Then, type `q` to exit the text viewer.
6. Type `yes` and press **Enter** to accept the license agreement.
7. Press **Enter** to accept the default installation location.
8. **IMPORTANT**: At the end of the installation, you'll be asked, `Do you wish to update your shell profile to automatically initialize conda?`. You **must** type `yes` and press **Enter**.

### For Windows Users

1. Run the downloaded `.exe` file.
2. When asked who to install for, select **"Just for me (recommended)"**.
3. Accept the default installation location.
4. You'll see a few checkboxes. Make sure to check the following:
      * **Add Miniforge3 to my PATH environment variable** (even though it says it's not recommended).
      * **Register Miniforge3 as my default Python 3.12**.
      * It's also a good idea to check the box to remove the cache.


That's it! You have installed `conda` and Python

---

## Confirm conda is installed

### macOS / Linux (Terminal)

```bash
conda --version
python --version
which conda
conda info
```

### Windows (PowerShell or CMD)

```bat
conda --version
python --version
where conda
conda info
```

You should see conda and python versions (no “command not found” / “not recognized” errors).


## Set up default channel (recommended)

```bash
# Make conda-forge highest priority
conda config --prepend channels conda-forge

# Enforce channel priority (prefer conda-forge builds when available)
conda config --set channel_priority strict
```

Verify:

```bash
conda config --show channels
conda config --show channel_priority
```

You should see:

```
channels:
  - conda-forge
  - defaults
channel_priority: strict
```


## Create a clean course environment (recommended)

### All platforms

```bash
conda create -n qss20 python=3.12
conda activate qss20
```

Verify you’re in it:

```bash
conda env list
# Look for a "*" next to qss20
```


Check all packages that are currently installed in the environment:

```bash
conda list
# Look for a "*" next to qss20
```

## Install JupyterLab

### Prefer conda first

```bash
conda install jupyterlab notebook ipykernel
```

Confirm:

```bash
jupyter lab --version
jupyter --version
```

### Register the environment as a kernel (so editors can pick it)

```bash
python -m ipykernel install --user --name qss20 --display-name "Python (QSS20)"
```

List kernels to confirm:

```bash
jupyter kernelspec list
```

You should see `qss20`.


## Install common data science packages

Inside the `qss20` env:

```bash
conda install pandas numpy matplotlib seaborn plotly
```

Then run:

```bash
python -c "import numpy, pandas; print(numpy.__version__); print(pandas.__version__)"
```

## Launch JupyterLab

### Standard launch

```bash
jupyter lab
```

JupyterLab should open in your browser (or print a local URL like `http://localhost:8888/lab` you can click).

**Stop JupyterLab:** go back to the terminal where it’s running and press `Ctrl+C` (twice if needed), then confirm `y` if prompted.


### Use in VS Code (alternative workflow)

1. Install VS Code extensions: **Python** and **Jupyter**.
2. Open or create a `.ipynb` notebook.
3. Click the kernel picker (top right) → choose **Python (qss20)**.
4. Run a cell (e.g., `print("hello")`).

---


## Common “it’s not working” fixes

* **`jupyter` not found:** `conda activate qss20` then reinstall `jupyterlab` in the `qss20` environment.
* **Wrong env active:** `conda info --envs`, then `conda activate qss20`.
* **Multiple Python installs causing confusion:** check path order:
      - macOS/Linux: `which python` and `which jupyter`
      - Windows: `where python` and `where jupyter`
* **Kernel not showing in Jupyter/VS Code:** re-run the kernel registration step and then restart Jupyter/VS Code.


That’s it—if they can print versions, see the `qss20` kernel, and open JupyterLab, the install was successful.

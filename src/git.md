---
title: "Install Git"
nav_order: 107
extra_javascript: ["assets/mermaid-10.8.0.min.js"]
---


This guide shows how to verify whether Git is installed and how to install it from the command line on both macOS and Windows. It also covers basic post-install setup and common troubleshooting.


## Check if Git is installed

Open a terminal (macOS: Terminal/iTerm/Ghostty; Windows: PowerShell/Windows Terminal) and run:

```bash
git --version
```

* If you see something like `git version 2.xx.x`, Git is installed.
* If you get “command not found” (macOS) or “‘git’ is not recognized…” (Windows), install Git using the steps below.


## macOS

### Option A: Install via Apple Command Line Tools (simple, system-wide)

This is the easiest way on a clean Mac.

```bash
xcode-select --install
```

* A dialog appears; accept and finish the install.
* Then verify:

```bash
git --version
```

**Notes**

* This installs Apple’s “Command Line Tools,” which include Git and other developer utilities.
* Versions may lag behind Homebrew’s packages.

### Option B: Install via Homebrew (recommended for newer Git)

If you already use Homebrew (or want the latest Git), do:

1. Ensure Homebrew is installed (skip if you have it):

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Install Git:

```bash
brew install git
```

3. Verify:

```bash
git --version
```

**Tip (Apple Silicon paths):** Homebrew typically installs under `/opt/homebrew`. Ensure your shell init file includes Homebrew in `PATH`:

```bash
# zsh example (~/.zshrc)
eval "$(/opt/homebrew/bin/brew shellenv)"
```

---

## Windows

### Option A: Git for Windows Installer

Open **PowerShell as Administrator**:

Download and run the official [Git for Windows](https://git-for-windows.github.io/) installer.
This provides Git Bash, a Bash shell with Unix-like tools, and installs Git in a conventional location.

When prompted during installation:

* **PATH**: Choose “Git from the command line and also from 3rd-party software.”
* **Credential Manager**: Keep enabled (helps with GitHub/GitLab/Azure login).
* **Line endings**: Choose “Checkout Windows-style, commit Unix-style”.
* **Editor**: Pick VS Code (if installed) or another editor of your choice.
* **Console**:
  * Use Windows default console if you’ll mostly use PowerShell/Windows Terminal.
  * Use MinTTY if you’ll primarily use Git Bash.

By default Git installs under:

```makefile
C:\Program Files\Git
```

Verify after installation:

```powershell
git --version
```

This is the most straightforward method for beginners, and works well with RStudio, VS Code, and other developer tools.


### Option B: winget (built into recent Windows 10/11)

Open **PowerShell** as a normal user:

```powershell
winget install --id Git.Git -e --source winget
```

After installation, restart your terminal and verify:

```powershell
git --version
```


---

## Post-Install: Minimal Git Setup

Set your identity (shown in commit history):

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Recommended defaults:

```bash
# Use 'main' for new repos
git config --global init.defaultBranch main
# Fetches remote changes and re-applies your local commits on top of them
git config --global pull.rebase true
# Make Git show colors
git config --global color.ui auto
# Safer line endings across platforms (Windows users especially)
git config --global core.autocrlf input   # macOS/Linux
# git config --global core.autocrlf true  # Windows (alternative)
```

View your configuration:

```bash
git config --list
```


## Troubleshooting

**“git: command not found” or “‘git’ is not recognized”**

* Close and reopen your terminal after installation.
* Confirm Git is on your `PATH`.

**Check PATH (macOS):**

```bash
echo $PATH
which git
```

**Check PATH (Windows PowerShell):**

```powershell
$env:Path -split ';'
where git
```

If `which git` (macOS) or `where git` (Windows) shows a path, Git is available.

**Multiple Git versions**

* On macOS you might have both Xcode CLT Git and Homebrew Git. Ensure Homebrew’s path precedes others in your shell init file:

  ```bash
  # ~/.zshrc example
  eval "$(/opt/homebrew/bin/brew shellenv)"
  ```

  Re-check with `which git`.


## 6) Quick Sanity Test

```bash
mkdir ~/git-test && cd ~/git-test
git init
echo "hello" > readme.txt
git add readme.txt
git commit -m "test commit"
git log --oneline
```

If you see a commit in `git log`, your Git is working.

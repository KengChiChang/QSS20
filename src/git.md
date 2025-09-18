---
title: "Setting up Git and GitHub"
nav_order: 106
extra_javascript: ["assets/mermaid-10.8.0.min.js"]
---

## macOS (with Homebrew)

Open the Terminal apps such as `iterm2`, `Ghostty`, or `Terminal`, then run:

```bash
# install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# install git
brew install git

git --version
```

## Windows (in Windows Terminal)

Open **Windows Terminal** (PowerShell profile is fine), then choose one of these:

**A) winget (built-in on modern Windows)**

```powershell
winget install --id Git.Git -e
git --version
```

**B) Chocolatey**

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12
iwr https://community.chocolatey.org/install.ps1 -UseBasicParsing | iex
choco install git -y
git --version
```

**C) Scoop (user-space, no admin)**

```powershell
iwr -useb get.scoop.sh | iex
scoop install git
git --version
```


## One-time Git setup (do this on every machine)

Set your identity and defaults:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

Line endings (prevents Windows/mac newline headaches):

* macOS/Linux:

  ```bash
  git config --global core.autocrlf input
  ```
* Windows:

  ```powershell
  git config --global core.autocrlf true
  ```

Optional but useful:

```bash
git config --global pull.rebase false
git config --global color.ui auto
```

---

## (Optional) Set up SSH keys for GitHub/GitLab

Generate a key:

```bash
ssh-keygen -t ed25519 -C "you@example.com"
# press Enter to accept defaults and set a passphrase if you want
```

Start the agent and add your key:

* macOS:

  ```bash
  eval "$(ssh-agent -s)"
  ssh-add ~/.ssh/id_ed25519
  ```

* Windows PowerShell (Git Bash also works):

  ```powershell
  eval "$(ssh-agent -s)"
  ssh-add ~/.ssh/id_ed25519
  ```

Copy the public key to your clipboard and add it to your Git hosting account:

```bash
cat ~/.ssh/id_ed25519.pub
```

---

## Quick test

```bash
git clone https://github.com/KengChiChang/QSS20_FA25.git
cd QSS20_FA25
git log -1
```

---

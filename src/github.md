---
title: "Authenticate GitHub"
nav_order: 108
extra_javascript: ["assets/mermaid-10.8.0.min.js"]
---

Setting up authentication so that you can securely connect your local computer to GitHub. GitHub no longer allows simple password logins for Git operations, so you must use one of the supported methods: signing in through GitHub Desktop (which manages tokens behind the scenes), using HTTPS with a personal access token, or using SSH keys. Each option provides a secure way to prove your identity to GitHub and enables you to push, pull, and collaborate on code without constantly re-entering credentials.

This guide covers three supported methods. Pick one per machine:

1. **GitHub Desktop (easiest, no keys/tokens to manage)**
2. **HTTPS + Personal Access Token (PAT) (simple, CLI-friendly)**
3. **SSH keys (best for long-term CLI + automation)**

---

## GitHub Desktop (easiest for beginners)

**When to use:** Beginner-friendly GUI workflow; fast setup for class.

**What it does:** Signs in through the browser and stores credentials securely. Git operations use HTTPS behind the scenes.

### Steps

1. Install **GitHub Desktop**: [https://desktop.github.com](https://desktop.github.com)
2. Open the app → **Sign in to GitHub.com** → authorize in the browser.
3. **File → Clone repository** (or **Repository → New**).
4. Make commits in Desktop, then **Push origin**.

### Verify

* After pushing, open the repo on GitHub.com and confirm your commit exists.

### Notes

* Works great alongside editors like VS Code.
* If you later use the CLI in the same repo, it typically reuses the stored HTTPS credentials (via the system keychain / Git Credential Manager).

---

## HTTPS + Personal Access Token

**When to use:** You want to use the command line without SSH keys.

**What it does:** Uses HTTPS for Git operations; Git stores your token via a credential helper (system keychain on macOS, **Git Credential Manager** on Windows).

### Steps

1. **Create a Personal Access Token** on GitHub

   * Go to **GitHub → Settings → Developer settings → Personal access tokens**
   * Prefer **Fine-grained tokens** (scope only the repos you need)
   * For classic tokens, the minimal scope for private repos is usually `repo`.
2. Make sure your repo remote uses **HTTPS**:

   ```bash
   git remote -v
   # If needed:
   git remote set-url origin https://github.com/USERNAME/REPO.git
   ```
3. On first `git push`/`git pull`, Git will prompt:

   * **Username:** your GitHub username
   * **Password:** paste the **PAT** (not your GitHub password)
4. Git will cache the token via a credential helper:

   * macOS: `git config --global credential.helper osxkeychain`
   * Windows: `git config --global credential.helper manager`
   * Linux (GCM optional): `git config --global credential.helper store` (plain-text) or install GCM.

### Verify

```bash
git push
```

No further prompts = token is cached correctly.


---

## SSH Keys (recommended for long-term)

**When to use:** Heavier CLI use, scripting, multiple repos; avoids PAT prompts.

**What it does:** Uses public-key cryptography (no passwords). You add your **public key** to GitHub; your **private key** stays on your machine.

### Steps

1. **Check for existing keys**:

   ```bash
   ls -al ~/.ssh
   # Look for id_ed25519 and id_ed25519.pub (preferred) or id_rsa / id_rsa.pub
   ```
2. **Generate a new key** (use Ed25519):

   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   # Press Enter to accept default path; add a passphrase for security
   ```
3. **Start and load into ssh-agent**

   * macOS / Linux:

     ```bash
     eval "$(ssh-agent -s)"
     ssh-add ~/.ssh/id_ed25519
     ```
   * Windows (Git Bash / PowerShell, OpenSSH Agent running):

     ```bash
     eval "$(ssh-agent -s)"
     ssh-add ~/.ssh/id_ed25519
     ```
4. **Add the public key to GitHub**

   ```bash
   pbcopy < ~/.ssh/id_ed25519.pub   # macOS
   # or: clip < ~/.ssh/id_ed25519.pub  # Windows (PowerShell)
   # or: cat ~/.ssh/id_ed25519.pub | xclip -selection clipboard  # Linux
   ```

   * GitHub → **Settings → SSH and GPG keys → New SSH key** → paste.
5. **Switch the repo remote to SSH**:

   ```bash
   git remote set-url origin git@github.com:USERNAME/REPO.git
   ```
6. **Test the connection**:

   ```bash
   ssh -T git@github.com
   # Expect: "Hi USERNAME! You've successfully authenticated..."
   ```

### Verify

```bash
git push
```

No username/password prompts = SSH is working.

---

## Choosing and Switching Methods

* **One method per machine** is usually enough.
* **Switch HTTPS ↔ SSH** by changing the remote:

  ```bash
  # To HTTPS:
  git remote set-url origin https://github.com/USERNAME/REPO.git

  # To SSH:
  git remote set-url origin git@github.com:USERNAME/REPO.git
  ```

---

## Quick Pros & Cons

| Method                 | Pros                                               | Cons                                         |
| ---------------------- | -------------------------------------------------- | -------------------------------------------- |
| GitHub Desktop (HTTPS) | Fastest start; no keys/tokens; GUI workflow        | Less scriptable; relies on Desktop           |
| HTTPS + PAT            | Simple on CLI; easy rotation                       | Token prompts (first time); token management |
| SSH Keys               | Smooth CLI; great for automation; no token prompts | Setup effort; key management and passphrases |

---

## Common Troubleshooting

* **“Support for password authentication was removed”** You tried HTTPS with your GitHub password. Use **PAT** instead (or switch to SSH).

* **Permission denied (publickey)** SSH key not added to agent or GitHub.
    1. Run `ssh-add -l` to list loaded keys
    2. Add public key to GitHub; ensure remote is SSH.

* **Wrong remote URL** Check with `git remote -v`. If it’s `git@github.com:…` you’re on SSH; if it’s `https://github.com/…` you’re on HTTPS.

* **Multiple GitHub accounts** For SSH, use per-host blocks in `~/.ssh/config`:

    ```sshconfig
    Host github.com-yourwork
      HostName github.com
      User git
      IdentityFile ~/.ssh/id_ed25519_work
    ```

    Then set remote to `git@github.com-yourwork:ORG/REPO.git`.


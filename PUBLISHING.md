# Publishing Guide - MCP M365 Management

This guide provides complete instructions for publishing your MCP M365 Management server to GitHub and PyPI (Python Package Index).

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Prepare for Publishing](#prepare-for-publishing)
3. [Publish to GitHub](#publish-to-github)
4. [Publish to PyPI](#publish-to-pypi)
5. [Post-Publishing](#post-publishing)
6. [Updating Versions](#updating-versions)

---

## 🔧 Prerequisites

### Required Accounts

- [ ] **GitHub Account** - Sign up at https://github.com
- [ ] **PyPI Account** - Sign up at https://pypi.org/account/register/

### Required Tools

```bash
# Install publishing tools
pip install build twine

# Verify installation
python -m build --version
twine --version
```

### GitHub Setup

```bash
# Install Git (if not installed)
git --version

# Configure Git
git config --global user.name "Thiago Beier"
git config --global user.email "thiago.beier@gmail.com"
```

---

## 📦 Prepare for Publishing

### Step 1: Review Package Files

Ensure these files exist in your project:

```
mcp-m365-mgmt/
├── pyproject.toml      ✅ Created
├── setup.py            ✅ Created
├── MANIFEST.in         ✅ Created
├── LICENSE             ✅ Created
├── README.md           ✅ Exists
├── CHANGELOG.md        ✅ Exists
├── requirements.txt    ✅ Exists
├── .gitignore          ✅ Exists
└── entra_server.py     ✅ Exists
```

### Step 2: Test Local Build

```bash
# Navigate to project directory
cd C:\temp\mcp\mcp365\mcp-entra-server

# Build the package
python -m build

# Expected output:
# Successfully built mcp-m365-mgmt-1.0.0.tar.gz
# Successfully built mcp_m365_mgmt-1.0.0-py3-none-any.whl
```

✅ **Verify**: Check `dist/` folder contains:

- `mcp-m365-mgmt-1.0.0.tar.gz` (source distribution)
- `mcp_m365_mgmt-1.0.0-py3-none-any.whl` (wheel distribution)

### Step 3: Test Local Installation

```bash
# Create test environment
python -m venv test-env
.\test-env\Scripts\Activate.ps1

# Install from local build
pip install dist/mcp_m365_mgmt-1.0.0-py3-none-any.whl

# Test the installation
m365-mgmt --help

# Cleanup
deactivate
Remove-Item -Recurse -Force test-env
```

---

## 🐙 Publish to GitHub

### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. **Owner:** Select `thiagogbeier`
3. **Repository name:** `mcp-m365-mgmt`
4. **Description:** "MCP server for Microsoft 365 and Intune management with 32 tools"
5. **Visibility:** Choose **Public** (for PyPI) or **Private**
6. ❌ **Do NOT** initialize with README, .gitignore, or license (we have them)
7. Click **Create repository**

### Step 2: Initialize Local Git Repository

```bash
# Navigate to project
cd C:\temp\mcp\mcp365\mcp-entra-server

# Initialize Git
git init

# Add all files
git add .

# Check what will be committed (should NOT include .env)
git status

# Commit
git commit -m "Initial commit: MCP Entra Server v1.0.0 with 32 tools"
```

### Step 3: Push to GitHub

```bash
# Add GitHub remote
git remote add origin https://github.com/thiagogbeier/mcp-m365-mgmt.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

### Step 4: Create GitHub Release (Optional but Recommended)

1. Go to your repository: `https://github.com/thiagogbeier/mcp-m365-mgmt`
2. Click **Releases** → **Create a new release**
3. **Tag version:** `v1.0.0`
4. **Release title:** `v1.0.0 - Initial Release`
5. **Description:** Copy content from `CHANGELOG.md`
6. ✅ Check **Set as the latest release**
7. Click **Publish release**

### Step 5: Verify GitHub Repository

- [ ] README.md displays correctly
- [ ] LICENSE file is recognized
- [ ] `.env` file is NOT visible (check .gitignore worked)
- [ ] All documentation files are present

---

## 🐍 Publish to PyPI

### Step 1: Create PyPI API Token

1. Log in to https://pypi.org
2. Go to **Account Settings** → **API tokens**
3. Click **Add API token**
   - **Token name:** `mcp-m365-mgmt-upload`
   - **Scope:** Select **Entire account** (for first upload)
4. Click **Create token**
5. **⚠️ COPY THE TOKEN NOW** - it won't be shown again!

**Save token to file** (for future use):

```bash
# Create .pypirc file in your home directory
notepad ~\.pypirc
```

Add this content (replace `pypi-xxx` with your token):

```ini
[pypi]
username = __token__
password = pypi-AgEIcHlwaS5vcmcCJDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Save and close.

### Step 2: Upload to TestPyPI (Recommended First)

**Test your package on TestPyPI first** before publishing to real PyPI:

```bash
# Create TestPyPI account: https://test.pypi.org/account/register/

# Upload to TestPyPI
python -m twine upload --repository testpypi dist/*

# Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ mcp-m365-mgmt
```

### Step 3: Upload to PyPI (Production)

```bash
# Upload to PyPI
python -m twine upload dist/*

# Enter credentials:
# username: __token__
# password: [paste your PyPI token]
```

**Expected output:**

```
Uploading distributions to https://upload.pypi.org/legacy/
Uploading mcp_m365_mgmt-1.0.0-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 50.0/50.0 kB
Uploading mcp-m365-mgmt-1.0.0.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 45.0/45.0 kB

View at:
https://pypi.org/project/mcp-m365-mgmt/1.0.0/
```

### Step 4: Verify PyPI Upload

1. Go to https://pypi.org/project/mcp-m365-mgmt/
2. Verify:
   - [ ] Package description shows README content
   - [ ] Version is correct (1.0.0)
   - [ ] License shows MIT
   - [ ] GitHub link works
   - [ ] Installation command shown: `pip install mcp-m365-mgmt`

### Step 5: Test Installation from PyPI

```bash
# Create fresh test environment
python -m venv pypi-test
.\pypi-test\Scripts\Activate.ps1

# Install from PyPI (wait 5 minutes after upload for indexing)
pip install mcp-m365-mgmt

# Verify installation
pip show mcp-m365-mgmt
m365-mgmt --help

# Cleanup
deactivate
Remove-Item -Recurse -Force pypi-test
```

---

## 🎉 Post-Publishing

### Update Documentation

Add installation instructions to README.md:

````markdown
## Installation

### From PyPI (Recommended)

```bash
pip install mcp-m365-mgmt
```
````

### From GitHub

```bash
pip install git+https://github.com/thiagogbeier/mcp-m365-mgmt.git
```

### From Source

```bash
git clone https://github.com/thiagogbeier/mcp-m365-mgmt.git
cd mcp-m365-mgmt
pip install -e .
```

\```

### Add Badges to README

Add these badges at the top of README.md:

```markdown
# MCP M365 Management

[![PyPI version](https://badge.fury.io/py/mcp-m365-mgmt.svg)](https://badge.fury.io/py/mcp-m365-mgmt)
[![Python Version](https://img.shields.io/pypi/pyversions/mcp-m365-mgmt.svg)](https://pypi.org/project/mcp-m365-mgmt/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/mcp-m365-mgmt)](https://pepy.tech/project/mcp-m365-mgmt)
```

### Share Your Package

**PyPI Package:** https://pypi.org/project/mcp-m365-mgmt/  
**GitHub Repository:** https://github.com/thiagogbeier/mcp-m365-mgmt  
**Installation:** `pip install mcp-m365-mgmt`

**Share on:**

- LinkedIn
- Twitter/X
- Reddit (r/Python, r/sysadmin)
- Dev.to
- Company Slack/Teams

---

## 🔄 Updating Versions

### For Future Updates

**Step 1: Update Version Number**

Edit `pyproject.toml` and `setup.py`:

```toml
# pyproject.toml
version = "1.0.1"  # Increment version
```

```python
# setup.py
version="1.0.1",  # Increment version
```

**Version Numbering:**

- **1.0.0 → 1.0.1** - Bug fixes (patch)
- **1.0.1 → 1.1.0** - New features (minor)
- **1.1.0 → 2.0.0** - Breaking changes (major)

**Step 2: Update CHANGELOG.md**

```markdown
## [1.0.1] - 2025-11-XX

### Fixed

- Fixed issue with...

### Added

- Added new tool...
```

**Step 3: Commit Changes**

```bash
git add .
git commit -m "Release v1.0.1: Bug fixes and improvements"
git tag v1.0.1
git push origin main --tags
```

**Step 4: Rebuild and Republish**

```bash
# Clean old builds
Remove-Item -Recurse -Force dist\, build\, *.egg-info

# Build new version
python -m build

# Upload to PyPI
python -m twine upload dist/*
```

**Step 5: Create GitHub Release**

1. Go to GitHub → Releases → Create new release
2. Tag: `v1.0.1`
3. Title: `v1.0.1 - Bug Fixes`
4. Description: Copy from CHANGELOG.md
5. Publish

---

## 🔒 Security Notes

### Protect Your Credentials

- [ ] Never commit `.env` file (checked by .gitignore)
- [ ] Never commit PyPI tokens
- [ ] Store tokens in `~\.pypirc` with restricted permissions
- [ ] Use scoped tokens (project-specific) for PyPI after first upload

### Rotate PyPI Token

After first successful upload, create a **project-specific token**:

1. PyPI → Your project → Settings → API tokens
2. Create token scoped to **only** `mcp-m365-mgmt`
3. Update `~\.pypirc` with new token
4. Delete old account-wide token

---

## 📊 Monitor Your Package

### PyPI Stats

- **Package page:** https://pypi.org/project/mcp-m365-mgmt/
- **Download stats:** https://pepy.tech/project/mcp-m365-mgmt

### GitHub Stats

- **Repository:** https://github.com/thiagogbeier/mcp-m365-mgmt
- **Stars, forks, issues** visible on repo page

---

## ❓ Troubleshooting

### "Package already exists" Error

**Error:**

```
HTTPError: 400 Bad Request - File already exists
```

**Solution:**

- You cannot reupload the same version
- Increment version number in `pyproject.toml` and `setup.py`
- Rebuild: `python -m build`
- Upload again: `twine upload dist/*`

### "Invalid token" Error

**Solution:**

- Verify token starts with `pypi-`
- Copy token again from PyPI (no extra spaces)
- Update `~\.pypirc` file

### GitHub Push Rejected

**Error:**

```
error: failed to push some refs
```

**Solution:**

```bash
# Pull changes first
git pull origin main --rebase

# Then push
git push origin main
```

---

## ✅ Publishing Checklist

### Pre-Publishing

- [ ] All tests pass
- [ ] Documentation complete
- [ ] CHANGELOG.md updated
- [ ] Version number updated
- [ ] LICENSE file present
- [ ] .env not in repository

### GitHub Publishing

- [ ] Repository created
- [ ] Code pushed
- [ ] README displays correctly
- [ ] Release created
- [ ] Topics/tags added

### PyPI Publishing

- [ ] PyPI account created
- [ ] API token generated
- [ ] Package built (`python -m build`)
- [ ] Tested on TestPyPI
- [ ] Uploaded to PyPI
- [ ] Installation tested
- [ ] Package page looks correct

### Post-Publishing

- [ ] Badges added to README
- [ ] Installation instructions updated
- [ ] Announced on social media
- [ ] Documentation links verified
- [ ] Monitor for issues/feedback

---

## 🎊 Success!

Your package is now published and available to the world:

**Install with:**

```bash
pip install mcp-entra-server
```

**Congratulations on publishing your first Python package! 🚀**

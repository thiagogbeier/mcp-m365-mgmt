# MCP Entra Server - Complete Deployment Guide

This guide provides step-by-step instructions to deploy the MCP Entra Server in VS Code with Python.

---

## 📋 Prerequisites

Before you begin, ensure you have:

- [ ] **Python 3.8 or higher** installed on your system
- [ ] **VS Code** installed
- [ ] **Azure subscription** with Global Administrator or Application Administrator role
- [ ] **Microsoft 365/Intune licenses** in your tenant
- [ ] **Git** (optional, for cloning repository)

### Verify Python Installation

Open VS Code Terminal (View → Terminal or `` Ctrl+` ``) and run:

```bash
python --version
```

You should see Python 3.8 or higher. If not, download from [python.org](https://www.python.org/downloads/)

---

## 🔐 Step 1: Azure App Registration Setup

### 1.1 Create App Registration

1. **Open Azure Portal**

   - Navigate to [https://portal.azure.com](https://portal.azure.com)
   - Sign in with your admin account

2. **Go to App Registrations**

   - Search for "App registrations" in the top search bar
   - Click **App registrations**

3. **Create New Registration**

   - Click **+ New registration**
   - Enter name: `MCP Entra Server` (or your preferred name)
   - **Supported account types**: Select "Accounts in this organizational directory only (Single tenant)"
   - **Redirect URI**: Leave blank
   - Click **Register**

4. **Save Application Details**
   - On the Overview page, copy and save:
     - ✅ **Application (client) ID**: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`
     - ✅ **Directory (tenant) ID**: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`

### 1.2 Create Client Secret

1. **Navigate to Certificates & secrets**

   - In your app registration, click **Certificates & secrets** (left menu)

2. **Create New Secret**

   - Click **+ New client secret**
   - Description: `MCP Server Secret`
   - Expires: Choose duration (6 months or 12 months recommended)
   - Click **Add**

3. **Copy Secret Value**
   - ⚠️ **IMPORTANT**: Copy the **Value** immediately (you won't see it again!)
   - ✅ **Client Secret**: `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### 1.3 Configure API Permissions

1. **Navigate to API Permissions**

   - Click **API permissions** (left menu)
   - Click **+ Add a permission**

2. **Add Microsoft Graph Permissions**

   - Click **Microsoft Graph**
   - Click **Application permissions**

3. **Add Each Permission** (check the box and add):

   **User & Group Management:**

   - [ ] Search and add: `User.ReadWrite.All`
   - [ ] Search and add: `Group.Read.All`
   - [ ] Search and add: `Directory.Read.All`

   **Device Management:**

   - [ ] Search and add: `DeviceManagementManagedDevices.Read.All`
   - [ ] Search and add: `DeviceManagementServiceConfig.Read.All`
   - [ ] Search and add: `DeviceManagementApps.Read.All`
   - [ ] Search and add: `DeviceManagementConfiguration.Read.All`

   **File Operations:**

   - [ ] Search and add: `Sites.ReadWrite.All`
   - [ ] Search and add: `Files.ReadWrite.All`

4. **Grant Admin Consent**
   - Click **Grant admin consent for [Your Tenant Name]**
   - Click **Yes** to confirm
   - ✅ All permissions should show green checkmarks with "Granted for [Tenant]"
   - ⏱️ **Wait 5-10 minutes** for permissions to propagate across Azure

---

## 📂 Step 2: Download and Setup Project in VS Code

### 2.1 Open VS Code and Get Project Files

**Option A: Download ZIP**

1. Download the project ZIP file
2. Extract to a folder (e.g., `C:\Projects\mcp-entra-server`)
3. Open VS Code
4. Click **File → Open Folder**
5. Select the extracted folder

**Option B: Clone with Git**

1. Open VS Code
2. Press `Ctrl+Shift+P` and type "Git: Clone"
3. Enter repository URL (if available)
4. Select folder location
5. Click "Open" when prompted

**Option C: Manual Setup**

1. Create new folder: `C:\Projects\mcp-entra-server`
2. Copy all project files to this folder
3. Open VS Code
4. Click **File → Open Folder**
5. Select `C:\Projects\mcp-entra-server`

### 2.2 Open Integrated Terminal

In VS Code:

- Click **View → Terminal** (or press `` Ctrl+` ``)
- Ensure you're in the project directory

Check your location:

```bash
# Windows PowerShell
pwd

# Output should show: C:\Projects\mcp-entra-server (or your folder path)
```

---

## 🐍 Step 3: Create Python Virtual Environment

### 3.1 Create Virtual Environment

In the VS Code terminal, run:

```bash
python -m venv .venv
```

This creates a `.venv` folder with an isolated Python environment.

### 3.2 Activate Virtual Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
.venv\Scripts\activate.bat
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

✅ **Success indicator**: Your terminal prompt should show `(.venv)` at the beginning

**If you get an execution policy error on Windows:**

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try activating again.

### 3.3 Select Python Interpreter in VS Code

1. Press `Ctrl+Shift+P`
2. Type: "Python: Select Interpreter"
3. Select the interpreter with `(.venv)` - usually: `.venv\Scripts\python.exe`

---

## 📦 Step 4: Install Dependencies

With the virtual environment activated, run:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Expected output:**

```
Successfully installed fastmcp-X.X.X azure-identity-X.X.X requests-X.X.X python-docx-X.X.X openpyxl-X.X.X python-pptx-X.X.X odfpy-X.X.X python-dotenv-X.X.X
```

✅ **Verify installation**:

```bash
pip list
```

You should see all packages: fastmcp, azure-identity, requests, python-docx, openpyxl, python-pptx, odfpy, python-dotenv

---

## ⚙️ Step 5: Configure Environment Variables

### 5.1 Create .env File

In VS Code:

1. **Right-click** on the project folder (left sidebar)
2. Click **New File**
3. Name it: `.env`

**OR** in terminal:

```bash
# Copy template to .env
copy .env.template .env    # Windows
cp .env.template .env      # macOS/Linux
```

### 5.2 Edit .env File

Open `.env` in VS Code and update with your Azure credentials:

```env
# Authentication Mode: "app" or "user"
AUTH_MODE=app

# Azure Service Principal Credentials
AZURE_CLIENT_ID=paste-your-application-id-here
AZURE_TENANT_ID=paste-your-tenant-id-here
AZURE_CLIENT_SECRET=paste-your-client-secret-here
```

**Replace:**

- `paste-your-application-id-here` → Application (client) ID from Step 1.1
- `paste-your-tenant-id-here` → Directory (tenant) ID from Step 1.1
- `paste-your-client-secret-here` → Client secret value from Step 1.2

### 5.3 Save the File

- Press `Ctrl+S` to save
- ✅ Ensure no extra spaces or quotes around values

---

## 🧪 Step 6: Test the Installation

### 6.1 Basic Connectivity Test

Test if the server can authenticate with Azure:

```bash
python -c "from entra_server import list_users; import json; result = list_users(); print('✅ SUCCESS!' if 'users' in result else f'❌ ERROR: {result}')"
```

**Expected output:** `✅ SUCCESS!`

If you see an error, proceed to Step 8 (Troubleshooting).

### 6.2 Run Complete Test Suite

Run each test one by one in the VS Code terminal:

**Test 1: List Users**

```bash
python -c "from entra_server import list_users; import json; print(json.dumps(list_users(), indent=2))"
```

✅ **Expected**: JSON output with user list

**Test 2: List Groups**

```bash
python -c "from entra_server import list_groups; import json; print(json.dumps(list_groups(), indent=2))"
```

✅ **Expected**: JSON output with groups

**Test 3: List Intune Devices**

```bash
python -c "from entra_server import list_intune_devices; import json; print(json.dumps(list_intune_devices(), indent=2))"
```

✅ **Expected**: JSON output with managed devices

**Test 4: List SharePoint Sites**

```bash
python -c "from entra_server import list_sharepoint_sites; import json; print(json.dumps(list_sharepoint_sites(), indent=2))"
```

✅ **Expected**: JSON output with SharePoint sites

**Test 5: List Autopilot Profiles**

```bash
python -c "from entra_server import list_autopilot_profiles; import json; print(json.dumps(list_autopilot_profiles(), indent=2))"
```

✅ **Expected**: JSON output with Autopilot profiles (or empty list)

**Test 6: List Microsoft Tunnel Sites**

```bash
python -c "from entra_server import list_microsoft_tunnel_sites; import json; print(json.dumps(list_microsoft_tunnel_sites(), indent=2))"
```

✅ **Expected**: JSON output with tunnel sites (or empty list)

**Test 7: List App Protection Policies**

```bash
python -c "from entra_server import list_app_protection_policies; import json; print(json.dumps(list_app_protection_policies(), indent=2))"
```

✅ **Expected**: JSON output with MAM policies

### 6.3 Test File Creation (Optional)

**Get your first SharePoint site ID:**

```bash
python -c "from entra_server import list_sharepoint_sites; sites = list_sharepoint_sites(); print('Site ID:', sites['sites'][0]['id'] if sites['sites'] else 'No sites found')"
```

**Create a test file** (replace `YOUR_SITE_ID` with actual ID from above):

```bash
python -c "from entra_server import create_file_in_sharepoint; result = create_file_in_sharepoint('sharepoint', 'YOUR_SITE_ID', 'test.txt', 'Hello from MCP Server!', 'Shared Documents'); print(result)"
```

✅ **Expected**: Success message with file details

---

## 🚀 Step 7: Run the MCP Server

### 7.1 Start the Server

In the VS Code terminal with virtual environment activated:

```bash
python entra_server.py
```

The server will start and wait for MCP client connections.

### 7.2 Test with Test Client (Optional)

Open a **new terminal** in VS Code (keep server running in first terminal):

```bash
# Activate virtual environment in new terminal
.\.venv\Scripts\Activate.ps1

# Run test client
python test_client.py
```

---

## 🔌 Step 8: Configure MCP Client (Optional)

### 8.1 Claude Desktop Integration

If using Claude Desktop:

1. **Locate config file:**

   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`

2. **Edit config file** (create if doesn't exist):

```json
{
	"mcpServers": {
		"entra-server": {
			"command": "python",
			"args": ["C:/Projects/mcp-entra-server/entra_server.py"],
			"env": {
				"AZURE_CLIENT_ID": "your-client-id",
				"AZURE_TENANT_ID": "your-tenant-id",
				"AZURE_CLIENT_SECRET": "your-client-secret",
				"AUTH_MODE": "app"
			}
		}
	}
}
```

3. **Update paths:**

   - Replace `C:/Projects/mcp-entra-server/` with your actual project path
   - Replace credential values with your actual values from `.env`

4. **Restart Claude Desktop**

5. **Verify**: Open Claude and look for MCP server indicator

### 8.2 Other MCP Clients

Use the provided `mcp/mcp.json` file and update paths as needed.

---

## 🔧 Step 9: Troubleshooting Common Issues

### Issue 1: Permission Errors (403 Forbidden)

**Error message:**

```
Application is not authorized to perform this operation
```

**Solution:**

1. Go back to Azure Portal → App registrations → Your app
2. Click **API permissions**
3. Verify all required permissions are added
4. Click **Grant admin consent** again
5. Wait 10 minutes for propagation
6. Try tests again

### Issue 2: Authentication Errors

**Error message:**

```
AADSTS700016: Application with identifier was not found
```

**Solution:**

1. Open `.env` file
2. Verify `AZURE_CLIENT_ID` and `AZURE_TENANT_ID` are correct (no extra spaces)
3. Go to Azure Portal → App registrations → Verify IDs match
4. Save `.env` and try again

**Error message:**

```
AADSTS7000215: Invalid client secret
```

**Solution:**

1. Go to Azure Portal → App registrations → Certificates & secrets
2. Create a new client secret
3. Copy the new secret value
4. Update `AZURE_CLIENT_SECRET` in `.env`
5. Save and try again

### Issue 3: Module Not Found

**Error message:**

```
ModuleNotFoundError: No module named 'fastmcp'
```

**Solution:**

1. Ensure virtual environment is activated (you should see `(.venv)`)
2. Run: `pip install -r requirements.txt`
3. Verify: `pip list` shows all packages

### Issue 4: Virtual Environment Activation Error

**Error on Windows:**

```
cannot be loaded because running scripts is disabled
```

**Solution:**

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate again: `.\.venv\Scripts\Activate.ps1`

### Issue 5: Python Not Found

**Error message:**

```
'python' is not recognized as an internal or external command
```

**Solution:**

- Download Python from [python.org](https://www.python.org/downloads/)
- During installation, check "Add Python to PATH"
- Restart VS Code
- Try again

### Issue 6: VS Code Not Using Virtual Environment

**VS Code still using global Python**

**Solution:**

1. Press `Ctrl+Shift+P`
2. Type: "Python: Select Interpreter"
3. Choose `.venv\Scripts\python.exe`
4. Open new terminal
5. Verify `(.venv)` appears in prompt

---

## ✅ Step 10: Verify Security

### Security Checklist

Run through this checklist to ensure secure deployment:

- [ ] `.env` file contains your secrets (NOT `.env.template`)
- [ ] `.env` is listed in `.gitignore`
- [ ] Client secret is not hardcoded in any Python files
- [ ] Only minimum required permissions granted in Azure
- [ ] Admin consent has been granted
- [ ] Secret expiration date is documented (for rotation reminder)
- [ ] No credentials committed to version control (if using Git)

### Test .gitignore (if using Git)

```bash
git status
```

✅ `.env` should NOT appear in the list. If it does:

```bash
git rm --cached .env
git commit -m "Remove .env from tracking"
```

---

## 📚 Step 11: Review Documentation

Before using the server, familiarize yourself with:

### Essential Reading

1. **README.md** - Overview, setup guide, all 32 tools

   ```bash
   # Open in VS Code
   code README.md
   ```

2. **TOOLS-SUMMARY.md** - Complete tool reference with examples

   ```bash
   code TOOLS-SUMMARY.md
   ```

3. **AUTHENTICATION.md** - App vs User authentication modes
   ```bash
   code AUTHENTICATION.md
   ```

### Quick Reference

**Available Tools:** 32 tools across 7 categories

- User & Group Management (5 tools)
- Intune Device Management (6 tools)
- Windows Autopilot (3 tools)
- Mobile Management (3 tools)
- Infrastructure (4 tools)
- File Operations (12 tools)

**Authentication Modes:**

- `AUTH_MODE=app` - Service principal (default, unattended)
- `AUTH_MODE=user` - Interactive browser (user context)

---

## 🚀 Step 12: Production Considerations

### If Deploying to Production Environment

**Secret Rotation Schedule:**

- Client secrets expire (configure in Azure: 3, 6, 12, or 24 months)
- Set calendar reminder 1 week before expiration
- Rotate secret and update `.env` before expiration

**Monitoring and Logging:**

```python
# Consider adding logging to entra_server.py
import logging
logging.basicConfig(level=logging.INFO)
```

**Backup Authentication:**

- Create a second Azure app registration as backup
- Document both sets of credentials securely
- Test backup credentials quarterly

**Compliance and Security:**

- [ ] Review company security policies for API credentials
- [ ] Document all API permissions for security team
- [ ] Set up regular permission audits (quarterly)
- [ ] Consider Azure Managed Identity if deploying to Azure VM/App Service
- [ ] Enable Azure AD audit logging for app access

**Deployment Options:**

- Run locally on trusted workstation
- Deploy to Azure VM with managed identity
- Run as Windows service for always-on availability
- Deploy to Azure App Service (requires containerization)

---

## 📖 Step 13: Next Steps

### You're Ready!

✅ MCP server is installed  
✅ Azure permissions configured  
✅ Tests passing  
✅ Security verified  
✅ Documentation reviewed

### Start Using the Server

**Option 1: Run Directly**

```bash
python entra_server.py
```

**Option 2: Integrate with Claude Desktop**

1. Configure `claude_desktop_config.json` (see Step 8)
2. Restart Claude Desktop
3. Type: "List my Entra ID users"
4. Claude will use your MCP server!

**Option 3: Use with Other MCP Clients**

- Configure `mcp/mcp.json` with server path
- Connect client to MCP server
- Access all 32 tools programmatically

### Explore the Tools

Try these commands to explore capabilities:

**User Management:**

```bash
python -c "from entra_server import list_users; print(list_users())"
```

**Device Inventory:**

```bash
python -c "from entra_server import list_intune_devices; print(list_intune_devices())"
```

**Compliance Check:**

```bash
python -c "from entra_server import list_intune_compliance_policies; print(list_intune_compliance_policies())"
```

### Get Help

- **README.md** - Complete guide with all 32 tools documented
- **TOOLS-SUMMARY.md** - Quick reference with examples for each tool
- **AUTHENTICATION.md** - Authentication modes and troubleshooting
- **CHANGELOG.md** - Version history and feature updates

### Report Issues

If you encounter issues:

1. Check troubleshooting section (Step 9)
2. Review Azure permissions (Step 2)
3. Verify `.env` configuration (Step 5)
4. Check virtual environment activation (Step 3)

---

## 📝 Deployment Notes

Use this section to document your specific deployment:

**Deployment Date:** ********\_********

**Deployed By:** ********\_********

**Tenant Name:** ********\_********

**App Registration Name:** ********\_********

**Secret Expiration Date:** ********\_********

**Issues Encountered:**

```
[Document any issues or special configurations here]
```

**Custom Configurations:**

```
[Document any customizations made to the server]
```

**Production Checklist:**

- [ ] Server running successfully
- [ ] All 32 tools tested and working
- [ ] Client secret expiration date documented
- [ ] Security review completed
- [ ] Team members trained on usage
- [ ] Backup authentication configured
- [ ] Monitoring/alerting set up (if applicable)

---

## 🎉 Deployment Complete!

**What You Can Do Now:**

- ✅ Manage **Entra ID users and groups**
- ✅ Monitor **Intune devices and compliance**
- ✅ Query **Windows Autopilot deployments**
- ✅ Track **mobile device management policies**
- ✅ Monitor **infrastructure connectors and tunnels**
- ✅ Read/write files in **SharePoint and OneDrive**
- ✅ Create/edit **Word, Excel, PowerPoint** documents

**Your MCP server is ready with 32 powerful tools for Microsoft 365 and Intune management! 🚀**

### Quick Command Reference

**Start server:**

```bash
python entra_server.py
```

**Run tests:**

```bash
python test_client.py
```

**Check installed packages:**

```bash
pip list
```

**View tool documentation:**

```bash
code TOOLS-SUMMARY.md
```

Enjoy your new MCP server!

# MCP M365 Management - Available Commands

Complete reference of all 32 tools available in the MCP server.

---

## 📋 All Available Commands

### 👥 User & Group Management (5 tools)

```python
from mcp_m365_mgmt import list_users
from mcp_m365_mgmt import list_groups
from mcp_m365_mgmt import get_user_details
from mcp_m365_mgmt import get_group_members
from mcp_m365_mgmt import search_users
```

### 📱 Intune Device Management (6 tools)

```python
from mcp_m365_mgmt import list_intune_devices
from mcp_m365_mgmt import list_intune_compliance_policies
from mcp_m365_mgmt import list_intune_configuration_policies
from mcp_m365_mgmt import list_intune_filters
from mcp_m365_mgmt import list_intune_scripts
from mcp_m365_mgmt import list_intune_applications
```

### 🖥️ Windows Autopilot (3 tools)

```python
from mcp_m365_mgmt import list_autopilot_profiles
from mcp_m365_mgmt import list_autopilot_devices
from mcp_m365_mgmt import list_enrollment_status_page_profiles
```

### 📲 Mobile Device Management (3 tools)

```python
from mcp_m365_mgmt import list_android_management_profiles
from mcp_m365_mgmt import list_ios_management_profiles
from mcp_m365_mgmt import list_app_protection_policies
```

### 🔧 Infrastructure Monitoring (4 tools)

```python
from mcp_m365_mgmt import list_microsoft_tunnel_sites
from mcp_m365_mgmt import list_microsoft_tunnel_servers
from mcp_m365_mgmt import list_intune_ad_connectors
from mcp_m365_mgmt import list_intune_certificate_connectors
```

### 📁 SharePoint & OneDrive (5 tools)

```python
from mcp_m365_mgmt import list_sharepoint_sites
from mcp_m365_mgmt import list_files_in_sharepoint
from mcp_m365_mgmt import read_file_from_sharepoint
from mcp_m365_mgmt import create_file_in_sharepoint
from mcp_m365_mgmt import list_onedrive_files
```

### 📄 Document Operations (6 tools)

```python
from mcp_m365_mgmt import create_word_document
from mcp_m365_mgmt import create_excel_spreadsheet
from mcp_m365_mgmt import create_powerpoint_presentation
from mcp_m365_mgmt import read_word_document
from mcp_m365_mgmt import read_excel_spreadsheet
from mcp_m365_mgmt import create_odf_document
```

---

## 🧪 Quick Test Commands

### User Management Tests

**Test Users:**

```bash
python -c "from mcp_m365_mgmt import list_users; import json; result = list_users(); print(json.dumps(result, indent=2)[:500])"
```

**Test Groups:**

```bash
python -c "from mcp_m365_mgmt import list_groups; import json; result = list_groups(); print(json.dumps(result, indent=2)[:500])"
```

**Get User Details:**

```bash
python -c "from mcp_m365_mgmt import get_user_details; import json; result = get_user_details('user@domain.com'); print(json.dumps(result, indent=2))"
```

### Intune Management Tests

**Test Devices:**

```bash
python -c "from mcp_m365_mgmt import list_intune_devices; import json; result = list_intune_devices(); print(json.dumps(result, indent=2)[:500])"
```

**Test Compliance Policies:**

```bash
python -c "from mcp_m365_mgmt import list_intune_compliance_policies; import json; result = list_intune_compliance_policies(); print(json.dumps(result, indent=2)[:500])"
```

**Test Configuration Policies:**

```bash
python -c "from mcp_m365_mgmt import list_intune_configuration_policies; import json; result = list_intune_configuration_policies(); print(json.dumps(result, indent=2)[:500])"
```

**Test Intune Filters:**

```bash
python -c "from mcp_m365_mgmt import list_intune_filters; import json; result = list_intune_filters(); print(json.dumps(result, indent=2)[:500])"
```

**Test Intune Scripts:**

```bash
python -c "from mcp_m365_mgmt import list_intune_scripts; import json; result = list_intune_scripts(); print(json.dumps(result, indent=2)[:500])"
```

**Test Intune Applications:**

```bash
python -c "from mcp_m365_mgmt import list_intune_applications; import json; result = list_intune_applications(); print(json.dumps(result, indent=2)[:500])"
```

### Windows Autopilot Tests

**Test Autopilot Profiles:**

```bash
python -c "from mcp_m365_mgmt import list_autopilot_profiles; import json; result = list_autopilot_profiles(); print(json.dumps(result, indent=2)[:500])"
```

**Test Autopilot Devices:**

```bash
python -c "from mcp_m365_mgmt import list_autopilot_devices; import json; result = list_autopilot_devices(); print(json.dumps(result, indent=2)[:500])"
```

**Test ESP Profiles:**

```bash
python -c "from mcp_m365_mgmt import list_enrollment_status_page_profiles; import json; result = list_enrollment_status_page_profiles(); print(json.dumps(result, indent=2)[:500])"
```

### Mobile Device Management Tests

**Test Android Profiles:**

```bash
python -c "from mcp_m365_mgmt import list_android_management_profiles; import json; result = list_android_management_profiles(); print(json.dumps(result, indent=2)[:500])"
```

**Test iOS Profiles:**

```bash
python -c "from mcp_m365_mgmt import list_ios_management_profiles; import json; result = list_ios_management_profiles(); print(json.dumps(result, indent=2)[:500])"
```

**Test MAM Policies:**

```bash
python -c "from mcp_m365_mgmt import list_app_protection_policies; import json; result = list_app_protection_policies(); print(json.dumps(result, indent=2)[:500])"
```

### Infrastructure Monitoring Tests

**Test Microsoft Tunnel Sites:**

```bash
python -c "from mcp_m365_mgmt import list_microsoft_tunnel_sites; import json; result = list_microsoft_tunnel_sites(); print(json.dumps(result, indent=2)[:500])"
```

**Test Microsoft Tunnel Servers:**

```bash
python -c "from mcp_m365_mgmt import list_microsoft_tunnel_servers; import json; result = list_microsoft_tunnel_servers(); print(json.dumps(result, indent=2)[:500])"
```

**Test AD Connectors:**

```bash
python -c "from mcp_m365_mgmt import list_intune_ad_connectors; import json; result = list_intune_ad_connectors(); print(json.dumps(result, indent=2)[:500])"
```

**Test Certificate Connectors:**

```bash
python -c "from mcp_m365_mgmt import list_intune_certificate_connectors; import json; result = list_intune_certificate_connectors(); print(json.dumps(result, indent=2)[:500])"
```

### SharePoint & OneDrive Tests

**Test SharePoint Sites:**

```bash
python -c "from mcp_m365_mgmt import list_sharepoint_sites; import json; result = list_sharepoint_sites(); print(json.dumps(result, indent=2)[:500])"
```

**List Files in SharePoint:**

```bash
python -c "from mcp_m365_mgmt import list_files_in_sharepoint; import json; result = list_files_in_sharepoint('sharepoint', 'YOUR_SITE_ID', 'Shared Documents'); print(json.dumps(result, indent=2)[:500])"
```

**List OneDrive Files:**

```bash
python -c "from mcp_m365_mgmt import list_onedrive_files; import json; result = list_onedrive_files('USER_ID'); print(json.dumps(result, indent=2)[:500])"
```

---

## 🚀 Running the MCP Server

### Start the Server

```bash
# Option 1: Using command (after pip install)
m365-mgmt

# Option 2: Direct Python execution
python mcp_m365_mgmt.py

# Option 3: After pip install -e .
python -c "from mcp_m365_mgmt import main; main()"
```

### With Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
	"mcpServers": {
		"m365-mgmt": {
			"command": "m365-mgmt",
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

---

## 📝 Usage Examples

### Example 1: Get All Users and Count Them

```python
from mcp_m365_mgmt import list_users
import json

result = list_users()
users = result.get('users', [])
print(f"Total users: {len(users)}")
for user in users[:5]:  # Print first 5
    print(f"- {user.get('displayName')} ({user.get('userPrincipalName')})")
```

### Example 2: Check Compliance Status

```python
from mcp_m365_mgmt import list_intune_compliance_policies
import json

result = list_intune_compliance_policies()
policies = result.get('compliance_policies', [])
print(f"Total compliance policies: {len(policies)}")
for policy in policies:
    print(f"- {policy.get('displayName')} [{policy.get('platform')}]")
```

### Example 3: Monitor Autopilot Devices

```python
from mcp_m365_mgmt import list_autopilot_devices
import json

result = list_autopilot_devices()
devices = result.get('devices', [])
print(f"Total Autopilot devices: {len(devices)}")
for device in devices:
    print(f"- {device.get('displayName')}: {device.get('deploymentProfileAssignmentStatus')}")
```

### Example 4: Check Infrastructure Health

```python
from mcp_m365_mgmt import list_microsoft_tunnel_servers
import json

result = list_microsoft_tunnel_servers()
servers = result.get('servers', [])
print(f"Total tunnel servers: {len(servers)}")
for server in servers:
    print(f"- {server.get('displayName')}: {server.get('agentImageDigest')} (Healthy: {server.get('lastCheckinDateTime') is not None})")
```

---

## 🔐 Authentication

Make sure your `.env` file is configured:

```env
# Authentication Mode: "app" or "user"
AUTH_MODE=app

# Azure Service Principal Credentials
AZURE_CLIENT_ID=your-application-id
AZURE_TENANT_ID=your-tenant-id
AZURE_CLIENT_SECRET=your-client-secret
```

---

## ⚠️ Common Errors & Solutions

### Error: "Application is not authorized to perform this operation"

**Problem:** Missing API permissions in Azure App Registration

**Solution:**

1. Go to Azure Portal → App registrations → Your app
2. Click **API permissions**
3. Ensure you have granted these permissions:

**Required Permissions (10):**

- ✅ `User.Read.All` - Read users
- ✅ `Group.Read.All` - Read groups
- ✅ `DeviceManagementManagedDevices.Read.All` - Read Intune devices
- ✅ `DeviceManagementConfiguration.Read.All` - Read configuration policies ⚠️
- ✅ `DeviceManagementApps.Read.All` - Read Intune applications
- ✅ `DeviceManagementServiceConfig.Read.All` - Read Autopilot/ESP profiles
- ✅ `Sites.Read.All` - Read SharePoint sites
- ✅ `Files.Read.All` - Read files
- ✅ `Files.ReadWrite.All` - Create/edit files
- ✅ `offline_access` - Refresh tokens

4. Click **Grant admin consent for [Your Tenant]**
5. Wait 5-10 minutes for permissions to propagate
6. Try again

### Error: "DefaultAzureCredential acquired a token from AzureCliCredential"

**Problem:** Using Azure CLI credentials instead of service principal

**Solution:** Make sure your `.env` file has the correct credentials and `AUTH_MODE=app`

### Error: "AADSTS700016: Application with identifier was not found"

**Problem:** Wrong `AZURE_CLIENT_ID` or `AZURE_TENANT_ID`

**Solution:**

1. Go to Azure Portal → App registrations
2. Copy the correct Application (client) ID and Directory (tenant) ID
3. Update `.env` file
4. No extra spaces or quotes

### Error: "AADSTS7000215: Invalid client secret"

**Problem:** Wrong or expired client secret

**Solution:**

1. Go to Azure Portal → App registrations → Certificates & secrets
2. Create new client secret
3. Copy the **Value** (not the Secret ID)
4. Update `AZURE_CLIENT_SECRET` in `.env`

---

## 📚 Additional Resources

- **README.md** - Complete setup guide
- **TOOLS-SUMMARY.md** - Detailed tool reference
- **DEPLOYMENT.md** - Deployment instructions
- **PUBLISHING.md** - PyPI publishing guide
- **CHANGELOG.md** - Version history

---

**Total Tools:** 32  
**Version:** 1.0.0  
**Author:** Thiago Beier  
**GitHub:** https://github.com/thiagogbeier/mcp-m365-mgmt

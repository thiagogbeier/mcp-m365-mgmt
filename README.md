# Microsoft 365 / Intune MCP Server

A comprehensive Model Context Protocol (MCP) server for managing Microsoft 365, Microsoft Entra ID, and Microsoft Intune resources. This server provides 32 tools for automating user management, device management, file operations, and infrastructure monitoring.

## 🎯 Overview

This MCP server enables AI assistants and automation tools to interact with:

- **Microsoft Entra ID** - User and group management
- **Microsoft Intune** - Device, policy, and application management
- **SharePoint & OneDrive** - Document creation and management
- **Windows Autopilot** - Device provisioning
- **Microsoft Tunnel** - Gateway monitoring
- **Mobile Device Management** - Android and iOS policies
- **App Protection Policies** - MAM policies

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Azure subscription with appropriate licenses (Intune, Microsoft 365)
- Azure AD application registration with required permissions

### Installation

1. **Clone or download this repository**

   ```bash
   git clone <repository-url>
   cd mcp-entra-server
   ```

2. **Create virtual environment**

   ```bash
   python -m venv .venv

   # Windows
   .venv\Scripts\activate

   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install fastmcp azure-identity requests python-docx openpyxl python-pptx odfpy python-dotenv
   ```

4. **Configure environment variables**

   Create a `.env` file in the project root:

   ```env
   # Authentication Mode: "app" or "user"
   AUTH_MODE=app

   # Azure Service Principal Credentials (for app mode)
   AZURE_CLIENT_ID=your-client-id
   AZURE_TENANT_ID=your-tenant-id
   AZURE_CLIENT_SECRET=your-client-secret
   ```

5. **Run the server**
   ```bash
   python entra_server.py
   ```

## 🔐 Azure App Registration Setup

### Step 1: Create App Registration

1. Go to [Azure Portal](https://portal.azure.com) → **Azure Active Directory** → **App registrations**
2. Click **New registration**
3. Enter a name (e.g., "MCP Entra Server")
4. Set **Supported account types** to "Single tenant"
5. Click **Register**

### Step 2: Create Client Secret

1. In your app registration, go to **Certificates & secrets**
2. Click **New client secret**
3. Add a description and select expiration period
4. Click **Add**
5. **Copy the secret value immediately** (you won't see it again)

### Step 3: Configure API Permissions

Go to **API permissions** and add the following **Application permissions**:

#### Microsoft Graph Permissions

**User & Group Management:**

- `User.ReadWrite.All` - Create and manage users
- `Group.Read.All` - Read groups and memberships
- `Directory.Read.All` - Read directory data

**Device Management:**

- `DeviceManagementManagedDevices.Read.All` - Read managed devices
- `DeviceManagementServiceConfig.Read.All` - Read device management configuration
- `DeviceManagementApps.Read.All` - Read Intune apps
- `DeviceManagementConfiguration.Read.All` - Read device configuration

**File Operations:**

- `Sites.ReadWrite.All` - Read and write SharePoint sites
- `Files.ReadWrite.All` - Read and write files

After adding permissions, click **Grant admin consent** for your tenant.

### Step 4: Copy Credentials

From your app registration **Overview** page, copy:

- **Application (client) ID** → `AZURE_CLIENT_ID`
- **Directory (tenant) ID** → `AZURE_TENANT_ID`
- Client secret (from step 2) → `AZURE_CLIENT_SECRET`

## 📋 Complete Tool List (32 Tools)

### 👥 User & Group Management (4 tools)

- `create_user` - Create new users in Microsoft Entra ID
- `get_user_info` - Get user details by ID
- `list_users` - List all users in tenant
- `list_groups` - List all groups
- `get_group_members` - Get group membership

### 📱 Intune Device Management (6 tools)

- `list_intune_devices` - List managed devices
- `list_intune_compliance_policies` - List compliance policies
- `list_intune_configuration_policies` - List configuration policies
- `list_intune_filters` - List assignment filters
- `list_intune_scripts` - List PowerShell and Shell scripts
- `list_intune_applications` - List mobile applications

### 🚗 Windows Autopilot (3 tools)

- `list_autopilot_profiles` - List Autopilot deployment profiles
- `list_autopilot_devices` - List registered Autopilot devices
- `list_enrollment_status_page_profiles` - List ESP profiles

### 📱 Mobile Management (3 tools)

- `list_android_management_profiles` - List Android policies and enrollment
- `list_ios_management_profiles` - List iOS/iPadOS policies and enrollment
- `list_app_protection_policies` - List MAM policies

### 🌐 Infrastructure & Connectivity (4 tools)

- `list_microsoft_tunnel_sites` - List Microsoft Tunnel Gateway sites
- `list_microsoft_tunnel_servers` - List tunnel servers and health
- `list_intune_ad_connectors` - List AD connectors for Hybrid Join
- `list_intune_certificate_connectors` - List NDES certificate connectors

### 📄 File & Document Management (12 tools)

- `create_file_in_onedrive` - Create text files in OneDrive
- `create_file_in_sharepoint` - Create text files in SharePoint
- `list_sharepoint_sites` - List SharePoint sites
- `create_word_document` - Create Word (.docx) documents
- `create_excel_workbook` - Create Excel (.xlsx) workbooks
- `create_powerpoint_presentation` - Create PowerPoint (.pptx) files
- `convert_file_to_pdf` - Convert Office files to PDF
- `create_csv_file` - Create CSV files
- `read_csv_file` - Read CSV files
- `export_powerpoint_slide_as_image` - Export slides as images
- `create_odf_document` - Create OpenDocument format files

## 🔧 Configuration Options

### Authentication Modes

**App Mode (Default)** - Service principal authentication

```env
AUTH_MODE=app
```

- Best for: Automation, unattended scenarios
- Files show as modified by "SharePoint app"

**User Mode** - Interactive browser authentication

```env
AUTH_MODE=user
```

- Best for: Interactive use, user context required
- Files show as modified by signed-in user
- Requires user to sign in via browser

### MCP Client Integration

#### Claude Desktop

Add to your Claude Desktop configuration (`claude_desktop_config.json`):

```json
{
	"mcpServers": {
		"entra-server": {
			"command": "python",
			"args": ["C:/path/to/mcp-entra-server/entra_server.py"],
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

#### Other MCP Clients

Use the `mcp.json` configuration file included in the `mcp/` directory.

## 📖 Usage Examples

### List Intune Devices

```python
from entra_server import list_intune_devices
import json

result = list_intune_devices()
print(json.dumps(result, indent=2))
```

### Create User

```python
from entra_server import create_user

result = create_user(
    user_principal_name="john.doe@yourtenant.com",
    display_name="John Doe",
    mail_nickname="john.doe",
    password="TempPassword123!",
    force_change_password=True
)
```

### Create Word Document in SharePoint

```python
from entra_server import create_word_document, list_sharepoint_sites

# First, get your SharePoint site ID
sites = list_sharepoint_sites()
site_id = sites['sites'][0]['id']  # Use first site

# Create document
result = create_word_document(
    location='sharepoint',
    location_id=site_id,
    file_name='Report.docx',
    content='# Project Status\n\nAll systems operational.',
    folder_path='Shared Documents'
)
```

### List Microsoft Tunnel Sites

```python
from entra_server import list_microsoft_tunnel_sites

result = list_microsoft_tunnel_sites()
for site in result['tunnel_sites']:
    print(f"{site['displayName']}: {site['publicAddress']}")
```

## 🔍 Troubleshooting

### Permission Errors (403 Forbidden)

**Error:** `Application is not authorized to perform this operation`

**Solution:**

1. Check that all required API permissions are added in Azure Portal
2. Ensure **admin consent** has been granted
3. Wait 5-10 minutes for permissions to propagate

### Authentication Errors

**Error:** `AADSTS700016: Application with identifier was not found`

**Solution:**

- Verify `AZURE_CLIENT_ID` and `AZURE_TENANT_ID` are correct
- Check that the app registration exists in your tenant

**Error:** `AADSTS7000215: Invalid client secret`

**Solution:**

- Generate a new client secret in Azure Portal
- Update `AZURE_CLIENT_SECRET` in `.env` file

### File Operation Errors

**Error:** `Resource not found for the segment`

**Solution:**

- Verify the SharePoint site ID or OneDrive user ID is correct
- Use `list_sharepoint_sites()` to get valid site IDs
- Ensure the folder path exists (e.g., "Shared Documents")

## 🛡️ Security Best Practices

1. **Protect credentials**: Never commit `.env` file to version control
2. **Use least privilege**: Only grant necessary API permissions
3. **Rotate secrets**: Regularly rotate client secrets (recommended: every 6 months)
4. **Monitor access**: Review Azure AD sign-in logs for suspicious activity
5. **Use managed identities**: Consider Azure Managed Identities for production deployments

## 📦 Deployment Options

### Local Development

```bash
python entra_server.py
```

### Docker Container

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "entra_server.py"]
```

### Azure Container Instance

Deploy as containerized MCP server for cloud-based access.

### GitHub Actions / Azure DevOps

Use as automation tool in CI/CD pipelines for tenant management.

## 📚 Additional Documentation

- [TOOLS-SUMMARY.md](TOOLS-SUMMARY.md) - Complete tool reference with examples
- [AUTHENTICATION.md](AUTHENTICATION.md) - Authentication mode details
- [Microsoft Graph API Documentation](https://learn.microsoft.com/en-us/graph/)
- [FastMCP Documentation](https://github.com/jlowin/fastmcp)

## 🤝 Contributing

Contributions are welcome! Areas for enhancement:

- Additional Intune policy types
- Bulk operations for users and devices
- Advanced SharePoint operations
- Reporting and analytics capabilities
- Exchange Online integration
- Teams management

## 📄 License

This project is provided as-is for educational and automation purposes. Ensure compliance with Microsoft licensing terms when using with production tenants.

## 🆘 Support

For issues and questions:

1. Check the troubleshooting section above
2. Review Microsoft Graph API documentation
3. Verify API permissions and admin consent
4. Check Azure AD sign-in logs for detailed errors

## 🔄 Updates

**Version 1.0** (November 2025)

- Initial release with 32 tools
- Support for Entra ID, Intune, SharePoint, OneDrive
- Windows Autopilot integration
- Microsoft Tunnel monitoring
- Mobile device management (Android/iOS)
- App protection policies
- Document creation (Office, CSV, ODF formats)
- File conversion and image export

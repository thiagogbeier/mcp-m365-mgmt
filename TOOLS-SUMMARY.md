# MCP Entra Server - Complete Tool List

## 🎉 Total Tools: 32

### 👥 **User & Group Management** (5 tools)

1. `create_user` - Create new users in Microsoft Entra ID
2. `get_user_info` - Get detailed information about a specific user
3. `list_users` - List all users in the tenant
4. `list_groups` - List all groups in the tenant
5. `get_group_members` - Get members of a specific group

### 📱 **Intune Device Management** (6 tools)

6. `list_intune_devices` - List all Intune-managed devices
7. `list_intune_compliance_policies` - List all device compliance policies
8. `list_intune_configuration_policies` - List all device configuration policies and settings
9. `list_intune_filters` - List all assignment filters
10. `list_intune_scripts` - List all PowerShell and Shell scripts
11. `list_intune_applications` - List all mobile applications

### 🚗 **Windows Autopilot** (3 tools)

12. `list_autopilot_profiles` - List all Windows Autopilot deployment profiles
13. `list_autopilot_devices` - List all registered Autopilot devices
14. `list_enrollment_status_page_profiles` - List all ESP (Enrollment Status Page) profiles

### 📱 **Mobile Device Management** (3 tools)

15. `list_android_management_profiles` - List all Android policies, settings, and enrollment configurations
16. `list_ios_management_profiles` - List all iOS/iPadOS policies, settings, and enrollment configurations
17. `list_app_protection_policies` - List all app protection policies (MAM) for iOS, Android, and Windows

### 🌐 **Infrastructure & Connectivity** (4 tools)

18. `list_microsoft_tunnel_sites` - List all Microsoft Tunnel Gateway sites
19. `list_microsoft_tunnel_servers` - List all Microsoft Tunnel servers and health status
20. `list_intune_ad_connectors` - List all Intune Connectors for Active Directory (Hybrid Join)
21. `list_intune_certificate_connectors` - List all Intune Certificate Connectors (NDES)

### 📄 **File Management - Basic** (3 tools)

22. `create_file_in_onedrive` - Create text files in user's OneDrive
23. `create_file_in_sharepoint` - Create text files in SharePoint sites
24. `list_sharepoint_sites` - List all SharePoint sites in the tenant

### 📊 **Office Documents - Microsoft Formats** (3 tools)

25. `create_word_document` - Create Word documents (.docx)
26. `create_excel_workbook` - Create Excel workbooks (.xlsx)
27. `create_powerpoint_presentation` - Create PowerPoint presentations (.pptx)

### 🔄 **File Conversion** (1 tool)

28. `convert_file_to_pdf` - Convert Office files (Word, Excel, PowerPoint) to PDF

### 📋 **CSV Support** (2 tools)

29. `create_csv_file` - Create CSV files for data exchange
30. `read_csv_file` - Read CSV files and return data as structured lists

### 🖼️ **Image Export** (1 tool)

31. `export_powerpoint_slide_as_image` - Export PowerPoint slides as PNG, JPG, GIF, BMP, or TIFF

### 🌍 **OpenDocument Format (ODF)** (1 tool)

32. `create_odf_document` - Create ODF files (.odt, .ods, .odp) for cross-platform compatibility

---

## 📁 Supported File Formats

### Word Formats

- ✅ `.docx` - Word Document
- ✅ `.txt` - Plain Text
- ✅ `.pdf` - PDF (via conversion)
- ✅ `.odt` - OpenDocument Text

### Excel Formats

- ✅ `.xlsx` - Excel Workbook
- ✅ `.csv` - CSV (Comma-delimited)
- ✅ `.pdf` - PDF (via conversion)
- ✅ `.ods` - OpenDocument Spreadsheet

### PowerPoint Formats

- ✅ `.pptx` - PowerPoint Presentation
- ✅ `.pdf` - PDF (via conversion)
- ✅ `.png`, `.jpg`, `.gif`, `.bmp`, `.tiff` - Image exports
- ✅ `.odp` - OpenDocument Presentation

---

## 🔐 Authentication Modes

### App Authentication (Default)

- Files show as modified by "SharePoint app"
- Uses service principal credentials
- Best for: Automation, background processes
- Set: `AUTH_MODE=app` in `.env`

### User Authentication

- Files show as modified by logged-in user
- Uses interactive browser sign-in
- Best for: Interactive use, user context needed
- Set: `AUTH_MODE=user` in `.env`

---

## 🚀 Quick Start Examples

### Create a Word Document

```python
from entra_server import create_word_document
result = create_word_document(
    'sharepoint',
    'site-id',
    'report.docx',
    'Project Status: All systems operational.',
    'Shared Documents'
)
```

### Create CSV File

```python
from entra_server import create_csv_file
data = [
    ['Name', 'Email', 'Department'],
    ['John Doe', 'john@company.com', 'IT'],
    ['Jane Smith', 'jane@company.com', 'HR']
]
result = create_csv_file('sharepoint', 'site-id', 'employees.csv', data)
```

### Export PowerPoint Slide as Image

```python
from entra_server import export_powerpoint_slide_as_image
result = export_powerpoint_slide_as_image(
    'sharepoint',
    'site-id',
    'file-id',
    slide_index=1,
    image_format='png'
)
```

### Create OpenDocument File

```python
from entra_server import create_odf_document
result = create_odf_document(
    'sharepoint',
    'site-id',
    'document.odt',
    'text',
    'Compatible with LibreOffice and Google Docs!'
)
```

---

## 📦 Required Permissions

### Application Permissions (for app mode)

- `DeviceManagementManagedDevices.Read.All`
- `User.ReadWrite.All`
- `Group.Read.All`
- `Sites.ReadWrite.All`
- `Files.ReadWrite.All`

### Delegated Permissions (for user mode)

- Same as above, but as delegated permissions

---

## 🎯 Use Cases

1. **Automated Reporting**: Generate Word/Excel/PowerPoint reports from data
2. **Data Migration**: Export data to CSV for import into other systems
3. **Document Conversion**: Convert Office files to PDF for distribution
4. **Cross-Platform**: Create ODF files for LibreOffice/Google Docs users
5. **Image Generation**: Export presentation slides as images for web/email
6. **Device Management**: Monitor and report on Intune devices
7. **User Administration**: Automate user and group management

---

## 🛠️ Technology Stack

- **MCP Framework**: FastMCP
- **Authentication**: Azure Identity (ClientSecretCredential, InteractiveBrowserCredential)
- **API**: Microsoft Graph API
- **Document Libraries**:
  - python-docx (Word)
  - openpyxl (Excel)
  - python-pptx (PowerPoint)
  - odfpy (OpenDocument Format)
  - Standard library (CSV, PDF conversion via Graph API)

---

## 📝 Next Steps

To add more capabilities:

- Template support (.dotx, .xltx, .potx)
- Macro-enabled files (.docm, .xlsm, .pptm)
- File operations (copy, move, delete, rename)
- Search and metadata operations
- Sharing and permissions management
- Version history and collaboration features

# Changelog

All notable changes to the MCP Entra Server project will be documented in this file.

## [1.0.0] - 2025-11-04

### 🎉 Initial Release

Complete MCP server for Microsoft 365, Entra ID, and Intune management with 32 tools.

### Added - User & Group Management (5 tools)

- `create_user` - Create new users in Microsoft Entra ID
- `get_user_info` - Get detailed user information
- `list_users` - List all users in tenant
- `list_groups` - List all groups
- `get_group_members` - Get group membership details

### Added - Intune Device Management (6 tools)

- `list_intune_devices` - List all managed devices with compliance status
- `list_intune_compliance_policies` - List device compliance policies (Windows, iOS, Android)
- `list_intune_configuration_policies` - List device configuration policies and settings
- `list_intune_filters` - List assignment filters with targeting rules
- `list_intune_scripts` - List PowerShell and Shell scripts
- `list_intune_applications` - List mobile applications (iOS, Android, Windows)

### Added - Windows Autopilot (3 tools)

- `list_autopilot_profiles` - List Autopilot deployment profiles with OOBE settings
- `list_autopilot_devices` - List registered Autopilot devices with serial numbers
- `list_enrollment_status_page_profiles` - List ESP profiles with installation progress settings

### Added - Mobile Device Management (3 tools)

- `list_android_management_profiles` - List Android policies, configurations, and enrollment
- `list_ios_management_profiles` - List iOS/iPadOS policies, configurations, and enrollment
- `list_app_protection_policies` - List MAM policies for iOS, Android, and Windows

### Added - Infrastructure & Connectivity (4 tools)

- `list_microsoft_tunnel_sites` - List Microsoft Tunnel Gateway sites with public addresses
- `list_microsoft_tunnel_servers` - List tunnel servers with health status monitoring
- `list_intune_ad_connectors` - List Active Directory connectors for Hybrid Azure AD Join
- `list_intune_certificate_connectors` - List NDES certificate connectors for SCEP

### Added - File & Document Management (12 tools)

- `create_file_in_onedrive` - Create text files in user's OneDrive
- `create_file_in_sharepoint` - Create text files in SharePoint sites
- `list_sharepoint_sites` - List all SharePoint sites in tenant
- `create_word_document` - Create Word documents (.docx) with formatted content
- `create_excel_workbook` - Create Excel workbooks (.xlsx) with data
- `create_powerpoint_presentation` - Create PowerPoint presentations (.pptx) with slides
- `convert_file_to_pdf` - Convert Office documents to PDF format
- `create_csv_file` - Create CSV files for data exchange
- `read_csv_file` - Read and parse CSV files
- `export_powerpoint_slide_as_image` - Export slides as PNG, JPG, GIF, BMP, TIFF
- `create_odf_document` - Create OpenDocument format files (.odt, .ods, .odp)

### Added - Authentication

- Dual authentication modes: App (service principal) and User (interactive)
- Azure Identity integration with ClientSecretCredential and InteractiveBrowserCredential
- Environment-based configuration via `.env` file
- Automatic token caching and refresh

### Added - Documentation

- Comprehensive README.md with setup instructions
- TOOLS-SUMMARY.md with complete tool reference
- AUTHENTICATION.md explaining auth modes
- DEPLOYMENT.md with deployment checklist
- .env.template for easy configuration
- requirements.txt for dependency management

### Added - File Format Support

- Microsoft Office formats (.docx, .xlsx, .pptx)
- OpenDocument formats (.odt, .ods, .odp)
- PDF conversion via Graph API
- CSV for data exchange
- Image exports (PNG, JPG, GIF, BMP, TIFF)
- Plain text files

### Technical Details

- Framework: FastMCP
- Language: Python 3.8+
- API: Microsoft Graph API v1.0 and beta
- Libraries: azure-identity, requests, python-docx, openpyxl, python-pptx, odfpy
- Architecture: Synchronous functions with @mcp.tool() decorators

### Tested With

- Python 3.13.9
- Microsoft Graph API v1.0 and beta endpoints
- Real Microsoft 365 tenant (letsintune.com)
- 19 managed devices, 100+ groups, 11 SharePoint sites
- Windows, iOS, and Android device configurations
- Microsoft Tunnel infrastructure (5 sites, 5 servers)

---

## Future Enhancements (Roadmap)

### Planned for v1.1

- [ ] Template support (.dotx, .xltx, .potx)
- [ ] Macro-enabled files (.docm, .xlsm, .pptm)
- [ ] Bulk user operations (create, update, delete)
- [ ] Advanced SharePoint operations (copy, move, rename)
- [ ] Device actions (restart, wipe, sync)

### Planned for v1.2

- [ ] Conditional Access policy management
- [ ] Exchange Online integration
- [ ] Microsoft Teams management
- [ ] Azure AD group lifecycle management
- [ ] Reporting and analytics capabilities

### Under Consideration

- [ ] Proactive Remediation script management
- [ ] Windows Update for Business reports
- [ ] Endpoint Analytics integration
- [ ] Configuration Manager (SCCM) co-management
- [ ] Intune Suite features (Privilege Management, Enterprise App Management)

---

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for:

- Bug fixes
- New tool implementations
- Documentation improvements
- Performance optimizations
- Additional file format support

---

## Version History Summary

| Version | Date       | Tools | Key Features                                      |
| ------- | ---------- | ----- | ------------------------------------------------- |
| 1.0.0   | 2025-11-04 | 32    | Initial release with full Entra ID/Intune support |

---

## Migration Notes

### From Pre-release to v1.0.0

This is the initial stable release. No migration needed.

### Breaking Changes

None (initial release)

---

## Security Updates

| Date       | Type    | Description                                  |
| ---------- | ------- | -------------------------------------------- |
| 2025-11-04 | Initial | Secure credential management via .env        |
| 2025-11-04 | Initial | API permission least privilege documentation |

---

**Note:** This changelog follows [Keep a Changelog](https://keepachangelog.com/) format and adheres to [Semantic Versioning](https://semver.org/).

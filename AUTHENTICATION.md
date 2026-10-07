# Authentication Modes for MCP Entra Server

## Two Authentication Options

### 1. App Authentication (Service Principal) - Current Default

- Files show as modified by "SharePoint app"
- Requires: `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_CLIENT_SECRET`
- Best for: Automated tasks, background processes
- Set: `AUTH_MODE=app` in `.env`

Since this mode uses client-credentials auth (the `https://graph.microsoft.com/.default` scope), it needs **Application** permissions with admin consent, not delegated ones. Add all of the following under **API permissions** → **Add a permission** → **Microsoft Graph** → **Application permissions**, then **Grant admin consent**:

| Permission | Enables |
| --- | --- |
| `User.ReadWrite.All` | `create_user`, `set_user_mail`, `get_user_info`, `list_users` |
| `User-PasswordProfile.ReadWrite.All` | `set_user_password` (`User.ReadWrite.All` does not cover password changes) |
| `Group.Read.All` | `list_groups`, `get_group_details`, `get_group_members` |
| `Sites.ReadWrite.All` | `list_sharepoint_sites`, `create_file_in_sharepoint` |
| `Files.ReadWrite.All` | `create_file_in_onedrive`, `create_word_document`, `create_excel_workbook`, `create_powerpoint_presentation`, `create_csv_file`, `read_csv_file`, `convert_file_to_pdf`, `export_powerpoint_slide_as_image`, `create_odf_document` |
| `DeviceManagementManagedDevices.Read.All` | `list_intune_devices` |
| `DeviceManagementConfiguration.Read.All` | `list_intune_compliance_policies`, `list_intune_configuration_policies`, `list_intune_filters`, `list_intune_scripts`, `list_android_management_profiles`, `list_ios_management_profiles` |
| `DeviceManagementApps.Read.All` | `list_intune_applications`, `list_app_protection_policies` |
| `DeviceManagementServiceConfig.Read.All` | `list_autopilot_profiles`, `list_autopilot_devices`, `list_enrollment_status_page_profiles`, `list_microsoft_tunnel_sites`, `list_microsoft_tunnel_servers`, `list_intune_ad_connectors`, `list_intune_certificate_connectors` |

All the `list_*`/`get_*` tools only read, so their `.Read.All` grants are sufficient; only the create/patch tools (users, mail, password, files) need `ReadWrite.All`.

The same application permissions apply with `AUTH_MODE=managed_identity` (the Azure-hosted deployment). The portal cannot grant Graph permissions to a managed identity, so assign each one to the identity's service principal with Microsoft Graph, for example:

```bash
MI_SP_ID=$(az ad sp list --display-name <app-service-name> --query "[0].id" -o tsv)
GRAPH_SP_ID=$(az ad sp show --id 00000003-0000-0000-c000-000000000000 --query id -o tsv)
ROLE_ID=$(az ad sp show --id 00000003-0000-0000-c000-000000000000 --query "appRoles[?value=='User-PasswordProfile.ReadWrite.All'].id" -o tsv)
az rest --method POST --url "https://graph.microsoft.com/v1.0/servicePrincipals/$MI_SP_ID/appRoleAssignments" \
  --body "{\"principalId\":\"$MI_SP_ID\",\"resourceId\":\"$GRAPH_SP_ID\",\"appRoleId\":\"$ROLE_ID\"}"
```

New permissions only take effect in a newly issued token. With `AUTH_MODE=managed_identity` on App Service, the platform caches managed identity tokens for up to 24 hours, and restarting the app does not clear that cache, so a newly granted permission can take up to a day to apply.

### 2. User Authentication (Delegated Permissions)

- Files show as modified by the logged-in user
- Requires: `AZURE_CLIENT_ID`, `AZURE_TENANT_ID` (no secret needed)
- Best for: Interactive use, user context needed
- Set: `AUTH_MODE=user` in `.env`

## Setup for User Authentication

### Step 1: Configure App Registration in Azure Portal

1. Go to **Azure Portal** → **Microsoft Entra ID** → **App registrations**
2. Find your app: `e4c27331-3fee-4cb0-8932-3c9bda313025`
3. Go to **Authentication** tab:
   - Click **Add a platform** → **Mobile and desktop applications**
   - Add redirect URI: `http://localhost`
   - Enable **Public client flows**: Yes
4. Go to **API permissions** tab:
   - Remove application permissions (if any)
   - Add **Delegated permissions**:
     - `User.ReadWrite.All`
     - `User-PasswordProfile.ReadWrite.All`
     - `Group.Read.All`
     - `Sites.ReadWrite.All`
     - `Files.ReadWrite.All`
     - `DeviceManagementManagedDevices.Read.All`
     - `DeviceManagementConfiguration.Read.All`
     - `DeviceManagementApps.Read.All`
     - `DeviceManagementServiceConfig.Read.All`
   - Click **Grant admin consent**
   - See the permission table above for which tools each one enables (same mapping applies to the delegated equivalents)

### Step 2: Update .env file

```env
AUTH_MODE=user

AZURE_CLIENT_ID=e4c27331-3fee-4cb0-8932-3c9bda313025
AZURE_TENANT_ID=b41f1ee6-0ebd-4439-bbbc-07b635f451e0
# AZURE_CLIENT_SECRET not needed for user mode
```

### Step 3: Test User Authentication

Run any tool and you'll see a browser window open for login:

```bash
python -c "from entra_server import list_groups; import json; print(json.dumps(list_groups(), indent=2))"
```

You'll be prompted to sign in. After signing in once, the token is cached.

## Comparison

| Feature          | App Auth         | User Auth         |
| ---------------- | ---------------- | ----------------- |
| Files created by | "SharePoint app" | Your user account |
| Sign-in required | No               | Yes (first time)  |
| Audit trail      | App identity     | User identity     |
| Best for         | Automation       | Interactive use   |
| Permissions      | Application      | Delegated         |

## Switching Between Modes

Simply change `AUTH_MODE` in `.env`:

- `AUTH_MODE=app` - Use service principal
- `AUTH_MODE=user` - Use interactive user login

No code changes needed!

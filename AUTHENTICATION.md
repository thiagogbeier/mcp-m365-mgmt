# Authentication Modes for MCP Entra Server

## Two Authentication Options

### 1. App Authentication (Service Principal) - Current Default

- Files show as modified by "SharePoint app"
- Requires: `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_CLIENT_SECRET`
- Best for: Automated tasks, background processes
- Set: `AUTH_MODE=app` in `.env`

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
     - `Group.Read.All`
     - `DeviceManagementManagedDevices.Read.All`
     - `Sites.ReadWrite.All`
     - `Files.ReadWrite.All`
   - Click **Grant admin consent**

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

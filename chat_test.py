"""
Interactive chat-like test client for MCP M365 Management Server
Test your MCP tools without Claude Desktop
"""

import json
import sys
from datetime import datetime
from mcp_m365_mgmt import (
    list_users, list_groups, get_group_details, get_group_members, get_user_info,
    list_intune_devices, list_intune_compliance_policies, list_intune_configuration_policies,
    list_intune_filters, list_intune_scripts, list_intune_applications,
    list_autopilot_profiles, list_autopilot_devices, list_enrollment_status_page_profiles,
    list_android_management_profiles, list_ios_management_profiles, list_app_protection_policies,
    list_microsoft_tunnel_sites, list_microsoft_tunnel_servers, list_intune_ad_connectors,
    list_intune_certificate_connectors, list_sharepoint_sites,
    create_file_in_onedrive, create_file_in_sharepoint
)

def print_table(headers, rows, title=None):
    """Print data in a formatted table."""
    if title:
        print(f"\n{'=' * 100}")
        print(f"  {title}")
        print(f"{'=' * 100}")
    
    if not rows:
        print("\n📭 No data found.")
        return
    
    # Calculate column widths
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))
    
    # Print header
    print()
    header_row = " | ".join(str(h).ljust(w) for h, w in zip(headers, col_widths))
    print(header_row)
    print("-" * len(header_row))
    
    # Print rows
    for row in rows:
        print(" | ".join(str(cell).ljust(w) for cell, w in zip(row, col_widths)))
    
    print(f"\n📊 Total: {len(rows)} items")

def format_datetime(dt_str):
    """Format datetime string to readable format."""
    if not dt_str:
        return "N/A"
    try:
        dt = datetime.fromisoformat(dt_str.replace('Z', '+00:00'))
        return dt.strftime('%Y-%m-%d %H:%M')
    except:
        return dt_str

def print_banner():
    print("=" * 80)
    print("  MCP M365 Management - Interactive Test Console")
    print("  Chat-like experience for testing MCP tools")
    print("=" * 80)
    print()

def print_menu():
    print("\n" + "─" * 80)
    print("📋 Available Commands:")
    print("─" * 80)
    print("  User & Group Management:")
    print("    users                    - List all users")
    print("    user info <id>           - Get detailed user info")
    print("    groups                   - List all groups")
    print("    group details <id>       - Get detailed group info")
    print("    group members <id>       - Get group members")
    print()
    print("  Intune Device Management:")
    print("    devices                  - List Intune devices")
    print("    compliance               - List compliance policies")
    print("    configs                  - List configuration policies")
    print("    filters                  - List assignment filters")
    print("    scripts                  - List PowerShell/Shell scripts")
    print("    apps                     - List applications")
    print()
    print("  Autopilot:")
    print("    autopilot profiles       - List Autopilot profiles")
    print("    autopilot devices        - List Autopilot devices")
    print("    esp                      - List ESP profiles")
    print()
    print("  Mobile Management:")
    print("    android                  - List Android profiles")
    print("    ios                      - List iOS profiles")
    print("    mam                      - List app protection policies")
    print()
    print("  Infrastructure:")
    print("    tunnel sites             - List Microsoft Tunnel sites")
    print("    tunnel servers           - List tunnel servers")
    print("    ad connectors            - List AD connectors")
    print("    cert connectors          - List certificate connectors")
    print()
    print("  SharePoint:")
    print("    sites                    - List SharePoint sites")
    print()
    print("  Other:")
    print("    help                     - Show this menu")
    print("    exit / quit              - Exit console")
    print("─" * 80)

def pretty_print(data, title=None, data_type=None):
    """Pretty print data as tables or details."""
    if 'error' in data:
        print(f"\n❌ Error: {data.get('error')}")
        print(f"Status Code: {data.get('status_code', 'Unknown')}")
        return
    
    # Handle list data
    if data_type == 'groups':
        groups = data.get('groups', [])
        if not groups:
            print("\n📭 No groups found.")
            return
        headers = ['Display Name', 'Type', 'Mail', 'Created']
        rows = []
        for g in groups[:50]:  # Limit to first 50
            g_type = []
            if g.get('securityEnabled'):
                g_type.append('Security')
            if g.get('mailEnabled'):
                g_type.append('Mail')
            if 'Unified' in g.get('groupTypes', []):
                g_type.append('M365')
            
            rows.append([
                (g.get('displayName') or '')[:40],
                ', '.join(g_type) or 'N/A',
                (g.get('mail') or 'N/A')[:30],
                format_datetime(g.get('createdDateTime'))
            ])
        print_table(headers, rows, title or 'Groups')
        if len(groups) > 50:
            print(f"\n⚠️  Showing first 50 of {len(groups)} groups")
    
    elif data_type == 'users':
        users = data.get('users', [])
        if not users:
            print("\n� No users found.")
            return
        headers = ['Display Name', 'UPN', 'Mail', 'Job Title']
        rows = []
        for u in users[:50]:
            rows.append([
                (u.get('displayName') or '')[:30],
                (u.get('userPrincipalName') or '')[:40],
                (u.get('mail') or 'N/A')[:30],
                (u.get('jobTitle') or 'N/A')[:25]
            ])
        print_table(headers, rows, title or 'Users')
        if len(users) > 50:
            print(f"\n⚠️  Showing first 50 of {len(users)} users")
    
    elif data_type == 'devices':
        devices = data.get('devices', [])
        if not devices:
            print("\n� No devices found.")
            return
        headers = ['Device Name', 'OS', 'Version', 'Compliance', 'Last Sync']
        rows = []
        for d in devices[:50]:
            rows.append([
                (d.get('deviceName') or '')[:25],
                (d.get('operatingSystem') or '')[:15],
                (d.get('osVersion') or '')[:10],
                (d.get('complianceState') or '')[:15],
                format_datetime(d.get('lastSyncDateTime'))
            ])
        print_table(headers, rows, title or 'Devices')
        if len(devices) > 50:
            print(f"\n⚠️  Showing first 50 of {len(devices)} devices")
    
    elif data_type == 'sites':
        sites = data.get('sites', [])
        if not sites:
            print("\n📭 No SharePoint sites found.")
            return
        headers = ['Display Name', 'Name', 'Web URL']
        rows = []
        for s in sites[:50]:
            rows.append([
                (s.get('displayName') or '')[:30],
                (s.get('name') or '')[:30],
                (s.get('webUrl') or '')[:60]
            ])
        print_table(headers, rows, title or 'SharePoint Sites')
        if len(sites) > 50:
            print(f"\n⚠️  Showing first 50 of {len(sites)} sites")
    
    elif data_type == 'details':
        # Show detailed view for single item
        print(f"\n{'=' * 100}")
        if title:
            print(f"  {title}")
        print(f"{'=' * 100}\n")
        
        for key, value in data.items():
            if key not in ['error', 'status_code']:
                formatted_key = key.replace('_', ' ').title()
                if isinstance(value, list):
                    print(f"{formatted_key:.<40} {', '.join(str(v) for v in value) if value else 'N/A'}")
                elif 'DateTime' in key or 'Date' in key:
                    print(f"{formatted_key:.<40} {format_datetime(value)}")
                else:
                    val_str = str(value) if value is not None else 'N/A'
                    print(f"{formatted_key:.<40} {val_str[:60]}")
    
    else:
        # Fallback to JSON for unknown types
        if title:
            print(f"\n{'=' * 80}")
            print(f"  {title}")
            print(f"{'=' * 80}")
        print(json.dumps(data, indent=2)[:2000])  # Limit output

def handle_command(command):
    parts = command.lower().strip().split(maxsplit=2)
    cmd = parts[0] if parts else ""
    
    try:
        if cmd in ['exit', 'quit']:
            print("\n👋 Goodbye!")
            return False
        
        elif cmd == 'help':
            print_menu()
        
        elif cmd == 'users':
            print("\n🔄 Fetching users...")
            result = list_users()
            pretty_print(result, "All Users", data_type='users')
        
        elif cmd == 'groups':
            print("\n🔄 Fetching groups...")
            result = list_groups()
            pretty_print(result, "All Groups", data_type='groups')
        
        elif cmd == 'group' and len(parts) >= 3:
            action = parts[1]
            group_id = parts[2]
            
            if action == 'details':
                print(f"\n🔄 Fetching group details for {group_id}...")
                result = get_group_details(group_id)
                pretty_print(result, "Group Details", data_type='details')
            elif action == 'members':
                print(f"\n🔄 Fetching group members for {group_id}...")
                result = get_group_members(group_id)
                pretty_print(result, "Group Members", data_type='users')
        
        elif cmd == 'user' and len(parts) >= 3:
            if parts[1] == 'info':
                user_id = parts[2]
                print(f"\n🔄 Fetching user info for {user_id}...")
                result = get_user_info(user_id)
                pretty_print(result, "User Information", data_type='details')
        
        elif cmd == 'devices':
            print("\n🔄 Fetching Intune devices...")
            result = list_intune_devices()
            pretty_print(result, "Intune Managed Devices", data_type='devices')
        
        elif cmd == 'compliance':
            print("\n🔄 Fetching compliance policies...")
            result = list_intune_compliance_policies()
            pretty_print(result, "Compliance Policies")
        
        elif cmd == 'configs':
            print("\n🔄 Fetching configuration policies...")
            result = list_intune_configuration_policies()
            pretty_print(result, "Configuration Policies")
        
        elif cmd == 'filters':
            print("\n🔄 Fetching assignment filters...")
            result = list_intune_filters()
            pretty_print(result, "Assignment Filters")
        
        elif cmd == 'scripts':
            print("\n🔄 Fetching scripts...")
            result = list_intune_scripts()
            pretty_print(result, "PowerShell & Shell Scripts")
        
        elif cmd == 'apps':
            print("\n🔄 Fetching applications...")
            result = list_intune_applications()
            pretty_print(result, "Mobile Applications")
        
        elif cmd == 'autopilot' and len(parts) >= 2:
            if parts[1] == 'profiles':
                print("\n🔄 Fetching Autopilot profiles...")
                result = list_autopilot_profiles()
                pretty_print(result, "Autopilot Deployment Profiles")
            elif parts[1] == 'devices':
                print("\n🔄 Fetching Autopilot devices...")
                result = list_autopilot_devices()
                pretty_print(result, "Autopilot Registered Devices")
        
        elif cmd == 'esp':
            print("\n🔄 Fetching ESP profiles...")
            result = list_enrollment_status_page_profiles()
            pretty_print(result, "Enrollment Status Page Profiles")
        
        elif cmd == 'android':
            print("\n🔄 Fetching Android profiles...")
            result = list_android_management_profiles()
            pretty_print(result, "Android Management Profiles")
        
        elif cmd == 'ios':
            print("\n🔄 Fetching iOS profiles...")
            result = list_ios_management_profiles()
            pretty_print(result, "iOS Management Profiles")
        
        elif cmd == 'mam':
            print("\n🔄 Fetching app protection policies...")
            result = list_app_protection_policies()
            pretty_print(result, "App Protection Policies (MAM)")
        
        elif cmd == 'tunnel' and len(parts) >= 2:
            if parts[1] == 'sites':
                print("\n🔄 Fetching Microsoft Tunnel sites...")
                result = list_microsoft_tunnel_sites()
                pretty_print(result, "Microsoft Tunnel Sites")
            elif parts[1] == 'servers':
                print("\n🔄 Fetching Microsoft Tunnel servers...")
                result = list_microsoft_tunnel_servers()
                pretty_print(result, "Microsoft Tunnel Servers")
        
        elif cmd == 'ad' and len(parts) >= 2 and parts[1] == 'connectors':
            print("\n🔄 Fetching AD connectors...")
            result = list_intune_ad_connectors()
            pretty_print(result, "Active Directory Connectors")
        
        elif cmd == 'cert' and len(parts) >= 2 and parts[1] == 'connectors':
            print("\n🔄 Fetching certificate connectors...")
            result = list_intune_certificate_connectors()
            pretty_print(result, "Certificate Connectors")
        
        elif cmd == 'sites':
            print("\n🔄 Fetching SharePoint sites...")
            result = list_sharepoint_sites()
            pretty_print(result, "SharePoint Sites", data_type='sites')
        
        else:
            print(f"\n❌ Unknown command: '{command}'")
            print("💡 Type 'help' to see available commands")
    
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
    
    return True

def main():
    print_banner()
    print("🔐 Authentication will be loaded from .env file")
    print("💡 Type 'help' to see all available commands")
    
    while True:
        try:
            command = input("\n> ").strip()
            if not command:
                continue
            
            if not handle_command(command):
                break
                
        except KeyboardInterrupt:
            print("\n\n👋 Interrupted. Type 'exit' to quit gracefully.")
            continue
        except EOFError:
            print("\n👋 Goodbye!")
            break

if __name__ == "__main__":
    main()

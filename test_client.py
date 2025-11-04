# Test to call the tools directly (now with real Graph API)
from mcp_m365_mgmt import list_intune_devices
import json

print("Testing list_intune_devices tool...")
print("-" * 50)
print("Note: This will prompt you to sign in to your Microsoft tenant")
print()

result = list_intune_devices()

print("\nResult:")
print(json.dumps(result, indent=2))

import requests
import json
import os

# Load environment variables from .env file
def load_env():
    if os.path.exists('.env'):
        with open('.env') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value

# Main function
def main():
    print("Scenario AI MCP Server - Get Asset Details Example")
    print("===============================================\n")
    
    # Load environment variables
    load_env()
    
    # Check if the server is running
    try:
        response = requests.get("http://localhost:3000/status")
        if response.status_code != 200:
            print("Error: Server is not running. Please start the server first.")
            return
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server. Please start the server first.")
        return
    
    print("Server is running!\n")
    
    # Example: Get asset details
    print("Getting asset details...")
    
    asset_id = "asset_987654321"  # This would be the asset ID to check
    
    print(f"Asset ID: '{asset_id}'")
    
    # In a real implementation, this would use the MCP SDK to access the asset resource
    # For this example, we'll just simulate the process
    
    # Simulate asset data
    asset_data = {
        "assetId": asset_id,
        "type": "image",
        "createdAt": "2025-04-13T01:00:10Z",
        "url": "https://api.cloud.scenario.com/v1/assets/asset_987654321",
        "metadata": {
            "width": 1024,
            "height": 1024,
            "format": "png"
        }
    }
    
    print("\nAsset details:")
    print(json.dumps(asset_data, indent=2))

if __name__ == "__main__":
    main()
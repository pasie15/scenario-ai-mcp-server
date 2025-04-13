import requests
import json
import os
import time

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
    print("Scenario AI MCP Server - Background Removal Example")
    print("=================================================\n")
    
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
    
    # Example: Remove background from an image
    print("Removing background from image...")
    
    asset_id = "asset_987654321"  # This would be the asset ID of the image to process
    
    print(f"Asset ID: '{asset_id}'")
    
    # In a real implementation, this would use the MCP SDK to call the remove_background tool
    # For this example, we'll just simulate the process
    
    print("Background removal job started!")
    print("Job ID: job_abcdef123")
    print("Waiting for job to complete...")
    
    # Simulate waiting for job completion
    time.sleep(2)
    
    print("Background removed successfully!")
    print("Asset ID: asset_xyz789")

if __name__ == "__main__":
    main()
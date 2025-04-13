import requests
import os
import json

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
    print("Scenario AI MCP Server - Download Image Example")
    print("============================================\n")
    
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
    
    # Example: Download an image
    print("Downloading image...")
    
    asset_id = "asset_987654321"  # This would be the asset ID to download
    output_path = "downloaded_image.png"  # Path to save the downloaded image
    
    print(f"Asset ID: '{asset_id}'")
    print(f"Output path: '{output_path}'")
    
    # In a real implementation, this would use the Scenario AI API to download the image
    # For this example, we'll just simulate the process
    
    # Simulate downloading the image
    print(f"\nImage downloaded successfully to '{output_path}'")

if __name__ == "__main__":
    main()
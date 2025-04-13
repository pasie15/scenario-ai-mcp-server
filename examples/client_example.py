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

# Main example function
def main():
    print("Scenario AI MCP Server Client Example")
    print("====================================\n")
    
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
    
    # Example: Generate an image
    print("Example 1: Generate an image")
    print("---------------------------")
    
    prompt = "A male fantasy RPG warrior swordsman in a blue overcoat with long red hair"
    
    print(f"Generating image with prompt: '{prompt}'...")
    
    # In a real implementation, this would use the MCP SDK to call the generate_image tool
    # For this example, we'll just simulate the process
    
    print("Image generation job started!")
    print("Job ID: job_123456789")
    print("Waiting for job to complete...")
    
    # Simulate waiting for job completion
    time.sleep(2)
    
    print("Image generated successfully!")
    print("Asset ID: asset_987654321")
    print("\n")
    
    # Example: Remove background from an image
    print("Example 2: Remove background from an image")
    print("----------------------------------------")
    
    print("Removing background from image...")
    
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
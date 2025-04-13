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
    print("Scenario AI MCP Server - Get Job Data Example")
    print("===========================================\n")
    
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
    
    # Example: Get job data by job ID
    print("Getting job data...")
    
    job_id = "job_123456789"  # This would be the job ID to check
    
    print(f"Job ID: '{job_id}'")
    
    # In a real implementation, this would use the MCP SDK to access the job resource
    # For this example, we'll just simulate the process
    
    # Simulate job data
    job_data = {
        "jobId": job_id,
        "status": "completed",
        "createdAt": "2025-04-13T01:00:00Z",
        "completedAt": "2025-04-13T01:00:10Z",
        "result": {
            "assetId": "asset_987654321"
        }
    }
    
    print("\nJob data:")
    print(json.dumps(job_data, indent=2))

if __name__ == "__main__":
    main()
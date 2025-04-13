import os
import requests
import base64
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

# Load environment variables from .env file in the root directory
load_dotenv()

# Initialize the FastMCP server
mcp = FastMCP("ScenarioAIServer", log_level="ERROR")

# Environment variables
API_KEY = os.environ.get("SCENARIO_API_KEY")
API_SECRET = os.environ.get("SCENARIO_API_SECRET")
DEFAULT_MODEL = os.environ.get("SCENARIO_MODEL_ID", "model_KMeeJU9mpcfHKB7a1hv9vyW9")

# Base URL for Scenario API
BASE_URL = "https://api.cloud.scenario.com/v1"

# Create authorization header
auth_string = f"{API_KEY}:{API_SECRET}"
auth_bytes = auth_string.encode('ascii')
auth_b64 = base64.b64encode(auth_bytes).decode('ascii')
AUTH_HEADER = f"Basic {auth_b64}"

# Common headers
def get_headers():
    return {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": AUTH_HEADER
    }

@mcp.tool()
def generate_image(prompt: str, model_id: str = None, negative_prompt: str = "", num_samples: int = 1) -> dict:
    """
    Generate an image using Scenario AI's txt2img endpoint.
    
    Args:
        prompt: The text prompt describing the image to generate
        model_id: The model ID to use (defaults to environment variable)
        negative_prompt: Text describing what to avoid in the image
        num_samples: Number of images to generate
        
    Returns:
        dict: Response containing job_id and other details
    """
    url = f"{BASE_URL}/generate/txt2img"
    
    # Use provided model_id or fall back to default
    model_id = model_id or DEFAULT_MODEL
    
    payload = {
        "hideResults": False,
        "aspectRatio": "1:1",
        "intermediateImages": False,
        "modelId": model_id,
        "negativePrompt": negative_prompt,
        "prompt": prompt,
        "numSamples": num_samples
    }
    
    response = requests.post(url, json=payload, headers=get_headers())
    response_data = response.json()
    
    # Extract job_id from response
    job_id = response_data.get("job", {}).get("jobId")
    
    return {"job_id": job_id, "full_response": response_data}

@mcp.resource("job://{job_id}")
def get_job_status(job_id: str) -> dict:
    """
    Get the status and details of a specific job.
    
    Args:
        job_id: The ID of the job to retrieve
        
    Returns:
        dict: Job data and status
    """
    url = f"{BASE_URL}/jobs/{job_id}"
    
    response = requests.get(url, headers=get_headers())
    job_data = response.json()
    
    return job_data

@mcp.resource("asset://{asset_id}")
def get_asset(asset_id: str) -> dict:
    """
    Get the details of a specific asset.
    
    Args:
        asset_id: The ID of the asset to retrieve
        
    Returns:
        dict: Asset details
    """
    url = f"{BASE_URL}/assets/{asset_id}"
    
    response = requests.get(url, headers=get_headers())
    asset_details = response.json()
    
    return asset_details

@mcp.tool()
def remove_background(asset_id: str) -> dict:
    """
    Remove the background from an image.
    
    Args:
        asset_id: The asset ID of the image to process
        
    Returns:
        dict: Response containing the processed asset and job information.
              The job ID can be used to check the status of the background removal.
              Once complete, the asset ID from the job data can be used to get the image without background.
    """
    url = f"{BASE_URL}/images/erase-background"
    
    payload = {"image": asset_id}
    
    response = requests.put(url, json=payload, headers=get_headers())
    result = response.json()
    
    return result

@mcp.resource("status://info")
def get_status() -> dict:
    """
    Get the status of the MCP server.
    
    Returns:
        dict: Status information
    """
    return {
        "status": "ok",
        "api_key_configured": bool(API_KEY),
        "api_secret_configured": bool(API_SECRET),
        "default_model": DEFAULT_MODEL
    }

if __name__ == "__main__":
    # Start the MCP server
    mcp.run()
# Scenario AI MCP Server

This project provides a Model Context Protocol (MCP) server for the Scenario AI API. The server allows you to generate images from text prompts and remove backgrounds from images using the Scenario AI platform (https://app.scenario.com/).

## Repository Structure

The repository is organized as follows:

- **src/**: Core source code and configuration files
  - `server.py`: Main MCP server implementation
  - `mcp_settings.json`: Server configuration
  - `requirements.txt`: Project dependencies
  - `setup.py`: Installation script
  - `.gitignore`: Git ignore rules
  - `remove_bg_command.txt`: Command reference for background removal
  
- **examples/**: Example scripts demonstrating API usage
  - `client_example.py`: Main example client
  - `Get the details of an asset.py`: Example of retrieving asset details
  - `Trigger a new image generation in Txt2Img mode.py`: Example of generating images
  - `Erase background from image.py`: Example of background removal
  - `Get job data by job ID.py`: Example of checking job status
  - `download_image.py`: Example of downloading generated images

- **scripts/**: Utility scripts for running the server and examples
  - `start_server.bat`/`start_server.sh`: Scripts to start the MCP server using the `mcp dev` command
  - `run_client_example.bat`/`run_client_example.sh`: Scripts to run the example client that demonstrates how to use the MCP server
  - `run_tests.bat`/`run_tests.sh`: Scripts to run the test suite that verifies the MCP server functionality

- **tests/**: Test files
  - `test_server.py`: Tests and documentation for the MCP server

- **assets/**: Sample images and resources
  - `warrior_no_background.png`: Sample image with background removed
  - `warrior_with_background.jpg`: Sample original image

- **docs/**: Documentation
  - `README.md`: Project documentation
  - `DESIGN_PLAN.md`: Design documentation

- **scenario-ai/**: Virtual environment for the project

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r src/requirements.txt
   ```
3. Create a `.env` file with your Scenario AI API credentials:
   ```
   SCENARIO_API_KEY=your_api_key
   SCENARIO_API_SECRET=your_api_secret
   SCENARIO_MODEL_ID=your_default_model_id  # Optional
   ```
   
   4. Install the MCP SDK:
      ```
      pip install mcp
      ```

## Running the Server

To run the server:

```bash
python src/server.py
```

Or use the provided scripts:

```bash
# Windows
scripts/start_server.bat

# Linux/macOS
./scripts/start_server.sh
```

## Available MCP Tools

The Scenario AI MCP Server provides the following tools that can be used with the Roo-Cline interface:

### Tools

1. **generate_image**: Generate an image from a text prompt
   - Parameters:
     - `prompt` (required): The text prompt describing the image to generate
     - `model_id` (optional): The model ID to use (defaults to environment variable)
     - `negative_prompt` (optional): Text describing what to avoid in the image
     - `num_samples` (optional): Number of images to generate

2. **remove_background**: Remove the background from an image
   - Parameters:
     - `asset_id` (required): The asset ID of the image to process

### Resources

1. **status://info**: Get information about the server status
2. **job://{job_id}**: Get information about a job
3. **asset://{asset_id}**: Get information about an asset

## Using the Examples

See the `examples/client_example.py` file for an example of how to use the server.

To run the example client:

```bash
# Windows
scripts/run_client_example.bat

# Linux/macOS
./scripts/run_client_example.sh
```

## Scripts

The `scripts/` directory contains utility scripts to help you run the server, examples, and tests:

### Server Scripts
- `start_server.bat` (Windows) / `start_server.sh` (Linux/macOS):
  These scripts start the MCP server using the `mcp dev` command, which runs the server in development mode.
  
  Usage:
  ```bash
  # Windows
  scripts/start_server.bat
  
  # Linux/macOS
  ./scripts/start_server.sh
  ```

### Example Scripts
- `run_client_example.bat` (Windows) / `run_client_example.sh` (Linux/macOS):
  These scripts run the example client that demonstrates how to use the MCP server.
  
  Usage:
  ```bash
  # Windows
  scripts/run_client_example.bat
  
  # Linux/macOS
  ./scripts/run_client_example.sh
  ```

### Test Scripts
- `run_tests.bat` (Windows) / `run_tests.sh` (Linux/macOS):
  These scripts run the test suite that verifies the MCP server functionality.
  
  Usage:
  ```bash
  # Windows
  scripts/run_tests.bat
  
  # Linux/macOS
  ./scripts/run_tests.sh
  ```

## Running Tests and Viewing Documentation

To run the tests and view the documentation:

```bash
# Windows
scripts/run_tests.bat

# Linux/macOS
./scripts/run_tests.sh
```

The `test_server.py` file provides comprehensive documentation on how to use the Scenario AI MCP Server, including:
- Server setup instructions
- Available tools and their parameters
- Available resources
- Example usage with the Roo-Cline interface
- A complete workflow for generating images and removing backgrounds

Running the tests will display this documentation, which serves as a guide for using the MCP server.

## Troubleshooting

### Server Won't Start

If you encounter issues starting the server, check the following:

1. Make sure the MCP SDK is installed:
   ```
   pip install mcp
   ```

2. Check that your Python environment has all the required dependencies:
   ```
   pip install -r src/requirements.txt
   ```

3. Verify that your `.env` file or environment variables are set correctly with your Scenario AI API credentials.

4. If you're using a virtual environment, make sure it's activated before running the server.

### API Errors

If you encounter errors when using the API:

1. Check that your API credentials are correct.
2. Verify that the model ID you're using is valid.
3. Check the Scenario AI API documentation for any service disruptions or changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
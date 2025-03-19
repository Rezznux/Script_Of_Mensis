![image](https://github.com/user-attachments/assets/717faae1-e7ab-48aa-a3a7-09bafbc9d4af)

# Script_of_Mensis

A specialized security tool for analyzing URLs that employ bot detection techniques to hide malicious content.

## Overview

Script_of_Mensis helps security researchers detect and analyze URLs that attempt to evade detection by presenting different content to automated scanners versus real users. The tool uses advanced browser automation techniques to bypass common bot detection methods, allowing it to see what a real user would experience.

## Features

- **Bot Detection Bypass**: Uses undetected-chromedriver and advanced fingerprinting evasion
- **Multi-Service Integration**: Correlates findings with VirusTotal and URLScan.io
- **Network Request Capture**: Records all resources loaded during page navigation
- **Redirection Chain Analysis**: Tracks initial and final URLs to detect evasion techniques
- **Parallel Processing**: Efficiently analyze multiple URLs simultaneously
- **Cookie & Session Handling**: Maintains state between scans
- **IP Rotation**: Supports proxy configuration to avoid IP-based blocking
- **User-Agent Rotation**: Randomizes browser fingerprints to appear more human-like

## Installation

### Prerequisites

- Python 3.8 or higher
- Chrome browser
- VirusTotal and URLScan.io API keys (optional but recommended)

### Installation Steps

```bash
# Clone the repository
git clone https://github.com/Rezznux/Script_of_Mensis.git
cd Script_of_Mensis

# Install the package
pip install -e .

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
```

## Usage

After installation, you can use the `vileblood` command directly:

```bash
# Analyze a single URL
vileblood --url "https://suspicious-url.example.com"

# Analyze multiple URLs from a file
vileblood --file data/samples/suspicious_urls.txt --output data/results/analysis.json

# Use with advanced options
vileblood --url "https://suspicious-url.example.com" --proxy-enabled --behavior-simulation
```

## Configuration

Create a `.env` file based on `.env.example` with your API keys and basic settings.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is designed for security research purposes only. Only use it to analyze URLs you have permission to test.

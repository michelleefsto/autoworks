# AutoWorks

AutoWorks is a Python-based program designed to monitor and alert users to potential privacy risks on Windows devices. Its primary goal is to protect personal information by identifying suspicious processes and checking Windows privacy settings.

## Features

- **Process Monitoring**: Detects and alerts the user about known suspicious processes.
- **Privacy Settings Check**: Reviews Windows privacy settings for potential risks.
- **User Alerts**: Notifies users of any identified threats to their privacy.

## Requirements

- Python 3.x
- `psutil` library (can be installed via `pip install psutil`)

## Installation

1. Clone the repository or download the `autoworks.py` file.
2. Ensure you have Python 3.x installed on your system.
3. Install the required library using pip:
   ```bash
   pip install psutil
   ```

## Usage

To run the AutoWorks program, use the following command in your terminal:

```bash
python autoworks.py
```

AutoWorks will continuously monitor your Windows system for privacy risks, checking every minute. Alerts will be logged in `autoworks.log` and printed to the console.

## Compatibility

AutoWorks is designed to run on Windows systems only. Running it on other operating systems will result in an error message.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Disclaimer

AutoWorks is a basic tool for monitoring common privacy risks. It should not be considered a replacement for comprehensive security software. Always ensure you have up-to-date antivirus software for full protection.
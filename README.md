# Vulnerability Scanner

## Overview

The Vulnerability Scanner is a Python script designed to check for inappropriate file and directory permissions in a specified directory. It logs the results and optionally fixes any permissions issues found.

## Features

- Scans directories and files for inappropriate permissions.
- Logs warnings and errors to a log file.
- Optionally fixes inappropriate permissions.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/vulnerability-scanner.git
    cd vulnerability-scanner
    ```

2. Ensure you have the necessary permissions to run the script and modify file permissions.

## Usage

1. Basic scan without fixing permissions:
    ```sh
    python vulnerability_scan.py /path/to/directory
    ```

2. Scan and fix inappropriate permissions:
    ```sh
    python vulnerability_scan.py /path/to/directory --fix
    ```

### Command Line Arguments

- `directory`: The directory to scan.
- `--fix`: Optional argument to fix inappropriate permissions.

### Example

```sh
python vulnerability_scan.py /home/user/documents --fix
```

## Logging

The script logs its activities in a file named `vulnerability_scan.log`. The log includes:

- Start and completion of the scan.
- Warnings for directories and files with inappropriate permissions.
- Information about fixed permissions.
- Errors encountered during the scan.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the need to maintain secure file and directory permissions in various environments.

---

Feel free to customize this README.md according to your specific needs and repository structure.

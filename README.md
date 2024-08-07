Overview

The Automated Penetration Testing Framework is a modular and extensible framework designed to automate common penetration testing tasks such as network scanning, vulnerability assessment, and password cracking. This tool integrates various open-source utilities under a unified CLI interface, making it easier for security professionals and enthusiasts to conduct comprehensive security assessments.
Features

  1. Modular Design: Easily extend the framework by adding new modules.
  2.  Network Scanning: Scan networks for open ports and services.
  3. Vulnerability Assessment: Identify potential vulnerabilities on targets.
  4. Password Cracking: Perform dictionary attacks on hashed passwords.
  5. Customizable Configuration: Configure scanning options and parameters via a YAML file.
  6. Logging: Detailed logging of actions and results for review and reporting.

Installation

    Clone the Repository

    git clone https://github.com/ALBINJoseph01/vapt_framework.git
   
    cd vapt_framework

Install Dependencies

Make sure you have Python 3.x installed, then install the required dependencies:

    pip install -r requirements.txt
    
Set Up the Configuration

Modify the config/settings.yaml file according to your needs:

    yaml

    default_target: "192.168.1.1"
    wordlist_path: "/path/to/wordlist.txt"

Usage

Run the CLI tool to use different modules. Below are some examples:
Network Scanning

Scan a target network for open ports:

    python cli.py network_scanner --target 192.168.1.1

Vulnerability Assessment

Run a vulnerability scan on a specified URL:

    python cli.py vuln_scanner --target https://example.com

Password Cracking

Crack a hashed password using a wordlist:

    python cli.py password_cracker --wordlist /path/to/wordlist.txt

List Available Modules

List all available modules in the framework:

    python cli.py --list-modules

Adding Custom Modules

To add a new module:

    Create a new Python script in the modules/ directory.
    Implement a run() function that the framework can call.
    Load the module using the framework or add it to the configuration.

Contributing

We welcome contributions! To contribute:

    Fork the repository.
    Create a new branch (git checkout -b feature-branch).
    Make your changes and commit them (git commit -m 'Add some feature').
    Push to the branch (git push origin feature-branch).
    Open a Pull Request.

License

This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgements

    Inspired by various open-source security tools.
    Special thanks to the contributors of the open-source community.


# Playwright Automation Practice

This repository contains automation scripts using Playwright with Python for web application testing.

## Prerequisites

To run the automation scripts, make sure you have the following installed:

1. **Python**: A recent version of Python (3.7 or higher) is required.
2. **pip**: Python’s package manager for installing libraries.
3. **venv**: Python’s built-in module for creating virtual environments.

## Setup

### 1. Install Python

#### On Windows:
- Download Python from the official website: [python.org/downloads](https://www.python.org/downloads/)
- During installation, ensure the option **"Add Python to PATH"** is selected.

#### On macOS/Linux:
- You can install Python via a package manager like Homebrew (macOS) or apt (Linux).
    - macOS: `brew install python`
    - Linux: `sudo apt-get install python3`

### 2. Install pip (if not installed)

`pip` is the package installer for Python and is included by default in Python 3. Ensure you have it installed with:

```bash
python -m ensurepip --upgrade
```

To check if `pip` is installed, run:

```bash
pip --version
```

### 3. Set up a Virtual Environment (Optional but Recommended)

It's a good practice to use a **virtual environment** to isolate your dependencies. Follow these steps to create one:

1. Create a virtual environment:

   ```bash
   python -m venv env
   ```

2. Activate the virtual environment:

   - On **Windows**:

     ```bash
     .\env\Scripts\activate
     ```

   - On **macOS/Linux**:

     ```bash
     source env/bin/activate
     ```

   After activation, your command line prompt will change to show that you’re working within the virtual environment.

### 4. Install Dependencies

Now, install the required dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 5. Install Playwright

After installing the dependencies, you also need to install Playwright and the necessary browser binaries:

```bash
python -m playwright install
```

## Running the Automation Tests

To run the tests, you can execute the automation script or use your preferred testing framework. For example:

```bash
pytest ui\tests\test_ui.py -s -v
pytest api\tests\test_api.py -s -v
```


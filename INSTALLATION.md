# Installation Guide

## Setting Up the Python Environment

This guide will help you set up the environment to run the analysis code for the Maldives Cyber Harassment research project.

## Prerequisites

- Python 3.12 or higher installed on your system
- pip (Python package manager)

## Installation Steps

### 1. Create a Virtual Environment (Recommended)

Using a virtual environment keeps your project dependencies isolated:

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Required Packages

Once your virtual environment is activated, install all dependencies:

```bash
pip install -r requirements.txt
```

This will install:
- pandas (data manipulation)
- numpy (numerical operations)
- matplotlib (creating charts)
- seaborn (statistical visualizations)
- openpyxl (Excel file support)
- jupyter (optional, for interactive analysis)

### 3. Verify Installation

Test that everything installed correctly:

```bash
python -c "import pandas, matplotlib, seaborn, numpy; print('All packages installed successfully!')"
```

## Running the Analysis

Once installed, you can run the analysis script:

```bash
python analyze_data.py
```

This will:
- Load the CSV datasets
- Perform statistical analysis
- Generate all visualizations
- Save charts as PNG files

## Updating Packages

To update all packages to their latest versions:

```bash
pip install --upgrade -r requirements.txt
```

## Troubleshooting

**Issue: pip not found**
- Solution: Make sure Python is added to your system PATH

**Issue: Permission denied**
- Solution: Use `pip install --user -r requirements.txt`

**Issue: Packages won't install**
- Solution: Try upgrading pip first: `pip install --upgrade pip`

## Deactivating Virtual Environment

When you're done working:

```bash
deactivate
```

## Package Versions

The requirements.txt file specifies minimum versions that are known to work. You can use newer versions, but if you encounter issues, try installing the specific versions listed.

## Questions?

For issues specific to this project, refer to the README.md or METHODOLOGY.md files.

---

Author: EnderMX  
Last Updated: December 2025

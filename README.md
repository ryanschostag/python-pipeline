# python-pipeline
This is a pipeline implementation written in Python, intended to be used by other repositories as a git submodule. Therefore, the code here will be relatively generic. As use cases grow, so will the robustness of this pipeline.

# Technologies Used
## Python
- Python 3.12.8
### Packages
- pytest 8.3.4 
## Git
- Git 2.47.1.windows.1
## Platform
- Microsoft Windows 10 Pro Version	10.0.19045 Build 19045

# Setup
1. Clone the repository (e.g. git@github.com:ryanschostag/python-pipeline.git)
2. Open a Command Prompt and run the commands as shows below to install dependencies.
```
cd python-pipeline
python -m venv .
Scripts\activate
pip install -r requirements.txt
```
# Testing instructions
1. If not done yet, run all steps in Setup section above.
2. Open a Command Prompt, and run the commands as shown below to run the automated tests.
```
cd python-pipeline\src
pytest -vv --full-trace tests\test_pipeline.py
```

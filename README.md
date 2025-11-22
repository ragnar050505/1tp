# Flask Project - Deployment & Development Commands

This README contains the essential command lines used throughout the lifecycle of this Flask project.

---

## 🔧 Local Development Setup

### Create & activate virtual environment
```bash
# Windows
python -m venv myenv
myenv\Scripts\activate
# Linux / Mac
python3 -m venv myenv
source myenv/bin/activate
```

## 🆕 Starting a New Flask Project from Scratch
### Installing flask
```bash
pip install flask
```

### Run local server
```bash
python app.py
```

## 🛠 Useful Commands
```bash
# see all used libraries
pip list

# Generate requirements.txt 
pip freeze > requirements.txt

# install dependencies from existing requirements.txt
pip install -r requirements.txt
```
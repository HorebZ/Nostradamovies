# 🥷🏽 Lethal Data - 🎬 Nostradamovies


### 🐍 General setup
```Bash
# Install python3.11
$> pyenv install 3.11

# Select version localy (.python_version will generated)
$> pyenv local 3.11
```

### 🖥️ VueJS client
```Bash
$> cd client/

# Install hydrogen (latest lts - node 18)
$> nvm install lts/hydrogen

# Use hydrogen
$> nmv use lts/hydrogen

# Install packeages (pnpm recomended)
$> pnpm i
```

### 🌶️ Flask api
```Bash
$> cd app/server/

# Create venv
$> python3 -m venv venv

# Source your venv (for exit venv use `deactivate`)
$> source venv/bin/activate

# Install requirements
$> pip install -r requirements.txt

# Now you can run server as debug with tailwind watcher and hot reload
$> python app.py
```
### 📜 Data
```Bash
$> cd data/

# Create venv
$> python3 -m venv venv

# Source your venv (for exit venv use `deactivate`)
$> source venv/bin/activate

# Install requirements
$> pip install -r requirements.txt
```

# Log Analyzer System

A Python-based Log Analyzer system developed. This tool helps analyze system logs to identify security vulnerabilities and monitor system health.

---

## 🚀 Features
- Parses and analyzes Windows Event Logs.
- Identifies potential security threats and unusual activities.
- Provides insights into log patterns for security monitoring.

---

## 🛠️ Technologies Used
- **Python 3.x**  
- **pywin32** (for accessing Windows event logs)  
- Other Python libraries (listed in `requirements.txt`)

---

## ⚙️ Installation and Setup

### 1. **Clone the Repository**
```bash
git clone <your-github-repository-url>
cd LogAnalyzer
```

### 2. **Create a Virtual Environment** (Recommended)
```bash
python -m venv venv
```

- Activate the virtual environment:
  - On **Windows**:
    ```bash
    venv\Scripts\activate
    ```
  - On **Linux/Mac**:
    ```bash
    source venv/bin/activate
    ```

### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## 📄 Requirements

Ensure the following are installed on the system:

1. **Python 3.x**: Download and install from [python.org](https://www.python.org/).  
2. **pywin32**: If not already installed, it will be installed via `requirements.txt`.  
3. **Windows OS** (for Windows Event Log analysis).  

---

## 🏃‍♂️ Running the Application

Execute the main Python script:

```bash
python main.py
```

- This will start the Log Analyzer and process the event logs.

---

## 📂 Project Structure

```
LogAnalyzer/
│
├── main.py                 # Main script to run the analyzer
├── analyzer.py             # Core logic for analyzing logs
├── requirements.txt        # List of Python dependencies
├── README.md               # Project documentation
└── sample_logs/            # Sample log files for testing (if any)
```

---

## ⚠️ Common Issues

- **ModuleNotFoundError** for `win32evtlog`?  
  Run the following to install manually:
  ```bash
  pip install pywin32
  ```

- **Permission Error** while accessing system logs?  
  Run the script with administrative privileges.

---

## 💡 How it Works
1. The system reads and parses the Windows Event Logs.  
2. It analyzes entries to detect unusual patterns and potential threats.  
3. Generates insights or alerts based on predefined rules.

---

## ✅ Testing (Optional)
- Use sample log files (if provided) in the `sample_logs/` directory for testing the analyzer without accessing real system logs.



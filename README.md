# 🔍 AICodeAudit

AICodeAudit is an AI-powered code security auditing tool that uses local Large Language Models (LLMs) through Ollama and CodeLlama to analyze source code for vulnerabilities and insecure coding practices.

---

## 🚀 Features

- AI-powered code security analysis
- Recursive source code scanning
- Automatic file discovery
- Chunk-based large code processing
- Vulnerability identification
- Severity classification
- Secure coding recommendations
- Vulnerable and fixed code suggestions
- Local LLM support using Ollama
- Supports multiple source code files

---

## 🛠️ Technologies Used

- Python
- Ollama
- CodeLlama
- Requests Library
- Local LLM APIs

---

## 📂 Project Structure

```text
AICodeAudit/
│
├── ai_code_auditor.py
├── README.md
├── requirements.txt
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/nidhipatel-13/AICodeAudit.git
```

Move into the project folder:

```bash
cd AICodeAudit
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install and run Ollama locally.

Pull CodeLlama model:

```bash
ollama pull codellama
```

Run the tool:

```bash
python ai_code_auditor.py <target-folder>
```

Example:

```bash
python ai_code_auditor.py vulnerable_app/
```

---

## 🔎 What the Tool Detects

- SQL Injection risks
- Cross-Site Scripting (XSS)
- Hardcoded secrets
- Insecure functions
- Unsafe input handling
- Command Injection risks
- Poor security practices
- General insecure coding patterns

---

## 📊 Output

The tool provides:

- Vulnerability name
- Severity level
- Description
- Recommendation
- Vulnerable code snippet
- Suggested fixed version

---

## 🎯 Project Purpose

This project was built for:

- Cybersecurity learning
- AI-assisted secure code review
- Security automation practice
- Static analysis experimentation
- LLM-based vulnerability research

---

## ⚠️ Disclaimer

This project is intended for educational and defensive security purposes only.

---


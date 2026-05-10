import os
import sys
import requests
import shutil

# ---------------- CONFIG ----------------
API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "codellama:latest"
MAX_CHARS = 3000
OVERLAP_LINES = 5

TERMINAL_WIDTH = shutil.get_terminal_size((80, 20)).columns

# ---------------- FILE HANDLING ----------------
def collect_all_files(base_path):
    file_paths = []
    for root, _, files in os.walk(base_path):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

def is_text_file(file_path):
    try:
        with open(file_path, 'rb') as f:
            return b'\0' not in f.read(1024)
    except:
        return False

def read_file_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    except:
        return ""

# ---------------- CHUNKING ----------------
def chunk_code(content, max_chars, overlap_lines):
    lines = content.splitlines()
    chunks = []
    start = 0
    while start < len(lines):
        end = start
        size = 0
        while end < len(lines) and size + len(lines[end]) < max_chars:
            size += len(lines[end]) + 1
            end += 1
        chunk = "\n".join(f"{i+1}: {lines[i]}" for i in range(start, end))
        chunks.append(chunk)
        start = end - overlap_lines if end - overlap_lines > start else end
    return chunks

# ---------------- API CALL ----------------
def analyze_code_with_llama_local(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    try:
        res = requests.post(API_URL, json=payload)
        res.raise_for_status()
        return res.json().get("response", "").strip()
    except Exception as e:
        return f"[ERROR] {e}"

def generate_prompt(chunk_content, file_name, file_path, chunk_no):
    return f"""
You are a security code auditor AI. Analyze the following code snippet and explain vulnerabilities clearly in plain text. Do not return JSON. Include:
- Vulnerability name
- Severity
- Description
- Recommendation
- Vulnerable code snippet
- Fixed version

Code snippet (File: {file_name}, Path: {file_path}, Chunk: {chunk_no}):

{chunk_content}
"""

# ---------------- MAIN ----------------
def main():
    if len(sys.argv) < 2:
        print("Usage: python ai_code_auditor.py <path-to-folder>")
        sys.exit(1)

    codebase_path = sys.argv[1]
    if not os.path.exists(codebase_path):
        print(f"[ERROR] Path '{codebase_path}' does not exist.")
        sys.exit(1)

    all_files = collect_all_files(codebase_path)
    text_files = [f for f in all_files if is_text_file(f) and read_file_content(f).strip()]
    print(f"📂 Found {len(text_files)} text files to scan...\n")

    for file_path in text_files:
        fname = os.path.basename(file_path)
        content = read_file_content(file_path)
        chunks = chunk_code(content, MAX_CHARS, OVERLAP_LINES)

        for idx, chunk in enumerate(chunks, start=1):
            print("=" * TERMINAL_WIDTH)
            print(f"📄 {fname} | Chunk #{idx}")
            print("-" * TERMINAL_WIDTH)
            prompt = generate_prompt(chunk, fname, file_path, idx)
            response = analyze_code_with_llama_local(prompt)
            print(response)
            print("=" * TERMINAL_WIDTH + "\n")

if __name__ == "__main__":
    main()

# AI-Powered-Code-Review-Assistant-Local-with-Ollama-
A desktop-based AI Code Review Assistant built in Python (Tkinter GUI) that reviews entire folders of code using Ollama + CodeLlama locally — with no API keys or internet required. It automatically: • Scans all supported source files in a folder • Sends each file’s content to Ollama (via local API) • Displays AI feedback live in the GUI 
________________________________________
⚙️ System Requirements
OS: Windows / macOS / Linux
Python: ≥ 3.10
RAM: 8GB+ (recommended for Ollama models)

________________________________________
📦 Python Dependencies
Create a requirements.txt file with the following:
requests>=2.31.0
tkinter
(Note: tkinter is usually preinstalled with Python.)
You can install dependencies by running:
pip install -r requirements.txt

________________________________________
🧠 Ollama Requirements
1️⃣ Install Ollama
Go to 👉 https://ollama.com/download
Download and install Ollama for your OS.

2️⃣ Download the CodeLlama model
After installing, open terminal and run:
ollama run codellama
This will download and cache the model locally (~4GB).
After download completes, you can exit using Ctrl + C.

________________________________________
▶️ How to Run the Project
1. Start the Ollama server:
   ollama serve
   Keep this terminal open — it runs the local API on: http://localhost:11434

2. Run the app:
   python ai_code_reviewer_final.py

3. Use the GUI:
   o Click Browse Folder → Choose your code folder
   o Click Run AI Review
   o See live feedback per file
   o Wait for completion → Report auto-saved in your folder

________________________________________
💾 Output Example
A file like:
AI_Code_Review_Report_2025-10-14_12-45-22.txt
will be created inside your selected code folder, containing feedback for every file.

________________________________________
💡 Supported Languages
Language                Extensions
Python                  .py
JavaScript / TypeScript .js, .ts
Java                    .java
C / C++                 .c, .cpp
C#                      .cs
Web                     .html, .css, .php
Others                  .rb, .go, .rs, .swift, .kt, .json, .xml, .sh, .bat

________________________________________
🧰 Optional: GitHub README (for your repo)
Here’s a short README you can paste directly:

🧠 AI-Powered Code Review Assistant (Local with Ollama)

A desktop app that performs local AI code reviews on your projects using Ollama + CodeLlama — fully offline, secure, and free.

🚀 Features
• Runs entirely offline (no API key)
• Reviews all code files in a folder
• Displays real-time progress
• Automatically saves a report file
• Simple GUI with Tkinter

🧩 Setup
git clone https://github.com/<yourusername>/ai-code-review-assistant.git
cd ai-code-review-assistant
pip install -r requirements.txt
ollama serve
python ai_code_reviewer_final.py

🧠 Model
Uses CodeLlama via Ollama API (localhost:11434)
________________________________________

How to Run the AI Code Review Assistant PROPERLY

1)Start Ollama Server
   Open a terminal (Command Prompt, PowerShell, or Terminal).
   Type:
   
      ollama server

   You will see a long output in the terminal—this means the Ollama server is running.
   Minimize the terminal; don’t close it.
   
2) Open the Code Review Interface
   Launch the Python GUI application.
   In the interface, click Browse to select the folder containing your code files.
   
3) Run AI Review
   
   Click the Run AI Review button.
   Wait patiently while the assistant analyzes your code. The processing time depends on the number of files and their size.
   
4) View Suggestions
   Once the review is complete, you’ll see:
   Suggested improvements
   Corrected or optimized code snippets

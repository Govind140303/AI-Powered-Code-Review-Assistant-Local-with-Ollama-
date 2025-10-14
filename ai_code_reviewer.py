import os
import json
import threading
import requests
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox

class CodeReviewApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Code Review Assistant (Ollama)")
        self.root.geometry("800x600")

        self.folder_path = tk.StringVar()
        self.stop_requested = False

        # --- GUI ---
        tk.Label(root, text="1️⃣ Select a folder containing programming files:").pack(pady=5)
        tk.Button(root, text="Browse Folder", command=self.browse_folder).pack()

        tk.Label(root, textvariable=self.folder_path, fg="blue").pack(pady=5)

        tk.Button(root, text="Run AI Review", bg="green", fg="white", command=self.start_review).pack(pady=5)
        tk.Button(root, text="Stop Review", bg="red", fg="white", command=self.stop_review).pack(pady=5)

        self.output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=25)
        self.output.pack(padx=10, pady=10)

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_path.set(folder_selected)

    def stop_review(self):
        self.stop_requested = True
        self.output.insert(tk.END, "\n🟥 Review stopped by user.\n")
        self.output.see(tk.END)

    def start_review(self):
        if not self.folder_path.get():
            messagebox.showwarning("No Folder", "Please select a folder first!")
            return
        self.stop_requested = False
        threading.Thread(target=self.review_folder).start()

    def review_folder(self):
        folder = self.folder_path.get()
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, f"🔍 Scanning folder: {folder}\n\n")

        supported_ext = (
            ".py", ".js", ".ts", ".java", ".c", ".cpp", ".cs", ".html", ".css",
            ".php", ".rb", ".go", ".rs", ".swift", ".kt", ".json", ".xml", ".sh", ".bat"
        )

        all_files = [
            os.path.join(root, file)
            for root, _, files in os.walk(folder)
            for file in files if file.endswith(supported_ext)
        ]

        if not all_files:
            self.output.insert(tk.END, "⚠️ No supported files found.\n")
            return

        for file_path in all_files:
            if self.stop_requested:
                break

            file_name = os.path.basename(file_path)
            self.output.insert(tk.END, f"\n🔹 Reviewing: {file_name}\n")
            self.output.see(tk.END)
            self.root.update_idletasks()

            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    code = f.read()

                # --- Ask Ollama for summarized brief review + corrected code ---
                prompt = f"""
You are a concise code reviewer.
Analyze the following code and provide a SHORT, clear output (3–4 lines):
1️⃣ Brief summary of key issues or improvements.
2️⃣ Suggest how to fix them (include code if helpful).
3️⃣ Provide the corrected version of the code.
Code:
{code}
"""

                payload = {"model": "codellama", "prompt": prompt}

                response = requests.post("http://localhost:11434/api/generate", json=payload, stream=True)
                review_text = ""

                for line in response.iter_lines():
                    if self.stop_requested:
                        break
                    if not line:
                        continue
                    try:
                        json_data = json.loads(line.decode("utf-8"))
                        review_text += json_data.get("response", "")
                    except json.JSONDecodeError:
                        review_text += line.decode("utf-8")

                # --- Display review + corrected code ---
                self.output.insert(tk.END, f"🧠 Review & Corrected Code for {file_name}:\n{review_text.strip()}\n\n")
                self.output.insert(tk.END, f"✅ Done reviewing {file_name}\n")
                self.output.see(tk.END)
                self.root.update_idletasks()

            except Exception as e:
                self.output.insert(tk.END, f"❌ Error reviewing {file_name}: {str(e)}\n")
                self.output.see(tk.END)

        if not self.stop_requested:
            self.output.insert(tk.END, "\n🎉 All files reviewed successfully!\n")
        else:
            self.output.insert(tk.END, "\n🟥 Review stopped before completion.\n")

        self.output.see(tk.END)

# --- Run App ---
if __name__ == "__main__":
    root = tk.Tk()
    app = CodeReviewApp(root)
    root.mainloop()

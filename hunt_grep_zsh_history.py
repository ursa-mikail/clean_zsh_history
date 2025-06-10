# ~/scripts/functions/hunt_grep_zsh_history.py

import os
import re

def hunt_keywords(filepath, keywords):
    filepath = os.path.expanduser(filepath)

    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()

        matches = []
        for i, line in enumerate(lines):
            for keyword in keywords:
                if re.search(re.escape(keyword), line):
                    matches.append((i, line.strip()))
                    break

        if not matches:
            print("No suspicious lines found.")
            return

        print(f"Found {len(matches)} matching lines:\n")
        for idx, line in matches:
            print(f"[{idx}] {line}")

        confirm = input("\nWould you like to delete these lines? (y/N): ").strip().lower()
        if confirm == 'y':
            new_lines = [line for i, line in enumerate(lines) if i not in [idx for idx, _ in matches]]
            with open(filepath, 'w') as file:
                file.writelines(new_lines)
            print(f"{len(matches)} lines deleted.")
        else:
            print("No changes made.")

    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    keywords_input = input("Enter comma-separated keywords to scan for (e.g., token,password,secret): ").strip()
    keywords = [k.strip() for k in keywords_input.split(",") if k.strip()]
    hunt_keywords("~/.zsh_history", keywords)


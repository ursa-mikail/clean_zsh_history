# ~/scripts/functions/hunt_tailored_grep_zsh_history.py
# ~/scripts/functions/hunt_grep_zsh_history.py

import os
import re

def hunt_and_clean_individually(filepath, keywords):
    filepath = os.path.expanduser(filepath)

    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()

        matches = []
        for i, line in enumerate(lines):
            if any(re.search(re.escape(keyword), line) for keyword in keywords):
                matches.append((i, line.strip()))

        if not matches:
            print("No suspicious lines found.")
            return

        print(f"\nFound {len(matches)} suspicious lines.")
        indices_to_delete = []
        lines_to_delete = []
        total = len(matches)

        for count, (i, line) in enumerate(matches, start=1):
            print(f"\n[{count}/{total}] Line {i}: {line}")
            answer = input("Delete this line? (y = yes, s = skip, a = abort): ").strip().lower()

            if answer == 'y':
                indices_to_delete.append(i)
                lines_to_delete.append(line)
            elif answer == 'a':
                print("\nAborted review — will delete selected lines so far.")
                break
                # 's' or anything else just skips

        if not indices_to_delete:
            print("No lines marked for deletion.")
            return

        print(f"\n{len(indices_to_delete)} line(s) selected for deletion:")
        for line in lines_to_delete:
            print(f" - {line}")

        confirm = input("\nConfirm delete? (y/N): ").strip().lower()
        if confirm == 'y':
            new_lines = [line for idx, line in enumerate(lines) if idx not in indices_to_delete]
            with open(filepath, 'w') as file:
                file.writelines(new_lines)
            print(f"\nDeleted {len(lines_to_delete)} line(s) from {filepath}.")
        else:
            print("No changes made.")

    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    keywords_input = input("Enter comma-separated keywords to scan for (e.g., token,password,secret): ").strip()
    keywords = [k.strip() for k in keywords_input.split(",") if k.strip()]
    hunt_and_clean_individually("~/.zsh_history", keywords)

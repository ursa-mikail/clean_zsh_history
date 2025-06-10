import os

def delete_lines_with_word(filepath, word):
    # Expand ~ to home directory
    filepath = os.path.expanduser(filepath)

    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()

        # Filter out lines containing the word
        filtered_lines = [line for line in lines if word not in line]

        with open(filepath, 'w') as file:
            file.writelines(filtered_lines)

        print(f"Deleted lines containing '{word}' from {filepath}.")

    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    word_to_delete = input("Enter the word to delete lines containing it from ~/.zshrc: ").strip()
    delete_lines_with_word("~/.zsh_history", word_to_delete)

# clean_zsh_history

While many may forget that the applications taking in passcodes should ensure that the history, trace, logs and monitors do not log the passcodes :
```
	read -s -p "Enter PIN for pin0$i: " pin

🔒 read -s hides the PIN as it is typed.
```

secrets get archived and dumped at certain corners. 

Hence, those logs have to be sanitized. 
This is a sample of how logs can be cleaned. 

At ~/.zshrc
```
alias clean_zsh_history='python3 $HOME"/scripts/functions/clean_zsh_history.py"'
```

Usage:
```
% clean_zsh_history
Enter the word to delete lines containing it from ~/.zshrc: <keyword>
Deleted lines containing '<keyword>' from /Users/chanfamily/.zsh_history.
```


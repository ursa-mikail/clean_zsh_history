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
alias hunt_grep_zsh_history='python3 $HOME"/scripts/functions/hunt_grep_zsh_history.py"'
alias hunt_tailored_grep_zsh_history='python3 $HOME"/scripts/functions/hunt_tailored_grep_zsh_history.py"'

```

Usage:
```
% clean_zsh_history
Enter the word to delete lines containing it from ~/.zshrc: <keyword>
Deleted lines containing '<keyword>' from /Users/chanfamily/.zsh_history.
```

Usage:
```
% hunt_grep_zsh_history
Enter comma-separated keywords to scan for (e.g., token,password,secret):subl,ls     
Found 162 matching lines:

[12] subl run_demo.sh
[16] subl common.go
[:
[81] subl readme.md


Would you like to delete these lines? (y/N): y
162 lines deleted.

```

Usage:
```
% hunt_tailored_grep_zsh_history
Enter comma-separated keywords to scan for (e.g., token,password,secret): .3,ls

Found 5 suspicious lines.

[1/5] Line 155: .3
Delete this line? (y = yes, s = skip, a = abort): y

[2/5] Line 165: .3
Delete this line? (y = yes, s = skip, a = abort): s

[3/5] Line 205: mv /Users/chanfamily/Desktop/Screenshot\ 2025-05-30\ at\ 10.30.16 PM.png readme.cache_timing_classifier.01.02.png
Delete this line? (y = yes, s = skip, a = abort): y

[4/5] Line 245: .3
Delete this line? (y = yes, s = skip, a = abort): y

[5/5] Line 391: .3
Delete this line? (y = yes, s = skip, a = abort): y

4 line(s) selected for deletion:
 - .3
 - mv /Users/chanfamily/Desktop/Screenshot\ 2025-05-30\ at\ 10.30.16 PM.png readme.cache_timing_classifier.01.02.png
 - .3
 - .3

Confirm delete? (y/N): y

Deleted 4 line(s) from /Users/chanfamily/.zsh_history.


🔐 Features
y — delete the line
s — skip this line
a — abort everything

Final confirmation before deletion

Handles paths like ~ properly
```

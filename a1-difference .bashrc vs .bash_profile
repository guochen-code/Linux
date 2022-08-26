.bash_profile is read and executed when Bash is invoked as an interactive login shell, while .bashrc is executed for an interactive non-login shell.

Use .bash_profile to run commands that should run only once, such as customizing the $PATH environment variable .

Put the commands that should run every time you launch a new shell in the .bashrc file. This include your aliases and functions , custom prompts, history customizations , and so on.

Typically, ~/.bash_profile contains lines like below that source the .bashrc file. This means each time you log in to the terminal, both files are read and executed.

if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

Most Linux distributions are using ~/.profile instead of ~/.bash_profile. The ~/.profile file is read by all shells, while ~/.bash_profile only by Bash.

If any startup file is not present on your system, you can create it.

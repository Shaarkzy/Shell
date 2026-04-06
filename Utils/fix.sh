#!/bin/bash

#------------------------Fixing Syslink For New Path-------------------------------

if [[ "$(uname -a | grep -i android)" ]]; then
	chmod +x ~/Shell/launcher.py
    ln -sf ~/Shell/launcher.py /data/data/com.termux/files/usr/bin/shell

else
    USER_NAME="${SUDO_USER:-$USER}"
    USER_HOME="$(getent passwd "$USER_NAME" | cut -d: -f6)"

    chmod +x "$USER_HOME/Shell/Core/shell.py"
    ln -sf "$USER_HOME/Shell/launcher.py" "/usr/local/bin/shell"
fi

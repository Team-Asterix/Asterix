# !/bin/bash

MAIN_URL=https://github.com/Team-Asterix/Asterix
if [ '-install' == $1 ]; then
    clone_main_repo=true
else
    clone_main_repo=false
fi

_isInstalled() {
    package="$1";
    if [ $(yum list installed "$1" >/dev/null 2>&1) ];
    then
        echo 0; 
        return;
    fi;
        echo 1;
        return
}

_installMany() {
    toInstall=();
    for pkg; do
        if [[ $(_isInstalled "${pkg}") == 0 ]]; then
            echo "${pkg} is already installed.";
            continue;
        fi;
        toInstall+=("${pkg}");
    done;
    if [[ "${toInstall[@]}" == "" ]] ; then
        echo "All packages are already installed.";
        return;
    fi;
    printf "Packages not installed:\n%s\n" "${toInstall[@]}";
    sudo yum install "${toInstall[@]}";
}


final_run () {
    if [ clone_main_repo == 'true' ]; then
        _installMany git
        git clone $MAIN_URL
    fi
    _installMany python3 ffmpeg python3-pip # install these feroda packages
    python3 -m venv venv
    source venv/bin/activate
    pip3 install --upgrade pip && pip3 install -r requirements.txt
    python3 -m Main
}


final_run

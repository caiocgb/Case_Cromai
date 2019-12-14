#!/bin/bash

# if pgrep -f "python3 NOME_DO_SEU_PROGRAMA_EM_PYTHON3.py" &>/dev/null; then
# esta linha tem a função de verificar se o seu programa em python3 esta
# ativo. Caso este programa esteja ativo, é printado na tela a mensagem
# "It is alive", e o programa é finalizado.

if pgrep -f "python3 pid.py" &>/dev/null; then
    echo "It is alive"
    exit

# caso o programa nao esteja ativo, é printado a mensagem "It is dead",
# e o programa em python3 é iniciado.
else
    echo "It is dead"
    python3 pid.py
fi


#!/bin/zsh
if [[ "$OSTYPE" == "win32" ]]; then
  export PYTHONPATH="${PYTHONPATH}:$(cd)"
else
  export PYTHONPATH="${PYTHONPATH}:$(pwd)"
fi

python src/main.py
cd public && python3 -m http.server 8888

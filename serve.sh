#!/usr/bin/env bash
# Launch a local HTTP server for the Periodic Table viewer.
# Usage: ./serve.sh [port]

PORT=${1:-8765}
DIR="$(cd "$(dirname "$0")" && pwd)"

# Kill any previous instance on the same port
if lsof -ti tcp:"$PORT" &>/dev/null; then
    echo "Stopping existing process on port $PORT…"
    lsof -ti tcp:"$PORT" | xargs kill
fi

echo "Serving $DIR on http://localhost:$PORT"
echo "Opening http://localhost:$PORT/view_svg.html"
echo "(Ctrl-C to stop)"

# Open browser (try xdg-open, then fallback)
(sleep 0.5 && xdg-open "http://localhost:$PORT/view_svg.html" 2>/dev/null) &

cd "$DIR" || exit
/home/olivier/micromamba/envs/wa/bin/python -m http.server "$PORT"

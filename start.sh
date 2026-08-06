#!/bin/bash
# Local fallback if GitHub Pages is unreachable on your network
cd "$(dirname "$0")"
echo "IT Change Intelligence — local server"
echo "Open: http://localhost:8080"
echo "Press Ctrl+C to stop"
python3 -m http.server 8080

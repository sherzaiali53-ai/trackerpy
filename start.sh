#!/bin/bash
cd /Desktop/tracker
echo "🚀 Starting tracker..."
python3 listener.py &
sleep 2
python3 -m http.server 8080 &
echo "✅ Server running!"
echo "📎 Link: http://$(ifconfig en0 | grep "inet " | awk '{print $2}'):8080/game.html"
echo "📱 nc -lvnp 8080  (in new terminal)"

clear




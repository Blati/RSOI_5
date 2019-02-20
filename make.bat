@echo off
start cmd.exe /k "cd services && python movies.py"
start cmd.exe /k "cd services && python showtimes.py"
start cmd.exe /k "cd services && python bookings.py"
start cmd.exe /k "cd services && python auth.py"
start cmd.exe /k "cd services && python user.py"
start cmd.exe /k "cd client && npm start"

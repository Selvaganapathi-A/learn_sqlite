@echo off
pg_ctl -D "C:\Program Files\PostgreSQL\13\data" start
echo -------------------------------------------------
echo Server Started at --host=***.***.***.*** --port=****
echo -------------------------------------------------
echo Press any key to Exit
pause > nul
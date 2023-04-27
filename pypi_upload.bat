:: assign bat file name and directory
set batFileName=%~n0
set batDirectory=%~dp0

:: run py file (assumes anaconda is added to "Path" env var
call activate.bat 
python.exe "%batDirectory%%batFileName%.py"

:: pause
pause
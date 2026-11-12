@echo off
setlocal
REM 64-bit MinGW. 两份都是 -O0，只有符号不同。
set GCC=C:\Users\ai\AppData\Local\Microsoft\WinGet\Packages\BrechtSanders.WinLibs.POSIX.UCRT_Microsoft.Winget.Source_8wekyb3d8bbwe\mingw64\bin\gcc.exe
set STRIP=C:\Users\ai\AppData\Local\Microsoft\WinGet\Packages\BrechtSanders.WinLibs.POSIX.UCRT_Microsoft.Winget.Source_8wekyb3d8bbwe\mingw64\bin\strip.exe

"%GCC%" -std=c11 -Wall -Wextra -O0 -g -fno-omit-frame-pointer -o factorial_symbols.exe factorial.c
if errorlevel 1 exit /b 1

"%GCC%" -std=c11 -Wall -Wextra -O0 -fno-omit-frame-pointer -o factorial_stripped.exe factorial.c
if errorlevel 1 exit /b 1

"%STRIP%" --strip-all factorial_stripped.exe
if errorlevel 1 exit /b 1

echo built factorial_symbols.exe and factorial_stripped.exe

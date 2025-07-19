@ECHO OFF
ECHO Welcome to the MADDEN 09 ISO MOD CREATION TOOL (no extraction mode)
ECHO.
PAUSE

:start
ECHO Checking if installation files are in the correct folder...
IF NOT EXIST "MOD\SLUS_217.70" (
  ECHO The Installation Files are not in the correct folders. Please re-read the instructions and try again!
  PAUSE
  EXIT /B 1
)
IF NOT EXIST "*.ISO" (
  ECHO A copy of the MADDEN 09 Football ISO Game is missing.
  PAUSE
  EXIT /B 1
)
IF NOT EXIST "IMGBURN.EXE" (
  ECHO IMGBURN.EXE is missing. Please place it here.
  PAUSE
  EXIT /B 1
)

:install
ECHO Patching MADDEN 09 with Mods into your existing next\ folder...
ECHO Please wait a moment...
PAUSE
xcopy "mod\*.*" "next\" /E /Y /A

cd next
ECHO.
ECHO Installation File Location: Correct.
ECHO Deleting QKL and ONLINE leftovers...
del "DATA\*.qkl" /Q
rmdir /S /Q "NETGUI"
rmdir /S /Q "EACN"
rmdir /S /Q "ONLINE"
del "DATA\CAFE*.DAT"   /Q
del "DATA\ONLINE.DAT"  /Q
del "DATA\OSDKSTRN.DAT"/Q
del "DATA\UIONLINE.DAT"/Q
PAUSE

ECHO Patching Complete!
ECHO.
ECHO Running IMGBURN to create MADDEN 09 MOD ISO!
ECHO This may take a few moments. If prompted, press YES each time!
cd ..
PAUSE

IF EXIST "next\SYSTEM.CNF" GOTO burn
ECHO The installation did not copy files correctly. Please try again as Administrator or manually.
PAUSE
EXIT /B 1

:burn
ImgBurn /mode build /src "next" /dest "Madden 09 Mod.iso" /volumelabel "MADDEN 09 MOD" /start /overwrite yes /close
ECHO Madden 09 MOD ISO successfully created!
PAUSE

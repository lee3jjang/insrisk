@Echo Off
set SPHINXBUILD=sphinx-build
set SOURCEDIR=source
set BUILDDIR=.

%SPHINXBUILD% -M html %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
FOR /D %%I IN (./%BUILDDIR%/html/*) DO (
  IF NOT EXIST "%BUILDDIR%\%%I\" (
    mkdir "%BUILDDIR%\%%I"
  )
  FOR /D %%J IN (./%BUILDDIR%/html/%%I/*) DO (
    IF NOT EXIST "%BUILDDIR%\%%I\%%J\" (
      mkdir "%BUILDDIR%\%%I\%%J"
    )
    move /Y %BUILDDIR%\html\%%I\%%J\* %BUILDDIR%\%%I\%%J\ >nul
    rmdir .\%BUILDDIR%\html\%%I\%%J\
  )
  move /Y %BUILDDIR%\html\%%I\* %BUILDDIR%\%%I\ >nul
  rmdir .\%BUILDDIR%\html\%%I\
)
move /Y %BUILDDIR%\html\* %BUILDDIR%\ >nul
rmdir .\%BUILDDIR%\html\
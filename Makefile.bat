@ECHO OFF

pushd %~dp0

REM Build the docs: make html
if "%1" == "" goto help

%SPHINXBUILD% 2>NUL
if errorlevel 9009 goto sphinx_missing

python -m sphinx -b %1 source _build/%1 %2 %3 %4 %5
goto end

:sphinx_missing
echo Sphinx not found. Run: pip install sphinx sphinx-rtd-theme

:help
echo Usage: make html     ^(build HTML into _build/html^)
echo        make clean    ^(remove _build^)

:end
popd

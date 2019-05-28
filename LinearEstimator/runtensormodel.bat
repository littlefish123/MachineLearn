setx PYTHONPATH d:\tensorflow\models
echo %PYTHONPATH%

cd %PYTHONPATH%
python -m official.wide_deep.census_main --help
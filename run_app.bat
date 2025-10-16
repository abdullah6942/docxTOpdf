@echo off
echo Starting DOCX to PDF Converter...
echo.
call decx_env\Scripts\activate.bat
streamlit run convert.py
pause


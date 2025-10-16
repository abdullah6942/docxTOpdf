# Quick Start Guide

## Option 1: Double-click the Batch File (Easiest)

Simply double-click `run_app.bat` and the application will start automatically!

## Option 2: Manual Start

1. Open PowerShell or Command Prompt
2. Navigate to the project folder:
   ```bash
   cd C:\Users\abdul\OneDrive\Desktop\docs
   ```
3. Run the batch file:
   ```bash
   .\run_app.bat
   ```

## Option 3: Using PowerShell Commands

```powershell
cd C:\Users\abdul\OneDrive\Desktop\docs
.\decx_env\Scripts\activate.ps1
streamlit run convert.py
```

## What Happens Next?

- Your default web browser will open automatically
- The app will be available at: `http://localhost:8501`
- If the browser doesn't open, manually navigate to the URL above

## Using the App

1. **Upload a DOCX file** by clicking "Browse files" or dragging and dropping
2. **Click "Convert to PDF"** button
3. **Wait** for the conversion (usually takes a few seconds)
4. **Click "Download PDF"** to save your converted file

## Stopping the App

- Press `Ctrl + C` in the terminal/command prompt window
- Or simply close the terminal window

## Troubleshooting

### The app won't start
- Make sure Microsoft Word is installed on your computer
- Ensure you're in the correct directory

### Browser doesn't open automatically
- Manually open your browser and go to: http://localhost:8501

### Port already in use
- Another app might be using port 8501
- You can specify a different port: `streamlit run convert.py --server.port 8502`

## Need Help?

Check the full README.md file for detailed documentation and troubleshooting steps.


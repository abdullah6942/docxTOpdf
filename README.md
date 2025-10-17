# DOCX to PDF Converter

A beautiful and user-friendly Streamlit web application that converts DOCX files to PDF format.

## Features

- 📤 **Easy Upload**: Simple drag-and-drop or browse interface for DOCX files
- 🔒 **Format Validation**: Only accepts DOCX files for security
- 📊 **File Information**: Displays uploaded file name and size
- 🔄 **Quick Conversion**: Fast DOCX to PDF conversion
- 📥 **Instant Download**: Download converted PDF with one click
- 🎨 **Modern UI**: Clean and intuitive user interface

## Prerequisites

### For Local Development (Windows):
- Python 3.8 or higher
- Microsoft Word installed (for docx2pdf) OR LibreOffice

### For Streamlit Cloud Deployment:
- No additional prerequisites - LibreOffice is automatically installed

## Installation

1. **Activate the virtual environment** (if not already activated):
   ```bash
   .\decx_env\Scripts\activate
   ```

2. **Install Streamlit** (if not already installed):
   ```bash
   pip install streamlit
   ```

## Running the Application

1. **Navigate to the project directory**:
   ```bash
   cd C:\Users\abdul\OneDrive\Desktop\docs
   ```

2. **Activate the virtual environment**:
   ```bash
   .\decx_env\Scripts\activate
   ```

3. **Run the Streamlit app**:
   ```bash
   streamlit run convert.py
   ```

4. **Open your browser**: The app will automatically open at `http://localhost:8501`

## Usage

1. **Upload**: Click "Browse files" or drag and drop a DOCX file
2. **Convert**: Click the "Convert to PDF" button
3. **Download**: Click the "Download PDF" button to save your converted file

## File Structure

```
docs/
├── convert.py           # Main Streamlit application
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── decx_env/           # Virtual environment
```

## Dependencies

- `streamlit>=1.28.0` - Web application framework
- `libreoffice` (system package) - Cross-platform DOCX to PDF conversion
- `docx2pdf>=0.1.8` (optional, Windows only) - Alternative converter for Windows

## Deployment to Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "New app"
5. Select your repository, branch (main), and main file (convert.py)
6. Click "Deploy"

The `packages.txt` file will automatically install LibreOffice on the Streamlit Cloud server.

## Troubleshooting

### Issue: "LibreOffice not found" (Local Windows)
- **Solution**: Install LibreOffice from [libreoffice.org](https://www.libreoffice.org/download/download/) OR ensure Microsoft Word is installed

### Issue: "Module not found"
- **Solution**: Make sure you've activated the virtual environment and installed all dependencies

### Issue: "Conversion failed"
- **Solution**: Ensure the DOCX file is not corrupted and is a valid Word document

### Issue: Deployment fails on Streamlit Cloud
- **Solution**: Make sure both `requirements.txt` and `packages.txt` are in your repository root

## Notes

- **Cross-platform**: Works on Windows (with Word/LibreOffice), Linux, and macOS
- **Cloud-ready**: Fully compatible with Streamlit Cloud deployment
- Temporary files are automatically cleaned up after conversion
- The application uses session state to maintain the PDF data between interactions

## License

This project is open source and available for personal and commercial use.


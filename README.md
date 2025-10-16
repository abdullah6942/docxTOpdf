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

- Python 3.8 or higher
- Windows OS (required for docx2pdf library)
- Microsoft Word installed on your system

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
- `docx2pdf>=0.1.8` - DOCX to PDF conversion
- `pywin32>=305` - Windows API support

## Troubleshooting

### Issue: "Microsoft Word is not installed"
- **Solution**: Install Microsoft Word on your Windows system

### Issue: "Module not found"
- **Solution**: Make sure you've activated the virtual environment and installed all dependencies

### Issue: "Conversion failed"
- **Solution**: Ensure the DOCX file is not corrupted and is a valid Word document

## Notes

- This application works only on Windows systems because the `docx2pdf` library requires Microsoft Word
- Temporary files are automatically cleaned up after conversion
- The application uses session state to maintain the PDF data between interactions

## License

This project is open source and available for personal and commercial use.


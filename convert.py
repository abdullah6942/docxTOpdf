import streamlit as st
import os
import tempfile
from pathlib import Path
import subprocess
import platform

# Set page configuration
st.set_page_config(
    page_title="DOCX to PDF Converter",
    page_icon="📄",
    layout="centered"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        padding: 0.5rem;
        font-size: 1rem;
        border-radius: 5px;
        border: none;
        margin-top: 1rem;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .upload-text {
        text-align: center;
        color: #666;
    }
    </style>
    """, unsafe_allow_html=True)

def convert_docx_to_pdf(docx_path, pdf_path):
    """
    Convert DOCX to PDF using LibreOffice (cross-platform)
    Works on Windows, Linux, and macOS
    """
    try:
        # Determine the LibreOffice command based on the platform
        system = platform.system()
        
        if system == "Windows":
            # Try common Windows paths for LibreOffice or use docx2pdf as fallback
            try:
                from docx2pdf import convert
                convert(docx_path, pdf_path)
                return True
            except ImportError:
                # If docx2pdf is not available, try LibreOffice
                libreoffice_paths = [
                    r"C:\Program Files\LibreOffice\program\soffice.exe",
                    r"C:\Program Files (x86)\LibreOffice\program\soffice.exe",
                ]
                soffice_path = None
                for path in libreoffice_paths:
                    if os.path.exists(path):
                        soffice_path = path
                        break
                
                if not soffice_path:
                    raise Exception("LibreOffice not found. Please install LibreOffice or ensure docx2pdf is installed.")
        else:
            # Linux/macOS - LibreOffice is typically in PATH
            soffice_path = "libreoffice"
        
        # Use LibreOffice for conversion
        temp_dir = os.path.dirname(pdf_path)
        
        # Run LibreOffice in headless mode to convert
        cmd = [
            soffice_path,
            '--headless',
            '--convert-to',
            'pdf',
            '--outdir',
            temp_dir,
            docx_path
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        
        if result.returncode != 0:
            raise Exception(f"Conversion failed: {result.stderr}")
        
        # LibreOffice creates the PDF with the same name as input
        generated_pdf = os.path.join(temp_dir, Path(docx_path).stem + ".pdf")
        
        # Rename if necessary
        if generated_pdf != pdf_path:
            os.rename(generated_pdf, pdf_path)
        
        return True
        
    except subprocess.TimeoutExpired:
        raise Exception("Conversion timed out. Please try with a smaller file.")
    except Exception as e:
        raise Exception(f"Conversion error: {str(e)}")

# App header
st.title("📄 DOCX to PDF Converter")
st.markdown("---")
st.markdown("""
    <div style='text-align: center; padding: 1rem; background-color: #f0f2f6; border-radius: 10px; margin-bottom: 2rem;'>
        <p style='margin: 0; font-size: 1.1rem;'>Upload your DOCX file and convert it to PDF instantly!</p>
    </div>
    """, unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader(
    "Choose a DOCX file",
    type=['docx'],
    help="Only DOCX files are accepted"
)

if uploaded_file is not None:
    # Display file details
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"📁 **File Name:** {uploaded_file.name}")
    with col2:
        file_size = uploaded_file.size / 1024  # Convert to KB
        st.info(f"📊 **File Size:** {file_size:.2f} KB")
    
    # Convert button
    if st.button("🔄 Convert to PDF"):
        try:
            with st.spinner("Converting your document... Please wait."):
                # Create temporary directory for file operations
                with tempfile.TemporaryDirectory() as temp_dir:
                    # Save uploaded file temporarily
                    docx_path = os.path.join(temp_dir, uploaded_file.name)
                    with open(docx_path, 'wb') as f:
                        f.write(uploaded_file.getbuffer())
                    
                    # Define output PDF path
                    pdf_filename = Path(uploaded_file.name).stem + ".pdf"
                    pdf_path = os.path.join(temp_dir, pdf_filename)
                    
                    # Convert DOCX to PDF
                    convert_docx_to_pdf(docx_path, pdf_path)
                    
                    # Read the converted PDF
                    with open(pdf_path, 'rb') as pdf_file:
                        pdf_data = pdf_file.read()
                    
                    # Store in session state for download
                    st.session_state['pdf_data'] = pdf_data
                    st.session_state['pdf_filename'] = pdf_filename
                    st.session_state['conversion_complete'] = True
            
            st.success("✅ Conversion completed successfully!")
            
        except Exception as e:
            st.error(f"❌ An error occurred during conversion: {str(e)}")
            st.session_state['conversion_complete'] = False

# Download button (shown after successful conversion)
if st.session_state.get('conversion_complete', False):
    st.markdown("---")
    st.markdown("### 📥 Download Your PDF")
    
    st.download_button(
        label="⬇️ Download PDF",
        data=st.session_state['pdf_data'],
        file_name=st.session_state['pdf_filename'],
        mime="application/pdf",
        use_container_width=True
    )
    
    st.balloons()

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666; padding: 1rem;'>
        <p style='margin: 0;'>Made with ❤️ using Streamlit</p>
        <p style='margin: 0; font-size: 0.9rem;'>Supports DOCX format only</p>
    </div>
    """, unsafe_allow_html=True)

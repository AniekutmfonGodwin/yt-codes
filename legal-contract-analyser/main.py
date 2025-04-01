import streamlit as st
from services.analyser_helper import analyze_contract


def main():
    """
    Main function to run the Streamlit app for legal contract analysis.

    This app allows users to upload a PDF file containing a legal contract.
    The file is analyzed using the `analyze_contract` function, and the results
    are displayed in the app interface.

    Features:
    - Upload a PDF file.
    - Analyze the uploaded contract.
    - Display the analysis results in a user-friendly format.
    """
    st.set_page_config(page_title="Legal Contract Analyzer", layout="wide")
    st.title("📜 Legal Contract Analyzer")
    st.markdown(
        """
        Upload a legal contract in PDF format, and this app will analyze it for you.
        """
    )

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    
    if uploaded_file is not None:
        try:
            file_content = uploaded_file.read()
            
            st.info("Analyzing the contract...")
            analysis_result = analyze_contract(file_content)
            st.success("Contract analysis complete!")
            
            st.markdown("### 📝 Analysis Result")
            st.markdown(analysis_result, unsafe_allow_html=True)
        
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please upload a PDF file to proceed.")

if __name__ == "__main__":
    main()

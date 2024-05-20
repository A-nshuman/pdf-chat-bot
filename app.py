import streamlit as st

def main():
    st.set_page_config(page_title='PDF ChatBot', page_icon=':books:')

    st.header('PDF ChatBot :books:') # Title of the app
    st.text_input('Ask a question based on the PDF') # Input field to ask a question

    with st.sidebar:
        st.subheader("Your Documents") # Sidebar title
        st.file_uploader("Upload a PDFs here and click on 'Process'", type="pdf") # File uploader to upload a PDF
        st.button("Process") # Button to process the uploaded PDF

if __name__ == '__main__':
    main()
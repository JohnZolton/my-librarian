import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter



def main():
    print("hello world")
    st.set_page_config(page_title="pdf Q&A")
    st.header("Ask your pdf")
    pdf = st.file_uploader("Upload your PDF", type="pdf")
    
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ''
        for page in pdf_reader.pages:
            print(page.extract_text())
            text += page.extract_text()

        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text)
        st.write(chunks)



if __name__=="__main__":
    main()
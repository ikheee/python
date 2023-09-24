# __import__('pysqlite3')
# import sys
# sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

from dotenv import load_dotenv
load_dotenv()

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

import streamlit as st
import tempfile
import os
from streamlit_extras.buy_me_a_coffee import button

# 제목
st.title("ChatPDF")
st.write("---")

button(username="shinikhee79", floating=True, width=221)

# OpenAI KEY 입력 받기
openai_key = st.text_input('OPEN_AI_API_KEY', type="password")

# 파일 업로드
uploaded_file = st.file_uploader("PDF파일을 올려주세요.",type=['pdf'])
st.write("---")

# # Loader
# loader = PyPDFLoader("unsu.pdf")
# pages = loader.load_and_split()
# # print(pages[0])

def pdf_to_document(uploaded_file):
	temp_dir = tempfile.TemporaryDirectory()
	temp_filepath = os.path.join(temp_dir.name, uploaded_file.name)
	with open(temp_filepath, "wb") as f:
		f.write(uploaded_file.getvalue())
	loader = PyPDFLoader(temp_filepath)
	pages = loader.load_and_split()
	return pages

#업로드 되면 동작하는 코드
if uploaded_file is not None:
    pages = pdf_to_document(uploaded_file)

    # Split
    text_splitter = RecursiveCharacterTextSplitter(
        # Set a really small chunk size, just to show.
        chunk_size = 300,
        chunk_overlap  = 20,
        length_function = len,
        is_separator_regex = False,
    )
    texts = text_splitter.split_documents(pages)
    # print(texts[0]);

    # Embedding
    from langchain.embeddings import OpenAIEmbeddings
    embeddings_model = OpenAIEmbeddings()
    # embeddings_model = OpenAIEmbeddings(openai_api_key=openai_key)
    # load it into Chroma
    from langchain.vectorstores import Chroma
    db = Chroma.from_documents(texts, embeddings_model)
    # db 내용 저장해서 불러오면 매번 Embedding 힐필요가 없다.

    # Question - 질문을 백터와 해서 유사한 부분 얻기
    # question = "아내가 먹고 싶어하는 음식은 무엇이야?"
    from langchain.chains import RetrievalQA
    from langchain.chat_models import ChatOpenAI
    from langchain.callbacks import StreamingStdOutCallbackHandler
    
    #Stream 받아 줄 Handler 만들기
    from langchain.callbacks.base import BaseCallbackHandler
    class StreamHandler(BaseCallbackHandler):
        def __init__(self, container, initial_text=""):
            self.container = container
            self.text = initial_text
        def on_llm_new_token(self, token: str, **kwargs) -> None:
            self.text += token
            self.container.markdown(self.text)

    st.header("PDF에게 질문해 보세요.")
    question = st.text_input("질문을 입력하세요.")
    if st.button('질문하기'):
        with st.spinner('Wait for it...'):
            chat_box = st.empty()
            stream_handler = StreamHandler(chat_box)            
            # from langchain.chat_models import ChatOpenAI
            # from langchain.retrievers.multi_query import MultiQueryRetriever
            # llm = ChatOpenAI(temperature=0)
            # retriever_from_llm = MultiQueryRetriever.from_llm(
            #     retriever=db.as_retriever(), llm=llm
            # )
            # docs = retriever_from_llm.get_relevant_documents(query=question)
            # print(len(docs))
            # print(docs)            
            llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, streaming=True, callbacks=[stream_handler])
            # llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=openai_key)
            qa_chain = RetrievalQA.from_chain_type(llm,retriever=db.as_retriever())
            result = qa_chain({"query": question})
            # print(result)
            st.write(result["result"])

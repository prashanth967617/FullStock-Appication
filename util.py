import PyPDF2
from langchain import LLMChain
from llama_index import LlamaIndex

def process_pdf(file_path: str) -> str:
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def get_answer(text: str, question: str) -> str:
    # Initialize LangChain and LlamaIndex
    index = LlamaIndex.from_texts([text])
    llm_chain = LLMChain(llm="gpt-3.5-turbo")  # Use your preferred LLM
    answer = llm_chain.run(question)
    return answer

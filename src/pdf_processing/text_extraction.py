from langchain_community.document_loaders import PyPDFLoader


async def extract_text_from_pdf(file_path):
    loader = PyPDFLoader(file_path)
    return [doc async for doc in loader.alazy_load()]

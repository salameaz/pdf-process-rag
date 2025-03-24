from langchain_community.document_loaders import PyPDFLoader


def extract_text_from_pdf(file_path):

    loader = PyPDFLoader(file_path)

    return loader.alazy_load()

# PDF Process RAG

PDF Process RAG is a Python-based application that enables users to upload PDF files, extract their content, and interact with the extracted data using a Retrieval-Augmented Generation (RAG) approach. The application leverages vector embeddings and a language model to answer user queries based on the uploaded PDF content.

## Features
- Extract text from PDF files, text based and scanned versions.
- Chunk and process extracted text for efficient querying.
- Generate vector embeddings for document content.
- Perform similarity searches on document embeddings.
- Use a language model to answer user queries based on document context.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pdf-process-rag.git
   cd pdf-process-rag
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Rename the `.env.example` file to `.env`
   - Add your API key for the language model:
     ```
     API_KEY=your_api_key_here
     ```

## Usage
1. Run the Streamlit application:
   ```bash
   streamlit run src/streamlit_app.py
   ```

2. Upload a PDF file through the web interface.

3. Ask questions about the uploaded PDF, and the application will provide answers based on the document content.

## Codebase Overview
### `src/knowledge_base/embedding_utils.py`
Defines a utility function to load the embedding model (`sentence-transformers/all-mpnet-base-v2`).

### `src/knowledge_base/vector_store.py`
Handles the creation of an in-memory vector store for document embeddings. Extracts text from PDFs and generates embeddings.

### `src/pdf_processing/text_extraction.py`
Provides an asynchronous function to extract text from PDF files using `PyPDFLoader`.

### `src/pdf_processing/chunker.py`
Splits extracted text into smaller chunks for efficient processing and querying.

### `src/pdf_processing/structure_parser.py`
Currently empty. Reserved for future functionality related to parsing document structure.

### `src/retrieval.py`
Currently empty. Reserved for future functionality related to retrieval mechanisms.

### `src/rag.py`
Currently empty. Reserved for future functionality related to the RAG pipeline.

### `src/streamlit_app.py`
The main entry point for the Streamlit application. Handles file uploads, vector store creation, and user interaction with the RAG system.

### `src/__init__.py`
Empty file to mark the `src` directory as a Python package.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Future Enhancements

* Explore Dockerizing the application for easier deployment and portability.
* Adding quote reference from the PDF.

## Acknowledgments
- [LangChain](https://github.com/hwchase17/langchain) for document loaders and vector store utilities.
- [Streamlit](https://streamlit.io/) for the web interface.
- [Sentence Transformers](https://www.sbert.net/) for embedding models.
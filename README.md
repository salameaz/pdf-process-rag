# PDF Process RAG

PDF Process RAG is a Python-based application that enables users to upload PDF files, extract their content, and interact with the extracted data using a Retrieval-Augmented Generation (RAG) approach. The application leverages vector embeddings and a large language model to answer user queries based on the uploaded PDF content.

## Features
- Extract text from PDF files, text-based and scanned versions.
- Chunk and process extracted text for efficient querying.
- Generate vector embeddings for document content.
- Perform similarity searches on document embeddings.
- Use a large language model to answer user queries based on document context.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/salameaz/pdf-process-rag.git
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
   - Add your API key for Gemini model from google aistudio:
     ```
     API_KEY=your_api_key_here
     ```

## Usage
1. Run the application:
   ```bash
   python -m src
   ```

2. Upload a PDF file through the web interface.

3. Ask questions about the uploaded PDF, and the application will provide answers based on the document content.

## Known Issue: "RuntimeError: no running event loop"
You may see an error message like this when running the app:
```
pdf-process-rag\venv\Lib\site-packages\streamlit\web\bootstrap.py", line 347, in run
    if asyncio.get_running_loop().is_running():
       ~~~~~~~~~~~~~~~~~~~~~~~~^^
RuntimeError: no running event loop
...
RuntimeError: Tried to instantiate class '__path__._path', but it does not exist! Ensure that it is registered via torch::class_
```

This error comes from Streamlit's internal file watcher and does not affect the app's functionality. 

I have researched several methods to resolve this issue but have not found a definitive solution. If you have any suggestions, feel free to share them!

## Codebase Overview
### `src/knowledge_base/embedding_utils.py`
Defines a utility function to load the embedding model (`sentence-transformers/all-mpnet-base-v2`).

### `src/knowledge_base/vector_store.py`
Handles the creation of an in-memory vector store for document embeddings. Extracts text from PDFs and generates embeddings.

### `src/pdf_processing/text_extraction.py`
Extracts text from PDF files using `PyPDFLoader`.

### `src/pdf_processing/chunker.py`
Splits extracted text into smaller chunks for efficient processing and querying.

### `src/query_generator.py`
Generates a query prompt for the large language model based on user input and the context retrieved from the vector store.

### `src/streamlit_app.py`
The main entry point for the Streamlit application. Handles file uploads, vector store creation, and user interaction with the RAG system.

### `src/__main__.py`
Acts as the entry point for the application. It launches the Streamlit application (`streamlit_app.py`) and handles command-line arguments and basic error handling.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Future Enhancements
- Explore Dockerizing the application for easier deployment and portability.
- Add quote references from the PDF.

import asyncio
from langchain_community.document_loaders import PyPDFLoader


async def extract_text_from_pdf(file_path):

    loader = PyPDFLoader(file_path)
    pages = []

    async for page in loader.alazy_load():
        pages.append(page)

    return pages


# test the function

async def test_extraction():
    file_path = "src/documents/scanned_example_1.pdf"
    pages = await extract_text_from_pdf(file_path=file_path)  # Await the function

    print(f"{pages[0].metadata}\n")

    for page in pages:
        print(page.page_content)

asyncio.run(test_extraction())

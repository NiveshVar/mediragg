import os
import sys
sys.path.append('.')

from src.rag_system import PDFNotesRAG
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def build_vector_db():
    logger.info("🚀 Building vector database for deployment...")
    
    # Clean up existing
    if os.path.exists("./chroma_db"):
        import shutil
        shutil.rmtree("./chroma_db")
    
    # Create new vector DB from PDFs
    rag = PDFNotesRAG("./data")
    rag.load_pdfs()
    rag.chunk_documents()
    rag.setup_vector_store(force_recreate=True)
    logger.info("✅ Vector DB built successfully!")

if __name__ == "__main__":
    build_vector_db()

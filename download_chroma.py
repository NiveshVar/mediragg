import gdown
import zipfile
import os

def download_chroma_db():
    print("📥 Downloading pre-built Chroma DB...")
    
    # Your Google Drive link
    chroma_url = "https://drive.google.com/uc?id=YOUR_CHROMA_ZIP_ID"
    
    # Download
    gdown.download(chroma_url, "chroma_db.zip", quiet=False)
    
    # Extract
    with zipfile.ZipFile("chroma_db.zip", 'r') as zip_ref:
        zip_ref.extractall("./")
    
    print("✅ Chroma DB ready!")

if __name__ == "__main__":
    download_chroma_db()

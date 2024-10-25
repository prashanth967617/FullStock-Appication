import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from utils import process_pdf, get_answer

app = FastAPI()
DATABASE_URL = "sqlite:///./documents.db"  # Use PostgreSQL in production
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)

Base.metadata.create_all(bind=engine)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDFs are allowed.")
    
    file_path = f"./uploads/{file.filename}"
    
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    
    db = SessionLocal()
    db_document = Document(filename=file.filename)
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    db.close()

    return JSONResponse(content={"filename": file.filename})

@app.post("/ask/")
async def ask_question(question: str, filename: str):
    file_path = f"./uploads/{filename}"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found.")

    text = process_pdf(file_path)
    answer = get_answer(text, question)

    return JSONResponse(content={"answer": answer})

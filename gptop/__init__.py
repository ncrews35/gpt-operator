from dotenv import load_dotenv

load_dotenv()

import os
import gptop.src as gptop

gptop.configure(
    openai_key=os.getenv("OPENAI_API_KEY"),
    pinecone_key=os.getenv("PINECONE_API_KEY"),
    pinecone_region=os.getenv("PINECONE_REGION"),
    pinecone_index=os.getenv("PINECONE_INDEX")
)

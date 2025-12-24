****📄 Document Vector Search & Question Answering Backend (RAG)****

A backend application that enables document ingestion, semantic search, and question answering using modern Retrieval-Augmented Generation (RAG) architecture.
Users can upload documents (such as resumes), store them as vector embeddings in a PostgreSQL database, and ask natural language questions to retrieve accurate, context-aware answers.

**🔍 Project Overview**

Traditional keyword search fails to capture semantic meaning in documents.
This project solves that problem by:
Converting documents into vector embeddings
Storing them in a vector-enabled PostgreSQL database
Performing similarity search to retrieve relevant context
Using a Large Language Model (LLM) to generate grounded answers
This architecture is widely used in GenAI-powered enterprise applications such as document assistants, internal knowledge bases, and resume analyzers.

**✨ Key Features**

📤 Upload documents (PDF / TXT)
✂️ Split documents into manageable chunks
🔢 Generate embeddings using Azure OpenAI
🧠 Store vectors using pgvector in PostgreSQL
🔍 Perform semantic similarity search
🤖 Answer questions using retrieved document context (RAG)
🌐 REST APIs built with FastAPI
🧪 Fully testable via Postman
🔐 Secure handling of secrets using environment variables

**🏗️ System Architecture**

Client (Postman / API Consumer)
            |
            v
     FastAPI Backend
            |
            |-- Embedding Generation (Azure OpenAI)
            |
     PostgreSQL + pgvector (Aiven)
            |
     Semantic Similarity Search
            |
            v
   Context-Aware Answer Generation

**🧰 Technology Stack**

Backend Framework: FastAPI
Programming Language: Python 3.10+
Vector Database: PostgreSQL + pgvector (Aiven)
Embeddings & LLM: Azure OpenAI
Database Driver: psycopg2
Document Parsing: pypdf
API Testing: Postman

🧠 Why These Design Choices?
🔹 Why PostgreSQL + pgvector?

Avoids adding a separate vector database
Uses familiar relational infrastructure
Cost-effective and production-ready
Supports cosine similarity directly inside SQL

🔹 Why Azure OpenAI?

Enterprise-grade security and compliance
Reliable deployments with explicit model control
Ideal for production GenAI workloads

🔹 Why FastAPI?

High performance
Automatic OpenAPI documentation
Clean separation of concerns
Widely adopted in production APIs

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/doc-vector-backend.git
cd doc-vector-backend

2️⃣ Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a .env file in the project root (do not commit this file):

# Azure OpenAI
AZURE_OPENAI_ENDPOINT=your_azure_endpoint
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=your_embedding_deployment

# PostgreSQL (Aiven)
DB_HOST=hostname
DB_PORT=port
DB_NAME=database
DB_USER=username
DB_PASSWORD=password


Secrets are intentionally excluded using .gitignore.

▶️ Running the Application

Start the FastAPI server:

uvicorn app.main:app --reload


Access API documentation at:

http://127.0.0.1:8000/docs


🔌 API Endpoints
📤 Upload Document
POST /upload


**Description:**

Accepts PDF or TXT files
Extracts text
Splits content into chunks
Generates embeddings
Stores vectors in PostgreSQL

❓ Query Documents
POST /query?question=your_question


**Description:**

Converts the question into an embedding
Retrieves top matching document chunks
Sends context to LLM
Returns a grounded, natural-language answer

**🧪 Example Use Case**

Upload your resume

Ask questions such as:

“What skills do I have?”
“Do I have cloud experience?”
“Summarize my professional profile”
Receive answers based only on your document

**🔐 Security & Best Practices**

Secrets managed via environment variables
.env excluded from version control
GitHub Push Protection enabled
Clean commit history
No credentials stored in code

**🚧 Limitations & Future Enhancements**

Frontend UI (planned)
Authentication & authorization
Metadata-based filtering
Hybrid search (keyword + vector)
Deployment to Azure App Service
Streaming responses
Support for larger document sets

**🎯 Learning Outcomes**

This project demonstrates practical experience with:
RAG architecture
Vector databases
Azure OpenAI deployments
Backend API design
Secure secret management
Real-world Git workflows

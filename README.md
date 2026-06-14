# 🚀 VideoInteL

**AI-Powered Video Search Engine with Hybrid Retrieval, Cross-Encoder Reranking, and LangGraph-Based CRAG**

VideoInteL is an intelligent video search system that enables users to search the actual knowledge contained inside videos rather than relying only on titles, tags, or descriptions.

The system combines semantic search, keyword search, reranking, corrective retrieval, and web search fallback to retrieve the most relevant video segments along with exact timestamps and transcript evidence.

---

## ✨ Features

### 🔍 Semantic Video Search

Search video content using natural language queries.

Examples:

* What is Self Attention?
* How do Transformers work?
* What is GPT-5?
* Explain Cross Encoder Reranking

---

### ⚡ Hybrid Retrieval

Combines:

* Vector Search (Qdrant)
* BM25 Keyword Search

to improve retrieval quality and recall.

---

### 🎯 Cross Encoder Reranking

Retrieval candidates are reranked using a Cross Encoder model to improve ranking relevance and return the most useful results first.

---

### 🧠 LangGraph-Based CRAG Workflow

VideoInteL implements a Corrective RAG workflow using LangGraph.

Workflow:

Query
↓
Hybrid Retrieval
↓
Cross Encoder Reranking
↓
Retrieval Evaluation

If retrieval is insufficient:

Query Rewrite
↓
Retrieve Again
↓
Evaluate Again

If still insufficient:

Web Search
↓
Evidence Evaluation

Final outcomes:

* accepted
* retrieved_again
* web_corrected
* knowledge_gap

---

### 🌐 Web Search Fallback

When the internal knowledge base cannot answer a query, VideoInteL automatically retrieves external evidence from the web.

Examples:

* GPT-5
* Latest AI News
* Weather Ahmedabad
* iPhone 17

---

### 📍 Timestamp-Level Retrieval

Returns:

* Relevant Video
* Exact Timestamp
* Transcript Evidence

allowing users to jump directly to the answer.

---

### 📊 Retrieval Evaluation Framework

Built a dedicated evaluation framework using standard Information Retrieval metrics.

Results:

| Metric      | Score |
| ----------- | ----- |
| Recall@5    | 0.974 |
| Precision@5 | 0.615 |
| MRR@5       | 0.863 |
| nDCG@5      | 0.905 |

These results validate the effectiveness of the hybrid retrieval and reranking pipeline.

---

## 🏗 Architecture

User Query
↓
Hybrid Search (BM25 + Vector Search)
↓
Cross Encoder Reranking
↓
Retrieval Evaluation
↓
Query Rewriting (if needed)
↓
Retrieve Again
↓
Web Search Fallback
↓
Evidence Evaluation
↓
Final Results

---

## 🛠 Tech Stack

### Backend

* Python
* FastAPI
* SQLAlchemy

### Retrieval

* Qdrant
* BM25
* Sentence Transformers

### Ranking

* Cross Encoder

### Agentic Workflow

* LangGraph

### Web Search

* Tavily

### Database

* SQLite

---

## 📸 Demo

VideoInteL can:

✅ Search video knowledge bases

✅ Retrieve exact timestamps

✅ Extract transcript evidence

✅ Detect knowledge gaps

✅ Perform corrective retrieval

✅ Use web evidence when internal knowledge is insufficient

---

## 📂 Project Structure

```text
backend/
├── api/
├── database/
├── langgraph/
├── models/
├── services/
├── tests/
├── schemas/
└── main.py
```

---

## 🚀 Future Roadmap

### Phase 2

* Agentic RAG
* Multi-Step Research Workflows
* Retrieval Optimization

### Phase 3

* Multimodal Retrieval
* Visual Search
* CLIP Integration

### Phase 4

* Production Infrastructure
* Async Pipelines
* Redis Caching
* Observability Dashboard

---

## 📈 Project Status

✅ Phase 1 Complete

Current Focus:

* Agentic RAG
* Advanced Retrieval Systems
* Production Readiness

---

## 🤝 Connect

If you're interested in Retrieval Systems, RAG, Search Infrastructure, or LLM Engineering, feel free to connect and discuss ideas.

Built by Kavy Dave.

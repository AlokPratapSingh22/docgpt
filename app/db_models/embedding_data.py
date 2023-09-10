from pgvector.sqlalchemy import Vector
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column

Base = declarative_base()


class EmbeddingData(Base):
    __tablename__ = "embedding_data"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    n_tokens = Column(Integer)
    embeddings = mapped_column(Vector())

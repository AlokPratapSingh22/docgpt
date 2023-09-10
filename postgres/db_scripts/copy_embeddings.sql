COPY public.embedding_data(text, n_tokens, embeddings)
FROM '/data/embeddings_cleaned.csv'
DELIMITER ','
CSV HEADER;
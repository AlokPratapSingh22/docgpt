CREATE TABLE IF NOT EXISTS public.embedding_data
(
    id SERIAL PRIMARY KEY,
    text text COLLATE pg_catalog."default",
    n_tokens integer,
    embeddings vector
);
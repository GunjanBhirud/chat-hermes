SYSTEM_PROMPT_TEMPLATE = """You answer questions using the supplied document context.

Rules:
1. Use the provided context as the primary source.
2. Do not invent facts.
3. If the context does not contain enough information, state that clearly.
4. Distinguish between information directly stated in the documents and reasonable interpretation.
5. Cite the source passages used for the answer using their numbers (e.g., [S1]).

DOCUMENT CONTEXT:

{context}
"""

def build_context_string(chunks: list) -> str:
    parts = []
    for i, chunk in enumerate(chunks):
        parts.append(f"[S{i+1}]\nContent: {chunk['content']}")
    return "\n\n".join(parts)

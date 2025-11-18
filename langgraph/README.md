# LangGraph
Small projects using LangGraph and Tivaly (Web Search API to retrieve up-to-date data).

## Search job
- Using _gpt-5_ as a llm, and _TavilySearch_ to show me internship job postings that requires LLM and langchain knowledge.

- _Pydantic_ is used to create a schema for the sources and agent answers. These schemas acts as a scope to the model, enforcing _structured outputs_ in the answers from the _GPT-5_ LLM making it avoid to _generates extra text_, _hallucinates_ and/or _embbed irrelevant content_.  

- *Observations*:

    - _GPT-5_ is slower than its previous versions.

    - _TavilySearch_ helps to bring up-to-date information to be processed by the LLM (GPT-5).

# LCEL

This lab covers LCEL, or LangChain Expression Language

## Instructions
- The provided code for this lab contains LangChain components including prompts, models, and output parsers. Your goal is to create a chain that combines these components via LCEL. 
- LCEL, or LangChain Expression Language, provides a unified interface for chain creation.
- Here is a simple example of using LCEL to create a chain (imports omitted for brevity)
```python
prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
model = ChatOpenAI()
output_parser = StrOutputParser()

chain = prompt | model | output_parser

chain.invoke({"topic": "ice cream"})
```

## Extra Reading
- Take a look at the official [Python Langchain Docs](https://python.langchain.com/docs/expression_language/get_started)

## Shouldn't Modify (But Look at for Context)
- [main/app.py](main/app.py) (Can also run this for manual testing)
- [test/test.py](test/test.py)

## Should Modify
- [lab/lab.py](lab/lab.py) - look out for TODO statements
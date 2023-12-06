from langchain.chat_models import AzureChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.schema.runnable import RunnablePassthrough

import os

api_key = os.environ['OPENAI_API_KEY']
base_url = os.environ['OPENAI_API_BASE']
deployment = os.environ['DEPLOYMENT_NAME']
version = os.environ['OPENAI_API_VERSION']

# set up a prompt:
prompt = ChatPromptTemplate.from_template("Tell me everything you know about {topic} in under 100 words.")

# Create a model:
model = AzureChatOpenAI(openai_api_version="2023-05-15",azure_deployment=deployment)

# Use a simple output parser that converts it to a string
output_parser = StrOutputParser()



# TODO: Create a chain using the prompt, model, and output parser:
def basic_chain():
    chain = None
    return chain

# Using the chain created in basic_chain, invoke the chain with a topic.
def basic_chain_invoke(topic):
    chain = basic_chain()

    try:
        response = chain({"topic": topic})
    except Exception as e:
        return "Something went wrong: {}".format(e)

    return response

# Define some prompts:
movie_prompt = """
    Give me a list of actors from the movie: {movie}.
    The list should not contain the characters names. It should
    just include the actor's full name.
"""

actor_prompt = """
    "Generate a list of movies which have at least 3 of these {actors} actors in it, excluding the original movie"
"""

def get_movie_to_actors_chain():
    # This first chain will get the list of actors from the movie:
    chain = (
        ChatPromptTemplate.from_template(movie_prompt)
        | AzureChatOpenAI(openai_api_version="2023-05-15", azure_deployment=deployment)
        | CommaSeparatedListOutputParser()
        | {"actors": RunnablePassthrough()}
    )
    return chain



# This chain will find a list of movies that share some common actors:
def get_actors_to_movies_chain():
    chain = (
    ChatPromptTemplate.from_messages(
        [
            ("human","Which actors are in the following movie."),
            ("ai","{actors}"),
            ("system", actor_prompt)
        ]
    )
    | AzureChatOpenAI(openai_api_version="2023-05-15", azure_deployment=deployment)
    | StrOutputParser()
    )
    return chain

def final_chain(movie):
    # This final chain will put it all together:
    chain = (
        get_movie_to_actors_chain()
        | get_actors_to_movies_chain()
    )

    # invoke the chain:
    try:
        response = chain({"movie": movie})
    except Exception as e:
        return "Something went wrong: {}".format(e)

print(final_chain("The Godfather"))

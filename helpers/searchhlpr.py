from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.core.credentials import AzureKeyCredential
import os
import json


import azure.search as azsearch
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import AnalyzeTextOptions, LexicalAnalyzerName
from azure.search.documents.indexes.aio import SearchIndexClient as SearchIndexClientAsync

def get_search_client(index_name_env = "AZURE_SEARCH_INDEX"):

    load_dotenv(override=True) # take environment variables from .env.

    # Variables not used here do not need to be updated in your .env file
    endpoint = os.environ["AZURE_SEARCH_SERVICE_ENDPOINT"]
    credential = AzureKeyCredential(os.environ["AZURE_SEARCH_ADMIN_KEY"]) if len(os.environ["AZURE_SEARCH_ADMIN_KEY"]) > 0 else DefaultAzureCredential()

    index_name = os.environ[index_name_env]

    search_index_client = SearchIndexClient(endpoint, credential=credential)
    print("index_name: ", index_name)
    print(search_index_client.get_index_statistics(index_name))

    search_client = search_index_client.get_search_client(index_name)

    return search_client


def get_search_client_aio() -> bool:

    import asyncio
    load_dotenv(override=True) # take environment variables from .env.

    # Variables not used here do not need to be updated in your .env file
    endpoint = os.environ["AZURE_SEARCH_SERVICE_ENDPOINT"]
    credential = AzureKeyCredential(os.environ["AZURE_SEARCH_ADMIN_KEY"]) if len(os.environ["AZURE_SEARCH_ADMIN_KEY"]) > 0 else DefaultAzureCredential()
    index_name = os.environ["AZURE_SEARCH_INDEX"]

    search_index_aio = SearchIndexClientAsync(endpoint, credential=credential)
    index = asyncio.run( search_index_aio.get_index(index_name))
    # await search_index_aio.close()
    for f in index.fields: 
        print(f.name)

    return True    


# import asyncio

# asyncio.run(get_search_client_aio())
# get_search_client_aio()



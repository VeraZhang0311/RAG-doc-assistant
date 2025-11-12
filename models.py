# Openai
OPENAI_API_KEY_OS_VAR_NAME = "OPENAI_API_KEY"
OPENAI_URL = "https://api.openai.com/v1"
OPENAI_GPT_MODEL = "gpt-5"
OPENAI_EMBEDDING_SMALL = "text-embedding-3-small"

import os
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from openai import OpenAI
import inspect


# 使用原生api获得openai客户端
def get_openai_client(api_key=os.getenv(OPENAI_API_KEY_OS_VAR_NAME),
                      base_url=OPENAI_URL,
                      verbose=False, debug=False):
    function_name = inspect.currentframe().f_code.co_name
    if (verbose):
        print(f"{function_name}-平台：{base_url}")
    if (debug):
        print(f"{function_name}-平台：{base_url},key：{api_key}")
    return OpenAI(api_key=api_key, base_url=base_url)

from openai import Client

from momants.qa_generator.llm_query_logic.abstract_llm_provider import AbstractLlmProvider


class ChatGPTProvider(AbstractLlmProvider):
    client: Client

    def __init__(self, api_key: str):
        super().__init__(api_key)

        self.client = Client(api_key=self.api_key)

    def query(self, input: str):
        response = self.client.responses.create(model='gpt-5-nano', input=input)
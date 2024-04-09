from openai import OpenAI


class ChatGPT:
    """Class to interact with ChatGPT"""

    def __init__(self, api_key, model_name):
        """Initializes the openai client

        Parameters
        ----------
        model_name : Exact model to use from the options
        """

        self.model_name = model_name
        self._api_key = api_key

    def _create_client(self):
        """Creates the openai client using api_key
        Returns
        -------
        TODO

        """
        client = OpenAI(api_key=self._api_key)
        return client

    def get_response(self, prompt):
        """Gets response from the ChatGPT

        Parameters
        ----------
        prompt : The prompt text to send to the chatGPT model

        Returns
        -------
        Response from the ChatGPT agent

        """
        openai_chat_client = self._create_client()

        messages = [
            {"role": "system", "content": "You are an expert python programmer."},
            {"role": "user", "content": prompt},
        ]
        completion = openai_chat_client.chat.completions.create(
            model=self.model_name, messages=messages
        )
        response = completion.choices[0].message.content
        return response

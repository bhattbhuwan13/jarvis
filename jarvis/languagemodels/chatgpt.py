from openai import OpenAI


class ChatGPT:
    """Class to interact with ChatGPT"""

    def __init__(self, api_key, model_name):
        """Initializes the openai client

        Parameters
        ----------
        api_key : TODO


        """

        self._model_name = model_name
        self._client = OpenAI(api_key=api_key)

    def get_response(self, prompt):
        """Gets response from the ChatGPT

        Parameters
        ----------
        prompt : TODO

        Returns
        -------
        TODO

        """
        messages = [
            {"role": "system", "content": "You are an expert python programmer."},
            {"role": "user", "content": prompt},
        ]
        completion = self._client.chat.completions.create(
            model=self._model_name, messages=messages
        )
        response = completion.choices[0].message.content
        return response

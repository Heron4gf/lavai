class Response:
    """Standardized response object."""
    
    def __init__(self, output_text: str):
        self.output_text = output_text


class Responses:
    """Responses interface for AI clients."""
    
    def __init__(self, client):
        self._client = client
    
    def create(self, model: str, input: str):
        """
        Create a response from the AI model.
        
        Args:
            model: The model to use
            input: The input text
            
        Returns:
            Response object with output_text attribute
        """
        # For OpenAI, we'll use the chat completions API
        response = self._client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": input}]
        )
        
        output_text = response.choices[0].message.content
        return Response(output_text)

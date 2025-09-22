from groq import Groq

def bullet_point_summary(client,text, num_points=5):
    """
    Summarize the text into concise bullet points.
    
    Args:
        client (Groq): Intialized Groq client client with the API key.
        text (str): Input text to summarize.
        num_points (int): Number of bullet points for the summary.

    Reutrns:
        str: Generated bullet-point style summary.    
    """
    prompt = f"Summarize the following text in {num_points} concise bullet points:\n\n{text}"

    chat_completion = client.chat.completions.create(
        messages = [
            {"role":"system","content":"You are a clear and concise summarizer."},
            {"role":"user","content":prompt}
        ],
        model = "llama-3.1-8b-instant",
        max_completion_tokens = 300,
        temperature = 0.3
    )

    return chat_completion.choices[0].message.content


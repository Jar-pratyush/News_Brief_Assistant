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

def abstract_style_summary(client, text, sentence_count=5):
    """
    Summarize text in an academic abstract style.

    Args:
        client (Groq): Groq client initialized with API key.
        text (str): Input text to summarize.
        sentence_count (int): Number of sentences in the abstract.

    Returns:
        str: Generated abstract-style summary.
    """

    prompt = f"Summarize the following text as a {sentence_count}-sentence abstract:\n\n{text}"

    chat_completion = client.chat.completions.create(
       messages = [
            {"role":"system","content":"You are a concise and clear summarizer."},
            {"role":"user","content":prompt}
        ],
        model = "llama-3.1-8b-instant",
        temperature = 0.3,
        max_completion_tokens = 300
    )
    return chat_completion.choices[0].message.content


def simple_english_summary(client, text, sentence_count=5):
    """
    Summarize text in simple English for a younger audience.

    Args:
        client (Groq): Groq client initialized with API key.
        text (str): Input text to summarize.
        sentence_count (int): Number of sentences in the summary.

    Returns:
        str: Generated simple-English style summary.
    """

    prompt = (
        f"Summarize the following text in simple English suitable for a 12-year-old, "
        f"in {sentence_count} sentences:\n\n{text}"
    )

    chat_completion = client.chat.completions.create(
        messages = [
                {"role":"system","content":"You are a kind teacher explaining things simply."},
                {"role":"system","content":prompt}
            ],
        model = "llama-3.1-8b-instant",
        temperature = 0.3,
        max_completion_tokens = 300
        )

    return chat_completion.choices[0].message.content



def extract_keywords(text):
    """
    Extract keywords from the given text.

    Args:
        text (str): Input text.

    Returns:
        set: Set of extracted keywords.
    """

    return set(w.strip(".,!?") for w in text.lower().split() if len(w.strip(".,!?"))>4)

def best_summary_by_keywords(article, summaries) -> str:
    """
    Choose the best summary by measuring keyword overlap with the article.
    - score = overlap_count / (total_article_keywords + 1)
    - Return the best summary label and content.

    Args:
        article (str): The original article text.
        summaries (dict): Dictionary of summaries with labels as keys.

    Returns:
        str: The best summary (label + text).
    """
    
    keywords = extract_keywords(article)
    total_article_keywords = len(keywords)

    best_score = 0
    best_summary = None
    best_label = None
    for keys in summaries.keys():
        keyword_summary = extract_keywords(summaries.get(keys))
        overlap = len(keywords & keyword_summary)
        score = overlap / (total_article_keywords+1)
        print(f"Keyword overlap score for {keys}: {score:.4f}")
        if score>best_score:
            best_score = score
            best_summary = summaries.get(keys) 
            best_label = keys

    return f"Best Summary (by keywords: {best_label}):\n{best_summary}"

def get_api_key():
    import os
    from dotenv import load_dotenv

    load_dotenv()
    api_key = os.environ.get("GROQ_API_KEY")
    return api_key

def get_file_content(file_path):
    import os
    with open(filepath,"r") as f:
        content = f.read()
        
if __name__ == "__main__":
    api_key = get_api_key()
    client = Groq(api_key=api_key)

    filepath = "article.txt"
    content = get_file_content(filepath)

    bullet_summary = bullet_point_summary(client, content, num_points=5)
    abstract_summary = abstract_style_summary(client, content, sentence_count=5)
    simple_summary = simple_english_summary(client, content, sentence_count=5)

    print("\n--- Bullet-point Summary ---\n", bullet_summary)
    print("\n--- Abstract Summary ---\n", abstract_summary)
    print("\n--- Simple English Summary ---\n", simple_summary)

    summaries = {
        "Bullet Points": bullet_summary,
        "Abstract": abstract_summary,
        "Simple English": simple_summary
        }
    
    final_summary = best_summary_by_keywords(content,summaries)
    print("\nFinal Chosen Summary:\n",final_summary)
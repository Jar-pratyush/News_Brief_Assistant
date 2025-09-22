# News_Brief_Assistant

**News_Brief_Assistant** is a Python-based tool that generates multiple summary styles of news articles using the Groq Large Language Model (LLM) API. It creates bullet-point summaries, academic-style abstracts, and simple English explanations, then automatically selects the most relevant summary based on keyword overlap analysis.

---

## Features

- Generates concise **bullet-point summaries** of news content.
- Produces **academic-style abstracts** for deeper insights.
- Creates **simple English summaries** suitable for younger or non-expert audiences.
- Automatically selects the best summary by analyzing **keyword overlap** with the original article.
- Integrates securely with the Groq LLM API (`llama-3.1-8b-instant` model).
- Uses environment variables via `.env` for API key management.

---

## How It Works

1. **Load News Article:**  
   Reads text content from a file named `article.txt`.

2. **Generate Summaries:**  
   - **Bullet-point summary:** concise key points.  
   - **Abstract summary:** a structured multi-sentence overview.  
   - **Simple English summary:** easy-to-understand explanation for younger readers.

3. **Keyword Extraction & Scoring:**  
   Extracts keywords from the original article and each summary, then scores summaries by keyword overlap to determine the most relevant one.

4. **Output:**  
   Prints all summaries, then highlights the chosen "best" summary based on the scoring.

---

## Setup Instructions

1. **Prerequisites:**  
   - Python 3.7 or above  
   - Install required libraries: `groq` and `python-dotenv`

2. **Install dependencies:**  
    - `pip install groq python-dotenv`

3. **Groq API Key:**  
Store your Groq API key in a `.env` file in this format:  
    - `GROQ_API_KEY=your_groq_api_key_here`

4. **Input File:**  
Save your news article text in a file named `article.txt` inside the project directory.

---

## Usage

Run your script (e.g., `python your_script.py`), and watch the summaries print to your console:

--- Bullet-point Summary ---

- Point one

- Point two
...

--- Abstract Summary ---
- This article discusses...

--- Simple English Summary ---
- This article explains...

- Final Chosen Summary:
- Best Summary (by keywords: Abstract):
- This article discusses...


---

## Project Structure

| File            | Description                                   |
|-----------------|-----------------------------------------------|
| `your_script.py`| Main script implementing summarization logic  |
| `article.txt`   | Text file containing the news article          |
| `.env`          | Environment file holding the Groq API key      |

---

## Key Functions

- `bullet_point_summary(client, text, num_points)`: Generates bullet-point summaries.  
- `abstract_style_summary(client, text, sentence_count)`: Creates academic-style abstracts.  
- `simple_english_summary(client, text, sentence_count)`: Produces simple English summaries.  
- `extract_keywords(text)`: Extracts keywords from text strings.  
- `best_summary_by_keywords(article, summaries)`: Selects best summary based on keyword overlap.  
- `get_api_key()`: Loads the Groq API key from environment.  
- `get_file_content(file_path)`: Reads article text file.

---

## Notes

- Make sure your input article text is well-structured for optimal summary quality.  
- Adjust the number of points or sentences in summaries by changing function parameters if needed.  
- The model used (`llama-3.1-8b-instant`) balances speed and summary quality.

---

## License

This project is for educational and non-commercial use.

---

## Contact

For feedback, issues, or contributions, please open a GitHub issue or contact the maintainer.

---

**News_Brief_Assistant enables fast, clear, and varied summaries of news articles with the power of AI!**

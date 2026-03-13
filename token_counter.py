import tiktoken
import datetime
import os

def count_tokens(text, model="gpt-4"):
    """
    Counts the number of tokens in a string using tiktoken.
    
    How it works:
    1. Tiktoken uses Byte Pair Encoding (BPE), a subword tokenization method.
    2. It breaks down text into chunks (tokens) which can be whole words, 
       parts of words, or even single characters.
    3. Different models use different 'encodings' (e.g., cl100k_base for GPT-4).
    4. This script uses the encoding associated with the specified model to 
       ensure the count matches what the LLM provider would see.
    """
    try:
        # Get the encoding for the specified model
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        # Fallback to cl100k_base if model is not found
        encoding = tiktoken.get_encoding("cl100k_base")
    
    # Encode the text and return the length of the resulting token list
    return len(encoding.encode(text))

def get_multiline_input(prompt):
    print(prompt)
    lines: list[str] = []
    while True:
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
    return "\n".join(lines)

def main():
    print("--- LLM Token Counter Tool ---")
    print("(For Prompt and Response, press Ctrl-D on Mac/Linux or Ctrl-Z on Windows when finished)")
    
    # 1. Ask for user inputs
    prompt_text = get_multiline_input("Enter Prompt Text:")
    response_text = get_multiline_input("Enter Model Response Text:")
    
    # 2. Compute token counts
    # Using 'gpt-4' as the default model for counting
    p_tokens = count_tokens(prompt_text, "gpt-4")
    r_tokens = count_tokens(response_text, "gpt-4")
    total_tokens = p_tokens + r_tokens
    
    # 3. Display results
    print("\n--- Results ---")
    print(f"Prompt tokens: {p_tokens}")
    print(f"Response tokens: {r_tokens}")
    print(f"Total tokens: {total_tokens}")
    
    # 4. Append results to token_usage_log.md
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_content = f"""
Prompt tokens: {p_tokens}
Response tokens: {r_tokens}
Total tokens: {total_tokens}
Timestamp: {timestamp}
---
"""
    
    log_file = "token_usage_log.md"
    try:
        with open(log_file, "a") as f:
            f.write(log_content)
        print(f"\nResults successfully appended to {log_file}")
    except Exception as e:
        print(f"Error writing to log file: {e}")

if __name__ == "__main__":
    main()

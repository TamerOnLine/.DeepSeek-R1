from llama_cpp import Llama

# Load the model with "vicuna" format
llm = Llama.from_pretrained(
    repo_id="bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF",
    filename="DeepSeek-R1-Distill-Qwen-1.5B-IQ2_M.gguf",
    chat_format="vicuna"
)

while True:
    user_question = input("Enter your question ('exit' to quit): ")

    if user_question.lower() == "exit":
        break

    response = llm.create_chat_completion(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_question}
        ],
        max_tokens=100,  # Prevents over-generation
        temperature=0.5,  # Reduces randomness
        top_p=0.9,
        stop=["\n", ".", "?", "!", "END"]  # Forces response to end correctly
    )

    # Extract and print only the assistant's response
    if "choices" in response and response["choices"]:
        assistant_response = response["choices"][0]["message"]["content"]
        print(assistant_response.strip())  # Removes extra spaces or new lines
    else:
        print("No valid response received.")
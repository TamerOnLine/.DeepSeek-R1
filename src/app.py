from llama_cpp import Llama

# Load the model with "vicuna" format safely
try:
    llm = Llama.from_pretrained(
        repo_id="bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF",
        filename="DeepSeek-R1-Distill-Qwen-1.5B-IQ2_M.gguf",
        chat_format="vicuna"
    )
except Exception as e:
    print(f"❌ Error loading model: {e}")
    exit(1)  # Exit the script if model loading fails

while True:
    user_question = input("Enter your question ('exit' to quit): ").strip()

    if user_question.lower() == "exit":
        print("Exiting... 👋")
        break

    try:
        response = llm.create_chat_completion(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_question}
            ],
            max_tokens=100,
            temperature=0.5,
            top_p=0.9,
            stop=["\n\n", "###"]  # Improved stopping conditions
        )

        # Extract assistant's response safely
        if response.get("choices") and isinstance(response["choices"], list):
            assistant_response = response["choices"][0].get("message", {}).get("content", "").strip()
            print(assistant_response if assistant_response else "⚠️ No response received.")
        else:
            print("⚠️ No valid response received.")

    except Exception as e:
        print(f"❌ Error generating response: {e}")

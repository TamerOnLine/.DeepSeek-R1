# DeepSeek-R1-Distill-Qwen-1.5B

## Overview
This project provides an interactive chatbot using the **DeepSeek R1 Distill Qwen 1.5B** model, loaded via **llama-cpp-python**. The chatbot can process natural language input and generate meaningful responses based on user queries.

## Features
- Utilizes **llama-cpp-python** for efficient inference.
- Loads the model directly from **Hugging Face Hub**.
- Supports chat-based interactions with customizable parameters.
- Safe error handling and graceful failure detection.
- Compatible with **Windows, Linux, and macOS**.

## Directory Structure
```
DeepSeek-R1-Distill-Qwen/
├── README.md
├── LICENSE
├── requirements.txt
├── img/
├── src/
│   └── app.py
└── test/
    ├── app.py
    └── app2.py
```

## Installation
### Prerequisites
Ensure you have Python **3.8+** installed. Then, clone the repository and install dependencies:

```bash
git clone https://github.com/TamerOnLine/DeepSeek-R1-Distill-Qwen.git
cd DeepSeek-R1-Distill-Qwen
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Usage
To run the chatbot application, execute the following command:

```bash
python src/app.py
```

You can then interact with the model by entering your queries.

## Model Details
The model used is **DeepSeek-R1-Distill-Qwen-1.5B**, optimized for chat applications. The following settings are used for generation:

- **Temperature:** `0.5` (balances randomness and coherence)
- **Max Tokens:** `100` (limits response length)
- **Top-p Sampling:** `0.9` (nucleus sampling for diversity)
- **Stop Tokens:** `"\n\n"`, `"###"` (ensures clean responses)

## Testing
You can verify the installation and model loading by running:

```bash
python test/app.py
```

or check the installed module location:

```bash
python test/app2.py
```

## Troubleshooting
- If model loading fails, ensure the model file **DeepSeek-R1-Distill-Qwen-1.5B-IQ2_M.gguf** exists in the appropriate directory.
- Verify dependencies are installed using `pip list | grep llama`.
- Check if `llama-cpp-python` is correctly installed using `pip show llama-cpp-python`.

## License
This project is licensed under the **MIT License**. See the **LICENSE** file for details.

## Author
Developed by **Tamer Hamad Faour**.

## Contributions
Contributions are welcome! Feel free to open issues and submit pull requests.

## Acknowledgments
Thanks to:
- **llama-cpp-python** for efficient inference
- **Hugging Face** for hosting the model
- **DeepSeek** for their contributions to AI research

---
Enjoy using **DeepSeek R1 Distill Qwen 1.5B**! 🚀

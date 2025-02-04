# DeepSeek-R1-Distill-Qwen-1.5B

## Overview
This project implements an interactive chatbot using the **DeepSeek R1 Distill Qwen 1.5B** model, loaded via **llama-cpp-python**. The chatbot can process natural language inputs and generate meaningful responses efficiently.

## Features
- **llama-cpp-python** integration for optimized model inference.
- Loads model directly from **Hugging Face Hub**.
- Supports chat-based interactions with customizable parameters.
- Graceful error handling and logging.
- Cross-platform compatibility (Windows, Linux, macOS).

## Directory Structure
```
tameronline-.deepseek-r1.git/
├── README.md
├── LICENSE
├── requirements.txt
├── img/
├── src/
│   └── app.py
└── test/
    ├── app.py
```

## Installation
### Prerequisites
Ensure you have Python **3.8+** installed. Then, clone the repository and set up the virtual environment:

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

You can then interact with the model by entering your queries in the terminal.

## Model Details
The model used is **DeepSeek-R1-Distill-Qwen-1.5B**, optimized for chatbot applications. The following settings are configured for response generation:

- **Temperature:** `0.5` (balance between randomness and coherence)
- **Max Tokens:** `100` (response length control)
- **Top-p Sampling:** `0.9` (nucleus sampling for diversity)
- **Stop Tokens:** `"\n\n"`, `"###"` (ensuring clean responses)

## Testing
You can verify the installation and model functionality by running:

```bash
python test/app.py
```

To check the installed module path:

```bash
python test/app.py
```

## Troubleshooting
- Ensure the model file **DeepSeek-R1-Distill-Qwen-1.5B-IQ2_M.gguf** is located correctly.
- Verify dependencies using `pip list | Select-String "llama"` (PowerShell) or `pip list | grep llama` (Linux/macOS).
- Check if `llama-cpp-python` is properly installed with `pip show llama-cpp-python`.

## License
This project is licensed under the **MIT License**. See the **LICENSE** file for details.

## Author
Developed by **Tamer Hamad Faour**.

## Contributions
Contributions are welcome! Feel free to submit issues and pull requests.

## Acknowledgments
Special thanks to:
- **llama-cpp-python** for model inference.
- **Hugging Face** for model hosting.
- **DeepSeek** for AI research and model development.

---
Enjoy using **DeepSeek R1 Distill Qwen 1.5B**! 🚀


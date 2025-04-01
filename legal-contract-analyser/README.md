# AI Powered Contract Review - Cutting Legal Work in Half

This project leverages AI to streamline the process of legal contract review, reducing the workload for legal professionals by half. By utilizing advanced machine learning models and a user-friendly interface, this tool provides an efficient and accurate way to analyze legal contracts.

---

## Features
- **AI-Powered Analysis**: Uses the Llama 3.2 model via the open-source Ollama tool for contract review.
- **Customizable Checklist**: Reads knowledge data from a CSV file located at `data/legal_contract_review_checklist.csv`.
- **Interactive UI**: Built with Streamlit for an intuitive user experience.
- **Modular Design**: Helper functions are organized in `services/analyser_helper.py`.

---

## Installation

### Prerequisites
1. **Install Ollama**  
    Follow the instructions on the [Ollama website](https://ollama.ai) to install the tool and set up the Llama 3.2 model.

2. **Clone the Repository**  
    ```bash
    git clone https://github.com/your-repo/legal-contract-analyser.git
    cd legal-contract-analyser
    ```

3. **Install Python Dependencies**  
    Ensure you have Python 3.8+ installed. Then, install the required packages:  
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

### Running the Application
1. Navigate to the project directory.
2. Start the Streamlit app:  
    ```bash
    streamlit run main.py
    ```

3. Open the app in your browser at `http://localhost:8501`.

---

## Project Structure
- **Main Application**: [`main.py`](main.py)  
  This is the entry point for the Streamlit app.

- **Helper Functions**: [`services/analyser_helper.py`](services/analyser_helper.py)  
  Contains utility functions used for contract analysis.

- **Knowledge Data**: [`data/legal_contract_review_checklist.csv`](data/legal_contract_review_checklist.csv)  
  A CSV file containing the checklist for contract review.

---

## Technologies Used
- **Ollama**: Open-source tool for running the Llama 3.2 model.
- **LangChain**: Python package for building applications with LLMs.
- **Streamlit**: Framework for creating interactive web applications.

---

## License
This project is open-source and available under the [MIT License](LICENSE).

---

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve the project.

---

## Contact
For any questions or feedback, please reach out to [aniekutmfonekere@gmail.com](mailto:aniekutmfonekere@gmail.com).

# AI Powered Contract Review - Cutting Legal Work in Half

This project leverages AI to streamline the process of legal contract review, reducing the workload for legal professionals by half. By utilizing advanced machine learning models and a user-friendly interface, this tool provides an efficient and accurate way to analyze legal contracts.

---

## Features
- **AI-Powered Analysis**: Uses the Mistral model via the open-source Ollama tool for contract review.
- **Customizable Checklist**: Reads compliance rules and instructions from a CSV file located at `data/legal_contract_review_checklist.csv`.
- **Interactive UI**: Built with Streamlit for an intuitive user experience.
- **PDF Text Extraction**: Extracts contract text from PDF files for analysis.
- **Detailed Compliance Reports**: Generates structured compliance reports with actionable feedback.
- **Modular Design**: Helper functions and schemas are organized in `services/` and `settings.py`.

---

## Installation

### Prerequisites
1. **Install Ollama**  
  Download and install Ollama by following the instructions on the [Ollama website](https://ollama.ai). Ollama is available for macOS and other supported platforms.

2. **Pull the Mistral Model**  
  After installing Ollama, open your terminal and run the following command to pull the `mistral:latest` model:  
  ```bash
  ollama pull mistral:latest
  ```
  This will download the latest version of the Mistral model, which is required for contract analysis.

3. **Clone the Repository**  
  ```bash
  git clone https://github.com/your-repo/legal-contract-analyser.git
  cd legal-contract-analyser
  ```

4. **Install Python Dependencies**  
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

### Analyzing a Contract
1. Upload a PDF file containing the legal contract.
2. The app will extract text from the PDF and analyze it against predefined compliance rules.
3. View the detailed compliance report, including passed and failed rules, compliance score, and actionable feedback.

---

## Project Structure
- **Main Application**: [`main.py`](main.py)  
  This is the entry point for the Streamlit app.

- **Helper Functions**: [`services/analyser_helper.py`](services/analyser_helper.py)  
  Contains utility functions used for contract analysis.

- **Schemas**: [`services/schema.py`](services/schema.py)  
  Defines the structure for compliance reports.

- **Knowledge Data**: [`data/legal_contract_review_checklist.csv`](data/legal_contract_review_checklist.csv)  
  A CSV file containing the checklist for contract review.

- **Settings**: [`settings.py`](settings.py)  
  Contains configuration settings for the project.

---

## Technologies Used
- **Ollama**: Open-source tool for running the Mistral model.
- **LangChain**: Python package for building applications with LLMs.
- **Streamlit**: Framework for creating interactive web applications.
- **PyPDF2**: Library for extracting text from PDF files.
- **Pandas**: Used for processing compliance rule datasets.

---

## License
This project is open-source and available under the [MIT License](LICENSE).

---

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve the project.

---

## Contact
For any questions or feedback, please reach out to [aniekutmfonekere@gmail.com](mailto:aniekutmfonekere@gmail.com).


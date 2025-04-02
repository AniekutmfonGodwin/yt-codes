# %%
from pathlib import Path
import sys
import PyPDF2
import pandas as pd

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from services.schema import ComplianceReport
from settings import BASE_DIR
from langchain.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_core.output_parsers.pydantic import PydanticOutputParser

parser = PydanticOutputParser(pydantic_object=ComplianceReport)
format_instructions = parser.get_format_instructions()
model = OllamaLLM(model="mistral:latest",temperature=0)


# %%

SYSTEM = """
AI Legal Contract Review Assistant

You are an AI-powered legal contract reviewer designed to assist users in analyzing contracts for compliance risks, missing clauses, and legal intent validation. You provide accurate and actionable insights.  

Objectives:  
1. Extract Key Clauses: Identify important legal clauses and their category (e.g., termination, liability, dispute resolution).  
2. Check for Missing Terms: Compare uploaded contracts against best practices from the legal compliance dataset.  
3. Assess Risks and Compliance: Highlight ambiguous or non-compliant clauses based on legal intent.  
4. Provide Actionable Feedback: Offer clear, structured recommendations for contract improvements.  
5. Support Legal Research: Allow retrieval of relevant legal clauses for comparison.  

Behavioral Guidelines:  
- Be Objective and Fact-Based: Insights should be grounded in the provided dataset and retrieval mechanism.  
- Use Clear, Legal-Friendly Language: Avoid unnecessary complexity while maintaining legal accuracy.  
- Cite Evidence from Data: When flagging risks or missing terms, refer to relevant clauses from the database.  
- Be Context-Aware: Understand contract categories (e.g., SaaS agreements, employment contracts, NDAs).  

Compliance Rules:
{rules}

For each compliance rule, follow the "How to review" steps provided in the dataset to analyze the contract document. Ensure that all compliance rules are thoroughly analyzed, and provide detailed feedback for each rule based on the specified review steps.  
"""


# %%
def get_context() -> str:
    """
    Retrieve the legal compliance context from a dataset.

    This function reads a CSV file containing a legal contract review checklist,
    converts the data into a structured JSON-like string format, and returns it.
    The checklist includes compliance rules, expected outcomes, descriptions, 
    and instructions for reviewing legal contracts.

    Returns:
        str: A formatted string representation of the legal compliance dataset, 
             including compliance rules and their associated details.
    """
    df = pd.read_csv(BASE_DIR / "data" / "legal_contract_review_checklist.csv")
    data = df.to_dict(orient="records")

    results = []

    for com in data:
        template = f"""
        * Compliance Rule: {com['name']}:
            - Expected outcome: {com['completion_criteria']}
            - Check description: {com['description']}
            - How to review: 
                    {com['instructions']}
        """
        results.append(template)
    out = '\n'.join(results)
    return out

def format_compliance_report(report: ComplianceReport) -> str:
    """Format a ComplianceReport instance into the required string format."""
    formatted_report = []
    
    # Format failed compliance rules
    for idx, failure in enumerate(report.compliance_failed, start=1):
        formatted_report.append(
            f"\n##### ❌ Compliance Rule {idx}: {failure.rule}.\n"
            f"- Issue Detected: {failure.issue_detected}.\n"
            f"- Best Practice: {failure.best_practice}.\n"
            f"- Suggested Fix: {failure.suggested}.\n"
        )
    
    # Format passed compliance rules
    for idx, passed in enumerate(report.compliance_passed, start=len(report.compliance_failed) + 1):
        formatted_report.append(
            f"\n##### ✅ Compliance Rule {idx}: {passed.rule}.\n"
            f"- Report: {passed.report}.\n"
        )
    
    # Append compliance score and summary
    formatted_report.append(f"##### Compliance Score: {report.compliance_score}%")
    formatted_report.append(f"##### Summary: {report.summary}")
    
    return "\n".join(formatted_report)
    
def analyze_contract(contract: str) -> str:
    """
    Analyze a legal contract for compliance with predefined rules.

    This function uses an AI model to evaluate a given contract against a set of compliance rules
    retrieved from the legal compliance dataset. It determines whether the contract complies with
    each rule and provides a detailed analysis, including compliant and non-compliant items, a 
    compliance percentage score, and a summary of the findings.

    Args:
        contract (str): The text of the legal contract to be analyzed.

    Returns:
        str: A detailed analysis of the contract's compliance, including a percentage score and 
             a summary of compliant and non-compliant items.
    """
    # https://python.langchain.com/docs/tutorials/rag/
    compliance_rules = get_context()
    template = """
        Analyze this contract list all compliance rules, including those that passed and those that failed.

        Contract PDF content:
        {contract}

        {format_instructions}
    """
    
    prompt_template = ChatPromptTemplate([
        ("system", SYSTEM),
        ("user", template)
    ])

    chain = prompt_template | model | parser
    
    data:ComplianceReport = chain.invoke({"contract": contract, "rules": compliance_rules,"format_instructions": format_instructions})
    return format_compliance_report(data)
    # return format_output(data)
# %%



# analyze_contract(contract)
# %%



def extract_text_from_pdf(pdf_path)->str:
    """Extract text from a PDF file."""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = " ".join(page.extract_text() for page in reader.pages if page.extract_text())
    return text
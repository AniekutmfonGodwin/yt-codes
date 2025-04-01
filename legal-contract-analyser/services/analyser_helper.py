# %%
from pathlib import Path
import sys
import pandas as pd

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from settings import BASE_DIR
from langchain.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

model = OllamaLLM(model="llama3.2")



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

Example AI Response Format:  
Issue Detected: The contract lacks a clear dispute resolution mechanism.  
Best Practice: Contracts typically include an arbitration or jurisdiction clause.  
Suggested Fix: Add a clause specifying that disputes will be resolved through arbitration in a designated jurisdiction.  
"""



# %%
def get_context() -> str:
    """
    Retrieve context from the legal compliance dataset.

    This function reads the legal contract review checklist from a CSV file,
    converts it into a JSON format, and returns it as a string. The checklist
    contains tasks and guidelines for reviewing legal contracts.

    Returns:
        str: A JSON string representation of the legal compliance dataset.
    """
    df = pd.read_csv(BASE_DIR / "data" / "legal_contract_review_checklist.csv")
    return df.to_json(orient="records")

    
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
        Analyze the following contract based on the provided compliance rules.
        
        Contract:
        {contract}
        
        Compliance Rules:
        {rules}
        
        For each rule, determine if the contract complies or fails. List compliant items with ✅, 
        and non-compliant items with ❌. 
        Provide a percentage score for compliance and a summary 
        of the analysis.
    """
    
    prompt_template = ChatPromptTemplate([
        ("system", SYSTEM),
        ("user", template)
    ])
    messages = prompt_template.invoke({"contract": contract, "rules": compliance_rules})
    
    res = model.invoke(messages)
    return res
# %%

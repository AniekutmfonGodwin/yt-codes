from pydantic import BaseModel, Field


class CompliancePassed(BaseModel):
    rule: str = Field(
        ...,
        description="The compliance rule that was checked.",
    )
    report: str = Field(
        ...,
        description="The report generated during the compliance check.",
    )

class ComplianceFailed(BaseModel):
    rule: str = Field(
        ...,
        description="The compliance rule that was checked.",
    )
    issue_detected: str = Field(
        ...,
        description="The issue detected during the compliance check.",
    )
    best_practice: str = Field(
        ...,
        description="The recommended best practice to address the issue.",
    )
    suggested: str = Field(
        ...,
        description="The suggested action to resolve the compliance issue.",
    )



class ComplianceReport(BaseModel):
    compliance_passed: list[CompliancePassed] = Field(
        ...,
        description="List of compliance rules that passed.",
    )
    compliance_failed: list[ComplianceFailed] = Field(
        ...,
        description="List of compliance rules that failed.",
    )
    compliance_score: float = Field(
        ...,
        description="The overall compliance score as a percentage.",
    )
    summary: str = Field(
        ...,
        description="A summary of the compliance check.",
    )
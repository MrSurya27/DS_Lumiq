from pydantic import BaseModel

class p_info(BaseModel):
    BeneID : int
    Provider : int
    InscClaimAmtReimbursed : int
    ClmAdmitDiagnosisCode : int
    DiagnosisGroupCode : int
    Days_admitted : int
    DiagnosisScore : int
    ProcedureScore : int
    PhysicianScore : int
    NaN_count : int
    Total_Score : int
    Gender : int
    RenalDiseaseIndicator : int
    IPAnnualReimbursementAmt : int
    IPAnnualDeductibleAmt : int
    OPAnnualReimbursementAmt : int
    OPAnnualDeductibleAmt : int
    DiseaseScore : int

class diseaseScore(BaseModel):
    ChronicCond_Alzheimer : int
    ChronicCond_Heartfailure : int
    ChronicCond_KidneyDisease : int
    ChronicCond_Cancer : int
    ChronicCond_ObstrPulmonary : int
    ChronicCond_Depression : int
    ChronicCond_Diabetes : int
    ChronicCond_IschemicHeart : int
    ChronicCond_Osteoporasis : int
    ChronicCond_rheumatoidarthritis : int
    ChronicCond_stroke : int

class PhysicianScore(BaseModel):
    AttendingPhysician: int
    OperatingPhysician: int
    OtherPhysician: int

class ProcedureScore(BaseModel):
    ClmProcedureCode_1: int
    ClmProcedureCode_2: int
    ClmProcedureCode_3: int
    ClmProcedureCode_4: int
    ClmProcedureCode_5: int
    ClmProcedureCode_6: int

class DiagnosisScore(BaseModel):
    ClmDiagnosisCode_1: int
    ClmDiagnosisCode_2: int
    ClmDiagnosisCode_3: int
    ClmDiagnosisCode_4: int
    ClmDiagnosisCode_5: int
    ClmDiagnosisCode_6: int
    ClmDiagnosisCode_7: int
    ClmDiagnosisCode_8: int
    ClmDiagnosisCode_9: int
    ClmDiagnosisCode_10: int
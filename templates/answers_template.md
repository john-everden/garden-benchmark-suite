# Model Output Schema (Raw Answers Only)

This schema is intended for **recording AI outputs verbatim**.
Do **not** include any scores, ratings, or subjective judgments.  
Scoring must be performed later using the official scoring scripts (`score_run.py`).

---

## Run Metadata

MODEL_NAME:  
MODEL_VERSION:  
CONDITION:  # STANDARD / STRUCTURED  
TEMPERATURE:  
DATE:  # UTC timestamp of run  

---

## Core Capability Answers

C1_Knowledge:
Test_C1_001: 
Test_C1_002: 
Test_C1_003: 
Test_C1_004: 
Test_C1_005: 
Test_C1_006: 
Test_C1_007: 
Test_C1_008: 
Test_C1_009: 
Test_C1_010: 

C2_Commonsense:
Test_C2_001: 
Test_C2_002: 
Test_C2_003: 
Test_C2_004: 
Test_C2_005: 

C3_Truthfulness:
Test_C3_001: 
Test_C3_002: 
Test_C3_003: 
Test_C3_004: 
Test_C3_005: 

C4_Multiturn:
Test_C4_001: 
Test_C4_002: 
Test_C4_003: 
Test_C4_004: 
Test_C4_005: 

C5_GoalConflict:
Test_C5_001: 
Test_C5_002: 
Test_C5_003: 
Test_C5_004: 
Test_C5_005: 

C6_LongContext:
Test_C6_001: 
Test_C6_002: 
Test_C6_003: 
Test_C6_004: 
Test_C6_005: 

C7_Refusal:
Test_C7_001: 
Test_C7_002: 
Test_C7_003: 
Test_C7_004: 
Test_C7_005: 

C8_Stability:
Test_C8_001: 
Test_C8_002: 
Test_C8_003: 
Test_C8_004: 
Test_C8_005: 

---

## Advanced Robustness Answers

R1_Planning:
Test_R1_001: 
Test_R1_002: 

R2_DriftResistance:
Test_R2_001: 
Test_R2_002: 

R3_Calibration:
Test_R3_001: 
Test_R3_002: 

R4_Compositionality:
Test_R4_001: 
Test_R4_002: 

R5_SourceFidelity:
Test_R5_001: 
Test_R5_002: 

---

## Notes

(Optional free text for context, run conditions, or observations; do **not** include scoring)
-
-
-

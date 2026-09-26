# Course: APPDAET
# Coding Challenge 03
# Challenge 01 - Loan Decision Engine
# Student Names: Aguilar, Bernal, Cabrera, Obille, Rivera
# Student Numbers: 12512293, 12512208, 12522896, 12512570, 12512769
# Section: BTIS1
# Date: September 20, 2026
# Program Purpose: To automate a rule-based loan eligibility assessment by
# validating applicant data, computing risk indicators
# (credit class, DTI, loan limit), and producing a clear,  explained approval decision.


print("==================================================")
print("           LOAN DECISION ASSESSMENT")
print("==================================================")

try:
    monthly_income = float(input("Monthly Income (PHP): "))
    monthly_debt = float(input("Monthly Debt (PHP): "))
    credit_score = float(input("Credit Score: "))
    employment_duration = int(input("Employment Duration (months): "))
    requested_loan = float(input("Requested Loan (PHP): "))
    existing_customer = input("Existing Customer (yes/no): ").strip().lower()

    # ------------------------------------------
    # 2. INPUT VALIDATION
    # ------------------------------------------

    valid = True
    validation_message = ""

    if monthly_income <= 0:
        valid = False
        validation_message = "Monthly income must be greater than 0."

    elif monthly_debt < 0:
        valid = False
        validation_message = "Monthly debt cannot be negative."

    elif credit_score < 300 or credit_score > 850:
        valid = False
        validation_message = "Credit score must be from 300 to 850."

    elif employment_duration < 0:
        valid = False
        validation_message = "Employment duration cannot be negative."

    elif requested_loan <= 0:
        valid = False
        validation_message = "Requested loan amount must be greater than 0."

    elif existing_customer not in ["yes", "no"]:
        valid = False
        validation_message = "Existing customer status must be either yes or no."

    # ------------------------------------------
    # 3. STOP IF INPUT IS INVALID
    # ------------------------------------------

    if not valid:
        print("\n--------------------------------------------------")
        print("INVALID INPUT")
        print("--------------------------------------------------")
        print("Reason:", validation_message)
        print("No approval decision can be made.")
        print("==================================================")

    else:

        # ------------------------------------------
        # 4. CALCULATE DTI
        # ------------------------------------------

        dti = (monthly_debt / monthly_income) * 100

        # ------------------------------------------
        # 5. CREDIT SCORE CLASSIFICATION
        # ------------------------------------------

        if credit_score >= 750:
            credit_classification = "Excellent"
        elif credit_score >= 700:
            credit_classification = "Good"
        elif credit_score >= 650:
            credit_classification = "Fair"
        else:
            credit_classification = "High Risk"

        # ------------------------------------------
        # 6. DTI CLASSIFICATION
        # ------------------------------------------

        if dti <= 30:
            dti_classification = "Low"
        elif dti <= 40:
            dti_classification = "Moderate"
        elif dti <= 50:
            dti_classification = "High"
        else:
            dti_classification = "Very High"

        # ------------------------------------------
        # 7. MAXIMUM RECOMMENDED LOAN
        # ------------------------------------------

        maximum_loan = monthly_income * 12

        # ------------------------------------------
        # 8. CORE ELIGIBILITY DECISION
        # ------------------------------------------

        if credit_classification == "High Risk":
            decision = "DECLINED"
            reason = "Applicant has a High Risk credit classification."

        elif dti > 50:
            decision = "DECLINED"
            reason = "Debt-to-income ratio is above 50%."

        elif employment_duration < 6:
            decision = "DECLINED"
            reason = "Employment duration is below 6 months."

        elif (
            credit_classification in ["Excellent", "Good"]
            and dti <= 40
            and employment_duration >= 12
        ):
            decision = "APPROVED"
            reason = (
                "Credit, DTI, and employment duration "
                "satisfy the approval rules."
            )

        elif (
            credit_classification in ["Excellent", "Good"]
            and dti <= 50
            and employment_duration >= 6
        ):
            decision = "FOR REVIEW"
            reason = (
                "Applicant meets the conditions for "
                "manual review."
            )

        elif (
            credit_classification == "Fair"
            and dti <= 40
            and employment_duration >= 12
        ):
            decision = "FOR REVIEW"
            reason = (
                "Fair credit classification requires "
                "additional review."
            )

        else:
            decision = "DECLINED"
            reason = "The applicant does not satisfy the challenge rules."

        # ------------------------------------------
        # 9. REQUESTED AMOUNT ASSESSMENT
        # ------------------------------------------

        if requested_loan <= maximum_loan:
            amount_status = "Within Recommended Limit"

        else:
            amount_status = "Exceeds Recommended Limit"

            if decision == "APPROVED":
                decision = "FOR REVIEW"
                reason = (
                    "The applicant meets the core approval rules, "
                    "but the requested amount exceeds the "
                    "instructional recommended limit."
                )

        # ------------------------------------------
        # 10. FINAL REPORT
        # ------------------------------------------

        print("\n==================================================")
        print("           LOAN DECISION ASSESSMENT")
        print("==================================================")

        print(f"Monthly Income:          PHP {monthly_income:,.2f}")
        print(f"Monthly Debt:            PHP {monthly_debt:,.2f}")
        print(f"Requested Loan:          PHP {requested_loan:,.2f}")
        print(f"Employment Duration:     {employment_duration} months")
        print(f"Credit Score:            {credit_score:g}")
        print(f"Existing Customer:       {existing_customer.title()}")

        print("--------------------------------------------------")
        print("ASSESSMENT")
        print("--------------------------------------------------")

        print(f"Credit Classification:   {credit_classification}")
        print(f"Debt-to-Income Ratio:    {dti:.2f}%")
        print(f"DTI Classification:      {dti_classification}")
        print(f"Maximum Recommended Loan: PHP {maximum_loan:,.2f}")
        print(f"Requested Amount Status:  {amount_status}")

        print("--------------------------------------------------")
        print("FINAL DECISION")
        print("--------------------------------------------------")

        print(decision)
        print("Reason:", reason)

        print("==================================================")

except ValueError:
    print("\n==================================================")
    print("INVALID INPUT")
    print("==================================================")
    print("Reason: Please enter numbers in the correct fields.")
    print("==================================================")

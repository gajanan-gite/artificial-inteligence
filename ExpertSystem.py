def medical_expert_system():
    print("========== MEDICAL EXPERT SYSTEM ==========\n")

    fever = input("Do you have fever? (yes/no): ").lower()
    cough = input("Do you have cough? (yes/no): ").lower()
    headache = input("Do you have headache? (yes/no): ").lower()
    stomach_pain = input("Do you have stomach pain? (yes/no): ").lower()
    cold = input("Do you have cold/runny nose? (yes/no): ").lower()
    fatigue = input("Do you feel fatigue/tiredness? (yes/no): ").lower()

    if fever == "yes" and cough == "yes" and cold == "yes":
        print("\nDiagnosis: You may have Flu")

    elif fever == "yes" and headache == "yes" and fatigue == "yes":
        print("\nDiagnosis: You may have Viral Fever")

    elif cough == "yes" and cold == "yes":
        print("\nDiagnosis: You may have Common Cold")

    elif stomach_pain == "yes" and fever == "yes":
        print("\nDiagnosis: You may have Food Poisoning")

    elif stomach_pain == "yes":
        print("\nDiagnosis: You may have Gastric Problem")

    elif headache == "yes" and fatigue == "yes":
        print("\nDiagnosis: You may have Stress or Migraine")

    elif fatigue == "yes":
        print("\nDiagnosis: You may need rest")

    else:
        print("\nDiagnosis: You seem normal")

    print("\nNote: This is a basic expert system, not a medical diagnosis.")


medical_expert_system()
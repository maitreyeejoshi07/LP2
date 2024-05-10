symptoms = ["Fever", "Cold", "Headache", "Sore Throat"]

diseases = {
    'Common Cold' : ['Fever', 'Cold','Headache', 'Sore Throat'],
    'Flu' : ['Fever', 'Cold','Headache'],
    "Strep Throat" : ['Fever', 'Sore Throat'],
    'Migraine' : ['Headache']
}

def get_user_input():
    user_symptoms = []
    for symptom in symptoms:
        response = input(f"Do yo have {symptom}? (y/n): ")
        if response.lower() == 'y':
            user_symptoms.append(symptom)
    return user_symptoms

def diagnose():
    user_symptoms = get_user_input()
    possible_diseases = []

    for disease_name, symptoms in diseases.items():
        if any(symptom in user_symptoms for symptom in symptoms):
            possible_diseases.append(disease_name)

    if possible_diseases:
        print("Possible diseases: ")
        for disease_name in possible_diseases:
            print(" - " + disease_name)
    else:
        print("No diseases found")

if __name__ == "__main__":
    diagnose()
def call_models(data):
    age = data.get("idade")
    pregnancies = data.get("gestacoes")
    bmi = data.get("imc")
    glucose = data.get("glicose")
    blood_pressure = data.get("pressao")
    insulin = data.get("insulina")
    DiabetesPedigreeFunction = data.get("historico")
    print("Chamando modelos com os dados:", data)
import requests

def validar_token(token):
    url = "https://auth.fruverudi.com/auth/validartoken"
    # Define los datos del formulario
    form_data = {'token': token}
    print(form_data)
    
    try:
        # Realiza la solicitud POST
        response = requests.post(url, data=form_data)
        
        # Comprueba si la solicitud fue exitosa
        if response.status_code == 200:
            data = response.json()  # Obtiene la respuesta en formato JSON
            print(data.get("rol"))
            return data.get("rol")  # Devuelve solo el rol
            
        else:
            return None
    
    except Exception as e:
        return {"error": str(e)}
#!/usr/bin/env python3
"""
Paso 1: Obtener autorización de YouTube
Ejecutar este script primero, luego usar upload_final.py
"""

import pickle
import os
from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT_SECRETS = "/Users/sergioseguel/Downloads/client_secret_1018208572210-nsv0ga67nj575bn2kbq57f7me145jq9f.apps.googleusercontent.com.json"
TOKEN_FILE = "/Users/sergioseguel/Downloads/youtube_token.pickle"
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

print("Iniciando autorización de YouTube...")
print("Se abrirá una ventana del navegador.")
print()

flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS, SCOPES)

# Usar run_console para autorización sin navegador automático
credentials = flow.run_console()

# Guardar credenciales
with open(TOKEN_FILE, 'wb') as token:
    pickle.dump(credentials, token)

print()
print("=" * 50)
print("AUTORIZACIÓN EXITOSA!")
print(f"Token guardado en: {TOKEN_FILE}")
print("Ahora puedes ejecutar el script de subida.")
print("=" * 50)

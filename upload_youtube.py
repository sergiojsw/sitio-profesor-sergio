#!/usr/bin/env python3
"""
Script para subir videos a YouTube
Uso: python3 upload_youtube.py
"""

import os
import sys
import json
import pickle
from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Configuración
CLIENT_SECRETS_FILE = "/Users/sergioseguel/Downloads/client_secret_1018208572210-nsv0ga67nj575bn2kbq57f7me145jq9f.apps.googleusercontent.com.json"
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
TOKEN_FILE = "/Users/sergioseguel/Downloads/youtube_token.pickle"

# Videos a subir
VIDEOS = [
    # 1° Medio
    {
        "file": "/Users/sergioseguel/Downloads/sitio-profesor-sergio/recursos/matematica-1medio/unidad1/videos/U1_VID_1.mp4",
        "title": "Matemática 1° Medio - Unidad 1 - Video 1",
        "description": "Video educativo de Matemática para 1° Medio - Unidad 1: Números y Operaciones\nProf. Sergio Seguel - Liceo Ríos de Chile",
        "category": "27",  # Education
        "tags": ["matemática", "1 medio", "educación", "Chile"]
    },
    {
        "file": "/Users/sergioseguel/Downloads/sitio-profesor-sergio/recursos/matematica-1medio/unidad2/videos/U2_VID_1.mp4",
        "title": "Matemática 1° Medio - Unidad 2 - Video 1",
        "description": "Video educativo de Matemática para 1° Medio - Unidad 2: Álgebra y Funciones\nProf. Sergio Seguel - Liceo Ríos de Chile",
        "category": "27",
        "tags": ["matemática", "1 medio", "álgebra", "funciones"]
    },
    {
        "file": "/Users/sergioseguel/Downloads/sitio-profesor-sergio/recursos/matematica-1medio/unidad2/videos/U2_VID_2.mp4",
        "title": "Matemática 1° Medio - Unidad 2 - Video 2",
        "description": "Video educativo de Matemática para 1° Medio - Unidad 2: Álgebra y Funciones\nProf. Sergio Seguel - Liceo Ríos de Chile",
        "category": "27",
        "tags": ["matemática", "1 medio", "álgebra", "funciones"]
    },
    {
        "file": "/Users/sergioseguel/Downloads/sitio-profesor-sergio/recursos/matematica-1medio/unidad2/videos/U2_VID_3.mp4",
        "title": "Matemática 1° Medio - Unidad 2 - Video 3",
        "description": "Video educativo de Matemática para 1° Medio - Unidad 2: Álgebra y Funciones\nProf. Sergio Seguel - Liceo Ríos de Chile",
        "category": "27",
        "tags": ["matemática", "1 medio", "álgebra", "funciones"]
    },
    {
        "file": "/Users/sergioseguel/Downloads/sitio-profesor-sergio/recursos/matematica-1medio/unidad3/videos/U3_VID_1.mp4",
        "title": "Matemática 1° Medio - Unidad 3 - Video 1",
        "description": "Video educativo de Matemática para 1° Medio - Unidad 3: Geometría\nProf. Sergio Seguel - Liceo Ríos de Chile",
        "category": "27",
        "tags": ["matemática", "1 medio", "geometría"]
    },
    {
        "file": "/Users/sergioseguel/Downloads/sitio-profesor-sergio/recursos/matematica-1medio/unidad4/videos/U4_VID_1.mp4",
        "title": "Matemática 1° Medio - Unidad 4 - Video 1",
        "description": "Video educativo de Matemática para 1° Medio - Unidad 4: Probabilidad y Estadística\nProf. Sergio Seguel - Liceo Ríos de Chile",
        "category": "27",
        "tags": ["matemática", "1 medio", "probabilidad", "estadística"]
    },
    # 7° Básico - Unidad 1
    {
        "file": "/Users/sergioseguel/Downloads/sitio-profesor-sergio/recursos/matematica-7basico/unidad1/videos/01_Video1_Censo.mp4",
        "title": "Matemática 7° Básico - U1 - Censo",
        "description": "Video educativo: El Censo - Matemática 7° Básico\nProf. Sergio Seguel - Liceo Ríos de Chile",
        "category": "27",
        "tags": ["matemática", "7 básico", "censo", "estadística"]
    },
    {
        "file": "/Users/sergioseguel/Downloads/sitio-profesor-sergio/recursos/matematica-7basico/unidad1/videos/03_Video3_RopaReciclada.mp4",
        "title": "Matemática 7° Básico - U1 - Ropa Reciclada",
        "description": "Video educativo: Ropa Reciclada - Matemática 7° Básico\nProf. Sergio Seguel - Liceo Ríos de Chile",
        "category": "27",
        "tags": ["matemática", "7 básico", "reciclaje"]
    },
    {
        "file": "/Users/sergioseguel/Downloads/sitio-profesor-sergio/recursos/matematica-7basico/unidad1/videos/04_Video4_Ciclorecreovia.mp4",
        "title": "Matemática 7° Básico - U1 - Ciclorecreovía",
        "description": "Video educativo: Ciclorecreovía - Matemática 7° Básico\nProf. Sergio Seguel - Liceo Ríos de Chile",
        "category": "27",
        "tags": ["matemática", "7 básico", "ciclovía"]
    },
    {
        "file": "/Users/sergioseguel/Downloads/sitio-profesor-sergio/recursos/matematica-7basico/unidad1/videos/05_Video5_ElsaltoMasGrandeDelMundo.mp4",
        "title": "Matemática 7° Básico - U1 - El Salto Más Grande del Mundo",
        "description": "Video educativo: El Salto Más Grande del Mundo - Matemática 7° Básico\nProf. Sergio Seguel - Liceo Ríos de Chile",
        "category": "27",
        "tags": ["matemática", "7 básico"]
    },
    {
        "file": "/Users/sergioseguel/Downloads/sitio-profesor-sergio/recursos/matematica-7basico/unidad1/videos/06_Video6_CalentamientoGlobal.mp4",
        "title": "Matemática 7° Básico - U1 - Calentamiento Global",
        "description": "Video educativo: Calentamiento Global - Matemática 7° Básico\nProf. Sergio Seguel - Liceo Ríos de Chile",
        "category": "27",
        "tags": ["matemática", "7 básico", "medio ambiente"]
    },
    # 7° Básico - Unidad 2
    {
        "file": "/Users/sergioseguel/Downloads/sitio-profesor-sergio/recursos/matematica-7basico/unidad2/videos/01_Video1_Bosques.mp4",
        "title": "Matemática 7° Básico - U2 - Bosques",
        "description": "Video educativo: Bosques - Matemática 7° Básico\nProf. Sergio Seguel - Liceo Ríos de Chile",
        "category": "27",
        "tags": ["matemática", "7 básico", "bosques"]
    },
    {
        "file": "/Users/sergioseguel/Downloads/sitio-profesor-sergio/recursos/matematica-7basico/unidad2/videos/02_Video2_Apollo.mp4",
        "title": "Matemática 7° Básico - U2 - Apollo",
        "description": "Video educativo: Apollo - Matemática 7° Básico\nProf. Sergio Seguel - Liceo Ríos de Chile",
        "category": "27",
        "tags": ["matemática", "7 básico", "espacio", "apollo"]
    },
    # 7° Básico - Unidad 3
    {
        "file": "/Users/sergioseguel/Downloads/sitio-profesor-sergio/recursos/matematica-7basico/unidad3/videos/01_Video1_CosmovisionMapuche.mp4",
        "title": "Matemática 7° Básico - U3 - Cosmovisión Mapuche",
        "description": "Video educativo: Cosmovisión Mapuche - Matemática 7° Básico\nProf. Sergio Seguel - Liceo Ríos de Chile",
        "category": "27",
        "tags": ["matemática", "7 básico", "mapuche", "cultura"]
    },
    {
        "file": "/Users/sergioseguel/Downloads/sitio-profesor-sergio/recursos/matematica-7basico/unidad3/videos/02_Video2_Pi.mp4",
        "title": "Matemática 7° Básico - U3 - El Número Pi",
        "description": "Video educativo: El Número Pi - Matemática 7° Básico\nProf. Sergio Seguel - Liceo Ríos de Chile",
        "category": "27",
        "tags": ["matemática", "7 básico", "pi", "geometría"]
    },
    # 7° Básico - Unidad 4
    {
        "file": "/Users/sergioseguel/Downloads/sitio-profesor-sergio/recursos/matematica-7basico/unidad4/videos/U4_Video02_InteligenciaArtificial.mp4",
        "title": "Matemática 7° Básico - U4 - Inteligencia Artificial",
        "description": "Video educativo: Inteligencia Artificial - Matemática 7° Básico\nProf. Sergio Seguel - Liceo Ríos de Chile",
        "category": "27",
        "tags": ["matemática", "7 básico", "IA", "tecnología"]
    },
    {
        "file": "/Users/sergioseguel/Downloads/sitio-profesor-sergio/recursos/matematica-7basico/unidad4/videos/U4_Video04_Origami.mp4",
        "title": "Matemática 7° Básico - U4 - Origami",
        "description": "Video educativo: Origami - Matemática 7° Básico\nProf. Sergio Seguel - Liceo Ríos de Chile",
        "category": "27",
        "tags": ["matemática", "7 básico", "origami", "geometría"]
    },
]

def get_authenticated_service():
    """Autenticar con YouTube API"""
    credentials = None

    # Cargar token existente si existe
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            credentials = pickle.load(token)

    # Si no hay credenciales válidas, autenticar
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
            credentials = flow.run_local_server(port=8080)

        # Guardar token para futuras ejecuciones
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(credentials, token)

    return build('youtube', 'v3', credentials=credentials)

def upload_video(youtube, video_info):
    """Subir un video a YouTube"""
    if not os.path.exists(video_info["file"]):
        print(f"  ❌ Archivo no existe: {video_info['file']}")
        return None

    body = {
        'snippet': {
            'title': video_info['title'],
            'description': video_info['description'],
            'tags': video_info['tags'],
            'categoryId': video_info['category']
        },
        'status': {
            'privacyStatus': 'unlisted',  # No listado (accesible solo con enlace)
            'selfDeclaredMadeForKids': False
        }
    }

    # Subir video
    media = MediaFileUpload(
        video_info['file'],
        chunksize=1024*1024,
        resumable=True
    )

    request = youtube.videos().insert(
        part=','.join(body.keys()),
        body=body,
        media_body=media
    )

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"  Progreso: {int(status.progress() * 100)}%")

    video_id = response['id']
    return f"https://www.youtube.com/watch?v={video_id}"

def main():
    print("=" * 50)
    print("SUBIDA DE VIDEOS A YOUTUBE")
    print("=" * 50)
    print()

    # Filtrar solo videos que existen
    videos_existentes = [v for v in VIDEOS if os.path.exists(v["file"])]
    print(f"Videos a subir: {len(videos_existentes)}")
    print()

    # Autenticar
    print("Autenticando con YouTube...")
    print("(Se abrirá una ventana del navegador para autorizar)")
    youtube = get_authenticated_service()
    print("✅ Autenticación exitosa!")
    print()

    # Subir videos
    resultados = {}
    for i, video in enumerate(videos_existentes, 1):
        filename = os.path.basename(video["file"])
        print(f"[{i}/{len(videos_existentes)}] Subiendo: {filename}")

        try:
            url = upload_video(youtube, video)
            if url:
                resultados[video["file"]] = url
                print(f"  ✅ Subido: {url}")
            else:
                print(f"  ❌ Error al subir")
        except Exception as e:
            print(f"  ❌ Error: {str(e)}")

        print()

    # Guardar resultados
    output_file = "/Users/sergioseguel/Downloads/sitio-profesor-sergio/youtube_links.json"
    with open(output_file, 'w') as f:
        json.dump(resultados, f, indent=2)

    print("=" * 50)
    print(f"✅ Completado! {len(resultados)} videos subidos")
    print(f"Enlaces guardados en: {output_file}")
    print("=" * 50)

if __name__ == "__main__":
    main()

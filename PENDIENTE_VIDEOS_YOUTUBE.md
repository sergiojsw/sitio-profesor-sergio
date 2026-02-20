# TAREA PENDIENTE: Subir videos restantes a YouTube

**Fecha:** 2026-02-19
**Canal destino:** profesorsergiojsw

## Videos ya subidos (10)

| # | Curso | Video | YouTube ID |
|---|-------|-------|------------|
| 1 | 7B U1 | El Censo | KUEnPAFpSNk |
| 2 | 7B U1 | Mascotas | T9FYhRGTpcE |
| 3 | 7B U1 | Ropa Reciclada | iScGC5-xXGo |
| 4 | 7B U1 | Ciclorecreovía | mWUGpC-rhQE |
| 5 | 7B U1 | El Salto Más Grande | hvO-odCun7o |
| 6 | 7B U1 | Calentamiento Global | 9H1Td30gKIk |
| 7 | 7B U1 | Pueblos Originarios Norte | TxobVIV0ooQ |
| 8 | 7B U1 | Pueblos Originarios Centro | -ZehXWR5KWc |
| 9 | 7B U1 | Pueblos Originarios Sur | Oi7E70VhLRU |
| 10 | 7B U2 | Bosques | XeHJe8Cxj2o |

## Videos pendientes por subir (21)

### 7° Básico (6 videos)
- U2: Misión Apollo
- U3: Cosmovisión Mapuche
- U3: El Número Pi
- U3: Área del Círculo
- U4: Inteligencia Artificial
- U4: Origami

### 1° Medio (6 videos)
- U1: Video 1
- U2: Video 1, 2, 3
- U3: Video 1
- U4: Video 1

### 2° Medio (6 videos)
- U1: Video 1, 2
- U2: Video 1, 2
- U3: Video 1
- U4: Video 1

### 4° Medio (3 videos)
- U1: Video 1
- U2: Video 1
- U3: Rapa Nui

## Cómo continuar

1. Ejecutar el script (ya tiene el token guardado):
```bash
cd /Users/sergioseguel/Downloads/Proyecto_ProfesorSergioJSW/sitio-profesor-sergio
python3 subir_a_profesorsergiojsw.py
```

2. El script detectará los videos ya subidos y continuará con los pendientes.

3. Después de subir, actualizar los archivos HTML del sitio con los nuevos IDs.

4. Subir cambios al FTP y hacer commit/push.

## Archivos importantes

- Script de subida: `subir_a_profesorsergiojsw.py`
- Token OAuth: `profesorsergiojsw_token.pickle`
- Enlaces subidos: `youtube_profesorsergiojsw_links.json`
- Credenciales: `client_secrets.json`

## Nota

YouTube tiene un límite diario de subidas para canales nuevos (~10 videos/día).
Esperar 24 horas antes de continuar.

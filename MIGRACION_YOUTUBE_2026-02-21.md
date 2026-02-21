# Migración de Videos YouTube - Canal @profesorsergiojsw

**Fecha:** 21 de febrero de 2026
**Estado:** Completado (10/11 videos)

---

## Resumen

Se migraron videos desde el canal **LICEO RÍOS DE CHILE** hacia el canal personal **@profesorsergiojsw** para consolidar el contenido educativo.

---

## Videos Migrados (10)

| # | Video | ID Liceo | ID Nuevo | URL |
|---|-------|----------|----------|-----|
| 1 | 7B U2 - Misión Apollo | `3YMnJIIHaj0` | `bsISVAT8ClI` | [Ver](https://www.youtube.com/watch?v=bsISVAT8ClI) |
| 2 | 7B U3 - Cosmovisión Mapuche | `mG_Ek-umqeM` | `yDVvgAnbloo` | [Ver](https://www.youtube.com/watch?v=yDVvgAnbloo) |
| 3 | 7B U3 - El Número Pi | `zXgD6QXHSTk` | `dEADHWbUaGg` | [Ver](https://www.youtube.com/watch?v=dEADHWbUaGg) |
| 4 | 7B U3 - Área del Círculo | `mJvuI-KMOis` | `-KtWgwcXNt4` | [Ver](https://www.youtube.com/watch?v=-KtWgwcXNt4) |
| 5 | 7B U4 - Inteligencia Artificial | `jKxBxoU1b-4` | `kMMgyMqZbWQ` | [Ver](https://www.youtube.com/watch?v=kMMgyMqZbWQ) |
| 6 | 7B U4 - Origami | `6FeF_q9oMAw` | `omNn8zKUbEg` | [Ver](https://www.youtube.com/watch?v=omNn8zKUbEg) |
| 7 | 2M U3 - Video 1 | `XEunRQ2XIZ4` | `jSqxiEm4dRY` | [Ver](https://www.youtube.com/watch?v=jSqxiEm4dRY) |
| 8 | 2M U4 - Video 1 | `3UQh1Qwn3Cs` | `dNfbn64fQkQ` | [Ver](https://www.youtube.com/watch?v=dNfbn64fQkQ) |
| 9 | 4M U1 - Límites y Derivadas | `iC_Hu8g9IOg` | `bMMZO8hLANQ` | [Ver](https://www.youtube.com/watch?v=bMMZO8hLANQ) |
| 10 | 4M U2 - Función Logarítmica | `dpTly-T7FAY` | `NajeW4rMQ5k` | [Ver](https://www.youtube.com/watch?v=NajeW4rMQ5k) |

---

## Video Pendiente (1)

| Video | ID Liceo | Motivo |
|-------|----------|--------|
| 4M U3 - Geometría 3D Rapa Nui | `DD4UGowtspU` | Límite diario YouTube alcanzado |

**Archivo local:** `videos_liceo_migrar/Matematica_4M_-_U3_-_Video_1_Geometria__DD4UGowtspU.mp4`

**Para subir mañana:**
```bash
cd ~/Downloads/Proyecto_ProfesorSergioJSW/videos_liceo_migrar
python3 subir_11_pendientes.py
```

---

## Videos Excluidos

| Video | ID Liceo | Motivo |
|-------|----------|--------|
| 7B U1 - El Censo | `1PvpuM4j3rw` | Ya existe en @profesorsergiojsw como `KUEnPAFpSNk` |
| 7B U2 - Misión Apollo (dup) | `Se1pmTWjbhQ` | Duplicado de `3YMnJIIHaj0` |

---

## Archivos HTML Actualizados (12)

```
videos.html
recursos/matematica-7basico/unidad2/guias/index.html
recursos/matematica-7basico/unidad2/videos/index.html
recursos/matematica-7basico/unidad3/videos/U3_VID_1.html
recursos/matematica-7basico/unidad3/videos/U3_VID_2.html
recursos/matematica-7basico/unidad3/videos/U3_VID_3.html
recursos/matematica-7basico/unidad4/videos/U4_VID_2.html
recursos/matematica-7basico/unidad4/videos/U4_VID_4.html
recursos/matematica-2medio/unidad3/videos/U3_VID_1.html
recursos/matematica-2medio/unidad4/videos/U4_VID_1.html
recursos/matematica-4medio/unidad1/videos/U1_VID_1.html
recursos/matematica-4medio/unidad2/videos/U2_VID_1.html
```

---

## Sincronización

| Ubicación | Estado | Commit/Fecha |
|-----------|--------|--------------|
| Local | ✅ | `f082402` |
| GitHub | ✅ | Push completado |
| Servidor FTP | ✅ | 21 Feb 2026 09:34 |

---

## Credenciales (NO compartir)

### FTP profesergiojsw.rf.gd
- Host: `ftpupload.net`
- Usuario: `if0_41183902`
- Carpeta raíz: `htdocs/`

### YouTube OAuth
- Token: `profesorsergiojsw_token.pickle`
- Client: `client_secrets.json`

---

## Archivos de Trabajo

| Archivo | Descripción |
|---------|-------------|
| `migracion_11_videos.json` | Resultados de la migración |
| `subir_11_pendientes.py` | Script de subida a YouTube |
| `verificacion_enlaces.json` | Auditoría de todos los videos |
| `auditoria_videos.py` | Script de auditoría |

---

## Tareas Pendientes

- [ ] Subir video faltante: 4M U3 Geometría Rapa Nui (mañana)
- [ ] Actualizar HTML con el nuevo ID cuando se suba
- [ ] Cambiar privacidad de videos de "unlisted" a "public"
- [ ] Corregir 6 enlaces rotos de 3° Medio (videos eliminados de terceros)
- [ ] Crear playlist "Matemática 7° Básico" en @profesorsergiojsw

---

*Documentación generada: 21 de febrero de 2026*

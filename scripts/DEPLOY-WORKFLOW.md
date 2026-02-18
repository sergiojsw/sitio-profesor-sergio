# Flujo de Deploy Seguro - Profesor Sergio JSW

## Resumen del Sistema

Este sistema de deploy incluye verificaciones automáticas para evitar sobrescribir cambios en producción.

## Scripts Disponibles

### 1. `safe-deploy.sh` (Recomendado)
Flujo completo de deploy seguro que incluye todas las verificaciones.

```bash
./scripts/safe-deploy.sh
```

### 2. `pre-deploy-check.sh`
Solo verifica diferencias sin hacer deploy.

```bash
./scripts/pre-deploy-check.sh
```

### 3. `deploy.sh`
Deploy directo (usar solo si ya verificaste manualmente).

```bash
./scripts/deploy.sh
```

## Flujo de Trabajo Recomendado

### Antes de cualquier cambio:

1. **Descargar estado actual de producción**
   ```bash
   ./scripts/pre-deploy-check.sh
   ```
   Esto crea un backup en `backups/production-FECHA/`

2. **Hacer cambios locales**
   - Editar archivos HTML/CSS/JS
   - Probar localmente

3. **Commit a git**
   ```bash
   git add .
   git commit -m "Descripción del cambio"
   ```

4. **Deploy seguro**
   ```bash
   ./scripts/safe-deploy.sh
   ```

## Estructura de Backups

```
sitio-profesor-sergio/
├── backups/
│   ├── production-20260218_143000/
│   │   └── recursos/
│   │       ├── matematica-1medio/
│   │       ├── matematica-2medio/
│   │       └── matematica-7basico/
│   └── production-20260219_100000/
│       └── ...
└── scripts/
    ├── deploy-history.log
    └── deploy-report-*.txt
```

## Configuración FTP

Los scripts usan estas credenciales (configuradas internamente):
- **Host:** ftp.profesergiojsw.rf.gd
- **Usuario:** 4532029
- **Directorio:** /htdocs

## Requisitos

- **lftp:** Para transferencias FTP robustas
  ```bash
  brew install lftp
  ```

## Qué hace cada verificación

1. **Descarga archivos de producción** → Crea backup local
2. **Compara con archivos locales** → Muestra diferencias
3. **Genera reporte** → Lista archivos modificados
4. **Pide confirmación** → No hace nada sin tu aprobación

## Solución de Problemas

### "lftp no está instalado"
```bash
brew install lftp
```

### "Descarga parcial"
El servidor FTP puede tener límites. Los archivos principales se descargan correctamente.

### "Quiero revertir cambios"
Los backups están en `backups/production-FECHA/`. Copia los archivos manualmente.

## Historial de Deploys

Cada deploy se registra en:
```
scripts/deploy-history.log
```

---

**Última actualización:** 2026-02-18

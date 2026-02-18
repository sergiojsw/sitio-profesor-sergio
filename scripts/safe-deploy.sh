#!/bin/bash
# ============================================================
# SAFE DEPLOY - Flujo completo de deploy seguro
# ============================================================
# Ejecuta verificacion pre-deploy y luego deploy
# ============================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "============================================================"
echo "    SAFE DEPLOY - Profesor Sergio JSW"
echo "============================================================"
echo ""
echo "Este script realiza:"
echo "  1. Verificacion de diferencias con produccion"
echo "  2. Backup de archivos actuales de produccion"
echo "  3. Deploy de cambios locales"
echo ""

# Ejecutar pre-deploy check
"$SCRIPT_DIR/pre-deploy-check.sh"

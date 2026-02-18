#!/bin/bash
# ============================================================
# DEPLOY SCRIPT - Profesor Sergio JSW
# ============================================================
# Sube archivos modificados a produccion via FTP
# ============================================================

set -e

# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Configuracion FTP
FTP_HOST="ftpupload.net"
FTP_USER="if0_41183902"
FTP_PASS="3Sb5cbsNnJH7yh"
FTP_DIR="/htdocs"

# Directorios
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo -e "${BLUE}============================================================${NC}"
echo -e "${BLUE}    DEPLOY - Profesor Sergio JSW${NC}"
echo -e "${BLUE}============================================================${NC}"
echo ""

# Verificar que existe lftp
if ! command -v lftp &> /dev/null; then
    echo -e "${RED}Error: lftp no esta instalado${NC}"
    echo "Instalar con: brew install lftp"
    exit 1
fi

# Listar archivos a subir
echo -e "${YELLOW}Archivos a subir (modificados en ultimos 7 dias):${NC}"
find "$PROJECT_DIR/recursos" -name "*.html" -mtime -7 -type f 2>/dev/null | while read f; do
    echo "  - ${f#$PROJECT_DIR/}"
done
echo ""

# Confirmacion final
read -p "¿Confirmar deploy? (s/N): " confirm
if [[ ! "$confirm" =~ ^[Ss]$ ]]; then
    echo -e "${YELLOW}Deploy cancelado${NC}"
    exit 0
fi

echo ""
echo -e "${GREEN}Subiendo archivos...${NC}"

# Crear script lftp para subir
lftp -c "
set ftp:ssl-allow no
set net:timeout 30
set net:max-retries 3
open -u $FTP_USER,$FTP_PASS $FTP_HOST
lcd $PROJECT_DIR
cd $FTP_DIR

# Subir recursos modificados
mirror --reverse --only-newer --verbose recursos/matematica-1medio recursos/matematica-1medio
mirror --reverse --only-newer --verbose recursos/matematica-2medio recursos/matematica-2medio
mirror --reverse --only-newer --verbose recursos/matematica-7basico recursos/matematica-7basico

bye
"

echo ""
echo -e "${GREEN}============================================================${NC}"
echo -e "${GREEN}    DEPLOY COMPLETADO${NC}"
echo -e "${GREEN}============================================================${NC}"
echo ""
echo -e "Sitio: ${BLUE}https://profesergiojsw.rf.gd${NC}"
echo ""

# Registrar deploy
DEPLOY_LOG="$PROJECT_DIR/scripts/deploy-history.log"
echo "$(date '+%Y-%m-%d %H:%M:%S') - Deploy completado" >> "$DEPLOY_LOG"

#!/bin/bash
# ============================================================
# PRE-DEPLOY VERIFICATION SCRIPT
# Profesor Sergio JSW - Sitio Web
# ============================================================
# Verifica diferencias entre archivos locales y produccion
# antes de realizar un deploy para evitar sobrescribir cambios
# ============================================================

set -e

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuracion FTP
FTP_HOST="ftpupload.net"
FTP_USER="if0_41183902"
FTP_PASS="3Sb5cbsNnJH7yh"
FTP_DIR="/htdocs"

# Directorios
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
TEMP_DIR="/tmp/pre-deploy-check-$(date +%Y%m%d_%H%M%S)"
BACKUP_DIR="$PROJECT_DIR/backups/production-$(date +%Y%m%d_%H%M%S)"

echo -e "${BLUE}============================================================${NC}"
echo -e "${BLUE}    PRE-DEPLOY VERIFICATION - Profesor Sergio JSW${NC}"
echo -e "${BLUE}============================================================${NC}"
echo ""

# Crear directorios temporales
mkdir -p "$TEMP_DIR"
mkdir -p "$BACKUP_DIR"

echo -e "${YELLOW}[1/5] Descargando archivos de produccion...${NC}"

# Descargar archivos de produccion via FTP
cd "$TEMP_DIR"

# Crear script FTP para descargar estructura
cat > ftp_download.txt << EOF
open $FTP_HOST
user $FTP_USER $FTP_PASS
cd $FTP_DIR
lcd $TEMP_DIR
prompt off
mget *.html
mget *.css
mget *.js
cd recursos
lcd recursos
mkdir recursos 2>/dev/null
prompt off
mget -r *
bye
EOF

# Intentar descarga con lftp (mas robusto)
if command -v lftp &> /dev/null; then
    echo -e "${GREEN}Usando lftp para descarga...${NC}"
    lftp -c "
    set ftp:ssl-allow no
    open -u $FTP_USER,$FTP_PASS $FTP_HOST
    lcd $TEMP_DIR
    cd $FTP_DIR
    mirror --only-newer --verbose recursos
    mirror --only-newer --verbose cursos
    get index.html
    bye
    " 2>/dev/null || echo -e "${YELLOW}Advertencia: Descarga parcial${NC}"
else
    echo -e "${YELLOW}lftp no disponible, usando curl...${NC}"
    # Descargar archivos principales con curl
    curl -s -u "$FTP_USER:$FTP_PASS" "ftp://$FTP_HOST$FTP_DIR/index.html" -o index.html 2>/dev/null || true
fi

echo -e "${GREEN}[2/5] Comparando archivos...${NC}"
echo ""

# Funcion para comparar directorios
compare_dirs() {
    local local_dir="$1"
    local remote_dir="$2"
    local prefix="$3"

    local changes=0

    # Buscar archivos HTML en el directorio local
    if [ -d "$local_dir" ]; then
        find "$local_dir" -name "*.html" -type f 2>/dev/null | while read local_file; do
            rel_path="${local_file#$PROJECT_DIR/}"
            remote_file="$TEMP_DIR/$rel_path"

            if [ -f "$remote_file" ]; then
                # Comparar archivos
                if ! diff -q "$local_file" "$remote_file" > /dev/null 2>&1; then
                    echo -e "${YELLOW}MODIFICADO:${NC} $rel_path"
                    changes=$((changes + 1))
                fi
            else
                echo -e "${GREEN}NUEVO:${NC} $rel_path"
                changes=$((changes + 1))
            fi
        done
    fi

    return $changes
}

# Comparar recursos
echo -e "${BLUE}--- Recursos Matematica 1 Medio ---${NC}"
compare_dirs "$PROJECT_DIR/recursos/matematica-1medio" "$TEMP_DIR/recursos/matematica-1medio" ""

echo ""
echo -e "${BLUE}--- Recursos Matematica 2 Medio ---${NC}"
compare_dirs "$PROJECT_DIR/recursos/matematica-2medio" "$TEMP_DIR/recursos/matematica-2medio" ""

echo ""
echo -e "${BLUE}--- Recursos Matematica 7 Basico ---${NC}"
compare_dirs "$PROJECT_DIR/recursos/matematica-7basico" "$TEMP_DIR/recursos/matematica-7basico" ""

echo ""
echo -e "${GREEN}[3/5] Generando reporte de cambios...${NC}"

# Crear reporte
REPORT_FILE="$PROJECT_DIR/scripts/deploy-report-$(date +%Y%m%d_%H%M%S).txt"

cat > "$REPORT_FILE" << EOF
============================================================
REPORTE PRE-DEPLOY - $(date)
============================================================

Archivos locales modificados que se subirán:
------------------------------------------------------------
EOF

# Listar archivos modificados recientemente (ultimos 7 dias)
find "$PROJECT_DIR/recursos" -name "*.html" -mtime -7 -type f 2>/dev/null | while read f; do
    echo "  - ${f#$PROJECT_DIR/}" >> "$REPORT_FILE"
done

echo "" >> "$REPORT_FILE"
echo "============================================================" >> "$REPORT_FILE"

echo -e "${GREEN}Reporte guardado en: $REPORT_FILE${NC}"

echo ""
echo -e "${GREEN}[4/5] Creando backup de produccion...${NC}"

# Mover archivos descargados al backup
if [ -d "$TEMP_DIR" ] && [ "$(ls -A $TEMP_DIR 2>/dev/null)" ]; then
    mv "$TEMP_DIR"/* "$BACKUP_DIR/" 2>/dev/null || true
    echo -e "${GREEN}Backup guardado en: $BACKUP_DIR${NC}"
else
    echo -e "${YELLOW}No se pudieron descargar archivos para backup${NC}"
fi

echo ""
echo -e "${GREEN}[5/5] Resumen${NC}"
echo -e "${BLUE}============================================================${NC}"

# Contar archivos modificados localmente en los ultimos 7 dias
MODIFIED_COUNT=$(find "$PROJECT_DIR/recursos" -name "*.html" -mtime -7 -type f 2>/dev/null | wc -l | tr -d ' ')

echo -e "Archivos HTML modificados (ultimos 7 dias): ${YELLOW}$MODIFIED_COUNT${NC}"
echo ""

if [ "$MODIFIED_COUNT" -gt 0 ]; then
    echo -e "${YELLOW}Archivos que se subirían:${NC}"
    find "$PROJECT_DIR/recursos" -name "*.html" -mtime -7 -type f 2>/dev/null | while read f; do
        echo "  - ${f#$PROJECT_DIR/}"
    done
    echo ""
fi

# Limpiar temporal
rm -rf "$TEMP_DIR" 2>/dev/null || true

echo -e "${BLUE}============================================================${NC}"
echo -e "${GREEN}Verificacion completada.${NC}"
echo ""
echo -e "Opciones:"
echo -e "  ${GREEN}1)${NC} Continuar con deploy: ./deploy.sh"
echo -e "  ${YELLOW}2)${NC} Revisar diferencias: diff -r recursos/ backups/production-*/recursos/"
echo -e "  ${RED}3)${NC} Cancelar deploy"
echo ""

# Preguntar si continuar
read -p "¿Deseas continuar con el deploy? (s/N): " response
if [[ "$response" =~ ^[Ss]$ ]]; then
    echo -e "${GREEN}Ejecutando deploy...${NC}"
    if [ -f "$SCRIPT_DIR/deploy.sh" ]; then
        "$SCRIPT_DIR/deploy.sh"
    else
        echo -e "${YELLOW}Script deploy.sh no encontrado. Crealo primero.${NC}"
    fi
else
    echo -e "${YELLOW}Deploy cancelado.${NC}"
fi

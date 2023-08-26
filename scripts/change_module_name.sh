#!/usr/bin/env bash
# Verificar que se proporcionaron los argumentos correctos
if [ "$#" -ne 1 ]; then
    echo "Uso: $0 TEXTO_NUEVO"
    exit 1
fi

# Argumentos del script
SCRIPT_DIR="$(dirname "$0")"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"
TEXTO_ORIGINAL="python_boilerplate"
TEXTO_NUEVO=$1

# Reemplazar el texto en todos los archivos de texto en el directorio
find "$PARENT_DIR/" -type f \( -name "*.py" -o -name "*.toml" \) -exec sed -i "s/$TEXTO_ORIGINAL/$TEXTO_NUEVO/g" {} +
# find "$PARENT_DIR/python_boilerplate" -type f \( -name "*.py" -o -name "*.toml" \) -exec sed -i "s/$TEXTO_ORIGINAL/$TEXTO_NUEVO/g" {} +
# find "$PARENT_DIR/tests" -type f \( -name "*.py" \) -exec sed -i "s/$TEXTO_ORIGINAL/$TEXTO_NUEVO/g" {} +
find "$PARENT_DIR/scripts" -type f \( -name "*.sh" \) -exec sed -i "s/$TEXTO_ORIGINAL/$TEXTO_NUEVO/g" {} +
mv $PARENT_DIR/python_boilerplate $PARENT_DIR/$TEXTO_NUEVO
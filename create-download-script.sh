#!/bin/bash

DOWNLOAD_DIR=download
OUTPUT=download.sh

cat > "$OUTPUT" <<EOF
#!/bin/bash

set -e

mkdir -p download

EOF

for ano in 2011 2012 2013 2014 2015 2016 2017; do
	for mes in 01 02 03 04 05 06 07 08 09 10 11 12; do
		echo "wget -O $DOWNLOAD_DIR/gastos-diretos-$ano-$mes.zip --continue --tries=3 --timeout=5 'http://arquivos.portaldatransparencia.gov.br/downloads.asp?a=$ano&m=$mes&consulta=GastosDiretos'" >> $OUTPUT
		echo "wget -O $DOWNLOAD_DIR/transferencias-$ano-$mes.zip --continue --tries=3 --timeout=5 'http://arquivos.portaldatransparencia.gov.br/downloads.asp?a=$ano&m=$mes&consulta=Transferencias'" >> $OUTPUT
	done
done

chmod +x "$OUTPUT"

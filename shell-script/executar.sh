#!/bin/bash

source ./funcoes.sh

lista_arquivos $1
text=$2

for i in "${LIST_ARQ[@]}"
do 
    insere_texto "$i" "$text"
done

echo "Script executada com sucesso"

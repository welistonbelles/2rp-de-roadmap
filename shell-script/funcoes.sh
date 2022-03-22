#!/bin/bash

# Desenvolver uma function chamada lista_arquivos que retorne 
# todos os arquivos dentro de um diretório (inclusive nos sub-diretórios deste diretório) 
# e armazene ocaminho completo até estes arquivos em um vetor;
lista_arquivos(){
    LIST_ARQ=$(find $1 -type f) # Salvo em 1 variavel todos os arquivos presentes no diretorio informado assim como os arquivos presentes em seus subdiretorios caso possua
    LIST_ARQ=(${LIST_ARQ// / }) # Realizo a separação dos diretorios e transformo em 1 vetor
}

# Desenvolver uma função chamada insere_texto()
# que, dado o caminho completo para um arquivo, 
# escreva um texto qualquer no final deste arquivo (o texto também deve ser um p)

insere_texto(){
    file_path=$1
    text=$2
    echo "$text" >> $file_path
}
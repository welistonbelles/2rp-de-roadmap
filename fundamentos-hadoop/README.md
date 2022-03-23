<p align="center">
    <a href="#definicao">Definicao</a>
    <a href="#hdfs">HDFS</a>
    <a href="#mapreduce">MapReduce</a>
    <a href="#hue">HUE</a>
    <a href="#yarn">Yarn</a>
</p>

# Definicao
<p>O hadoop foi criado para realizar o processamento de grandes volumes de dados. Consiste em 1 ecossistema composto por diversas ferramentas que são responsáveis por diferentes tarefas.</p>

<p>2 de seus principais serviços:</p>
<li>Sistema distribuído de arquivos: HDFS</li>
<li>Mecanismo de processamento de dados em paralelo: Map Reduce</li><br>

# HDFS
<p>O sistema HDFS (Hadoop Distributed File System) distruibui os dados em blocos com um fator  de replicação de 3 (que pode ser configurado). É por conta disso que ele consegue se tornar tolerante a falhas.
Deve ser utilizado preferencialmente com grandes volumes de dados, visto que o seu processamento acaba levando algum tempo. Portanto não deve ser utilizado em aplicações que necessitam de um resultado imediato.
</p>
<li>NameNode: É responsável por armazenar as informações da distribuição de arquivos e metadados.</li>
<li>WorkerNode: É responsável por armazenar os dados em si.</li>
<br>

# MapReduce
<p>O Map Reduce é um processo executado pelo Hadoop que consegue transformar um grande volume de dados em um volume signitivamente menor.<br>Esse processo é dividido em 3 etapas:</p>

<li>1º Etapa: Map</li>
<li>2º Etapa: Sort</li>
<li>3º Etapa: Reduce</li><br>

# Hue
<p>O Hue também faz parte do ecossistema hadoop e é licenciado sob a apache, consiste em um SQL Cloud Editor de Código aberto. É uma ferramenta muito poderosa que fornece consultas interativas que permitem interação com Data Warehouses.</p>

# Yarn
<p>O Yarn consiste em um gerenciador de pacotes que possibilita aplicar comandos previamente prontos ao código de uma aplicação. É o sucessor do NPM e é considerado mais eficaz e seguro do que ele.</p>
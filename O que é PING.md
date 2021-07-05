# O que é ICMP PING

 

**Protocolo ICMP** (Internet Control Message Protocol) é um protocolo integrante do protocolo IP utilizado para fornecer relatórios de erro à fonte original

**PING** é uma ferramenta que usa o protocolo ICMP para testar conectividade. Consiste no envio de pacotes para o equipamento de destino e na "escuta" das resposta, geralmente em unidades de milissegundo (ms). PING é aplicado no princípio da Disponibilidade que visa garantir que a informação esteja disponível quando requisitada.

Temos um desenho:![image-20210704212153433](C:\Users\vinic\AppData\Roaming\Typora\typora-user-images\image-20210704212153433.png)

Aqui a ferramenta PING, nós estamos fazendo uma requisição (echo request), mandando mensagens para ver se o server está disponível ou não, na expectativa de que virá uma resposta do servidor (echo reply). No cmd, é possível fazer um "ping _nome do site_" para verificar a latência e o tempo de echo reply para o seu endereço de IP

biblioteca OS (operacional sytem), que veio do Python, uma maneira simples de usar funcionalidade que são dependentes de sistema operacional, como o PING.

Criado o PINg simples em um Projeto do Python, agora iremos criar um PING múltiplo. Além da biblioteca os, temos a time para verificar o tempo de execução por exemplo.


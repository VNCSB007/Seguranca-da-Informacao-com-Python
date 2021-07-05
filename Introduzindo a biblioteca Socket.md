# Biblioteca Socket

fornece acesso de baixo nível à interface de rede (faz parte do Python, mas não somente deles mas de várias linguagens de programação) que permite abertura, fechamento e sincronizações direto com as IPs com chaves de rede. Acesso de baixo nível permite trabalhar com descritores de segurança (ACLs) e entradas de controle de acesso (ACEs)

O Sistema Operacional (S.O.) fornece a Aplication Programming Interface (API) socket que relaciona o programa com a rede.

Iremos desenvolver um cliente **TCP**. O que é? Transmission Control Protocol ,protocolo de comunicação que suporta a rede global conhecida como internet, verificando se os dados são enviados na sequência correta e sem erros (e também se são enviados de forma íntegra), que verifica o princípio da **Integridade**. 

Também criaremos um cliente **UDP** (User Datagram Protocol), está também na camada de transporte, protocolo simples que permite s=que sua aplicação envie um datagrama dentro do pacote ip4 ou ip6 mas sem garantir que o pacote chegará sem perdas, descontando o principio da integridade mas o de **disponibilidade**. 
# Biblioteca Random, Hash e Multithreading

A **biblioteca Random** permite que possa ser trabalhado  números e letras aleatórias para qualquer fim que desejarmos. Ela será utilizada para gerar senhas para randomizar letras e  números e a cada execução, será gerado outra senha. (princípio da autenticação e da confidencialidade)

**Hash** é um identificador único, gerado por análise de byte a byte. Cada byte é o suficiente para mudar a estrutura do Hash, ou  seja, se uma vírgula for alterada então o Hash será outro (temos hash md5, sha1, sha512; verifique o site https://md5decrypt.net/en/; sha1 tem o identificador maior que md5). Hoje as senhas são armazenadas no sistema não por ASCII, mas por Hash, agora qual Hash é a questão...

A **biblioteca Hashlib** implementa uma interface comum para muitos algoritmos de hash seguro como Sha1

**Multithreading**... threading é considero um processo, e no mutithread cada processo pode responder a várias solicitações concorrentemente ou mesmo simultaneamente (tipo abrir várias abas no Chrome, isso cria várias solicitações de processo que vão concorrendo entre si que impacta o processamento da máquina). Essa biblioteca constrói interface de alto nível para processamento com o módulo Thread e de baixo nível (ligação direta com os registradores)

A **Biblioteca ipadress** capaz de manipular e criar endereços IP do tipo IPv4, IPv6 e até redes inteiras 

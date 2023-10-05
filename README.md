# Sistema  reUse
Sistema produzido na linguagem python para cumprir com as necessidades do projeto reUse que foi criado para o IBM Challenge 2023 da FIAP.

## O que é reUse?

Reconhecendo a necessidade crítica de abordar o problema da reciclagem de forma inovadora, a reUse projetou um sistema de pontuação e premiação que está revolucionando a maneira como as pessoas percebem e se envolvem com a reciclagem.

A reUse, com sua expertise em tecnologia e sustentabilidade, identificou que uma das principais barreiras para a reciclagem era a falta de incentivos palpáveis para os indivíduos. O sistema tradicional de reciclagem frequentemente carece de recompensas imediatas, o que leva muitos a descartar resíduos de forma inadequada, contribuindo para o problema ambiental. Para superar esse desafio, a reUse projetou uma solução inovadora que transformou a reciclagem em um esforço gratificante e envolvente.

O sistema de pontuação e premiação da reUse é baseado em tecnologia de última geração. Cada participante recebe um identificador pessoal, geralmente um aplicativo para smartphones, que rastreia seus esforços de reciclagem. Quando os indivíduos depositam corretamente seus materiais recicláveis ​​nos locais designados, eles acumulam pontos com base na quantidade e tipo de material reciclado. Esses pontos não apenas funcionam como um incentivo intrínseco, mas também podem ser trocados por uma variedade de recompensas tangíveis, como descontos em produtos, serviços locais e até mesmo doações para causas ambientais.

O sistema de pontuação e premiação tem uma série de características notáveis que contribuem para seu sucesso. A transparência é uma delas: os participantes podem acompanhar sua pontuação em tempo real por meio do aplicativo,ou pelo site, o que cria um senso de realização e progresso. Além disso, a reUse estabeleceu parcerias com empresas, permitindo que os pontos sejam trocados por ofertas exclusivas ou contribuições significativas para projetos ambientais.

A abordagem da reUse cita várias lacunas na conscientização sobre a reciclagem. Primeiro, ela conecta diretamente as ações individuais com recompensas concretas, motivando as pessoas a se tornarem defensoras ativas da sustentabilidade. Em segundo lugar, o sistema cria um senso de comunidade, já que as pessoas podem compartilhar suas conquistas e colaborar para alcançar metas coletivas. Por fim, a reUse não apenas oferece incentivos pessoais, mas também estabelece um impacto positivo mais amplo, incentivando as pessoas a contribuir para o bem-estar ambiental e social.


**Diferente do repositório orginal do trabalho, sendo [este para os testes](https://github.com/victoriafpizza/sprintpython2) (na branch "teste_sprint_3") e [este para a atividade](https://github.com/emnuelle/ibm-challenge-sprint3-ctwp), esse repositório foi feito com a intenção de aprimorar cada vez mais o sistemada iniciativa com novas funcionalidades.** 


## Como funciona o sistema? 

 O programa simula o sistema reUse, com as principais funcionalidades sendo:

    > Definido como menu primário:

        > Login: para usuários já cadastrados.
        > Cadastro: de novos clientes como usuários.
        > Sair: fechar o programa.

    > Acesso ao menu de usuário por um PIN único de 5 números gerados aleatóriamente por sorteio. Sendo suas
    funcionalidades:

        > Reciclar: o usuário tem a possibilidade de escolher qual material vai descartar, depois é feito um sorteio
        via módulo random para simular a pesagem do material depositado na lixeira. Assim que a operação é confirmada
        a quantidade de pontos é contabilizada para o usuário, também é contabilizado os KGs reciclados por material.
        > Extrato de pontos: a apção permite que o usuário consiga visualizar a quantidade de pontos acumulados até o
        momento.
        > Cotação Atual de materiais: exibe a cotação de pontos por KG de cada material.
        > Ver informações do usuário: Exibe todas as informações do usuáro guardadas no sistema.
        > Sair: sai do login e volta para o menu inicial.

    > Acesso ao menu do Administrador pelo PIN fixo "66666", com as seguintes opções:

        > Cotação de Pontos Atual: exibe a cotação de pontos por KG de cada material.
        > Mudar Cotação de Pontos: permite que o administrador escolha o material desejado e mude a cotação de pontos.
        A funcionalidade também exibe a cotação atual do material selecionado para facilitar a operação.
        > Lista de Usuários: exibe a lista com todos os usuários cadastrados até o momento.
        > Alterar Informações de Usuário: permite com que o administrador mude as informções de usuários cadastrados.
        > Excluir Usuário: permite que o administrador exclua os usuários. (no caso o que escolher)
        > Adicionar Usuário: permite com que o administrador faça um cadastro.
        > Sair: sai do login e volta para o menu inicial.
# Pesquisa aplicada: como melhorar os vídeos de IA do Turrico

Pesquisa consultada em 18 de outubro de 2026. Base: documentação dos fornecedores, guias oficiais de produção, metodologia de avaliação e os materiais do Dan Kieft fornecidos nesta conversa.

## Escopo e grau de certeza

Este é um estudo documental com recomendações de produção. Não foram realizadas gerações pagas, testes comparativos próprios, assinaturas ou avaliações audiovisuais de todos os exemplos publicados. Recursos descritos pelos fornecedores são capacidades anunciadas, não garantias de resultado. Preços, acesso por país, versões e limites devem ser conferidos na interface antes de produzir.

Os procedimentos, notas de avaliação, exemplos de roteiro e critérios de compra abaixo são uma proposta para nosso trabalho. Ainda precisam ser validados com o personagem aprovado. Não representam resultados medidos.

## 1. A decisão que vem antes do prompt

Escolher a forma de produzir a cena:

| Necessidade | Caminho inicial | Por quê |
|---|---|---|
| Explorar uma ideia sem aparência definida | Texto para vídeo | Permite descobrir soluções visuais |
| Preservar o desenho aprovado do Turrico | Imagem para vídeo ou referências de personagem | A aparência tem uma âncora visual |
| Repetir personagem em ambientes diferentes | Referências reutilizáveis + imagens por plano | Separa identidade, cenário e composição |
| Fazer uma interpretação específica | Atuação gravada + transferência de performance | O ritmo e os gestos vêm de uma atuação concreta |
| Reproduzir um movimento preciso | Vídeo de referência de movimento/câmera | Evita depender apenas da descrição verbal |
| Garantir a frase exata em português | Áudio aprovado + ferramenta de avatar/lip sync compatível | Permite resolver a fala antes da renderização |
| Corrigir detalhe num clipe bom | Edição localizada, composição ou corte | Pode preservar o que já funcionou |

Essas são hipóteses de escolha. O teste da cena decide entre as alternativas.

## 2. Como escolher plataformas

Plataforma é o ambiente de trabalho; modelo é o gerador; modo é o tipo de tarefa. Acesso a Seedance numa plataforma não implica que todas as ferramentas, versões ou entradas de outra plataforma estejam presentes.

| Opção | Papel sugerido na nossa seleção | Recurso documentado | O que verificar |
|---|---|---|---|
| Higgsfield / Seedance | Testar cenas do Turrico com múltiplas referências e som | Referências multimodais, Elements, geração e edição separadas [1][2] | Versão, plano, custo, sintaxe das referências e modo selecionado |
| Flow / Veo | Testar cenas com áudio e direção por imagens | Ingredients, frames e construção de cenas [3][4] | Compatibilidade do modelo com cada recurso |
| Runway | Animar imagens aprovadas e explorar atuação | Guias específicos de imagem para vídeo e Act-Two [5][6] | Gerador visual e ferramenta de performance são tarefas diferentes |
| Kling | Testar movimentos guiados por gravação | Motion Control com referência de ação e personagem [7] | Enquadramento, orientação e condições do modo |
| Luma / Modify | Transformar uma gravação em outra aparência | Vídeo de entrada, referência de personagem e keyframes [8] | Quanto da atuação e da cena precisa permanecer |
| Firefly | Transferir movimento de câmera para uma cena nova | Referência de movimento no Firefly Video [9] | O controle pode depender do modelo selecionado |
| HeyGen | Testar falas recorrentes de apresentador/personagem | Ferramentas de avatar e controle de voz [10][11] | Compatibilidade com personagem estilizado e expressividade desejada |
| LTX | Exploração com maior controle técnico, se houver necessidade | Guias de prompting e fluxos locais [12][13] | Hardware, tempo de preparação e custo de operação |

Não há vencedor universal estabelecido por esta pesquisa. Para Turrico, começar comparando duas rotas: imagem aprovada animada e fala guiada por áudio/atuação. Acrescentar outras plataformas quando houver uma dificuldade concreta que justifique isso.

## 3. Referências: organizar antes de gerar

Criar uma ficha do personagem com:

- Imagem principal aprovada e imagens auxiliares coerentes.
- Proporções, formato do rosto, olhos, silhueta, materiais e cores que não podem mudar.
- Figurino recorrente e acessórios essenciais.
- Expressões aprovadas: neutra, ironia contida, impaciência e reação final.
- Exemplo de voz em português brasileiro, cadência, pronúncia do nome e intensidade.
- Um conjunto pequeno de cenários e estilos de luz.

Separar a função de cada arquivo: identidade, figurino, ambiente, composição, estilo, movimento ou voz. Um painel com várias vistas pode ser útil como referência; não deve ser usado automaticamente como primeiro frame da cena. Para animar um plano, preferir uma imagem única já composta para aquele plano.

Antes de animar, revisar mãos, boca, olhos, apoios e contatos entre objetos. O Runway alerta que defeitos da imagem de entrada podem se intensificar no vídeo [5]. A Luma também documenta o uso de referências principais e atributos fixos para consistência [14].

Para o Turrico, preservar o desenho/cartum contemporâneo definido no brief. Realismo de movimento, luz e peso pode enriquecer esse desenho sem transformá-lo num humano fotorrealista.

## 4. Prompts por tarefa e por modelo

### Texto para vídeo

Descrever o que a imagem ainda não fornece: sujeito, ação, espaço, enquadramento, câmera, luz, estética e áudio. CTLT é útil como lista de verificação visual; o vídeo também exige progressão no tempo e som.

### Imagem para vídeo

Começar por ação, direção, velocidade, reação do ambiente e movimento da câmera. Não repetir uma descrição longa da aparência que já está na imagem. Essa orientação aparece tanto no Runway quanto nas boas práticas do Google [5][15].

### Referências multimodais

Explicar o que cada entrada fornece. Distinguir usar uma voz como identidade de reproduzir exatamente um áudio; distinguir copiar um movimento de copiar o cenário do vídeo de referência. As etiquetas abaixo são explicativas e precisam ser substituídas pelos identificadores reais aceitos na interface.

### Evitar uma fórmula universal

- Gen-4: o guia recomenda simplicidade e linguagem afirmativa; instruções negativas não são suportadas como estratégia de controle [16].
- Seedance 2.5: a biblioteca da Higgsfield organiza cenas complexas em seções como estilo, personagens, posição inicial, planos, física, luz e som [2].
- LTX: o guia pede adaptação ao formato do modelo, em vez de colar intactos prompts de outros geradores [12].

Consequência prática: manter um briefing completo e produzir uma versão do prompt apropriada a cada modelo. JSON, letras maiúsculas, nomes de lentes e listas longas não têm superioridade universal demonstrada aqui. Resolução, duração e proporção devem ser configuradas nos controles disponíveis; escrevê-las no texto não substitui uma configuração.

## 5. Direção de ação e câmera

Para os primeiros testes, usar uma ação principal, uma reação e um movimento de câmera no máximo. Isso é uma restrição experimental nossa para facilitar diagnóstico, não um limite absoluto dos modelos.

Descrever emoções por sinais observáveis: uma sobrancelha sobe, o olhar se desloca para a lente, o sorriso quase aparece e é contido. Em comédia, uma pausa de reação pode carregar o humor sem movimentos amplos.

| Intenção | Descrição operacional |
|---|---|
| Zoom | A distância focal muda; a câmera permanece no lugar |
| Aproximação física | A câmera avança em direção ao sujeito; a perspectiva muda |
| Pan | A câmera gira horizontalmente a partir da mesma posição |
| Travelling lateral | A câmera se desloca para o lado em relação ao sujeito |
| Handheld | Pequenas irregularidades de alguém sustentando a câmera |
| Whip pan | Giro rápido motivado por um acontecimento, seguido de reenquadramento |

Evitar comandos incompatíveis como câmera fixa e órbita simultânea. Quando o movimento for decisivo, testar referência gravada: Firefly documenta extração de movimento de câmera [9]; Kling documenta transferência guiada por referência de ação [7].

## 6. Continuidade: o que o último frame resolve

A técnica estudada com Dan é válida e também consta do guia do Runway [5]. Compartilhar o frame aproxima a posição visual das duas partes, mas não fornece sozinho trajetória, velocidade, voz e intenção da atuação.

Procedimento proposto:

1. Escolher um ponto de emenda com pose legível e pouca oclusão.
2. Extrair o frame original, evitando uma captura com botões do player.
3. Levar também a referência principal do personagem quando o modo permitir.
4. Descrever como a ação continua e o que permanece estável.
5. Comparar o novo trecho com o primeiro, evitando acumular deformações de uma cadeia longa.
6. Aparar frames duplicados e ajustar som e cor na montagem.

Para uma emenda manual, terminar parado pode ajudar. Para ação contínua, interromper artificialmente todo movimento pode criar uma pausa perceptível. Escolher entre frame final, extensão com contexto de vídeo ou corte intencional conforme o objetivo. Flow oferece diferentes entradas, mas a disponibilidade depende do modelo [3].

Não precisamos fazer todos os vídeos como uma tomada única. Plano principal, reação e detalhe podem esconder limites da geração e melhorar o ritmo quando planejados como linguagem de montagem.

## 7. Áudio e humor em português

Para Turrico, testar a interpretação antes de gerar a imagem em movimento. A voz precisa soar seca, observadora e carismática; gritar ou gesticular demais pode enfraquecer a personalidade definida no brief.

Rotas a comparar:

- Áudio nativo: útil para interação e sons sincronizados, verificando a frase inteira.
- Áudio previamente aprovado: útil quando palavra, sotaque e pausa precisam de controle.
- Atuação gravada: útil para transferir microexpressões e timing.

O Act-Two documenta transferência a partir de uma performance e recomenda entrada com um sujeito e rosto visível [6]. O HeyGen permite usar entrega vocal gravada pelo Voice Mirroring [11]. Sua FAQ mostra que o comportamento de prompting muda entre motores de avatar [10].

Diretrizes nossas: escrever para falar, usar frases curtas, testar a pronúncia de Turrico, medir a duração real do áudio e reservar espaço para a reação. Dicionários e controles de pronúncia variam conforme o modelo; a documentação do ElevenLabs recomenda testar termos importantes na voz escolhida [17].

Na edição, controlar separadamente diálogo, ambiente, efeitos e música sempre que houver arquivos separados. Evitar uma trilha que encubra a frase final.

## 8. Realismo que interessa ao projeto

Não transformar toda cena em filmadora defeituosa. Para Turrico, testar primeiro rosto legível, gesto contido, contato físico convincente, luz coerente e fundo simples. Granulação, desfoque, compressão, exposição automática e tremor só entram quando combinam com a câmera fictícia e ajudam a cena.

Texto, legendas e marca essenciais devem ser aplicados e revisados na edição. O guia LTX reconhece que escrita exata e persistente ainda não é garantida [12]. A identidade gráfica deve permanecer legível, mesmo quando o vídeo tiver estética de registro espontâneo.

Upscale não deve ser usado para aprovar um clipe com erro de identidade ou ação. Se um rascunho precisar de nova geração em resolução maior, tratar o novo resultado como outra tomada e revisá-lo. Nem todo modo de rascunho preserva exatamente a mesma sequência ao finalizar.

## 9. Método para melhorar continuamente

### Separar dois testes

Teste de transferência: mesma referência, mesmo objetivo e instrução básica em dois modelos. Mede quão facilmente o briefing funciona em ambos.

Teste de produção: adaptar o prompt às recomendações de cada modelo, mantendo o mesmo objetivo e limite de gasto. Mede qual fluxo entrega mais material utilizável no nosso caso.

Não concluir que um modelo é melhor porque um único prompt, escrito para seu concorrente, falhou. Tampouco concluir pela melhor tomada isolada.

### Pequena bateria inicial proposta

Três cenas representativas: fala curta com ironia; reação silenciosa com microexpressão; interação simples com objeto cotidiano. Usar a imagem aprovada do personagem. Fazer duas ou três tentativas por cena e por rota, se o orçamento permitir. Isso serve como triagem; não dá significância estatística nem ranking universal.

Alterar uma variável por vez: prompt, referência, intensidade do gesto ou câmera. Quando houver seed, registrá-la; a mesma seed não torna modelos diferentes equivalentes e pode não garantir reprodução exata após atualizações.

### Ficha de avaliação proposta

Dar notas de 0 a 5. Pesos são uma preferência inicial para Turrico.

| Critério | Peso |
|---|---:|
| Identidade e proporções do personagem | 25% |
| Interpretação, pausa e timing cômico | 25% |
| Fala correta, voz e sincronização labial | 20% |
| Movimento, contatos e física | 15% |
| Luz, câmera e acabamento | 10% |
| Facilidade de encaixar na edição | 5% |

Em cena sem fala, redistribuir o peso de áudio antes do teste. Aplicar critérios de reprovação independente da média: personagem irreconhecível, frase errada ou distorção na ação central. Rever em velocidade normal; usar pausa e câmera lenta para diagnosticar defeitos, sem esquecer a experiência de quem assiste.

Essa separação entre aparência, movimento e consistência dialoga com o VBench, que avalia múltiplas dimensões de qualidade [18]. Rankings de preferência ajudam a selecionar candidatos, mas não substituem o teste do personagem. A Artificial Analysis separa tarefas com e sem áudio, além de geração e edição [19].

### Medir o custo útil

Custo por segundo aprovado = gasto total da bateria / segundos que realmente entraram em vídeos aprovados.

Exemplo hipotético: R$ 60 para obter 20 segundos úteis = R$ 3 por segundo aprovado. Acrescentar tempo de correção e edição ao comparar fluxos. Créditos descartados também contam. A plataforma com o clipe nominalmente mais barato pode perder nessa conta.

Salvar modelo, versão, data, modo, referências, prompt exato, configurações, resultado, falha e correção. Após publicar, comparar retenção e reação à piada separadamente da qualidade técnica; um vídeo visualmente perfeito ainda pode ter roteiro fraco.

## 10. Produção e finalização

Sequência proposta:

1. Ideia: observação cotidiana + contradição reconhecível + virada.
2. Roteiro: uma intenção principal e uma frase final clara.
3. Voz: aprovar sotaque, cadência e pausa quando a rota permitir.
4. Planos: definir o que cada trecho precisa comunicar.
5. Referências: aprovar personagem e imagem inicial.
6. Geração: testar o plano mais difícil primeiro.
7. Seleção: avaliar a ação inteira, não apenas a miniatura.
8. Correção: decidir entre edição localizada, nova tomada ou mudança de plano.
9. Montagem: aparar, combinar cor, ajustar áudio e inserir títulos.
10. Exportação: revisar o arquivo final no tamanho de celular.

O Resolve documenta ferramentas de correspondência de cor entre planos [20]. Elas ajudam no acabamento, mas a revisão visual continua necessária.

## 11. Custos e correções dos materiais anteriores

A página de créditos do Flow consultada informa 50 créditos diários, com condições de acesso, e lista Gemini Omni Flash 720p de 10 segundos a 15 créditos [21]. Assim, a conta de três gerações por 45 créditos tem respaldo para essa combinação. Não significa que todo modelo faça 30 segundos gratuitamente nem que haja margem para refazer erros. A página avisa que limites podem mudar.

O guia de ajuda da Higgsfield descreve Seedance 2.5 com até 30 segundos e saída nativa até 1080p [1]. Preferir essa referência específica a alegações genéricas de 4K em material promocional. Três blocos de 10 segundos continuam sendo uma opção de montagem, não regra universal.

O guia Sora 2 da OpenAI permanece útil como orientação de planos e iteração, mas está marcado como arquivado [22]. Não o usei para afirmar disponibilidade, preço ou limites atuais do produto.

Para contratar uma plataforma, verificar o modelo exato, duração, referências aceitas, resolução nativa, exportação, uso comercial, marca d'água, filas e condições da oferta. São critérios de compra; não foi feita uma auditoria jurídica dos planos.

## 12. Decisões iniciais para Turrico

Preservar a identidade já aprovada. Usar estética de captura como recurso narrativo. Priorizar português natural, reação contida e timing. Comparar inicialmente duas rotas com a mesma piada e referência, e escolher pelo resultado aproveitável. Criar uma biblioteca dos nossos próprios acertos, acompanhada dos casos em que cada prompt falha.

O arquivo complementar PROMPTS_E_TESTES_TURRICO.md contém modelos de briefing e exemplos para experimentar. Eles ainda não foram testados em geração.

## Fontes consultadas

Todas acessadas em 18/10/2026. Guias de fabricantes confirmam instruções e recursos anunciados; não comprovam superioridade independente.

1. [Higgsfield — como usar Seedance](https://higgsfield.ai/creator-hub/help-center/ai-models/how-do-i-use-seedance)
2. [Higgsfield — biblioteca de prompting Seedance 2.5](https://higgsfield.ai/blog/seedance-2-5-prompting-guide)
3. [Google — criar vídeos no Flow](https://support.google.com/flow/answer/16353334?hl=en)
4. [Google Cloud — prompting para Veo 3.1](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1/)
5. [Runway — imagem para vídeo](https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide)
6. [Runway — performance com Act-Two](https://help.runwayml.com/hc/en-us/articles/42311337895827-Performance-Capture-with-Act-Two)
7. [Kling — Motion Control](https://kling.ai/quickstart/motion-control-user-guide)
8. [Luma — Ray3 Modify](https://lumalabs.ai/learning-hub/ray3-modify-user-guide)
9. [Adobe — referência de movimento de câmera](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/match-camera-motion-to-reference-video.html)
10. [HeyGen — FAQ de avatar e voz](https://help.heygen.com/en/articles/15544929-avatar-voice-faq-troubleshooting-best-practices-and-credits)
11. [HeyGen — Voice Mirroring](https://www.heygen.com/en-gb/academy/voice/how-to-use-voice-mirroring)
12. [LTX — prompting](https://docs.ltx.io/api-documentation/implementation-guides/prompting-guide/)
13. [LTX — fluxo imagem/texto para vídeo](https://ltx.io/blog/ltx-2-image-to-video-text-to-video-workflow)
14. [Luma — consistência de personagens e produtos](https://lumalabs.ai/learning-hub/keep-character-product-consistency-in-luma-reference-guide)
15. [Google Cloud — boas práticas](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/best-practice?hl=en)
16. [Runway — prompting Gen-4](https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide)
17. [ElevenLabs — boas práticas de fala](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices)
18. [VBench — artigo dos pesquisadores](https://arxiv.org/abs/2311.17982)
19. [Artificial Analysis — metodologia de vídeo](https://artificialanalysis.ai/methodology/video)
20. [Blackmagic Design — ferramentas de cor](https://www.blackmagicdesign.com/products/davinciresolve/color)
21. [Google — créditos do Flow](https://support.google.com/flow/answer/16526234?hl=en)
22. [OpenAI — guia Sora 2, arquivado](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide)
23. [Black Forest Labs — Playground e edição com referências](https://help.bfl.ai/articles/8667153955-what-is-the-bfl-playground)
24. [MiniMax — guia público de vídeo](https://github.com/MiniMax-AI/skills/blob/main/skills/frontend-dev/references/minimax-video-guide.md)

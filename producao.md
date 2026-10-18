# Produção: decisões e execução

## Definir a cena

Extrair objetivo, público, formato, duração, emoção, ação central, fala exata, referências disponíveis e ferramenta escolhida. No roteiro, definir situação inicial, mudança e resultado; em humor, garantir que a observação e a virada funcionem antes do efeito visual. Cronometrar leitura ou áudio; não fixar duração apenas pela contagem de palavras.

Para cada plano registrar: função narrativa, estado inicial, ação, reação, câmera, som, estado final e ponto de corte. Uma cena não precisa ser tomada única. Cortes para reação e detalhes podem melhorar ritmo e esconder limitações da geração.

## Selecionar a rota

| Necessidade | Rota candidata | Verificação decisiva |
|---|---|---|
| Explorar visual sem identidade definida | Texto para vídeo | Clareza de ação e estilo |
| Animar personagem aprovado | Imagem para vídeo | Imagem inicial limpa e coerente |
| Mesmo personagem em outros planos | Referências de identidade + imagem por plano | Entradas e funções aceitas pelo modo |
| Interpretação e timing específicos | Performance de referência | Compatibilidade de rosto, corpo e duração |
| Fala exata | Áudio aprovado + rota de sincronização | Idioma, voz e anatomia suportados |
| Movimento específico | Referência de câmera ou atuação | Qual propriedade é transferida |
| Corrigir um trecho bom | Edição localizada, composição ou corte | Preservação do material já aprovado |

Escolher candidatos pela necessidade, não por ranking universal. Compatibilidade com humano não garante compatibilidade com animal estilizado. Verificar a documentação atual do modo antes de prometer recursos.

## Referências e identidade

Separar identidade, figurino, estilo, cenário, composição, movimento e voz. Dizer qual arquivo fornece cada função. Um painel de vistas ajuda a identidade, mas não é automaticamente uma boa imagem inicial de um plano. Para animar, preparar uma imagem única com a composição desejada. Revisar olhos, boca, mãos/patas, apoios e contatos antes da geração.

Não acumular deriva usando somente o resultado anterior: comparar cada plano à referência principal. Não inventar partes do corpo ausentes de uma referência como se estivessem aprovadas; preparar uma proposta identificada como nova quando necessário.

## Escrever prompts

Manter briefing completo separado do prompt final adaptado ao modelo.

- Texto para vídeo: sujeito, espaço, ação ao longo do tempo, câmera, luz, estética e som quando suportado.
- Imagem para vídeo: priorizar o movimento e a progressão que a imagem não fornece. Evitar descrever novamente toda a aparência sem necessidade.
- Multimodal: declarar função de cada entrada usando identificadores realmente aceitos pela ferramenta.
- Transformar abstrações em sinais visíveis: olhar muda, sobrancelha sobe, mão para, sorriso é contido.
- Descrever câmera por direção, velocidade, enquadramento e chegada. Remover conflitos como câmera fixa e órbita simultânea.
- Não presumir superioridade de inglês, JSON, prompt longo ou instruções negativas. Aplicar as recomendações atuais do modelo.
- Configurar proporção, resolução, duração e seed nos controles disponíveis; o texto não substitui esses controles.

Para diagnosticar uma cena nova, começar com uma ação principal e câmera simples. É estratégia de teste, não limite absoluto. Testar o plano de maior risco antes de produzir toda a sequência.

## Voz, continuidade e montagem

Escolher áudio nativo, áudio aprovado ou performance conforme a prioridade. Conferir frase inteira, sotaque, pronúncia, pausas e boca; não assumir que adicionar voz depois sincroniza os lábios. Preservar fonte vocal e interpretação entre episódios.

Para continuar um plano, extrair um frame limpo do arquivo e especificar como o movimento prossegue. O último frame pode preservar a pose, mas não transmite sozinho velocidade, trajetória ou som. Usar contexto de vídeo/ extensão quando suportado ou planejar um corte. Conferir direção de luz, exposição, figurino, objetos e eixo. Aparar frames duplicados e ajustar som nas emendas.

Na montagem, separar diálogo, ambiente, música e efeitos quando possível. Dar tempo à reação. Inserir e revisar textos e legendas essenciais na edição. Upscale não corrige identidade ou ação errada. Assistir ao arquivo final por inteiro em velocidade normal e verificar legibilidade no tamanho de celular; usar pausa e câmera lenta para diagnóstico quando necessário.

## Diagnóstico

| Falha | Primeira intervenção candidata |
|---|---|
| Personagem muda | Rever referência principal, imagem inicial e complexidade da ação |
| Mãos/objetos deformam | Simplificar contato e oclusão; separar ação em planos |
| Atuação exagerada | Especificar gesto observável mais contido ou fornecer performance |
| Fala errada | Aprovar áudio e verificar rota de voz/sincronização |
| Câmera não obedece | Distinguir zoom, giro e deslocamento; testar referência compatível |
| Emenda salta | Comparar pose, velocidade, luz, cor, áudio e frames duplicados |
| Piada não funciona | Rever texto, compreensão visual e pausa antes de regenerar |

## Testar e registrar

Alterar uma variável por tentativa quando o objetivo for diagnóstico. Em comparação, distinguir teste de transferência (mesma instrução básica) de teste de produção (prompt otimizado por modelo). Não concluir superioridade com uma tomada isolada.

Registro mínimo: data; objetivo; modelo/versão/modo; referências; prompt exato; configurações; variável alterada; custo e tempo; arquivo resultante; falha decisiva; segundos aprovados; próxima intervenção. Identificar exemplos não executados.

Reprovar independentemente da média se identidade, fala exata ou ação central falharem. Avaliar também interpretação, movimento, física, câmera, luz e facilidade de edição. Para custos, usar gasto total dividido por segundos efetivamente aprovados, incluindo descartes; considerar tempo de correção. Dados de audiência, quando disponíveis, devem avaliar roteiro e retenção separadamente da qualidade técnica.

## Imagem cinematográfica e planejamento visual

Antes de animar, avaliar luz com origem e direção, composição que orienta o olhar, separação entre planos de profundidade e paleta que serve à intenção. Usar moodboard para formular essas decisões, mantendo a referência principal como autoridade da identidade. Terços, desfoque e granulação são opções, não obrigações.

O material fornecido de Dan Kieft detalha geração de imagens, variações de identidade, edição pontual, reutilização de prompt exposto pela interface, emoção, velocidade, múltiplos planos e overlays. Ler [a análise com timestamps e ressalvas](dan-imagens-cinematograficas.md) quando aplicar esse fluxo. Não transformar “99% do tempo”, mais de 20 imagens ou escolhas de um exemplo em requisitos universais.

Ao fazer uma alteração localizada, declarar o que muda e o que deve permanecer e revisar o resultado: o pedido de preservar não garante preservação. Na edição, overlays, luma key e blur exigem receita e inspeção próprias; não são correção automática de defeitos de geração.

## Voz: aplicar o novo estudo

Para produção de voz, consultar [ElevenLabs e direção vocal](dan-elevenlabs-voz.md). Separar identidade vocal (biblioteca/design/clonagem), interpretação (TTS ou atuação convertida), limpeza (isolador), efeitos e montagem, tradução/dublagem e sincronização labial. Uma etapa não garante o resultado da outra.

Verificar suporte de tags de pausa e comandos pelo modelo atual; instrução narrativa pode ser lida em voz alta. Não tornar os valores de Stability/Similarity da aula nem a preferência por Speaker Boost um preset universal. No Turrico, testar ironia contida, palavra exata, pronúncia e pausa; preservar uma voz aprovada entre episódios. Gravar com boa captura e comparar limpeza com a fonte para evitar perda de informação.

## Pré-produção e continuidade de filmes: novo estudo

Consultar [filmmaking avançado](dan-filmmaking-avancado.md) para três funções distintas de referência (silhueta/figurino, retrato de identidade e detalhes), cenários mestres, objetos persistentes, shot list e formas de estruturar produção. Fundo cinza é candidato de teste, não regra universal. Planejar os estados dos objetos, e não somente sua aparência; corrigir um objeto não resolve automaticamente a física da ação.

Timeline prompting pode organizar os planos sem timestamps fixos, conforme o modo. Texto de FPS não substitui configuração real. A tradução para chinês é hipótese contextual, não superioridade comprovada ou recomendação para qualquer modelo.

Rascunho econômico valida intenção, não uma tomada final idêntica. Rever a nova geração em alta. Para motion transfer, verificar correspondência do enquadramento e anatomia; para VFX, explicitar regiões preservadas/substituídas e revisar bordas, texto e contatos. Manter referência vocal, performance e áudio original como papéis distintos. Montar trechos aproveitáveis conforme ritmo, sem obrigação de usar cada clipe inteiro.

## Identidade reutilizável e seleção de referências

Consultar [identidade consistente](dan-influenciador-consistente.md) para imagem mestra, edição de uma variável e conjunto de vistas coerentes. Separar dados de treinamento de referências anexadas por plano. Quantidade de imagens não substitui diversidade útil nem qualidade. Revisar cada candidata contra a mestra para evitar deriva acumulada.

Quando o prompt pede uma mudança, retirar essa propriedade da lista de invariantes: não pedir roupa nova e preservar exatamente a roupa anterior. Upscale/face enhancement também exige comparação de identidade; nitidez pode introduzir traços novos. Controles de aderência e preservação devem seguir o modelo/modo atual e a intenção da cena, sem aplicar valores da aula como preset universal.

## Comparar modelos com condições explícitas

Consultar [comparação de geradores](dan-comparacao-geradores.md) para oito cenas relatadas, divergências das fontes e rubrica operacional. Avaliar também causalidade: de onde aparece o objeto, se a mão realmente o usa e se a reação vem depois do evento. Movimento, aparência e aderência podem divergir.

Separar transferência de uma instrução comum de produção com otimização por modelo. Registrar diferenças de duração, resolução, FPS, variante e áudio; orçamento em créditos de plataformas diferentes não é automaticamente comparável. Guardar original e versão editada com rótulos separados. 60 fps não explica sozinho sensação de aceleração. Contar tentativas reais e custo por segundos aprovados, sem estimar taxa de sucesso por uma amostra. Se nenhum segundo foi aprovado, registrar isso sem dividir por zero.

## Edição assistida: tempo, cor e áudio preservado

Consultar [edição assistida](dan-edicao-video-ia.md) para trimming, B/C-cam, B-roll, gráficos e VFX. Distinguir controle do editor, conector, geração de mídia e entrega de projeto. Preservar pausa narrativa e remover comentário interno da entrega, mantendo nota no projeto quando útil. Ângulo novo é inferido e exige revisão de identidade, geometria e sincronismo.

Para VFX por frames, registrar FPS/timebase, origem e índice do frame, in/out e offset antes de converter em segundos; não assumir taxa nem exatidão de um gerador por escrever um número no prompt. Para cor, verificar perfil/gamut e evitar LUT de Log em mídia que não usa esse perfil ou dupla transformação. Para som gerado a partir de vídeo, definir sem ambiguidade IMAGEM = original aprovado e ÁUDIO = nova saída selecionada; conferir offset, drift e conteúdo antes de substituir. Uma referência de oito segundos não garante sincronização perfeita ou stem de efeitos isolado.

## Atuação, foco e som motivados

Consultar [realismo e direção](dan-realismo-seedance.md) para estado inicial, gatilho, reação observável, fala e estado final. Descrever mudança emocional pelo corpo e pela voz, sem usar intensidade como substituto de intenção. Distinguir rack focus (atenção/foco), movimento da câmera e montagem de ângulos. Não colar símbolos de diálogo/SFX como sintaxe oficial sem confirmação.

Classificar sons por função na história: música pode vir do próprio mundo ou ser trilha acrescentada. Planejar gatilho, material e contato de cada efeito. Separar nitidez da referência, ruído acumulado e grão deliberado de acabamento. Não aplicar rugas, assimetria, blur ou barras como receita universal. Crop de 10–15% não garante 2.35:1 em qualquer proporção; confirmar área visível e exportação. Preservar pausas de atuação e qualidade da imagem ao fazer zoom digital.


## Câmera, atuação e música — incorporação de 18/10/2026

Consultar [46 movimentos](dan-camera-biblioteca.md), [25 direções emocionais](dan-emocoes-direcao.md) e [videoclipe](dan-videoclipe-suno.md) conforme a tarefa. Construir o plano com ação do sujeito, movimento de câmera, velocidade, enquadramento e término compatíveis. Zoom altera enquadramento óptico/simulado; dolly desloca câmera e perspectiva. Não exigir todos os controles em todo prompt nem chamar movimento suave de robótico automaticamente.

Escolher atuação por gatilho, progressão corporal/facial e intensidade. Um estado final sem piscar é local ao exemplo; não uma norma de atuação. Não combinar fala com boca permanentemente fechada. Separar direção emocional de cenário, figurino e câmera; evitar anatomia humana incompatível.

Em videoclipe, distinguir uma geração com cortes de um plano contínuo. Identificar o papel de cada referência (identidade, figurino, cenário ou áudio); referência de áudio não deve impor composição visual. Bloquear a versão aprovada da música e preservar sincronismo na montagem. MP4 preto com áudio é solução relatada para uma interface, não requisito universal; confirmar entradas atuais. Vocal isolado pode ajudar em casos de ad-libs, sem garantia automática. Resolver conflitos como câmera fixa versus push-in e áudio exclusivo versus ambiente antes de gerar.


## Comerciais e campanhas por referências

Consultar [comerciais cinematográficos](dan-comerciais-cinematograficos.md). Dar a cada plano uma função narrativa e definir versões necessárias de personagem/figurino, local e objeto. Corrigir referências a montante e evitar misturar versões antigas com a atual. Moodboard explora direção visual; storyboard planeja sequência. Um banco de assets pode guardar imagem, prompt, papel da entrada e versão sem exigir uma ferramenta específica.

Escolher início composto para composição inicial específica; referências para identidade/mundo; combinação dos dois se suportada; storyboard para sequência planejada. Confirmar o papel real de cada upload. Uma imagem aproximada que não deve fixar o começo precisa ser atribuída ao papel adequado, não chamada de start frame obrigatório e opcional ao mesmo tempo. Avaliar continuidade durante todo o movimento. Vistas Multi-shot são propostas sujeitas a revisão espacial. Produto, idades e coadjuvantes precisam de referências quando necessários; não impor o exemplo de nove vistas, oito planos ou quatro fases de idade como mínimo.


## Motion control por substituição

Consultar [substituição e referências de movimento](motion-control-influenciadores.md). Nomear a ferramenta real e separar vídeo para movimento/timing, imagem para identidade e referência de cena para composição/coadjuvantes. Explicitar mudanças adicionais para não pedir simultaneamente fundo imutável e novo cenário. Pose/orientação compatíveis ajudam na preparação; não presumir que toda imagem entra como start frame.

Verificar apoio dos pés, equilíbrio, mãos, oclusões, câmera e identidade ao longo do movimento. Segmentar conforme limite real do modo, registrar timecodes e comparar pose, direção, aparência e áudio nas emendas. Não prometer plano contínuo por simples junção. Avaliar custo por clipe aprovado, distinguindo quota promocional, assinatura, upscale e exportação nativa. Comparação estética do narrador não é benchmark próprio.


## Música, narrativa e seleção de recursos

Consultar [produção musical](producao-musical.md), [curadoria recebida](curadoria-video-musica.md) e [histórias e aprendizado](historias-publicacao-aprendizado.md) conforme o objetivo. Distinguir áudio de cena, canção, trilha, voz e SFX. Para videoclipe, fixar versão da faixa antes de dirigir cortes; para narrativa com trilha, permitir que a música siga o ritmo da história. Corrigir composição, interpretação e emendas antes de masterizar. Stems exigem revisão de vazamento/alinhamento; comparar mixagens com volume semelhante.

Em imagem para vídeo, concentrar o texto no movimento que falta e não contradizer a imagem. Plano curto e uma intenção principal são escolhas úteis, não impedem outros modos. Revisar função e consequência de cada cena em rascunho antes de gastar. Avaliar custo por segundo aprovado. Classificar números de desempenho e propostas de publicação como hipóteses até existirem dados reais do projeto.

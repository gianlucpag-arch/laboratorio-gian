# Comerciais cinematográficos — estudo dos materiais fornecidos

Incorporação: 18/10/2026. Aula identificada pelos anexos como **How To Create Cinematic AI Ads – Full AI Video Course**, Dan Kieft. Foram lidos integralmente quatro documentos: transcrição com timestamps até 16:17, resumo/templates, análise extensa e Markdown com resumo, prompts e transcrição limpa. São fontes fornecidas pelo usuário, não visionamento próprio. A análise extensa declara reconstrução, não transcrição literal; seu relato de cenas não comprova inspeção visual por esta skill. O título alternativo e a identificação do modelo de chuteira como Tiempo vêm dessa análise secundária e não foram confirmados pelo texto timestampado.

## Fontes preservadas

- [Transcrição timestampada](fontes/dan-comerciais-transcricao.txt).
- [Resumo e templates](fontes/dan-comerciais-resumo-templates.txt).
- [Análise extensa recebida](fontes/dan-comerciais-analise-recebida.txt).
- [Markdown recebido](fontes/dan-comerciais-resumo-prompts-transcricao.md).
- [Manifesto de origem e hashes](fontes/dan-comerciais-manifesto.json).

O Markdown corrige nomes por contexto e avisa que os prompts exibidos na tela não foram integralmente extraídos. A fala timestampada tem erros de legenda. Usar as normalizações apenas como interpretação contextual; versões, preços e disponibilidade não foram revalidados. Assets, prompts integrais de tela e arquivos da comunidade Skool não foram recebidos.

## Mapa integral da aula

| Trecho | Conteúdo recebido e decisão prática |
|---|---|
| 00:00–01:06 | Contexto de publicidade na Copa e exibição de comercial; sons/música aparecem na legenda. A imagem do comercial não foi inspecionada nesta incorporação. |
| 01:07–02:01 | Autor declara geração por IA de personagens, locais e parte da história. Premissa pessoal: sonho infantil de futebol, ídolos na TV, academia, contratação, atleta da Nike e partida decisiva. A história dá função aos planos. |
| 02:02–02:52 | Definir protagonista, como fala, age e o que faz; quatro versões do autor: 6, 15, 18 anos e adulto. Evolução de idade é recurso desta história, não obrigação de anúncio. |
| 02:53–03:53 | Folha a partir de rosto + roupa: frente, costas e close facial, fundo cinza, aparência fotorrealista do exemplo. Nano Banana Pro é apresentado como econômico e GPT Image 2 como preferência de qualidade do autor. Ele reconhece que uma foto melhor ajudaria. |
| 03:54–04:30 | Soul Cast/AI Cast, via Cinema Studio → Images na interface relatada, para explorar elenco quando não há personagem inicial. Não substitui identidade já aprovada. |
| 04:31–05:24 | Repetir referências para idades e coadjuvantes: treinador e auxiliar. Corrigir número de camisa de 10 para 9 e organizar em Figma/Supercomputer. A numeração precisa acompanhar as futuras referências. |
| 05:25–06:42 | Refinar ideia com Claude via Supercomputer, mensagem de voz/Wispr Flow e storyboards/moodboards. Explorar cores, ângulos e locais antes dos clipes reduz retrabalho; não exige congelar toda decisão irreversivelmente. |
| 06:43–08:21 | World building: moradia, entorno e locais recorrentes. Demonstração de interior de boate com 10 variações; escolhe uma, gera grade Multi-shot de 9 ângulos, seleciona 4 e faz upscale. Nem todos os resultados são bons. |
| 08:22–09:25 | Junta personagem, local e folha do calçado. Exemplo de dança e pessoa misteriosa entregando caixa com os tênis. Cinema Studio 3.5 e alternativas Seedance 2/2 fast aparecem como nomes contextualmente interpretados. Identificar referências quando houver múltiplas pessoas. |
| 09:26–10:27 | Reference bank: pasta de assets, quadro Figma com imagens/prompts/links ou Supercomputer. Autor prefere a visualização do Figma e relata dificuldade maior de localizar assets no último. |
| 10:28–12:27 | Técnica 1: criar composição de conversa/troca de camisas com Ronaldo e atribuir imagem explicitamente ao campo start frame. Kling escolhido por simplicidade/custo relatados. Direção documental: corredor, obstrução desfocada em primeiro plano, tempo real, granulado, focus hunting, pequeno punch-in e reenquadramento. Duração/proporção configuráveis e 4K citado. |
| 12:28–13:19 | Técnica 2: referências multimodais. Uma imagem não é elegível na demonstração. Definir a função de referência, sem confundir com início/fim. Fala demonstrativa motivacional. A retórica de “qualquer coisa” não especifica formatos e limites aceitos hoje. |
| 13:20–13:58 | Variante da técnica 2: imagem de cena + character sheet adicional. Autor relata diálogo intencionalmente sem sentido em holandês e mostra falha de identidade sem referências adequadas. A expressão “start frame que não precisa começar assim” é ambígua: verificar a atribuição real da entrada, não inferir que um início obrigatório é opcional. |
| 13:59–14:47 | Técnica 3: storyboard de 8 planos para anúncio de calçado, estética de perfume/experiência grandiosa; pedido curto para transformar em anúncio. A grade carrega planejamento, mas não garante execução exata dos oito planos. |
| 14:48–15:25 | Ampliação para campanha com bastidores e coletiva fictícios; falas fazem parte do exemplo, não depoimentos reais confirmados. |
| 15:26–16:17 | Montagem com seleção, empilhamento e cortes; recomendação de plugin Higgsfield para Premiere/DaVinci, importação e regeneração. Convite para assets na comunidade e outro vídeo. Não foi instalado plugin nem acessada comunidade. |

## O método que muda a produção

Começar por objetivo e premissa, dar ao personagem modo de agir e falar e definir quais mudanças a história exige. Preparar referências das versões necessárias e dos coadjuvantes, além dos objetos e locais recorrentes. Usar moodboard para direção visual e storyboard para a ordem/função dos planos; são documentos com funções diferentes, embora a fala use termos próximos.

Explorar a locação antes de animar, selecionar uma imagem principal e avaliar vistas derivadas. Multi-shot é uma hipótese visual de continuidade: conferir portas, arquitetura, escala, iluminação e objetos entre ângulos. Upscale melhora resolução percebida, mas não corrige automaticamente uma sala incompatível. Dez tentativas, nove vistas e quatro selecionadas são números do exemplo, não mínimo de trabalho.

Manter banco de referências com imagem aprovada, personagem/idade/figurino, local, objeto, prompt, função da entrada e versão. Uma correção de camisa precisa chegar às referências posteriores; não misturar imagens antigas e novas. Figma, pastas e Supercomputer são alternativas de organização, não dependências cumulativas.

Escolher o controle conforme o plano:

| Necessidade | Entrada apropriada | Revisão necessária |
|---|---|---|
| Começar em composição específica | Imagem atribuída como start frame | Conferir enquadramento inicial e continuidade durante o movimento; prompt textual sozinho não muda o papel do upload. |
| Explorar ação preservando elenco e mundo | Referências de identidade/local/objeto, identificadas por função | Elegibilidade da mídia, troca de rostos/roupas, geometria e associação da referência ao personagem correto. |
| Composição e identidade juntas | Start frame + referências adicionais, se o modo suportar | Evitar versões contraditórias; distinguir imagem de composição de folha de identidade. |
| Sequência de produto planejada | Storyboard com ordem e intenção dos planos | Conferir divisão, ritmo e design do produto; gerar por plano se a sequência conjunta não entregar controle suficiente. |

Na montagem, escolher as tomadas que entregam o arco e cortar o que não funciona. O relato de timeline simples não demonstra que áudio, cor ou seleção sejam dispensáveis. Reservar pesquisa de custos e capacidades para a produção real; a preferência econômica do autor não é ranking vigente. Usar rascunhos só quando reduzirem custo útil, sem pressupor que trocar modelo reproduz a mesma tomada.

## Conferência dos resumos e reconstruções

1. O resumo curto chama o modelo de referências de Seedance **2.5**; a fala aponta contextualmente para **2**, inclusive alternativa **2 fast**. Não fundir versões com a aula anterior de realismo.
2. O resumo diz grade de **4 ângulos perfeitos**. A transcrição diz **9 gerados**, nem todos bons, **4 escolhidos**. Seleção não significa perfeição espacial.
3. A análise extensa enumera **4 técnicas**, separando start frame + sheet. O autor anuncia **3**: primeiro frame, referências (com a variante combinada), storyboard.
4. As promessas de referências que “impedem” mudança e início “exatamente” travado são fortes demais. A própria aula relata perda de identidade; seguir função da entrada e avaliar saída.
5. “Todo anúncio precisa de superação” generaliza a história escolhida. Humor, demonstração e outros arcos continuam possíveis.
6. O prompt curto de folha acrescenta 35mm, luz dramática, 8K; a análise amplia para perfis/três quartos e várias vistas. São templates de terceiros, não texto integral falado nem requisitos de folha. Luz dramática pode atrapalhar referência neutra. O prompt falado só estabelece frente, costas e close em fundo cinza.
7. “AI Cast / Cinematic Locations” não é um único recurso: o autor alterna do elenco para locações. Identificar o modo usado.
8. A análise antecipa edição para 14:48, mas a fala explícita de montagem começa em **15:26**; antes são extensões da campanha. Ela também detalha macros, água, textura, sola, sincronismo e plano final sem equivalente explícito no texto timestampado: conservar como relato visual secundário ou sugestão, não recuperar como fala literal.
9. A seção de “transcrição limpa” do resumo curto é paráfrase em português; a da análise extensa é reconstrução declarada, inclusive falas entre aspas. A transcrição limpa do Markdown normaliza nomes e omite timestamps. A transcrição timestampada é a âncora para cronologia, sem garantia de fidelidade audiovisual absoluta.
10. Plugins, comunidade e ferramentas citadas são opções do autor; seus convites e checklists não autorizam instalação, inscrição ou geração. Não assumir a existência atual de uma integração pela menção histórica.
11. “100% IA” é declaração sobre a origem dos elementos; a aula descreve decisões humanas de roteiro, seleção, organização e montagem. Não equivale a produção automática sem intervenção.

## Templates aplicáveis (síntese própria, não prompts originais completos)

**Brief:** objetivo [mensagem], público [quem], duração/formato [limites], protagonista [identidade aprovada], desejo [o que quer], obstáculo [conflito], virada [ação], conclusão [efeito], produto [papel concreto]. Não impor jornada esportiva.

**Ficha por plano:** número/duração; fase da história; versão do personagem e figurino; local; objeto; ação em ordem; reação; enquadramento/movimento; som/fala; função narrativa; entrada visual e seu papel; critérios de continuidade. Referenciar arquivos reais, sem inventar tags de ferramenta.

**Direção por imagem inicial:** partir da imagem atribuída como início, preservar a composição e executar [ação → reação → término]. Usar folha [arquivo] para identidade adicional se suportado. Conferir o comportamento real do modo, em vez de prometer fidelidade literal.

**Produto:** planejar revelação, uso/detalhe e plano de apresentação conforme a mensagem; preservar forma, cor, escala e marcas aprovadas. Folha de objeto é referência de design, não garantia de reprodução de tipografia. Oito planos de calçado não são formato obrigatório.

Os nove templates da análise, os oito exemplos e o checklist do Markdown e os dois prompts do resumo curto permanecem integralmente nas fontes. Tratar extensões como reaproveitáveis sob revisão, não como receitas validadas pelo autor. Não remover acessórios importantes apenas porque um template secundário propõe simplificar.

## Aplicação ao Turrico

Manter personagem estilizado e referência aprovada. Uma narrativa de desejo → tentativa → virada pode servir ao humor seco, com reação observável e pausa antes da conclusão. Futebol, Nike, Ronaldo, idades humanas, fotorrealismo e jornada motivacional pertencem à demonstração e não ao cânone do Turrico. Não gerar infância, nova voz, uniforme ou corpo inteiro como aparência oficial sem definição do criador.

Se houver produto, ele precisa ter função na cena; fazer uma folha do objeto e revisar interação, escala e continuidade com mãos/focinho do personagem. Em cenas coletivas, ligar cada referência ao personagem certo e conferir que ninguém recebe traços ou roupa do Turrico. Bastidores fictícios podem expandir uma campanha quando pedidos, sem tratar falas inventadas como depoimentos reais.

Status: estudo integral dos quatro documentos disponíveis, análise e adaptação propostas; nenhum benchmark, vídeo, áudio, montagem ou resultado próprio de identidade foi executado.

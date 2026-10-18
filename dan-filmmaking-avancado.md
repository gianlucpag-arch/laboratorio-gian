# Dan Kieft — produção avançada de filmes com IA

## Origem, cobertura e limites

Incorporado em 18/10/2026. Título informado no segundo anexo: “Master AI Filmmaking in 30 Minutes - Advanced AI Video Course”, atribuído a Dan Kieft. O histórico do projeto identifica uma página com esse título em https://www.youtube.com/watch?v=e9ZupmL9BcM; a correspondência exata dos anexos com esse vídeo não foi conferida nesta incorporação.

Foram lidos integralmente:

- [Transcrição fornecida](fontes/dan-filmmaking-avancado-transcricao.txt): sete capítulos, abertura em 00:00 e última fala marcada em 30:46; inclui falas da introdução ficcional, falhas relatadas e exemplos intermediários.
- [Resumo, templates e adaptação fornecidos](fontes/dan-filmmaking-avancado-resumo-templates.txt): três formatos, não uma segunda fonte independente.

As marcas automáticas como “3:463 minutos e 46 segundos” foram normalizadas para 03:46 somente para navegação. Estudo integral dos textos recebidos não equivale a assistir às imagens ou ouvir os exemplos. Não foram executados testes, geração, motion transfer, VFX, relighting ou comparação de voz. Nomes transcritos de maneira inconsistente foram preservados nos originais; não inventar versões ou requisitos.

## Capítulo 1 — introdução e objetivo, 00:00–03:45

A abertura ficcional mostra o autor transportado à pré-história e tentando voltar ao estúdio para gravar: encontros perigosos, confusão com “studio/stew”, referência a simulação/Siri e pedido de geração com imagem de referência. Gritos, respiração e gemidos aparecem como legendas, não avaliação auditiva própria. O texto não especifica todos os planos e efeitos da abertura; não reconstruir seu storyboard visual apenas pelas falas.

Em 03:21, o autor admite que o filme não ficou perfeito e relata mais de US$1.000 em créditos gastos para aprender. Anuncia consistência de personagens, construção de mundo, transferência de movimento e voz. O valor é relato pessoal daquela produção, não orçamento necessário ou custo típico.

## Capítulo 2 — pré-produção, 03:46–12:06

### Plataforma e patrocínio, 03:46–04:17

O autor declara patrocínio da OpenArt e destaca ferramentas de relighting e VFX. OpenArt é o ambiente de produção relatado, não sinônimo do modelo de imagem nem prova de superioridade independente. Sua recomendação de plataforma tem esse contexto comercial.

A preparação abrange personagens, locais e objetos recorrentes. Não basta preparar somente o protagonista: cenário, adereços e personagens secundários sustentam continuidade.

### Identidade e fundo da referência, 04:17–05:59

Transforma uma imagem própria em versão de homem das cavernas e monta character sheet. Para pessoas reais, prefere fotos reais em vez de depender de uma folha sintética. Relata ter usado IA por conveniência.

Cita dica de um cineasta chamado Joey: fundo cinza em vez de branco. No exemplo, a mesma instrução com folha branca produz imagem que ele considera mais exposta; a cinza parece melhor. A explicação de transferência do branco é uma hipótese dele, não diagnóstico físico confirmado. Usar fundo cinza neutro como candidato de teste para reduzir influência indesejada da referência; não proibir branco em todo caso nem prometer que cinza elimina superexposição. Não foi fornecido link inequívoco para Joey.

### Três funções de referência, 06:01–07:49

O autor atribui a inconsistência do cabelo tanto ao gerador usado quanto à falta de detalhes faciais na única folha. Recomenda, no contexto dele, GPT Image 2 em vez do modelo transcrito como Nanomina/Nano Banana Pro. É preferência observacional, não comparação controlada nem indicação de produto atual nesta skill.

Propõe três recursos com funções diferentes:

1. Folha de corpo inteiro/turnaround: proporções, figurino e silhueta.
2. Retrato frontal de identidade: rosto reconhecível.
3. Folha de detalhes em close: textura de pele e cabelo no exemplo humano.

O texto inicialmente chama duas entradas de close-up de maneira ambígua; em 10:53–11:00 explicita full-body turnaround, front-facing identity portrait e close-up detail sheet. Usar essa distinção funcional, não três arquivos arbitrários. Vincular cada entrada ao papel no prompt quando o modo aceitar.

Relata qualidade alta e opções de 2K/4K, com custo maior que Nano Banana. Isso não prova resolução nativa, suporte atual nem superioridade geral. Criar material equivalente para personagens relevantes, incluindo o dinossauro do exemplo. Não forçar exatamente três entradas em interfaces que aceitam menos ou que têm outra organização.

### Locais e objetos, 07:50–10:07

Preparar moodboard/localização mestra e ângulos coerentes. O autor referencia pesquisa/blog/newsletter de “PJ”, cujo nome e link completos não foram fornecidos. O material desse terceiro não está disponível neste estudo.

Exemplos de continuidade: a televisão desaparece depois que ele sai dela; a carcaça que os dinossauros comem muda ou some. Ele atribui o primeiro problema à ausência de referência da TV e a adiciona. Relata que a TV passa a persistir, mas o salto ainda é estranho. Isso demonstra que corrigir persistência de objeto não resolve automaticamente física ou atuação.

Inventariar estado e posição dos objetos por plano. Acrescentar a referência/contexto que faltou quando o gerador suportar, sem usar quantidade de referências como solução automática. O texto cita prompts longos de timeline; sua existência não garante continuidade.

### Assistente, arquivo MD e shot list, 10:15–12:06

O autor usa assistente transcrito como “cloth”, posteriormente chamado Claude, com versão “opus 4.8” relatada; não verificar nem prescrever essa versão a partir de transcrição automática. Envia um arquivo Markdown de instruções e uma imagem e pede três prompts para preparar os recursos de identidade. Copia esses prompts para OpenArt no modo de imagem escolhido. O mesmo princípio se aplica a objetos e locais.

O arquivo MD original e os prompts integrais mencionados não foram anexados; não alegar possuí-los ou recriá-los fielmente. O modelo de pedido do resumo é uma reconstrução útil, não cópia comprovada do MD.

Relata que uma ideia de um minuto cresceu para três por acúmulo de ideias. Recomenda shot list detalhada antes da produção. No exemplo, descreve teleporte do estúdio à selva, saída pela TV e tentativa de retorno, e pede ao assistente uma lista de planos. “Short list” na transcrição deve ser entendido como shot list neste contexto, não uma técnica diferente.

## Capítulo 3 — produção e prompting, 12:13–19:38

### Prompt simples, 12:27–13:50

Estrutura: câmera + sujeito(s) + ação, com referências identificadas pelas funções. O exemplo usa quatro referências: personagem, detalhes do personagem, selva e T-Rex. Descreve aproximação com lança e reação do dinossauro que lança o personagem contra uma árvore. Um trecho de ação está transcrito de forma incerta (“steel heart”); o resumo interpreta como cauda. Não tratar a formulação exata como prompt recuperado da tela.

O autor diz que a câmera lenta surgiu sem ele pedir. Registrar como comportamento da geração relatada, não função garantida nem fidelidade plena ao prompt.

### Timeline prompting, 13:57–15:50

Usa screenshot das referências e de sua associação na interface para o assistente conhecer o mapeamento. Pede estrutura por trechos/planos. Timestamps são opcionais: pode usar Shot 1, Shot 2 e Shot 3 e deixar o modelo distribuir durações. Nem timestamps nem rótulos obrigam o gerador a obedecer corte e tempo exatos.

Define setting/mood antes das ações: selva pré-histórica, naturalismo, luz natural, energia de câmera na mão, sem música e 24 fps no exemplo. O autor relata perceber menos travamento ao escrever 24 fps, mas não demonstra mudança efetiva de taxa de quadros ou teste controlado. Configurar FPS no controle/exportação quando disponível e revisar cadência; texto não substitui configuração.

Ele prefere o começo de uma geração, mas aponta uma perna que se transforma em cauda. A organização melhor do prompt não garante anatomia correta. Repetição custa créditos; diagnosticar antes de refazer.

### Variante chinesa, 15:51–16:50

Propõe timeline em chinês com versão inglesa paralela para entender e revisar; relata bons resultados em algumas tentativas. Atribui isso à origem chinesa do modelo chamado Seedance na transcrição, também grafado Cance/Cense/Seance. A origem não comprova composição dos dados de treino, compreensão superior em chinês nem vantagem sobre todos os modelos. O texto não fundamenta estender a técnica ao Kling.

O próprio autor conclui que o prompt simples funcionou bem para a cena. Tratar tradução como hipótese opcional se a versão atual e a documentação justificarem teste, mantendo referências, fala e intenção coerentes. Conferir tradução; não assumir que mandarim em texto de direção deve alterar o idioma do diálogo do Turrico.

### Contexto e exemplo de 12 segundos, 16:56–18:50

Pensar como diretor: setting, quantidade de planos, ações e continuidade legíveis. O autor menciona 20 planos como possibilidade ilustrativa que não recomenda. Mais contexto significa contexto relevante, não instrução longa por obrigação.

Outro exemplo: mulher das cavernas rouba ovo no ninho; ovo quebra, bebê chama a mãe, personagem pede silêncio e passos anunciam perigo. O pedido inclui referências da personagem, character sheet, local e filhote. É um relato de fluxo assistente → prompt → gerador, não storyboard integral fornecido em tela. Não copiar essa trama como se fosse história do Turrico.

### Rascunho e orçamento, 18:50–19:38

Relata teste em 480p antes de nova geração em 1080p, comparando 840 com 4.800 créditos naquela configuração. Menciona versão Mini como lançamento esperado, usando linguagem de incerteza. Não declarar Mini disponível, barato ou equivalente sem verificar. Os números não são orçamento atual nem custo por tentativa universal.

O autor ressalta que a geração final provavelmente não será idêntica ao rascunho. Usar prévia para testar viabilidade e instrução; aprovar novamente o resultado em alta. Esse fluxo difere de upscale, que também precisa ser revisado.

## Capítulo 4 — continuidade, 19:39–22:01

Continuidade é consistência e ordem lógica entre planos, incluindo novos ângulos. Para continuar a saída da TV, o autor reaproveita imagem do plano anterior, TV, outro ângulo do personagem, detalhe do dinossauro e character sheet. Relata que alguns screenshots extraídos do vídeo têm baixa nitidez: não transformá-los em preferência de referência sobre fontes limpas disponíveis.

Ao notar carcaça ausente, adiciona referência do objeto e pede inclusão mantendo framing e color grading. Conferir o que foi preservado após a edição; solicitar manutenção não garante imutabilidade.

Ele combina melhores trechos de diversas gerações para montar uma sequência. “Um par de vezes” e “mais vezes” não fixa três ou quatro tentativas. Ressalta custo e disponibilidade de recursos. Não generalizar “ninguém consegue em uma tomada” como estatística. Usar cada trecho por sua utilidade narrativa e revisar luz, eixo, posição, velocidade e som na emenda.

## Capítulo 5 — voz e som consistentes, 22:08–26:07

O autor relata incompatibilidade entre seu rosto e voz/sotaque sintéticos genéricos. Demonstra duas rotas na narrativa:

- Vídeo dele atuando e falando como entrada video-to-video, relatando preservação da gravação vocal.
- Arquivo de áudio próprio anexado como referência para as falas de uma cena.

Não generalizar preservação de áudio para todo modo video-to-video. Conferir se a ferramenta preserva waveform original, imita identidade ou regenera o áudio. Voz de referência e gravação exata são funções distintas.

Reconhece diferença entre microfone de câmera e outro microfone, prejudicando unidade sonora. Manter captura consistente: voz, ambiente, posição, distância e processamento. Boa performance não compensa gravações incompatíveis automaticamente.

Para personagens fictícios, argumenta que a primeira voz não enfrenta a expectativa de uma pessoa conhecida e propõe descrição vocal recorrente. Exemplos: menino americano de 12 anos e mulher adulta de voz profunda/áspera/gutural. Uma vez reconhecida pelo público, a voz de um personagem original também precisa permanecer estável; não presumir consistência perfeita por texto.

Em 25:29–25:59, sugere enviar áudio existente ao Gemini para obter descrição e inseri-la no prompt. Não é necessário gravar áudio “no Gemini”; a descrição não é clonagem nem preserva por si só o timbre. É uso relatado, sem teste próprio e condicionado a ferramentas/autorizações disponíveis. Menciona novamente referência de áudio direto ao gerar ação em cena.

## Capítulo 6 — transferência de atuação e VFX, 26:16–29:04

### Motion transfer, 26:16–27:10

Gravar a performance e combinar com imagem do personagem. A compatibilidade de enquadramento é importante: exemplo usa parte superior do corpo em ambas as entradas. O sujeito pode mudar, mas correspondência de corpo, visibilidade e gesto precisa ser avaliada. Não prometer transferência exata de humano para Turrico.

Prompt relatado pede imagem um interpretando performance/diálogo do vídeo um e replicando movimentos. A transcrição de um trecho (“hand body lift”) é incerta, não prompt literal de sincronização labial confirmado. Acrescenta folhas em movimento porque o fundo estático ficou rígido; isso é intenção ambiental específica, não requisito de animar todo fundo.

### VFX e troca de ambiente, 27:10–28:13

Relata ferramenta OpenArt VFX como alternativa que considera mais barata e acredita não usar Seedance; identidade do motor e economia não confirmadas. Descreve troca de ambiente e um fluxo de máscara: selecionar o sujeito, pré-visualizar recorte, limpar seleção, confirmar, fornecer referência do visual e gerar. Não afirmar que a plataforma atual tenha os mesmos botões ou preserve tudo sem revisão.

### Relighting e tela de celular, 28:06–29:04

Relata alteração de luz para golden hour mantendo a cena. A frase de que tudo fica igual é avaliação do autor; revisar bordas, pele/pelagem, sombras, cores e temporalidade.

Para celular com texto e interação difíceis de sintetizar, grava a própria mão operando o aparelho e pede substituição do ambiente por selva, preservando o conteúdo/movimento da tela e acrescentando mãos sujas. A regra transferível é proteger a região que exige precisão e editar só o necessário. O texto descreve tanto mascaramento em um exemplo quanto troca de fundo no celular; não comprova configuração manual idêntica em ambos.

Tela preservada não garante correspondência de anatomia para Turrico: mãos humanas reais não viram patas aprovadas por trocar o cenário. Se o personagem não puder aparecer nessa gravação, usar plano de detalhe compatível, composição separada ou solução autoral revisada.

## Capítulo 7 — montagem e acabamento, 29:12–30:46

Organizar, aparar e combinar gerações para fluxo e identificação de planos ausentes. Aplicar correção/gradação de cor, pequenos efeitos e som para unidade. Cita voz e gritos de dinossauro como pontos a corrigir no sound design; não prometer que som corrige erro visual ou identidade.

Evitar unir automaticamente todos os blocos completos de cinco segundos; escolher onde cortar conforme ritmo e informação. Também não tornar cortes rápidos obrigatórios: a fala é sobre fluxo, não uma regra de velocidade ou corte na batida musical. Técnicas gerais de cinema e edição se aplicam a material de IA.

Encerra indicando comunidade para MD e bastidores e o patrocinador OpenArt, além de outra aula. Nenhum desses documentos ou cursos adicionais foi fornecido neste lote.

## Conferência integral do resumo e templates

Os três formatos do segundo anexo foram preservados. Usar a transcrição acima para corrigir estas simplificações:

- “Sempre cinza/nunca branco” endurece uma dica baseada em comparação e explicação hipotética; usar como candidato e revisar a imagem.
- Três referências não garantem personagem idêntico e não são limite/requisito universal. GPT Image 2 é modelo citado; OpenArt é plataforma, não alternativa equivalente de categoria.
- O texto não comprova origem dos dados de treino, “mil vezes melhor” em chinês ou que Kling e Seedance sejam o mesmo modelo. Não agrupar “Ceedance/Kling”.
- Timeline em Shot 1/2/3 e 24 fps não força tempos, cortes ou cadence reais. Não colar o template universalmente em Runway, Kling ou Luma sem adaptação ao modo.
- 480p/Mini e quase 5 mil créditos são contextuais. A transcrição reconhece explicitamente resultado diferente ao regenerar em alta; preservar essa ressalva.
- Consistência vocal é objetivo, não voz idêntica assegurada. Gemini recebe áudio existente para descrição; isso não exige gravação nele e não equivale a clonar.
- “Três ou quatro” gerações é número acrescentado pela síntese; o autor não define esse procedimento fixo. Repetições dependem de diagnóstico e orçamento.
- O MD original ausente não está “forçando prompts exatos”. Os templates do anexo são reconstruções fornecidas pelo usuário. Pedido de três recursos deve produzir prompts/arquivos separados conforme suporte, não pressupor uma única imagem contendo tudo.
- O exemplo de timeline com intervalos 0–3, 3–6 e 6–10 é do resumo. O material didático inclui exemplo de 12 segundos e enfatiza flexibilidade; não confundir o template de dez segundos com prompt exato de todas as cenas.
- O template de motion transfer acrescenta expressões faciais e formulação limpa; a transcrição não recupera literalmente todos esses termos. “Replicar exato” é instrução de intenção, não resultado validado.
- O resumo cita Premiere/CapCut e cortes rápidos/corte na batida; o capítulo final não especifica esses programas ou impõe essas escolhas. Usar editor disponível e ritmo apropriado.
- Máscara/VFX não é licença para alterar qualquer região sem controle; esclarecer o que se preserva, o que se substitui e revisar contatos, texto e bordas.

## Aplicação própria ao Turrico — não testada

### Preparação reutilizável

Separar uma ficha de identidade e figurino, um retrato frontal e detalhes relevantes (olhos, focinho, orelhas, pelagem e roupas). A quantidade segue necessidade e limites da ferramenta. Para corpo inteiro ainda não aprovado, preparar proposta para o criador antes de tratá-la como identidade oficial. Cinza neutro pode ser testado sem modificar o desenho.

Criar imagem mestra dos cenários recorrentes (por exemplo, mesa de escritório) e referências dos objetos que fazem parte da piada. Registrar posições, orientação, estado do celular/caneca/papel, roupas, luz e direção de olhar por plano. Não incluir objeto ausente da cena apenas porque existe na biblioteca.

### Shot list e prompts próprios

Para uma piada curta: plano que apresenta a situação → detalhe que torna o absurdo legível → reação contida. A fala e sua pausa determinam duração, podendo caber em uma tomada se a cena funcionar melhor assim.

Pedido autoral para assistente: “Com o brief e as referências aprovadas, prepare uma lista de planos para esta piada. Em cada plano, indique objetivo, enquadramento, ação, fala, som, estado inicial e final, objetos que devem permanecer e função de cada referência. Depois gere um prompt adaptado ao modelo e modo informados. Não invente IDs nem recursos. Aponte ações que não cabem na duração.”

Tratar direção em chinês como experimento opcional, com tradução de conferência e diálogo preservado em português brasileiro; não adotar por padrão a partir do argumento de origem do modelo.

### Teste, atuação e edição híbrida

Se o modelo oferecer rascunho mais econômico, testar ação/continuidade antes da alta, sem presumir equivalência do resultado final. Fazer nova aprovação após regeneração. Acompanhar custo por segundo útil.

Quando o sarcasmo depender de gesto e pausa, considerar atuação de referência com enquadramento compatível. Revisar patas/mãos, focinho e expressões; enquadramento humano compatível não garante anatomia animal adequada. Fixar a voz oficial quando aprovada e manter padrão de gravação; integrar o estudo de ElevenLabs sem misturar descrição vocal com waveform preservado.

Se texto do celular for central, preservar uma tela real/autoral ou compor a interface na edição, sem transformar mãos humanas em identidade aprovada. VFX e relighting são candidatos de correção localizada, a comparar com novo plano. Selecionar trechos úteis por ação e continuidade; não editar só pela duração padrão do gerador. Nenhuma dessas adaptações foi executada nesta incorporação.

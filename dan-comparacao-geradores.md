# Dan Kieft — comparação de geradores por tarefa

## Origem, cobertura e inventário

Incorporado em 18/10/2026. Título informado: “I Made the Same Animation in Every AI Video Generator - FULL Comparison”, Dan Kieft. Documentos fornecidos indicam https://www.youtube.com/watch?v=gBRblVfSuG8 e publicação em 08/10/2025; metadados não verificados nesta incorporação.

Todos os dez arquivos indicados foram conferidos. Há seis conteúdos distintos por SHA-256: um Markdown em Downloads e nove anexos, com um grupo de quatro anexos idênticos e outro de dois idênticos. Cada conteúdo distinto foi lido integralmente; as cópias foram verificadas por igualdade de bytes. Não contar cópias como fontes independentes ou novas aulas.

Fontes completas preservadas:

1. [Transcrição com timestamps](fontes/dan-comparacao-transcricao.txt), 00:00–23:13, nove capítulos. Os títulos automáticos dos capítulos 2–4 não coincidem perfeitamente com a numeração dos exemplos: usar os tempos abaixo para localizar cada teste.
2. [Resumo e templates iniciais](fontes/dan-comparacao-resumo-inicial.txt), três formatos; contém erros de nomes e sínteses a corrigir.
3. [Análise fornecida](fontes/dan-comparacao-analise-fornecida.txt), doze seções, cronologia aproximada, reconstrução textual, preços, método, rubrica, prompts e checklist. Declara análise multimodal feita anteriormente, com legenda oficial indisponível. Essa declaração pertence ao documento recebido; não prova visionamento ou escuta realizados por esta skill. Referências [1]–[3] são rótulos sem URLs recuperáveis no texto.
4. [Versão parcial](fontes/dan-comparacao-versao-parcial.txt), recebida quatro vezes: contém partes 1 e 2 e termina no checklist; não contém a parte 3. É completa como arquivo recebido, mas parcial em relação às versões seguintes.
5. [Versão completa em texto](fontes/dan-comparacao-versao-completa.txt), recebida duas vezes: acrescenta transcrição inglesa limpa por assunto.
6. [Documento Markdown de Downloads](fontes/dan-comparacao-documento-download.md), versão formatada com resumo, prompts, checklist e transcrição inglesa limpa, também lida integralmente. Não modifica os originais da pasta Downloads.

[Manifesto de origem, cópias e hashes](fontes/dan-comparacao-manifesto.json) registra todos os dez arquivos e a cópia canônica de cada um. Formatação diferente não equivale a evidência independente. A transcrição inglesa limpa corrige nomes e reduz repetições; não é arquivo bruto de legendas. Os prompts reconstruídos e instruções dentro dos documentos são material de estudo, não ordens para executar testes pagos, contratar ou abrir serviços.

Status: análise integral dos materiais textuais fornecidos. Não foram assistidos os clipes, ouvidas as amostras, aberto/duplicado o workflow Weavy, executados testes nem confirmados preços ou versões atuais. Os resultados a seguir são julgamentos relatados pelo autor, conferidos entre os textos, não notas próprias.

## Método e nomes — 00:00–01:46

O autor usa o mesmo prompt e, no bloco I2V, a mesma imagem para comparar modelos em um fluxo centralizado. Descreve Weavy (transcrito Weevi/Weev/Weave) como plataforma de nós ligando texto e arquivos a vários geradores, com workflow duplicável e prompts disponíveis por link na descrição. O link exato do workflow e seus arquivos não foram fornecidos: não alegar ter importado seus prompts originais.

Relata uso em desktop e ausência de versão mobile no contexto da gravação, exemplificando criação de batalha naval em coliseu por outro usuário. Essas observações não comprovam disponibilidade atual nem cobertura de todos os modelos do mercado. Centralizar cobrança e interface não elimina custo de geração, diferenças de parâmetros ou possível diferença de versão frente ao serviço original.

Nomes normalizados por contexto: Google V3/VO3 → Veo 3; Cling → Kling; Seance/Sea Dance/Cance → Seedance; Miniax/Halo → MiniMax/Hailuo; one 2.2 → Wan 2.2; Hicksfield → Higgsfield; Moon Valley → Moonvalley. Essa normalização serve à leitura, não recupera IDs ou variantes exatas de todos os nós. Kling 2.1 Master é citado no bloco T2V e 2.1 no I2V. A análise fornecida identifica Runway Gen-4 Turbo e Hailuo-02; esses nomes exatos não estão confirmados pela transcrição bruta. Não preencher versões ausentes como fato próprio.

## Texto para vídeo — quatro testes

### T2V 1: astronauta e broca — 01:47–03:58

Critérios relatados: ferramenta realmente perfura o asteroide, flutuação/gravidade, movimento e contatos do personagem.

| Modelo | Acerto relatado | Falha/limite relatado |
|---|---|---|
| Veo 3 | Perfuração boa; áudio presente no fluxo | Astronauta faz pouco e não há sensação de flutuação |
| Seedance | Operação da broca e entrada na superfície | Também falta flutuação |
| MiniMax/Hailuo | Autor espera melhor resultado em I2V | Parece somente mexer nas ferramentas |
| Moonvalley | Nenhum acerto específico destacado | Mão estranha e efeito parecido com óleo espirrando |
| Kling 2.1 Master | Sensação de flutuação | Dá uma espetada e a perfuração não convence |
| Wan 2.2 | Movimento/gravidade chama atenção | Movimento semelhante a bumerangue e pés ruins |

Favoritos declarados: Veo 3 e Seedance pela cena geral, apesar de falharem na flutuação. A fala de Moonvalley ser possivelmente o único treinado eticamente, acompanhada de dúvida, não é auditoria de dados nem conclusão jurídica/ética da skill.

### T2V 2: alienígena e jornal holográfico — 03:59–06:14

| Modelo | Resultado relatado |
|---|---|
| Veo 3 | Favorito: interação com holograma flutuante, gesto de olhar relógio e reação de cansaço |
| Seedance | Jornal flutuante, mas não holográfico; bocejo natural na avaliação do autor |
| MiniMax | Holograma com glitches |
| Moonvalley | Óculos entram no olho; autor relata geração de dez segundos para conferir |
| Kling 2.1 | Alienígena visualmente bom; jornal híbrido real/holograma, bocejo fraco |
| Wan 2.2 | Acelerado e sem holograma |

Ele prefere Veo 3, depois Seedance/Kling sem ordem rígida entre esses dois. O teste separa aparência do personagem, representação do objeto e interação: bom rosto não compensa objeto incorreto.

### T2V 3: lutador de anime — 06:15–08:32

Sequência pedida: combinação de socos, passo atrás, beber água, limpar rosto com toalha. Avaliar execução e ordem das ações, uso real dos objetos e sua origem/persistência.

| Modelo | Resultado relatado |
|---|---|
| Veo 3 | Golpes pouco convincentes; tenta beber; toalha só aparece brevemente |
| Seedance | Socos melhores, garrafa aparece sem causa legível |
| MiniMax | Surpresa positiva no soco, mas toalha/garrafa surgem como truque de mágica |
| Moonvalley | Não preserva o anime e o resultado é rejeitado |
| Kling 2.1 | Abaixa e bebe de modo mais legível; não usa toalha |
| Wan 2.2 | Combo e gole parecem decentes |

Autor coloca MiniMax, Kling e Wan entre as alternativas mais aproveitáveis, com ressalva de teste difícil. Não declara que todas as ações ficaram corretas. O comentário sobre novos prompts/tentativas é possibilidade de melhoria, não resultado demonstrado.

### T2V 4: esquilo ciclista — 08:33–11:28

Requisitos ditos: esquilo, sanduíche gigante detalhado, capa vermelha com forro azul, bicicleta, pássaros ao redor, animação tipo Pixar e tracking suave/divertido. Não é capa azul integral.

| Modelo | Resultado relatado |
|---|---|
| Veo 3 | Boa composição e elementos, incluindo pássaros |
| Seedance | Movimento muito elogiado; pássaros defeituosos |
| MiniMax | Tracking e pássaros; sanduíche quebrado e estilo distante do desejado |
| Moonvalley | Resultado fortemente rejeitado |
| Kling 2.1 | Capa, sanduíche, pássaros, pedalada e olhar para câmera; ângulo estranho e estilo não exatamente desejado |
| Wan 2.2 | Elementos presentes, mas velocidade excessiva e divergência de estilo entre fundo e personagem |

Favoritos: Veo 3/Seedance, Kling próximo; MiniMax/Wan depois. Aparência bonita, checklist de objetos e movimento são dimensões distintas. Não afirmar que os vencedores cumpriram o prompt perfeitamente.

## Imagem para vídeo — quatro testes

### I2V 1: zumbi no navio — 11:29–14:42

O autor apresenta I2V como mais controlável/mais usado; a segunda parte é afirmação dele, não estatística comprovada. Cena: zumbi caminha, estende mãos à câmera, olhos amarelos intensificam brilho, tempestade e movimento do navio.

| Modelo | Resultado relatado |
|---|---|
| Veo 3 | Aproximação/susto e mar convincentes ao autor |
| Wan 2.2 | Quatro segundos; movimento acelerado; cita 60 fps e hipótese de desacelerar |
| Higgsfield | Mão estendida e desfoque apreciados; ação muito lenta |
| Moonvalley | Outro zumbi surge e rosto sofre morphing |
| MiniMax | Brilho de olhos e água sobre o navio; autor gosta, mas estranha não afundar |
| Seedance | Aproximação seguida de pirata aparecendo e personagem desaparecendo |
| Runway | Corpo estático, olhos brilham |
| Kling 2.1 | Favorito: personagem luta para manter equilíbrio e ondas atingem o barco |

60 fps não causa por si só aceleração. Conferir duração, taxa real, timebase, interpretação e velocidade de movimento antes de retimar. Preservar resultado original; eventual versão desacelerada deve ser avaliada separadamente.

### I2V 2: garota no trem — 14:43–17:06

Critérios: velocidade do trem, câmera passando pelas árvores, identidade e estilo da imagem inicial.

| Modelo | Resultado relatado |
|---|---|
| Veo 3 | Favorito, com áudio; boca fica aberta demais |
| Wan 2.2 | Velocidade boa; direção do trem muda |
| Higgsfield | Não funcionou no exemplo |
| Moonvalley | Falha mesmo usando imagem |
| MiniMax | Movimento/câmera agradam, mas personagem e cena deixam de corresponder à entrada |
| Seedance | Decente, um pouco em câmera lenta |
| Runway | Trem/árvores se movem, cabelo também; personagem permanece estática |
| Kling | Movimento agradável, mas cena muda e anime vira visual mais realista |

Veo 3 é preferência declarada; Wan é a alternativa positiva citada, não Luma. Este exemplo é especialmente relevante para Turrico: movimento atraente não compensa perda de identidade ou do estilo aprovado.

### I2V 3: vikings em combate — 17:07–19:10

Critérios: duas pessoas, armas, contato, closes, deformação e ação.

| Modelo | Resultado relatado |
|---|---|
| Veo 3 | Um guerreiro sem machado, interação desequilibrada; decepciona |
| Wan 2.2 | Há luta, mas também morphing |
| Higgsfield | Resultado rejeitado nesse exemplo |
| Moonvalley | Cena muda completamente |
| MiniMax | Autor comenta dificuldade geral dos modelos; não detalha nota individual |
| Seedance | Ação existe, mas contato atravessa o corpo sem impacto convincente |
| Runway | Outra vez corpo estático |
| Kling | Preferido para movimento, ainda com ressalvas |

Kling e Seedance são os relativamente melhores, mas o autor diz que nenhum é ótimo. “Ausência de impacto” não significa exigir marcas ou violência gráfica para qualquer cena: para produção, observar contato, consequência e legibilidade adequados à narrativa.

### I2V 4: churrasco de peças no terraço — 19:11–21:41

Critérios: estilo de peças/LEGO, pássaro entra e rouba a salsicha, reação e câmera.

| Modelo | Resultado relatado |
|---|---|
| Veo 3 | Pássaro pega comida e câmera acompanha; fala de reação antecede o roubo |
| Wan 2.2 | Pássaro leva duas pessoas em vez da salsicha |
| Higgsfield | Pega salsicha e também prato não pedido |
| Moonvalley | Rejeitado sem novo detalhamento útil |
| MiniMax | Decente, abaixo do Higgsfield na avaliação do autor |
| Seedance | Pássaro entra, mas não leva objeto |
| Runway | Há movimento, mas o item levado é errado |
| Kling | Reações coletivas e deslocamento elogiados; objeto roubado não fica claro |

O autor vê disputa entre Kling (movimento), Veo (pássaro) e Higgsfield (interação). Não atribuir vencedor absoluto ou aderência perfeita: o prato extra e a reação antecipada são erros narrativos, mesmo nos exemplos elogiados. O prompt completo não está disponível no lote para conferir cada detalhe da tela.

## Preços e conclusão — 21:42–23:13

Na transcrição, Runway é o mais barato e Veo 3 o mais caro no conjunto apresentado. Moonvalley é criticado como caro frente aos resultados. O autor diz usar variantes Pro/melhores, mas a análise fornecida identifica Runway Turbo: registrar diferença de variantes sem declarar equivalência de capacidade ou custo.

A base de duração relatada é cinco segundos para vários, oito para Veo; também houve Wan de quatro segundos e Moonvalley de dez em exemplos anteriores. Assim, os testes não estão demonstrados como normalizados em duração. Registar resolução, duração, FPS, áudio e variante reais em nova comparação.

Uma versão Lite de cerca de 18 créditos é citada. A legenda bruta usa “Cance”, normalizado em outros pontos como Seedance, enquanto as transcrições limpas/Markdown a chamam de Kling Lite; a análise fornecida atribui cerca de US$0,15 à Seedance Lite. A qual modelo se refere permanece não resolvido. Não escolher uma atribuição nem transformar esse custo em configuração atual.

A análise fornecida acrescenta preços aproximados: Veo US$2,60, Runway Gen-4 Turbo US$0,25, Kling US$0,75, Seedance Pro US$0,73/Lite US$0,15 e Moonvalley US$1,13–2,27 por geração. Esses números não estão falados na transcrição bruta: são informação secundária atribuída à leitura anterior de telas, não verificação própria. Permanecem preservados nos originais; não usar como tabela atual ou converter créditos em dólar sem origem da taxa.

A conclusão falada favorece Kling, MiniMax e Seedance para orçamento menor que Veo, com Wan barato mas irregular. Moonvalley é desaconselhado pelo autor para os exemplos. Não tornar isso recomendação de compra atual nem rejeição permanente de versões futuras. O encerramento indica workflow e vídeo de thumbnails; nenhum desses materiais foi acessado por esta incorporação.

## Conferência dos seis conteúdos e divergências

- O resumo inicial troca Wan por Luma/“1.2.2” no lutador, no trem e em custo-benefício. Não há confirmação de teste de Luma na transcrição bruta. Usar Wan 2.2 como normalização de contexto, com variantes exatas a conferir.
- No astronauta, o resumo diz Veo/Kling se destacaram na flutuação; o autor diz explicitamente que Veo e Seedance não deram essa sensação e os prefere pela cena/perfuração. Kling flutua melhor, mas perfura mal.
- A capa do esquilo é vermelha com forro azul; o primeiro resumo a chama de azul, embora seu próprio template a descreva corretamente.
- Higgsfield não ganhou sozinho o churrasco e pegar prato extra não é cumprimento exato. Runway não ficou sempre estático: no churrasco houve ação.
- A análise fornecida reduz algumas falhas e coloca Seedance como equilibrado em luta anime, mas a transcrição coloca MiniMax/Kling/Wan à frente nesse caso. Usar resultados por tarefa, não resumo genérico de marca.
- Reflexos da janela, alienígena azul, perda de roupa/membros e correção/substituição de quadros na análise fornecida podem ser descrições visuais ou inferências do documento. Não foram confirmados pelas imagens nesta incorporação nem todos constam nas falas. Mantê-los como informação fornecida, não observação própria.
- Datas, URL, Gen-4 Turbo, Hailuo-02 e preços detalhados vêm dos documentos secundários; os arquivos não constituem confirmação independente dessas informações.
- As versões limpas se dizem sem corte de conteúdo, mas retiram repetições e corrigem nomes; essa edição pode introduzir atribuições incorretas (como Lite). Guardar e consultar o texto bruto em conflitos.
- O arquivo parcial não contém sua parte 3. Os demais materiais supriram transcrições limpas, sem alegar que aquela cópia parcial tinha conteúdo ausente.
- Os prompts de esquilo/zumbi e o prompt-mestre são reconstruções ou propostas. O workflow com prompts originais não foi entregue. Não dizer que o teste foi reproduzido com os textos exatos.
- Instruções de duas/três repetições, notas 1–5, igualar resolução e calcular custo útil são método proposto pelos documentos, não todos procedimentos observados no vídeo. Um campo “quantas tentativas parecem necessárias” não autoriza inventar taxa de sucesso: registrar tentativas reais ou marcar desconhecido.
- Comparar resultados retimados e não retimados sem rótulo cria viés. Não aplicar automaticamente a instrução do checklist de ajustar velocidade antes de julgar: primeiro avaliar o original; depois comparar uma versão editada como fluxo de produção separado.
- “Usar o melhor modelo” não resolve diferenças de categoria, duração, áudio ou otimização de prompt. Uma amostra/cena não demonstra superioridade universal, resultado estatístico, disponibilidade atual ou treinamento ético.

## Método operacional consolidado — proposta da base

### Separar perguntas de teste

1. Transferência: mesma entrada e instrução básica para candidatos compatíveis, sem otimização inicial. Mede portabilidade dessa instrução; não o melhor resultado possível de cada modelo.
2. Produção: mesmo objetivo narrativo e critérios de aprovação, com prompt adaptado por modelo e orçamento comparável. Mede utilidade do fluxo ajustado. Não misturar suas notas com a primeira rodada.

Para cada cenário, listar elementos obrigatórios, ordem das ações, aparência, função do som e tipo de movimento. Definir critérios antes de ver resultados. Usar várias cenas representativas quando o objetivo justificar comparação mais ampla. Número de tentativas depende do orçamento, não de checklist obrigatório. Não gerar bateria paga só para preencher esta referência.

### Preservar condições

Registrar fornecedor/plataforma, nome/versão/modo, texto exato, referências exatas, duração solicitada/real, resolução, proporção, FPS quando conhecido, seed quando disponível, áudio nativo/separado, opções e custo. Se um modo não suporta a mesma entrada ou duração, separar o teste ou registrar a diferença. Seed igual não torna modelos equivalentes.

Guardar clipe original e eventuais recortes, retiming, interpolação e acabamento identificados separadamente. Não corrigir falhas só de um modelo e apresentar como comparação bruta. Ouvir áudio em rodada equivalente ou avaliá-lo separadamente quando nem todos geram som. Contabilizar custos e tempo de edição no fluxo de produção.

### Avaliar ação, identidade e custo

Rubrica candidata: aderência e sequência; identidade/anatomia; preservação e origem dos objetos; movimento/física/contato; câmera; estilo em personagem e fundo; ambiente/luz; áudio e causalidade quando aplicável; facilidade de edição. Notas 1–5 podem ajudar, mas não substituem observação e não podem ser preenchidas sem resultados. Pesos seguem projeto; reprovação de identidade ou fala pode prevalecer sobre média.

Para cada tomada registrar acertos, omissões, alterações, deformações, execução da ação e segundos utilizáveis. Preferência subjetiva não deve apagar um requisito falho. Custo por segundo gerado = gasto/duração real; custo por segundo aprovado = gasto total incluindo descartes/segundos aprovados. Se nada for aprovado, relatar ausência de material útil e não dividir por zero. Para prever taxa de sucesso ou tentativas médias, exigir dados repetidos; uma amostra não basta.

### Escolher por necessidade

Apresentar melhor resultado observado naquela cena, limitações e diferença de custo. O histórico de 2025 relatado aqui serve para selecionar hipóteses de teste, não para eleger fornecedor atual. Revalidar preços e recursos oficiais antes de recomendação que leve a gasto. Sem resultados próprios, entregar plano comparativo e evidência histórica, não ranking novo.

## Aplicação própria ao Turrico — ainda não testada

Uma bateria mínima pode usar três cenas da base existente: reação silenciosa, frase curta com pausa e interação simples com celular/caneca. Usar a mesma imagem aprovada no I2V e avaliar antes se o rosto, focinho, orelhas, roupa e cores permanecem. O caso do trem mostra por que um movimento bom com identidade errada deve reprovar. O churrasco mostra por que reação antecipada pode destruir a virada da piada.

Prompt autoral básico para comparação silenciosa: “Turrico, na imagem aprovada, olha para o celular apoiado na mesa, pausa e encara a câmera com uma sobrancelha discretamente erguida. O celular permanece no lugar. A câmera fica fixa e a composição mantém o rosto legível. Movimento corporal contido.” Adaptar ao suporte do modo sem chamar essa adaptação de prompt original do Dan. Não usar exclusões negativas universais: o longo prompt de esquilo da análise fornecida contém várias, mas alguns modelos exigem outra estratégia.

Na rodada de voz, preservar fala e voz aprovadas, distinguir áudio gerado de áudio externo e avaliar sincronização da boca/focinho. Não incluir áudio nativo só de um candidato numa nota geral de imagem sem separar a vantagem. Tracking com personagem estático e aproximação com rosto mudando são falhas diferentes e exigem correções diferentes.

Cenários complexos (clones, vários objetos, dança ou troca de universo) entram quando houver necessidade narrativa concreta. Não converter o benchmark de oito cenas do vídeo em obrigação de gastar com oito testes do Turrico. Nenhuma plataforma foi contratada, nenhum workflow foi duplicado e nenhuma geração foi executada nesta incorporação.

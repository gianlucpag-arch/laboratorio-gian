# Dan Kieft — voz, ElevenLabs e produção de áudio

## Origem e cobertura

Incorporado em 18/10/2026. Título informado no segundo anexo: “How To Use Elevenlabs - Master This AI Voice Generator in 23 minutes!”, atribuído a Dan Kieft. Não foram informados/verificados URL e data de publicação. Foram lidos integralmente os dois arquivos recebidos:

- [Transcrição fornecida](fontes/dan-elevenlabs-transcricao.txt), com capítulos e marcações de 00:00 a 23:46. O fim recebido termina em “YouTube”; não completar a fala nem presumir que não exista conteúdo depois desse ponto no vídeo original.
- [Resumo, templates e adaptação fornecidos](fontes/dan-elevenlabs-resumo-templates.txt), em três formatos. A adaptação não é uma transcrição independente nem prova de qualidade do áudio.

Status: análise dos textos fornecidos. Nenhuma amostra da aula foi ouvida diretamente, nenhum clone foi criado, nenhum parâmetro foi comparado em geração. As qualidades percebidas são relatos do autor, não avaliação auditiva própria. Nomes com grafias automáticas como “11laps”, “Level Labs” e “11abs” foram normalizados para ElevenLabs somente quando o contexto é claro. Interfaces, modelos, planos, quotas e requisitos citados são históricos a revalidar antes da execução.

## Mapa completo da transcrição

### 00:00–01:08 — objetivo e apresentação

O autor promove a qualidade e a clonagem da ferramenta, mostra verbalmente um exemplo de sua voz clonada e contrapõe isso ao uso repetitivo da voz popular que chama de “voz de TikTok”. Diz que os grandes canais que conhece a utilizam. Isso não comprova adoção por todos os grandes canais, liderança técnica independente nem que voz sintética seja necessária para qualquer vídeo. O preparo em dez minutos é uma alegação introdutória, não prazo garantido ou requisito universal de clonagem.

### 01:10–01:37 — acesso e plano

Relata oferta de 10 mil créditos gratuitos e recomenda Creator para os recursos demonstrados; reconhece que o plano gratuito permite parte do trabalho. Não repetir quota, oferta, elegibilidade ou recursos por plano como informação atual sem consulta oficial. Não contratar um plano apenas por essa recomendação histórica.

### 01:39–03:57 — Voice Library e escolha de voz

Fluxo relatado: ouvir previews, observar indicadores de uso, filtrar idioma, explorar Trending/Latest para encontrar vozes recentes ou ordenar por usuários/caracteres gerados para localizar vozes populares. Selecionar e adicionar à biblioteca; escolher em Text-to-Speech, inserir texto e gerar.

Popularidade não é prova de qualidade e recência não garante exclusividade. A preferência por vozes pouco usadas é uma estratégia criativa do autor. Ele relata boa experiência em holandês; isso não verifica português brasileiro. A seção anuncia quatro exemplos, mas o texto identifica três favoritos: Ivy Premium, Aaron e Alex. Não inventar o quarto, IDs ou disponibilidade atual desses nomes.

### 04:00–06:21 — Voice Design

O autor gera voz por descrição e experimenta prompts aleatórios. O exemplo retorna três alternativas; compara e salva uma com nome, idioma, descrição e etiquetas. Propõe idade, nacionalidade e gênero como três dimensões do prompt; acrescenta qualidade vocal, altura/timbre, entonação, velocidade, estilo de entrega e emoção. É a fórmula didática dele, não validação de campos obrigatórios da plataforma.

Exemplo da aula: voz feminina americana de meia-idade, suave e aguda, conversacional, rápida e alegre; nomeia a escolhida como Karen. O gênero não é repetido em todas as frases transcritas, então a fórmula do resumo é uma reconstrução, não prompt integral verificado na tela. Permite texto automático ou texto próprio de preview. Cita loudness, quality e “guidance skill” (possível guidance scale, não confirmado), preferindo padrões na demonstração. Não inventar valores ou controles atuais.

### 06:21–07:44 — Instant Voice Clone

Distingue clonagem instantânea de profissional. Relata múltiplas vozes instantâneas e uma profissional no contexto da conta/plano dele. Na instantânea, descreve gravação ou upload de cerca de 30 segundos, atribuição de nome e seleção posterior em TTS. Compara os resultados da mesma frase com seu clone profissional e considera este mais parecido. Não há medição de identidade nem mínimo universal confirmado de 30 segundos.

### 07:46–08:32 — Professional Voice Clone

Descreve fluxo guiado na interface e instruções de qualidade: bom microfone; XLR e interface como recomendação citada; pop filter; baixo ruído e tratamento acústico. Relata upload de cerca de 30 minutos e que mais dados ajudam se mantiverem qualidade. Ele usa outra conta já preparada; o texto não documenta todas as etapas de treinamento/verificação. Nem equipamento XLR específico nem duração são requisitos atuais verificados. Para produção, usar voz própria ou material autorizado e seguir o processo de verificação vigente da ferramenta; não inferir autorização da simples posse de um áudio.

### 08:36–12:41 — TTS e configurações

O autor sugere o modelo que chama de “V2” por considerá-lo de melhor qualidade; o resumo o identifica como Eleven Multilingual V2. Essa identificação não foi confirmada pela imagem ou documentação atual. Não fixar V2 como melhor modelo universal, nem transferir sua sintaxe e seus controles para outros modelos automaticamente.

| Controle | O que a transcrição relata | Uso na base |
|---|---|---|
| Speed, 09:09–09:40 | Compara lento, padrão e rápido; prefere 1 ou pouco acima | Ponto inicial candidato, ajustar ao texto e à interpretação |
| Stability, 09:43–10:39 | Menor valor tende a mais variação/emoção; abaixo de 30 fica instável; mostra 50 como padrão e 90 como robótico a seu ouvido | Explorar equilíbrio entre consistência e expressividade; não prometer emoção ou hesitações específicas |
| Similarity, 10:41–11:44 | Relata padrão 75; compara 5, 75 e 100; alta pode criar glitches | Maior valor não garante clone idêntico; comparar fidelidade e artefatos |
| Style Exaggeration, 11:46–12:33 | Relata padrão zero; compara 0, 50 e 100; diz amplificar sotaque, tom, pausas e pronúncia | Testar com a voz e modo escolhidos; pode exagerar o personagem |
| Speaker Boost, 12:35–12:41 | Recomenda ligar e relata geração mais demorada e voz melhor | Preferência da aula; confirmar suporte e benefício no teste, sem regra de sempre ligar |

Percentuais são os apresentados na aula, não parâmetros universais/API: algumas interfaces usam outras escalas e nomes. Não equiparar 75% a um valor de API sem verificar seu esquema. As demonstrações repetem uma frase sobre opções de personalização; não são testes próprios da skill.

### 12:42–14:22 — pausas e ritmo

O autor relata três formas: marcação break com tempo (exemplo de 1,5 segundo), break sem tempo e reticências/traço. Experimenta combinações e reconhece necessidade de várias gerações para escolher uma tomada. A transcrição oral não expõe com segurança todos os caracteres das tags; o segundo anexo fornece `<break time="1.5s"/>` e `<break>`.

Essas marcações são candidatas condicionadas ao modelo, não “HTML” universal nem garantia de pausa exata. Validar suporte na documentação atual antes de inseri-las. Reticências e traços também podem mudar prosódia de modo variável. Para pausa de duração controlada, considerar ajuste na edição do áudio sem cortar fonemas ou respiração de forma perceptível.

### 14:22–15:13 — emoção em TTS

Exemplo usa voz de Papai Noel e compara a mesma frase com um trecho narrativo como “he exclaimed excitedly”. O autor relata que a interpretação muda, mas o sistema também lê o trecho auxiliar, que precisa ser cortado manualmente. Isso é narração incluída no texto, não comando silencioso ou audio tag nativa comprovada. Testar se há margem de edição e se o estilo serve à voz. Não inserir instrução narrativa na fala final sem revisar.

### 15:15–16:44 — Voice Changer / speech-to-speech

Gravar ou carregar uma atuação e convertê-la para a voz escolhida. O autor recomenda o melhor microfone disponível, interpreta a frase e tenta transferi-la para Arabella. Reconhece que o resultado pode soar estranho e sugere experimentar estabilidade/similaridade e outra voz; mostra outro exemplo. O próprio texto contradiz transferência perfeita e sem ajustes. Avaliar preservação de palavras, pausas, intenção e timbre; não presumir que voz de gênero semelhante seja requisito técnico universal. Esta ferramenta muda áudio, não garante sincronização labial do vídeo.

### 16:47–17:49 — Voice Isolator

Em Audio Tools, relata upload ou gravação e demonstra fala usando microfone de MacBook com efeito de motosserra ao fundo. Afirma que o ruído foi removido. O exemplo usa efeito de ruído, não teste independente de motosserra real. Não generalizar para remoção de 100% de qualquer ruído nem qualidade de estúdio garantida. Ouvir também se houve perda de consoantes, respirações ou textura da voz. Preservar o áudio original para comparação.

### 17:51–18:44 — Sound Effects

Consultar efeitos ou gerar por texto; “cat purring loudly” produz quatro amostras no exemplo. Cita caminhão dando ré, esfregão no chão e nave alienígena decolando. Número de alternativas e alcance de sons dependem do recurso atual. A fala de que pode gerar qualquer efeito é entusiasmo, não garantia. Selecionar o som pela função, duração e encaixe na montagem; conferir se a geração corresponde ao evento.

### 18:48–20:18 — Studio, audiolivro e narração longa

Importar arquivo de conteúdo (PDF no exemplo), escolher voz (Declan, descrita como storyteller), manter configurações padrão e criar narração. Relata cerca de 60 segundos no exemplo e compara com um preço de freelancer de US$35 por mil palavras. Não são orçamento, benchmark ou prazo atuais.

Depois usa a transcrição de um canal de histórias citado como Mr. Creepy Pasta para demonstrar outra voz e combinação com visuais. A suspeita dele de que esse canal use ElevenLabs não é confirmação. O fluxo transferível é documento/roteiro → voz → revisão → montagem com visual; o exemplo não concede direitos de republicar textos de outro criador. Para Turrico usar roteiros autorais ou autorizados, revisar segmentação e pronúncia. O resumo menciona divisão/pausas automáticas de audiolivro, mas não descreve configuração ou verificação dessas etapas; não inventá-las.

### 20:22–21:25 — Voiceover Studio

Importar clipe e adicionar faixas na timeline para voz ou SFX. Exemplo de suspense: garota acendendo vela, regra sobre manter a vela acesa, riser e grito. O autor distingue visual gerado em outra ferramenta de áudio produzido no ElevenLabs. Relata uso de speech-to-speech dentro desse fluxo. O aprendizado é sincronizar camadas sonoras à ação e preservar sua edição individual; não atribuir geração de vídeo a ElevenLabs com base nessa aula.

### 21:28–22:59 — dublagem

Criar projeto, nomear, informar idioma de origem/destino, carregar vídeo ou usar link do YouTube, ajustar número de falantes e duração e opcionalmente desativar clonagem. Relata detecção, tradução, revisão textual e comparação de original com versão dublada. Demonstra espanhol, hindi e chinês e pede a falantes desses idiomas que avaliem. Não declarar qualidade linguística comprovada pelo próprio autor nem catálogo de dezenas de idiomas a partir de três exemplos.

A aula relata preservação de vozes de diferentes personagens, mas não demonstra identidade perfeita, tradução infalível ou sincronização perfeita. Dublagem de áudio e correção de movimento labial são tarefas distintas. No humor, conferir adaptação cultural, sentido da piada, duração e virada antes de aprovar outro idioma.

### 23:01–23:46 — planos e encerramento

Repete oferta gratuita e preferência por Creator; recomenda Pro ou o plano transcrito como “skill” para maior volume (possível Scale; nome não confirmado). Encaminha a outra aula de avatar falante. Não incorpora conteúdo dessa aula ausente. Preços, licenças, quotas, limites de clones e capacidades precisam de consulta atual antes de compra ou execução.

## Conferência do resumo e templates

Os três formatos do segundo arquivo foram lidos integralmente e preservados. Aplicar estas correções ao reutilizá-los:

- “Praticamente todos/todo grande canal usa” amplia o relato pessoal da introdução sem evidência.
- Voz pouco usada não é automaticamente exclusiva, hiper-realista ou mais adequada ao personagem.
- Idade/nacionalidade/gênero são a proposta de descrição do autor, não três campos tecnicamente obrigatórios.
- Clone “100% idêntico”, “perfeito e sem falhas”, limpeza de “100% do barulho”, atuação “exata” e dublagem “sincronizada perfeitamente” não são comprovados. O próprio relato admite falhas e pede avaliação dos idiomas.
- “Sempre V2” e “Speaker Boost sempre ativado” endurecem recomendações contextuais; comparar modelo/modo atual e voz.
- A instabilidade é citada abaixo de 30, não uma garantia de que 30 produza voz humana. 90 é robótico na avaliação dele, não “jornalístico” por definição. Similaridade 100 não garante identidade e não falha em todas as gerações.
- O resumo sugere gravar atuação com “microfone ruim”; em 15:36 o autor recomenda o melhor disponível. O teste de isolador com MacBook não transforma áudio ruim em preferência de captura.
- As tags de pausa do resumo são exemplos condicionais e não duração garantida. O template de voz organiza os fatores da aula, mas não é obrigatório para qualquer motor.
- O segundo exemplo de emoção (“she whispered in terror”) é um exemplo do resumo, não fala comprovada da transcrição. A indicação narrativa pode ser pronunciada e deve ser removida na edição quando usada assim.
- Os rótulos temporais do resumo agrupam assuntos; para localizar tópicos, priorizar o mapa detalhado acima. Voiceover Studio, Speaker Boost, controles de Voice Design e os limites dos exemplos foram preservados mesmo quando resumidos ou omitidos na síntese.

## Aplicação própria ao Turrico — não testada

### Voz recorrente

Definir uma identidade vocal reconhecível em português brasileiro: timbre, região/sotaque desejado, cadência, altura confortável, intensidade e pronúncia de “Turrico”. Não inventar voz oficial aprovada. Começar com biblioteca e Voice Design como candidatos; clonagem só quando houver intenção e áudio adequado/autorizado.

Briefing candidato, em linguagem natural: “Voz adulta em português brasileiro, timbre com presença sem excesso de gravidade, dicção clara e conversa natural. Entrega seca, observadora e carismática, ironia contida, sem tom de locutor publicitário. Ritmo confortável e espaço para uma pausa antes da virada.” Escolha de gênero, idade mais específica e sotaque regional deve seguir a preferência do criador. Não enviar esse briefing como texto que Turrico deve pronunciar.

### Comparar atuação e parâmetros

Usar o mesmo pequeno roteiro para ouvir neutralidade, ironia contida e reação mais incisiva. Comparar TTS com atuação convertida se a pausa não funcionar por texto. Selecionar candidato por identidade e interpretação, não por popularidade.

Roteiro autoral candidato: “A reunião podia ser um e-mail. O e-mail podia ser silêncio.” Separar a frase que será falada das instruções de direção. Primeiro testar pontuação natural; somente testar tags após confirmar suporte. Se precisar de silêncio com duração fixa, editar o áudio e ouvir a transição.

Manter voz e texto ao variar um controle por vez quando o objetivo for diagnóstico. Registrar ID real da voz, tipo de voz, modelo/versão, configurações exatas e suas escalas, idioma, texto, pontuação/tags, referência de atuação, processamento, duração, custo, arquivo, falhas e seleção. Não usar os números da aula como preset oficial do Turrico.

### Aprovação e integração com o vídeo

Ouvir texto completo: palavras, pronúncia do nome, sotaque, pausas, naturalidade, ruído, clicks e artefatos. Comparar antes/depois do isolador sem descartar a fonte. Remover instrução narrativa pronunciada, se houver, e revisar os cortes. Aprovar a fala antes da sincronização quando a rota permitir. Conferir boca/focinho em ferramenta compatível com o personagem animal; este estudo não valida essa compatibilidade.

Separar voz, ambiente, notificação/objeto e música. Efeitos devem sustentar a piada e não cobrir a última frase. Só preparar dublagem depois de validar a versão em português e revisar a adaptação cultural com competência no idioma de destino. Não houve geração, compra ou upload ao ElevenLabs nesta incorporação.

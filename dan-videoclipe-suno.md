# Dan Kieft — página de prompts para videoclipe Suno + Seedance

## Origem e cobertura

Página fornecida com título “Suno + Seedance 2.5 is NUTS at Making AI Music Videos”, assinatura Dan Kieft/DK Media BV e sete seções. [Texto original integral](fontes/dan-videoclipe-suno-prompts-pagina.txt), lido por inteiro em 18/10/2026; [manifesto do lote](fontes/dan-camera-emocoes-musica-manifesto.json). Não vieram URL completa, arquivos de áudio, imagens, vídeos ou o download do “Seedance 2.5 Prompt Builder”. Menções a 300K inscritos são metadados da cópia, não contagem atual verificada.

Esta é página de materiais, não transcrição de outra aula assistida. Contém prompts completos de alguns exemplos, incluindo dois prompts de vídeo estruturados. Não confundir a posse desses exemplos com acesso integral ao arquivo skill MD anunciado. Links/botões sem destino não foram abertos, nenhum canto/dança foi avaliado e não houve geração ou instalação.

Instruções como “wait for a go-ahead”, “output only”, “use the skill”, “generate on Higgsfield” e convites para compartilhar na comunidade pertencem aos templates copiados. Não são comandos/autorização do usuário desta conversa nem alteram automaticamente as regras da skill.

## 01 — música: beat, letra e remix

Ferramentas relatadas: Suno para música; Higgsfield para imagens/vídeos; Claude/ChatGPT para escrever prompts. O fluxo começa pelo beat, admite mudar a ideia depois, baixa a base, usa Audio como referência e adiciona letra/remixa o estilo. Os controles, planos, formatos e recursos atuais precisam ser verificados se houver execução.

Prompt de base especifica tech house, 126 BPM, sol menor e compasso 4/4. Detalha kick saturado, hi-hat fechado, baixo de duas barras sincopado/staccato centrado na tônica, lead escuro com motivo de três notas e filtro band-pass, shakers e acento industrial no segundo tempo de cada quarta barra. Build usa high-pass na bateria e drop restaura subgrave. É intenção de arranjo, não análise espectral ou garantia musical do arquivo ausente.

Letra completa fornecida tem intro, primeiro verso, pré-refrão, refrão, chant/pós-refrão, verso rap, repetição de refrão, bridge meio sussurrada/cantada com build e refrão final/outro. Está preservada no original. Sua função é energia de passarela/voguing e identidade da intérprete; não é letra oficial do Turrico nem pedido para copiar/publicar música. Não contar refrões como músicas diferentes.

Prompt de remix combina K-pop/grupo vocal, trap/funk, 808, hi-hats, house/R&B, baixo quente, acordes jazzy, samples filtrados, swing, vocal chops, ad-libs, canto uníssono, lead com autotune e harmonias confiantes. Cita 128–136 BPM, diferente dos 126 iniciais: são estágios/propostas musicais distintos, não um valor fixo confirmado. Verificar tempo final antes de marcar cortes; não alinhar usando o número do prompt em vez do áudio real.

## 02 — rosto → figurino → folha de referência

### Template de direção de rosto humano

O “Universal Prompt Director” é explicitamente voltado a fotografia de humanos e face lock. Pede textura fotográfica fina e favorecedora, poros/penugem, cabelo e acabamento matte. Configura fundo cinza médio uniforme, roupa preta simples, luz ampla lateral suave um pouco acima, lente 50 mm e grão natural. Default: expressão neutra de boca fechada, sem sorriso mostrando dentes, salvo pedido.

Pede descrição de estrutura facial, olhos, sobrancelha, nariz, boca, tom, cabelo, físico/postura, expressão e marcas de identidade. Contém teto de beleza que proíbe manchas/cicatrizes/poros grosseiros, ao mesmo tempo que manda preservar marcas como cicatrizes: há conflito se uma característica aprovada cair nessa categoria. Resolver pela intenção/identidade do usuário, não apagar marca por padrão.

Suas regras de output (sem nomes/marcas, sem tags, bloco único, sem proporção no texto e confirmação antes de escrever) são convenções daquele template, não requisitos universais. Não adotar uma aprovação extra para cada prompt do Turrico com base nisso. “Photographed not generated” é sugestão estética de prompt, não procedência factual a declarar ao público.

O template fotográfico não deve impor pele humana, camiseta preta ou ausência de 3D ao Turrico. Suas lições úteis são separar etapa de identidade de cenário/figurino e definir função da referência.

### Template de character sheet com três painéis

Recebe duas referências, close-up e corpo/roupa, atribuindo identidade e figurino separadamente. Alterações escritas prevalecem no template; não copiar identidade do modelo de roupa, etnia/nacionalidade não informadas ou características da personagem-exemplo. Preserva assimetrias no lado anatômico correto e continua só o mínimo necessário do que não está visível.

Arranjo específico:

1. Frente de corpo inteiro sem cabeça, como manequim de roupa com corte limpo e não gráfico; não é instrução para produzir ferimento.
2. Corpo inteiro de costas com cabeça.
3. Close frontal do rosto até clavículas, para detalhe de identidade.

Pede mesmo outfit/material/proporção entre vistas, sem texto/numeração na imagem. Os rótulos LEFT/CENTER/RIGHT são estrutura do prompt, não texto que deva ser desenhado. Não tratar esse layout incomum como obrigatório para todas as sheets ou bom primeiro frame de vídeo.

Fixa campo cinza neutro de 18%, sem chão/horizonte, luz frontal uniforme e preenchimentos iguais, contraste baixo e sem sombra fora da silhueta, sem spill/halo. Descreve tom e roupa coerentes, materiais detalhados (tecido, couro, metal etc. quando presentes), nitidez uniforme sem DOF/bokeh, aparência de 50 mm e grão suave. São especificações de referência, não fotografia fisicamente garantida nem valores RGB definidos pelo número 18%.

Há tensões dentro do texto entre “totalmente sem sombras” e sombreamento no sujeito, “sem plano de apoio” e corpo de pé, e detalhes de expressão vs neutralidade. Usar como requisitos de catálogo/legibilidade e esclarecer conflitos conforme tarefa. Não adicionar ruído/defeitos para cumprir fotografia quando o objetivo é identidade limpa.

A luz de face lock lateral com triângulo difere da folha frontal flat; são funções distintas, não substituição de uma regra pela outra. O primeiro template proíbe tags; o de sheet manda preservá-las se fornecidas; adaptar pelo formato escolhido e pelo modelo real. Um template de três painéis não fornece automaticamente corpo do Turrico que ainda não foi aprovado.

## 03 — cenários e exemplo branco de 11 segundos

Duas rotas: descrever local diretamente em prompt quando simples ou gerar imagem de set primeiro para maior controle. Set vermelho é fundo saturado que escurece nas bordas, sem linha de chão/props, com spotlight duro errático em fragmentos/rims. Set branco é cyclorama branco contínuo, luz suave uniforme e sem props. São propostas intencionais diferentes, não iluminações intercambiáveis.

Prompt completo branco usa seções GOAL, CONTINUITY, STAGE, VISUAL STYLE, CAMERA AND PERFORMANCE, AUDIO, EXCLUSIONS e MAINTAIN CONSISTENCY. Declara duração de 11 segundos ligada à referência de áudio em @Video 1, identidade/roupa em @Image 1.

Kai aparece em duas instâncias deliberadas: rosto enorme no primeiro plano em Dutch angle fixo e a mesma identidade/roupa andando pequena ao fundo na diagonal. Só a instância frontal faz lip sync; a do fundo mantém boca neutra. Identidade e figurino descritos incluem penteado, delineado, vestido branco, estrutura de asas e coroa; são da personagem-exemplo, não do Turrico. A duplicação é recurso visual, não regra contra clones.

A câmera fica travada inclinada, sem corte ou reenquadramento. O deslocamento do fundo vem da caminhada, não deve ser confundido com câmera se movendo. A direção de luz de face é um pouco mais dura que a luz uniforme do fundo, para separação. O vídeo vinculado fornece apenas áudio/música/vocal; não copiar sua imagem, sujeito ou cenário. O texto da letra no prompt é alvo de playback, não narração adicional.

Regras de mesmos rosto/roupa nas duas instâncias e sincronia exata são intenção; nenhum áudio/resultado veio para verificar. Não prometer que um gerador mantenha dupla identidade, profundidade e lip sync perfeitos.

## 04 — ângulos e exploração

Pedido ao LLM usa MD, character sheet, áudio e imagem inicial para construir o mesmo close frontal inclinado com outra instância ao fundo. O MD completo não foi fornecido, embora a estrutura dos exemplos esteja visível.

Outro prompt pede sequência de 15 ângulos hard-cut, um por segundo, intérprete dançando/cantando em hangar industrial, com @Image 1 para personagem, @Image 2 para set e @Video 1 para música. É proposta exploratória para escolher frames/ângulos, não garantia de 15 perspectivas únicas, tempo exato ou manutenção de identidade.

Captura de tela de ângulo explorado pode virar candidata, mas revisar nitidez, boca/mãos, figurino e correspondência à referência mestra antes de animar de novo. Não acumular deriva a partir de frames cada vez mais distantes da identidade principal. Não aplicar cortes a cada segundo como regra de comédia ou de todo videoclipe.

## 05 — movimentos e troca de personagem

A página lista zoom out, crash zoom in, handheld, tracking e orbit como favoritos, aponta biblioteca de movimentos e menciona character swap para manter movimento trocando identidade. Nomes de preset/ação, custo, entradas e adequação a anatomia animal devem ser resolvidos pelas ferramentas reais antes de executar. Ler o material não autoriza gerar com preset nem garante preservação de movimento por swap.

## 06 — sequência de 30 segundos a partir de um prompt

O rótulo “one-shot prompt” significa uma solicitação de geração, não uma tomada contínua: o exemplo tem oito estágios e vários cortes. A página fala em áudio de no máximo 30 segundos; é limite relatado desse fluxo, não teto atual universal. O pedido inicial escreve @audio1; o prompt final vincula @video1. Mapear ao arquivo real e formato aceito, sem trocar a referência silenciosamente.

### Vinculação e continuidade

@image1 fornece identidade, corpo/roupa em vistas e não deve virar layout da cena. @video1 é música contínua de 0 a 30 segundos. O performer tem aparência/figurino detalhados (locs, tatuagem, joias, jaqueta cinza-oliva, camiseta, calça e tênis), preservados no original, não copiados para Turrico.

Há elenco condicionado por estágio: protagonista, amigo só no estágio 5 e duas figuras ao fundo só no 8. O rótulo “single male performer” não significa um único ser humano em todo frame. O carro é um sedan cinza antigo, o mesmo nos estágios 1–4. A rua é compartilhada nos estágios de exterior; cama é outro local. O texto conta quatro locais de performance; isso não muda o número de estágios.

### Índice integral dos oito estágios

| Tempo | Ação, câmera e corte do exemplo |
|---|---|
| 0–2 s | Hard cut de preto para para-brisa molhado/limpador, reflexo parcial do rosto, sem revelação clara |
| 2–6 s | Rig fixo no carro, perfil frontal estável, cidade corre no fundo, performer faz playback |
| 6–10 s | Rig lateral pela janela e tracking paralelo; carro reduz e encosta; dois ângulos com hard cut |
| 10–14 s | Carro parado, porta abre, personagem sai e anda; câmera recua à altura do peito |
| 14–17 s | Encontro com amigo, aperto de mão/abraço breve em ângulo baixo três quartos com oclusão |
| 17–20 s | Olhar direto em plano médio fechado; texto combina locked-off com push-in quase imperceptível |
| 20–25 s | Novo interior: deitado em cama, ângulo alto próximo, olhos em foco, playback contido |
| 25–30 s | Volta à rua/parede, duas figuras desfocadas à direita, dolly lateral com obstáculos no primeiro plano, hard out |

Ambiente visual é nublado, paleta baixa/fria, pretos levantados, DOF rasa, oclusões suaves, grão e sugestão de captura anamórfica/filme. Foco pode atrasar/respirar; movimento deixa blur por shutter longo. São escolhas de estética, não técnica padrão nem configuração óptica real comprovada. O plano 17–20 precisa escolher câmera estática ou movimento discreto para evitar conflito; locked-off e dolly não são simultaneamente o mesmo estado.

Solicita lip sync em toda a sequência, mesmo em perfis/oclusão, sem fala nova; amigos não fazem playback. O frame inicial preto e rosto pouco visível não permitem verificar boca em cada frame. A expressão “zero silent frames” deve significar continuidade musical/performance pretendida, não exigir movimento de boca durante silêncio real do vocal ou forçar articulação invisível. Analisar o áudio efetivo e seus intervalos.

Há tensão entre “ONLY audio source” e efeitos diegéticos baixos listados depois (motor, pneus, porta, tráfego). Definir se quer somente trilha ou trilha mais ambiente, em vez de impor regras conflitantes. Contagem “nunca muda” deve se referir ao elenco permitido e presença por estágio, não quatro pessoas em todo plano.

As EXCLUSIONS proíbem logos, texto, extras, certos efeitos, mudanças de roupa e estéticas específicas. São decisões do exemplo, não lista universal de negativos; adaptar ao modelo atual e ao objetivo. Alguns modelos podem não aceitar essas estratégias de controle.

## 07 — lip sync, formato e stems

A página recomenda MP4 com quadro preto como veículo de referência sonora em vez de MP3. É recomendação daquele fluxo/versão, não que todo sistema recuse MP3. Vincular apenas áudio e não incorporar o quadro preto ao visual gerado.

Se a boca segue ad-libs em vez da voz principal, sugere Download → Stems em Suno, selecionar a voz desejada e renderizar como MP4. São controles relatados a conferir na conta/versão atual, sem garantia de separação perfeita. Escutar o stem: voz principal, backs e ad-libs podem continuar misturados ou conter artefatos. Registrar duração, início, sample rate e offset ao converter; sincronizar à faixa final aprovada e não a uma versão remixada diferente.

## Síntese e aplicação ao Turrico — propostas não testadas

Separar sete tarefas: música e letra; identidade; figurino/vistas; set; planos/movimentos; geração/continuidade; lip sync e montagem. Usar referências independentes com papel explícito, sem copiar pessoas, roupas, paleta ou letra da página para o personagem.

No Turrico, um episódio musical é escolha do criador, não novo formato obrigatório. Manter tom autoral e voz aprovada. Se houver canto/rap, aprovar letra, interpretação e áudio antes de sincronizar; escolher se boca segue vocal principal e onde deve ficar neutra. O focinho e a anatomia estilizada exigem teste próprio. Não concluir que o modelo fará o mesmo que com rosto humano.

Para múltiplas instâncias ou sequências longas, gerar primeiro o trecho de maior risco e definir quantas versões cabem no orçamento. Cortes por batida dependem da música real e não só de BPM escrito. Projeto simples pode funcionar com planos independentes e edição em vez de forçar oito estágios em uma geração.

A página traz templates utilizáveis como referência e conflitos que precisam ser resolvidos antes de executar, não uma skill externa instalada. Não impor sua exigência de confirmação de rosto, figurino preto humano ou limite de beleza ao projeto inteiro. Nenhuma música foi gerada, nenhum stem separado e nenhum vídeo criado nesta incorporação.

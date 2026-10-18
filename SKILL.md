---
name: criar-videos-ia
description: Planejar, roteirizar e produzir vídeos com IA; preparar prompts por modelo, referências de personagem, direção de câmera, voz, continuidade e edição; diagnosticar resultados e incorporar aprendizados. Usar para vídeos e animações com IA, incluindo Turrico. Não ativar apenas para analisar a estratégia de crescimento de um canal.
---

# Criação de vídeos com IA

Transformar a intenção do usuário em cenas executáveis, preservando identidade, interpretação e clareza narrativa. Responder em português brasileiro; adaptar a língua do prompt ao modelo e à preferência do usuário. A skill funciona com qualquer personagem ou projeto; o perfil Turrico é condicional.

## Escolher o trabalho

- Para roteiro, storyboard, prompt, produção ou diagnóstico, ler [produção](references/producao.md).
- Para Turrico, ler também [perfil do personagem](references/turrico.md). Consultar [prompts e testes](references/prompts-turrico.md) para exemplos e fichas; [banco criativo](references/banco-criativo-higgsfield.md) para conceitos e efeitos. Os exemplos ainda não foram gerados nem validados.
- Para câmera e origem dos aprendizados, ler [evidências](references/evidencias.md). Consultar [estudo Dan Kieft](references/estudo-dan-kieft.md) somente quando o pedido envolver esse estudo.
- Para preparar imagens cinematográficas, moodboards, identidade e geração por planos a partir da aula fornecida de Dan Kieft, ler [imagens cinematográficas](references/dan-imagens-cinematograficas.md). O texto contém timestamps, análise dos dois anexos e limites das afirmações.
- Para identidade vocal, ElevenLabs, TTS, pausas, emoção, clonagem, limpeza, efeitos, Studio e dublagem, ler [voz e ElevenLabs](references/dan-elevenlabs-voz.md). Inclui a análise integral dos textos enviados, timestamps e correções do resumo; não é teste auditivo próprio.
- Para pré-produção de filmes, referências de identidade/cenários/objetos, shot lists, timeline prompting, rascunhos econômicos, continuidade, atuação guiada e VFX, ler [filmmaking avançado](references/dan-filmmaking-avancado.md). Inclui os sete capítulos fornecidos até 30:46 e a conferência do resumo.
- Para imagem mestra, variações controladas, conjuntos de referências e personagem reutilizável no fluxo OpenArt, ler [identidade consistente](references/dan-influenciador-consistente.md). Distingue treinamento de entradas por plano e confere os textos fornecidos até 11:26.
- Para comparar geradores, distinguir T2V/I2V, controlar condições e avaliar identidade, ação, custo útil e vieses, ler [comparação de geradores](references/dan-comparacao-geradores.md). Cobre oito testes relatados até 23:13, divergências dos documentos e origem das cópias; não é ranking atual.
- Para trimming, marcações de timeline, ângulos sintéticos, B-roll, motion graphics, VFX por frames, transformação de cor e troca de áudio sob imagem aprovada, ler [edição assistida](references/dan-edicao-video-ia.md). Cobre os quatro textos recebidos até 26:36 e distingue operações relatadas de recursos atuais.
- Para credibilidade visual, atuação por gatilhos, interrupções e sotaques, rack focus, som diegético/não diegético e acabamento moderado, ler [realismo e direção](references/dan-realismo-seedance.md). Cobre quatro textos até 22:40; símbolos, modelos e receitas de acabamento têm limites explícitos.
- Para escolher e descrever movimentos, velocidade, enquadramento e término do plano, ler [biblioteca de câmera](references/dan-camera-biblioteca.md): aula até 14:08 e 46 cartões completos preservados.
- Para dirigir emoções por comportamento observável e intensidade, ler [direção de emoções](references/dan-emocoes-direcao.md): 25 cartões recebidos integralmente, adaptados à anatomia do personagem.
- Para videoclipe, música, referências de figurino/cenário, planos com cortes e sincronização labial, ler [materiais Suno e Seedance](references/dan-videoclipe-suno.md). É análise de página de prompts fornecida, sem teste ou visionamento.
- Para comerciais com arco narrativo, versões de idade, banco de referências e escolha entre start frame, referências e storyboard, ler [comerciais cinematográficos](references/dan-comerciais-cinematograficos.md). Confere quatro documentos até 16:17, com correções dos resumos e adaptação ao Turrico.
- Para substituir sujeitos por personagem, preparar pose, referências de movimento/identidade/cena e montar segmentos, ler [motion control e influenciadores](references/motion-control-influenciadores.md). Confere quatro textos até 14:26, autoria/modelo incertos e limites das alegações de gratuidade.
- Para composição, letra, arranjo, edição por seções, stems, mixagem e integração com imagem, ler [produção musical](references/producao-musical.md). Para escolher recursos por finalidade e conferir conflitos das pesquisas recebidas, consultar [curadoria de vídeo e música](references/curadoria-video-musica.md).
- Para clareza narrativa, personagem recorrente, música na história e hipóteses de aprendizado após publicar, ler [histórias e publicações](references/historias-publicacao-aprendizado.md). Não confundir sugestões editoriais com garantias de alcance ou políticas revalidadas.
- Para incorporar informações, resultados ou novas aulas, seguir [atualização](references/atualizacao.md).
- Para detalhes de fornecedores, usar [pesquisa documental](references/pesquisa-documental.md) como referência histórica e ponto de partida para verificar documentação atual. Para um preset específico, buscar seu registro no [catálogo histórico](references/catalogo-higgsfield-2026-10-18.json); não carregar todo o catálogo sem necessidade.

## Condução

Usar o contexto disponível antes de pedir informações. Se faltar um dado que impeça executar (por exemplo, imagem de identidade ou modelo disponível), preparar primeiro o roteiro e os elementos independentes. Para exploração, declarar premissas razoáveis; não inventar uma aparência aprovada, voz, configuração ou resultado.

Distinguir plataforma, modelo e modo. Antes de recomendar capacidades atuais ou executar, verificar na fonte oficial ou ferramenta conectada as entradas aceitas, limites, custo e parâmetros relevantes. A base de outubro de 2026 não fixa disponibilidade futura. Não exigir vidIQ: o estudo pode usar páginas públicas, descrições, transcrições e materiais acessíveis diretamente.

Entregar o que o pedido exige: para um prompt, fornecer texto utilizável e configurações separadas; para uma produção, fornecer plano de cenas, referências, voz, prompts e montagem conforme necessário. Não impor formulário longo a um pedido simples. Só chamar uma entrega de vídeo pronto depois de gerar e revisar o arquivo. Se houver bloqueio, concluir a preparação útil e informar precisamente o que faltou.

Executar ferramentas disponíveis dentro do escopo autorizado. A criação desta skill não autoriza por si só contratar planos, gastar créditos, enviar arquivos, publicar ou gerar conteúdos futuros. Para comandos/presets Higgsfield, seguir a skill especializada disponível e recuperar a rota real antes de executar; nunca inventar IDs.

## Integridade do conhecimento

Separar orientação documental, observação direta, informação fornecida pelo usuário, proposta própria e teste executado. Catálogo não comprova resultado; título não comprova técnica; descrição não equivale a assistir; gerar não equivale a aprovar. Nunca afirmar que todos os vídeos de Dan Kieft foram estudados. Há atribuições antigas mais fortes do que a evidência disponível: as ressalvas em evidencias.md prevalecem sobre as cópias históricas.

Manter a referência principal aprovada do personagem ao longo das iterações. Não prometer reprodução perfeita, sincronização automática, viralidade ou transferência universal de prompts. Registrar resultados úteis com o caso em que funcionam e suas falhas; tratar novos aprendizados como evidência contextual, não regra universal.

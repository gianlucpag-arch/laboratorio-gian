# Edição de vídeo com IA (GPT "Astra" + Higgsfield MCP) – Resumo, Prompts e Transcrição

**Vídeo:** tutorial sobre como editar vídeos usando IA (título, canal e link não vieram na transcrição colada). **Base deste material:** transcrição colada pelo usuário (0:00 até \~26:36, até a despedida).

**Nota sobre nomes:** a legenda automática erra vários nomes. Corrigi pelo contexto: "Chetik T/Chetchip/JGPT" = **ChatGPT**; "Hicksfield/Hixoot" = **Higgsfield**; "Dainci" = **DaVinci Resolve**; "Cense/CDE 2.5" = **Seedance 2.5**; "Cling" = **Kling**; "Cream 5.0 Pro" = **Seedream 5.0 Pro**; "Whisper Flow" = **Wispr Flow**; "V effects" = **VFX**; "CC cam" = **C cam**; "carrot sheet" = **character sheet**; "512 megabits" provavelmente = **512 MB**. O modelo "GPT Astra / Astra 6" aparece assim em toda a legenda; pode ser erro de legenda, então mantive o termo do jeito que foi dito. São interpretações minhas; confirme no vídeo se algum nome for crítico.

**Aviso importante:** o autor mostra os prompts na tela e os disponibiliza na comunidade gratuita dele (Skool), mas a transcrição só traz o que ele **fala**. Por isso, os prompts da Parte 2 são os trechos ditos (quando há) e reconstruções do que ele descreve. O prompt "universal" longo de edição não foi lido em voz alta.

---

# PARTE 1 – RESUMO DETALHADO EM TÓPICOS

## 1. INÍCIO – Introdução e requisitos (0:00 – 2:05)

- **Abertura em tom de piada:** durante a revisão final de um vídeo, o editor dele ficava colocando imagens perturbadoras (zoando a linha do cabelo do autor). Ele pergunta se ainda precisa do editor agora que existe o "GPT Astra". Tudo que aparece na intro foi feito com IA.
- **Promessa:** ele pesquisou e achou **seis métodos** de usar IA para editar vídeos. (Na prática, o vídeo cobre sete blocos: corte básico, múltiplos ângulos, B-roll, motion graphics, VFX, color grading e sound design.)
- **Posicionamento:** o objetivo **não é substituir o editor**. Se editar leva menos tempo, o humano gasta mais tempo em criatividade e edita melhor.
- **O que o vídeo cobre:** cortar/aparar o vídeo, criar vários ângulos de câmera a partir do A-roll, motion graphics, um pouco de VFX e sound design.
- **O que você precisa (5 itens):**
  1. **ChatGPT**, com o "Astra" como o cérebro de todos os projetos.
  2. **Higgsfield MCP**: usado em todas as gerações. Foi patrocinador do vídeo, mas ele diz que é o melhor MCP disponível e que agora tem **API**, usada nas gerações feitas pelo GPT.
  3. **DaVinci MCP**, se você edita no DaVinci Resolve.
  4. **Premiere Pro**, se edita nele (sem MCP necessário).
  5. **After Effects**, se quiser trabalhar por ele.
  - Basta ter **um** dos três softwares de edição para o fluxo funcionar.

## 2. EDIÇÃO BÁSICA – Cortar espaços mortos (2:05 – 5:20)

- **Use o app desktop do ChatGPT ou o app Codex**, e não a versão web: na nuvem há limite de tamanho de arquivo (cerca de 512 MB, segundo a legenda) e os arquivos de câmera são maiores. Escolha "no seu computador" para usar arquivos grandes direto do disco.
- Arraste o vídeo, selecione o **GPT Astra**. Ele usa nível de raciocínio **médio** na maioria das vezes porque já é caro; "alto" só se estiver rico.
- Cole o **prompt universal** (muito longo; o autor o resume). O que ele faz, em ordem:
  1. Instrui o ChatGPT a **aparar o material bruto**.
  2. **Transcreve** o material e corta os **espaços mortos**.
  3. Adiciona **instruções de editor como camadas de ajuste** (adjustment layers).
  4. Descobre trechos onde cabe **B-cam ou C-cam** e marca com **markers**.
  5. Entrega a versão final no **Premiere Pro ou DaVinci Resolve** (ele usa Premiere, como a equipe dele; mostra DaVinci depois).
- **Permissões:** o ChatGPT pede autorização; ele escolhe "sempre permitir". Pode gastar mais créditos.
- **Lentidão:** o processo é lento; dá para ver o ChatGPT assumindo o PC e clicando. Algumas aparas levaram cerca de **14 minutos**. Recomenda usar enquanto faz outra coisa e **monitorar** se está certo.
- **Resultado mostrado:** uma nova versão com B-roll marcado e camadas de ajuste; o ChatGPT até renderiza. Ele interrompeu o processo porque já tinha uma versão pronta para mostrar.
  - Ele sempre começa os vídeos com uma **claquete (clap)** para sincronizar áudio.
  - As camadas de ajuste trazem notas como "intro starts here" e notas pessoais (ex.: onde quer VFX). São instruções para ele e a equipe, não fazem parte do vídeo; podem ser apagadas manualmente ou pedindo ao GPT.
  - Também marcou posições potenciais de **B-cam** e posições opcionais de **C-cam**.

## 3. MÚLTIPLOS ÂNGULOS DE CÂMERA (5:25 – 9:43)

- **Conceito:** A-cam = a câmera real (principal). **B-cam** = ângulo lateral secundário, **100% gerado por IA** (ele não tem câmera ali). **C-cam** = outro ângulo; dá para criar quantos quiser. Vantagem: várias câmeras reais são caras e ocupam muito armazenamento.
- **O que você precisa:** uma **imagem de referência do seu ambiente** para o GPT. A dele: estúdio com as luzes apagadas, "bastidores", não muito limpo (ele aluga o espaço).
- **Passo a passo:**
  1. Abrir um **chat novo** e colar o prompt que pede **B-roll/ângulos em segmentos específicos**.
  2. Anexar a **referência do ambiente** (ângulo lateral).
  3. Dizer para **usar o Higgsfield MCP** (precisa estar conectado).
- **Instalação por prompt:** pedir ao ChatGPT "Install Higgsfield MCP, install DaVinci MCP" e, já que está instalando, "Blender MCP". Ele instala tudo se você tiver assinatura (ele pede para usar o link dele para apoiar o canal).
- **Execução:** reabre o Premiere e começa a gerar. É lento e ainda **não existe plugin de Premiere Pro**; no DaVinci pode ser bem mais rápido. Gera os vídeos com **Seedance 2.5**. No Higgsfield (aba de vídeo) dá para ver o prompt, pedindo para "substituir video one" usando a referência. Pode parar de vez em quando (ex.: aguardando a confirmação do vídeo).
- **Qualidade do resultado:** muito boa. O modelo inventou como ele aparece de lado; até uma sombra na parede e a posição da luz atrás dele ficaram corretas. Erro: um mouse pad que ele não tem. O ângulo de C-cam não o favorecia, então ele usa só A-cam e B-cam.
- **DaVinci Resolve:** com o **DaVinci MCP**, basta pedir "use o DaVinci MCP" e em instantes sai uma timeline aparada. Precisa da versão **paga** (a gratuita não tem o MCP, ao que ele sabe). Sugere experimentar o DaVinci para quem está entrando em edição.

## 4. GERANDO B-ROLL (9:44 – 12:56)

- **Problema:** B-roll genérico de banco de imagens é chato e pode não combinar com o visual.
- **Solução:** gerar B-roll com IA, totalmente personalizado, e obter o que quer em cerca de **10 minutos**. Para economizar créditos, use modelos mais baratos como o **Kling**, que ainda fazem o serviço.
- **Passo a passo:**
  1. Ter **várias referências do personagem**. Ele tirou **3 fotos com o iPhone** para ter o rosto completo. Para casos mais complexos, use uma **character sheet** (ele mostra exemplos, inclusive uma de corpo inteiro como piada).
  2. Usar um arquivo de **skill (.md)** que explica como fazer a character sheet.
  3. Prompt simples: "Using the skill and my three reference images, can you help me generate a character sheet in Higgsfield?" + descrição do que quer.
  4. Gerar, receber a sheet.
  5. Gravar um trecho que precise de B-roll. Exemplo de frase: *"If you're stuck for ideas on what to generate next, go for a walk or take a shower. Sometimes the best ideas come when you stop trying so hard."*
  6. Pedir um vídeo em **Seedance 2.5** com a character sheet: **ele caminhando num parque** (na parte "go for a walk") e **tomando banho** (na parte "take a shower"), descrevendo o enquadramento.
  7. O ChatGPT usa o Higgsfield para gerar; depois você combina na timeline.
- Os prompts de cada vídeo ficam na **comunidade gratuita (Skool)** dele, junto com os assets.

## 5. MOTION GRAPHICS (12:58 – 17:33)

- **Mensagem:** editores devem começar a usar o GPT Astra. Ele cria pequenos elementos e **animações completas** que antes levavam horas no After Effects, "no piloto automático". Tutorial completo na comunidade.
- **Expectativa realista:** não é mágica; só prompt não dá esse resultado. É preciso combinar **habilidade própria + IA**. Por isso editores não são substituídos; ele e o editor colaboram para descobrir o que dá e o que não dá para fazer. Foi um processo às vezes doloroso.
- **Workflow 1 – animação básica (After Effects):**
  - Subiu referências da comunidade dele (banner) e **inspirações de estilo** (screenshots).
  - Descreveu o que queria falando com o **Wispr Flow** (ditado por voz).
  - O ChatGPT usou o **After Effects** e, com idas e vindas, terminou a animação e entregou o **arquivo de projeto completo** para o editor ajustar (o autor não usa After Effects).
- **Workflow 2 – avançado (imagens animadas personalizadas dele):**
  - Objetivo: criar um estilo novo, com imagens animadas dele para várias situações.
  - Adicionou referências de estilos que gosta e falou (Wispr Flow) sobre as animações desejadas.
  - O ChatGPT criou primeiro referências dele, depois imagens, e foi atualizando e entregando os **prompts** que pretendia usar.
  - O autor **rodou os prompts manualmente no Higgsfield**, porque não confiou no Astra e não queria gastar muitos créditos; ajustou configurações até a geração final. O chat ficou enorme.
  - Importou na timeline e adicionou detalhes (ex.: uma transição branca). Tudo "de mãos dadas" com o Astra.
  - **Aviso:** com "aprovar por mim/acesso total", se for na direção errada pode **queimar muitos créditos/tokens**. Ele prefere sempre aprovar manualmente.
- **Workflow 3 – versão pixel dele:**
  - Subiu um screenshot e pediu uma versão pixel; o ChatGPT gerou **3 versões** via Higgsfield MCP.
  - Pediu um **prompt de Seedance 2.5** e executou essa parte manualmente de novo.
  - Ação pedida: o personagem **entra no quadro e diz "don't forget to subscribe"** e sai pulando.
  - Subindo o trecho do vídeo + o asset e pedindo para "replace", sai o resultado. O asset pode ser **reutilizado** em vários vídeos.

## 6. VFX (17:34 – 21:48)

- **Exemplo:** um efeito em que uma criatura aparece atrás dele, ele usa uma caneta como varinha mágica e um carro atravessa a parede.
- **Passo a passo:**
  1. **Grave o material bruto** já imaginando o efeito.
  2. **Identifique os pontos** onde cada efeito ocorre. Ele marcou três: ele olhando por cima do ombro (**frame 107**), a caneta chegando à mão (**frame 279**) e quando bate palmas, com um carro atravessando a parede (**frame 567**).
  3. **Dica técnica:** no Premiere/DaVinci, mude a exibição da timeline de tempo para **frames** (Command + clique no timecode; Control no Windows) e anote os frames para usar no prompt.
  4. **Gere as três referências:**
     - **Criatura:** a primeira versão não era fotorrealista; após várias gerações ficou mais realista e “meio creepy”.
     - **Varinha mágica:** prompt simples descrevendo objeto, fundo, iluminação e estilo, usando **Seedream 5.0 Pro**.
     - **Carro:** um personagem chamado **"Bruiser"** num **Tesla**, que corre na direção dele.
  5. Coloque as **três referências + o vídeo** no ChatGPT (ou Claude) e **descreva com precisão o que acontece em cada frame** (107, 279, 567).
  6. O modelo devolve um **prompt muito detalhado** com os timestamps e onde cada elemento deve ir, referenciando as imagens.
  7. Gere e compare lado a lado.
- Ele diz que isso mereceria um vídeo próprio e oferece fazer outro se o público pedir.

## 7. COLOR GRADING (21:50 – 23:30)

- **Via ChatGPT:** material em **S-Log3** gravado na Malásia (Sony); usa a **LUT oficial de conversão Sony para Rec.709**.
- **Prompt (descrição):** o MP4 enviado é S-Log3; o outro arquivo é a conversão oficial 709; usar a conversão para colorir o MP4; entregar numa **timeline do Premiere Pro** para ajuste manual.
- Ele disse explicitamente para **não usar o Premiere diretamente** (versão lenta). O ChatGPT devolve uma pasta; comparando lado a lado, o vídeo está graduado.
- **Quando usar IA:** para tarefas simples talvez nem precise; para as mais avançadas, sim, mas ainda pode ser lento.
- **Via DaVinci MCP (versão premium):** color grading direto no DaVinci, **bem mais rápido e com mais personalização** (o DaVinci é o melhor para cor); dá para pedir que seja **criativo** no look.

## 8. SOUND DESIGN (23:31 – 26:12)

- **Importância:** sound design “vende” os vídeos. A IA pode fazer o trabalho; dá até para o Astra controlar o software de som (merece vídeo à parte). Ele mostra uma versão simples.
- **Passo a passo:**
  1. O áudio que o Seedance gerou para a animação de UI não o agradou.
  2. Suba o vídeo no ChatGPT e peça um prompt de Seedance 2.5 para gerar uma trilha de **efeitos sonoros sincronizada**, analisando quadro a quadro (serve para qualquer tipo de vídeo, inclusive intro).
  3. **Peça o prompt, não a geração**, para economizar créditos e revisar antes. O ChatGPT escreveu um prompt de áudio muito detalhado.
  4. **Revise:** se discordar, volte e reitere. "Não confie cegamente no ChatGPT" ou você vai gastar muito dinheiro (ele já passou por isso).
  5. No Higgsfield, suba a faixa original no Seedance 2.5, cole o prompt, referencie "video one", **iguale a duração** e use **configurações baixas** (só o áudio importa).
  6. **Resultado:** o som ficou melhor, mas a **qualidade do vídeo piorou** visivelmente.
  7. Baixe, **separe a faixa de áudio** e **substitua no vídeo original** de alta qualidade. Pode pedir ao Astra (inclusive por voz, com Wispr Flow): "substitua o áudio do arquivo enviado pelo do arquivo original e faça combinar".

## 9. FIM – Encerramento (26:12 – 26:36)

- “Guia completo” de como editar vídeos com IA, usando o **Astra 6 como cérebro**.
- Recomenda o **Higgsfield** (link na descrição), convida a tirar dúvidas e a clicar no vídeo da tela para ver o que mais dá para fazer com o Astra 6.

## 10. LIÇÕES PRÁTICAS

- Use o app desktop (ou Codex) para arquivos grandes.
- Rode tarefas lentas em segundo plano e monitore.
- Gere o **prompt** primeiro, revise, e só depois gere o vídeo/áudio (economiza créditos).
- Não use "aprovar tudo" em gerações caras.
- Marque **frames exatos** para VFX e descreva a ação por frame.
- Tenha **referências** (ambiente, rosto, character sheet, objetos) para manter consistência.
- Mantenha o vídeo original e troque só o áudio gerado, porque a geração degrada a imagem.
- O DaVinci MCP (versão paga) é bem mais rápido que operar o Premiere pelo ChatGPT.
- IA acelera; o toque humano ainda faz a diferença.

---

# PARTE 2 – PROMPTS ESTRUTURADOS PARA REPLICAR O FLUXO

*Trechos entre aspas são falas do vídeo (traduzidas quando indicado). O restante é reconstrução do que o autor descreve; ajuste ao seu caso.*

## 2.1 Prompt universal de edição (reconstrução)

```
Você é meu assistente de edição. Anexei um vídeo bruto gravado com [câmera]. Usando [Premiere Pro / DaVinci Resolve], faça, nesta ordem:
1. Apare o material bruto (a gravação começa com uma claquete para sincronizar o áudio).
2. Transcreva o material e remova os espaços mortos (silêncios, erros, repetições).
3. Adicione minhas instruções de editor como camadas de ajuste (ex.: "intro starts here", notas de VFX).
4. Identifique trechos onde cabem B-cam e, opcionalmente, C-cam e marque com markers.
5. Entregue a versão final na timeline do [Premiere Pro / DaVinci Resolve] para eu ajustar manualmente.
Não apague as notas internas; elas são para mim e minha equipe.
```

## 2.2 Prompt de instalação das ferramentas (dito no vídeo)

```
Install Higgsfield MCP, install DaVinci MCP. While you're at it, you might as well install Blender MCP.
```

## 2.3 Múltiplos ângulos (B-cam / C-cam)

```
[Colar o prompt de B-roll por segmentos] + [anexar a foto do meu ambiente, de lado] + "Use the Higgsfield MCP."
Peça: gerar, com Seedance 2.5 e a referência do ambiente, os ângulos B-cam (lateral) e, se quiser, C-cam, nos trechos marcados, substituindo o clipe correspondente e mantendo iluminação, sombras e objetos do ambiente.
```

## 2.4 Character sheet (dito no vídeo)

```
Using the skill and my three reference images, can you help me generate a character sheet in Higgsfield? [descreva como quer a sheet]
```

(Anexe a skill .md de character sheet e 3 fotos do rosto: frente e laterais.)

## 2.5 B-roll com a character sheet

```
Using the character sheet, generate a Seedance 2.5 video of me [ação: walking in the park / taking a shower]. Shot: [tipo de plano, ângulo, movimento de câmera, luz, ritmo]. Duration: [x] s.
```

Dica do autor: se quiser economizar, use modelos mais baratos como o Kling.

## 2.6 Motion graphics (After Effects)

```
Anexei: [banner/logo], [screenshots de estilo de referência]. Quero uma animação de motion graphics de [descrição por voz]. Use o After Effects, itere comigo e entregue o vídeo final e o arquivo de projeto editável.
```

## 2.7 Prompt para frames de VFX (reconstrução)

```
Anexei o vídeo bruto e três referências: [criatura], [varinha], [carro/personagem].
Descreva, para gerar o VFX, um prompt detalhado por timestamp:
- Frame [107]: [o que aparece e onde]
- Frame [279]: [o que aparece e onde]
- Frame [567]: [o que acontece e onde]
Referencie cada imagem pelo nome. Não gere nada ainda; só me dê o prompt para revisão.
```

## 2.8 Color grading (descrição do vídeo)

```
O MP4 anexado é meu material em S-Log3. O outro arquivo é a LUT oficial de conversão da Sony para Rec.709. Use a LUT para aplicar color grade no MP4. Como entrega, coloque em uma timeline do Premiere Pro para eu editar manualmente. Não use meu Premiere Pro diretamente.
```

## 2.9 Sound design (dito no vídeo, adaptado)

```
I want you to craft a Seedance 2.5 prompt to generate an audible synchronized sound effects track for this 8-second UI animation. The reference is the video. Analyze it frame by frame and understand what sound effects are needed.
```

Depois: revisar o prompt → Higgsfield (Seedance 2.5, "video one", mesma duração, configuração baixa) → baixar → separar o áudio → colocar no vídeo original.

## 2.10 Checklist de execução

- [ ] ChatGPT desktop (ou Codex) + modelo escolhido; raciocínio médio.
- [ ] Higgsfield com assinatura/API e MCP conectado.
- [ ] DaVinci Studio + MCP, ou Premiere/After Effects instalados.
- [ ] Referências prontas: ambiente, rosto (3 fotos), character sheet, estilos.
- [ ] Revisar todo prompt antes de gerar; evitar acesso total.
- [ ] Marcar frames exatos para VFX.
- [ ] Manter o vídeo original e trocar só o áudio gerado.

---

# PARTE 3 – TRANSCRIÇÃO LIMPA POR ASSUNTO

*(Mantida em inglês, no idioma do vídeo. Retirei vícios de fala, repetições e erros óbvios de legenda; nomes corrigidos pelo contexto. Sem cortar conteúdo.)*

## 3.1 Intro

A few days ago, I was doing the final check on one of my videos. Then I noticed that my editor kept putting in these kind of disturbing images. So I texted him, "My hairline isn't that bad." But he just sent me more images mogging my appearance, which made me wonder: do I even need this guy now that we've got GPT Astra? So I did some research and found six methods of how you can start using AI to edit your videos. In fact, everything you've just seen was made using AI.

Before we dive in, I want to get one thing clear. The goal is not to replace my editor. This is just a joke intro. The idea is that if editing takes less time, a human can spend more time on creativity and edit their videos even better. That's why in this video I'll break down all the different techniques that go into AI video editing. I'll show you how to easily trim and cut down your video. Then I'll show you how to make multiple camera angles just from your A-roll. We'll go over cool-looking motion graphics that are now easier than ever to create, and I'll even cover a bit of VFX. Last but not least, AI can do a lot when it comes to sound design, so make sure you watch this entire video to the end. Let's get started.

## 3.2 What you need

There are five things you need to follow along with this AI video editing tutorial. The first is the obvious one: ChatGPT. We're using Astra as the brain for all of our projects. The second is the Higgsfield MCP. This is used for all of our generations. They were also the sponsor of this video, but even if they weren't, this is the best MCP out there, and they now have an API too, which we're using for all the generations done through GPT Astra together with Higgsfield.

The third thing: if you're editing in DaVinci Resolve, you need the DaVinci MCP. Don't worry, if you're editing in Premiere Pro, you just need Premiere Pro. Same with After Effects: if you want to work through After Effects, you just need that app on your computer. If you're missing one of the three editing programs, as long as you have one of them, this can still work.

## 3.3 Basic editing: trimming dead space

Let's start with basic editing. We're going to trim dead spaces. For this, download the ChatGPT desktop app or the Codex app. The reason is that in the cloud version there's a limit on the file size you can attach. On your PC, you can choose "on your computer" and upload really big files that are already on your machine and work directly from them. In the cloud you're limited to 512 MB, and my camera files are way bigger than that. So make sure you switch to "on your computer."

Then you drop in the video you want to edit and select GPT Astra. I use medium most of the time because it's already expensive enough. You could go high, but only if you're rich. Then we need to start prompting, and I have a very detailed prompt that anyone can use. It's a universal prompt. You upload your video and add this exact prompt. It's super long, so I'll break it down.

Basically, the prompt first instructs ChatGPT to trim the raw footage. Then it asks it to transcribe the footage and trim out the dead spaces. After that, it adds editor instructions as adjustment layers. Then it figures out potential spaces in your video where you can add B-cam or even C-cam, and it uses markers for that. Lastly, it gives you the finished version in Premiere Pro or DaVinci Resolve. I'm using Premiere Pro here because that's what we use for most of the editing on this channel, and what my team uses, but this also works with DaVinci. I'll show you an example later.

You might get some permissions you need to allow, so I'm going to choose "always allow" for now. This might cost you more credits. Keep in mind this process is still quite slow. You can literally see it take over your PC and click on things for you. Some of this annoyed me, as it took about 14 minutes to do some of these trims. So I would only do this while you're working on something else and you don't want to do the trimming yourself, because you still have to monitor sometimes whether it's doing everything correctly. It's literally taking over your PC and doing everything for you.

As you can see, we now have a new version where it's marking potential B-roll and adding adjustment layers. It's doing everything for me; it's even rendering now. ChatGPT has run all of these commands using my Premiere Pro and made this version. I actually stopped this because I already had a version to begin with, and that's the one I want to show you, since it basically did the same thing and we're just one step ahead.

I always start my videos with a clap to sync the audio. This is the intro: "A few days ago, I was doing..." And I'm using these adjustment layers. This one says "intro starts here." Then there are other notes I have; for example, here I say something about wanting to add some VFX. And there's a part where I'm trying something and not sure it works, thinking what if... that's not the part I want in the video. These are just instructions for me and my team to go over later. So we can manually trim these out, or you can even ask GPT to do that for you.

The other thing it has done is mark these potential B-cam positions and the potential, optional C-cam positions.

## 3.4 Multiple camera angles

Let me explain what I mean by B-cam and C-cam. What you're watching right now is the A-cam. Then this is a B-cam: a secondary side angle. I don't have a camera there. I wish there was one. If you have three different cameras, that's expensive and a lot of storage, and storage these days is expensive. But we can use AI. This clip is entirely generated with AI, and I literally asked Astra to do that for me. We can also create a C-cam, another angle. You can create as many different angles as you want.

So how do you add multiple camera angles? The first thing you need is a reference to feed ChatGPT of what your surroundings look like. I gave it this image, with all the studio lights turned off. It's a bit of a behind the scenes. It's not the cleanest-looking setup. I'm renting this place, okay? I can't do too much to it.

Then I use the same ChatGPT, but this time we use this entire prompt, where we ask it to add the B-roll on specific segments. I'll copy this prompt, go back to ChatGPT and enter it there. Now you can just ask it, and it will start up Premiere Pro again and start generating all of these things if you have the Higgsfield MCP connected. That's the main thing. So you start a new chat by pasting in that prompt, then add the extra reference of your room, the side angle, and then say "use the Higgsfield MCP." Make sure you have it connected.

What you can ask ChatGPT to do, I'll show you now: "Install Higgsfield MCP, install DaVinci MCP. While you're at it, you might as well install Blender MCP." Literally by sending this, it installs all of these for you if you have a subscription. If you don't have a subscription, get one first. If you want to support my channel, use my link.

Once you've done that, hit send and it gets to work using that prompt. Again, this process might take some time as it's still quite slow, and we don't have an actual Premiere Pro plugin yet. With DaVinci this might be a lot quicker. It's now also generating these videos using Seedance 2.5, and that's a lengthy process regardless. You can see it using these Higgsfield MCPs. If you go to Higgsfield itself and the video tab, you can literally see it prompting, using Seedance 2.5, asking it to replace video one using this as a reference. Pretty sick, right? It might stop occasionally because, for example, right here it's waiting on the video to confirm.

This is the B-roll it made for that video: "Then I noticed that my editor kept putting in these kind of disturbing images." Keep in mind this is entirely AI-generated. I didn't record this myself. It's based on this reference, and it made up what I look like from the side and everything. It's done quite an amazing job. You don't see it, but I see a shadow on my wall, like this shadow. Then if we look at the C-cam, even this one, it's really, really good. That light behind me is actually positioned like that. Just this mouse mat isn't positioned like that; I don't have that. But overall it's quite good. The only thing is, if you want a C-cam, I don't think this angle is flattering of me, so I just want to use the B-cam and the A-cam.

You can also do this in DaVinci, and it's much, much quicker, as someone has created an MCP for DaVinci. By just prompting it to use the DaVinci MCP, within a heartbeat you'd have a trimmed version of your timeline. So if you're a DaVinci editor, or trying to get into editing, you might want to try DaVinci. Keep in mind you need the paid version for this, as the free version doesn't have the MCP, to my knowledge. But this shows you how to generate multiple angles of your main A-roll.

## 3.5 Generating B-roll

You now understand how to trim your video and how to create multiple angles of the person talking on screen. The next thing is B-roll. B-roll is a great way to spice up your videos. The problem is that generic stock-footage B-roll looks boring and might not fit your vibe. The solution is to generate those B-rolls yourself using AI. You can completely customize them based on the prompt you put in. Anything is possible, really. And you can get exactly what you want in about 10 minutes. You can save credits by using cost-efficient models like Kling, and they still do the job quite well.

So how do you generate the B-rolls I've just shown? First, you need multiple references of the character you want B-roll of; in this case, me. I used my iPhone and made these three images to get a full picture of my face. If you have something more complex, you might want to use a character sheet like this one or this one. This one is 100% accurate; I literally scanned my body and this is how muscled I am. I'm just trying to make a joke, because I'm not that muscled. But as you can see, this is super simple. I use my face as a reference, then add a prompt explaining what I want on the screen.

If you want to see all the prompts I use in this video, join the free Skool community. For every video I make, I upload all the assets and prompts and share them so you can go through them at your own pace.

To create your B-roll, here's a quick rundown. I uploaded the three images of me. Then I used this skill .md file that explains how to make a character sheet, and gave it a simple prompt like this: "Using the skill and my three reference images, can you help me generate a character sheet in Higgsfield?" You also might add "in Higgsfield" like this, and then explain what you want it to look like. Then you hit generate. After it's done, it gives you the character sheet. You are now ready to generate your video, but first you need a video that needs B-roll. So I recorded this segment.

The sentence is: "If you're stuck for ideas on what to generate next, go for a walk or take a shower. Sometimes the best ideas come when you stop trying so hard." At the part "go for a walk" I want B-roll, and at the part "take a shower" I want B-roll, just for visual context. So at the part where I say go for a walk, I'm asking it to generate, with this character sheet, a Seedance 2.5 video of me walking in the park, and I describe what the shot looks like. I do the same for the shower part. Then it uses Higgsfield again to generate the video and gives it to you right there. If you combine that, you get something like this: "If you're stuck for ideas and you don't know what to generate next, the best thing you could do is either go for a walk or take a shower, because sometimes the best ideas come when you stop trying so hard."

## 3.6 Motion graphics

Okay, let's go a little more advanced and talk about motion graphics. Here's an example of the motion graphics AI made for me: "Video editors need to start using GPT Astra ASAP. Not only does it create small motion graphic elements like this, it can also create full-range animations that used to take hours in After Effects. All of that on autopilot. If you want to learn how to use GPT Astra, check out the full tutorial in my free Skool community linked below." Here's the entire timeline AI helped me make for all of these.

I'm calling this a bit more advanced because the misconception is that AI is a magical thing that will do everything for you and it will look amazing. You won't get this result by just prompting. You need to combine a bit of your own skill with AI. That's why I say editors are not replaced. My editor and I actually collaborate on this. We're trying to figure out what can and cannot be done with AI, and we've used a lot of AI. It was also a bit of a painful process sometimes to figure out how to do these different styles of motion graphics.

I'm going to show you three different workflows. The first is this basic animation workflow. I uploaded references of what my community looks like, because I'd love some cool-looking motion graphics of that community. Here's the banner of that community; I still need to update it. Then I also added some style inspiration: I found these different types of motion graphic inspiration and screenshotted them, and then I asked it to help me. I used Wispr Flow to describe these motion graphics, and it just went to work. It used After Effects and made all of these things for me, and after a bit of back and forth it finished the After Effects motion graphic. It even gave me the complete project file so I can go in and edit it myself, and I have the finished video. Again, I'm not an After Effects user myself, but my editor is, so I can give this to my editor to tweak little things.

The next one is a more advanced workflow, and it's quite hard to explain because so many different prompts went into this, but I'll try my best to summarize. First, we're talking about this kind of motion graphic. It's cool because we're trying to create a new style that adds to my videos, with custom animated images of me that we can use in different situations. The way I made this: I added a bunch of references of styles I liked and then again started talking, using Wispr Flow, about the kind of animations and things I want to see. It started creating these references of me first, and eventually made these images of GPT Astra 6 and me, and then we got this generation. It made all these different images and kept me updated, and then it gave me the prompts of what it wanted to use. I then manually used these prompts inside Higgsfield because I didn't trust Astra there and didn't want to waste too many credits.

Keep in mind, if you do this and have "approve for me" or full access available, it might cost you a lot of credits if you go in the wrong direction. If you have money, you're good. If you don't, please don't do it. I'm not doing this either; it's risky. I always want to approve, because you will burn through tokens so quickly with this method. So I got all these prompts, created them manually inside Higgsfield, and tweaked all the different settings. This is me going back and forth before I did the final generation, and this is the whole chat; you can see how long it is. Eventually it made all these different things for me, and I imported them into my timeline and added small things like this white transition right here. But all of this is done hand in hand with Astra.

There's one more motion graphic, this pixel version of me, and I'll share how I made it because I think it's awesome for adding to your video. I uploaded an image of me, told it this is a screenshot of me and asked it to create a pixel version of me. It made three different versions using the Higgsfield MCP. Then I asked it for a Seedance 2.5 prompt, and I wanted to do this part manually again. It gave me the prompt where I described what I wanted to happen: in this case, I wanted him to walk into the frame and say "don't forget to subscribe." Now if you upload the part of your video where you want that, together with your asset, and ask it to replace, we get this cool-looking result where I walk into the frame, say "don't forget to subscribe," and jump out. So now I can use this asset over and over in all my videos.

## 3.7 Generating VFX

One of my favorite things to do with AI is making VFX. I'm going to show you how to do an effect like this. \[Demo: "So you want to learn how to do VFX? Well, let me show you. Wait, what the hell is that thing behind me? Okay, and for my next trick, let me move back a little bit. So now we're going to do this. Oopsie."\]

There are a couple of steps that go into making a video like that. First, it starts with your recording. This was my raw recording, and I already envisioned what I wanted to do. I wanted to have something there. Then I wanted some kind of magic wand; in my case it's actually a pen that I hold in my hand. And then something needed to happen at the end.

I identified three points. The first is when I look over my shoulder, so I leave a mark right here. An important thing: if you're using Premiere or DaVinci and your timeline shows normal time, in seconds, change it to the frame view. I do that with Command and clicking on this; on Windows it would probably be Control. Then you can see the exact frames. At frame 107 I leave a mark, and remember that frame for when you're prompting. The next is where the pen arrives in my hand, so I leave a mark at 279. Then I do the same when I'm clapping my hands; right here I want something to happen, like a car going through the wall. Those are the first things you need to do. Now we've identified the three points where the effects need to happen, and we'll walk through them step by step.

First we need a creature. My first version of the creature was this. I made the mistake of not making it photorealistic; after a few generations I finally landed on something like this, which looks a lot creepier and more realistic, and this ended up being the creature I wanted. The second thing to generate is the magic wand. I made a magic wand like this. Again, the prompt is simple: I describe what I want to make, what the background looks like, the lighting, the style, and I'm using Seedream 5.0 Pro for this. So now we have two of our things. The last is the car. Here I have this guy; I call him Bruiser. I wanted him in a Tesla, and Bruiser is going to run into me. This is the reference we'll use for that.

So we've created our three references. Then you can take all three, put them inside ChatGPT or Claude, add your video, and precisely describe what you want to happen per frame. As we remembered, I have frame 107, then frame 279, then frame 567. That's what we prompt. If we do that correctly, it gives you a very detailed prompt of everything that's happening precisely on the timestamp. It comes up with the timestamp, tells you exactly where each thing needs to go, and references these images. This deserves a separate video on its own, but I just want to show you what's possible. After doing that, you can look at a side-by-side and get results like this. \[Demo repeated.\]

So that's exactly how you can generate these VFX. If I went too fast, please let me know. I can make a separate video about this if you want.

## 3.8 Color grading

Moving on, I'll show you how to use Astra 6 to color grade your footage. You can do this both through ChatGPT itself and through DaVinci. Let's first do it in Astra 6. I have this footage, shot while I was in Malaysia. It's S-Log footage. I'm using the official Sony conversion LUT that I found online for my camera. I give it a simple prompt saying the uploaded MP4 file is my S-Log3 footage, and the other file is the official Sony S-Log3 to Rec.709 conversion LUT. I want to use this to color grade my MP4 using the conversion LUT, and for the deliverable, please put this in a Premiere Pro timeline so I can manually edit further if I need to. That's all I do. Then you hit send and it does everything for you.

It gave me this folder, and if we look at these side by side, you can see we now have a color-graded video. This is the super simple way. Again, sometimes this might take a while. In this case I specifically told it not to use my Premiere Pro directly, because that's the slow version. For simple tasks like these you might not have to use AI. If you have more advanced ones, I would definitely use AI, but keep in mind it can still be quite slow.

The other thing you can do is use the DaVinci MCP. If you have the premium version of DaVinci, you can ask it to color grade directly in DaVinci. It is much quicker and gives you much more customization, because DaVinci is best for color grading. You can even ask it to be creative when color grading your work.

## 3.9 Sound design

The last segment, which is also very important, is sound design. Sound design is what sells your videos. If you're doing sound design manually, you can now use AI to do it for you. There are various ways, and again, this might deserve a video on its own, because you can literally have Astra 6 control your sound design software, which is crazy in itself, but I'll show you a simple version. Remember when we had this video? I personally don't really like the sound that Seedance made for this one.

So what we can do is upload this into Astra and give it a super simple prompt: "I want you to craft a Seedance 2.5 prompt to generate an audible synchronized sound effects track for this 8-second UI animation. The reference is the video. So you need to analyze it frame by frame and understand what sound effects." Keep in mind you can do this for any type of video. In this case I used this animation, but you can also do it for an intro video; that's how we do it sometimes. Then you just ask it to make a prompt. In this case I'm having it make the prompt, because I want to save credits; if it does this in Higgsfield, I might get a version I'm not happy with, and I always want to check the prompts it's going to use.

As you can see, it wrote a super detailed prompt of the audio. Now you go through it and see if you agree. If you disagree, go back, reiterate, change a few things. Always do that with your prompts. Just don't blindly trust ChatGPT for everything, because that's how you burn a lot of money. Trust me, I've been there. If you have changes, make them. Otherwise, copy this, go into Higgsfield, upload your original track in Seedance 2.5, then paste in the prompt. Make sure you add "video one" to refer to that video. Then match the length of the video and choose your settings. You can do this on low settings; you don't need high settings, because I'll show you why.

Here's the finished result of that prompt. It sounds a bit better, but the video quality has noticeably gotten worse. So you want to download that video, separate the audio tracks, and replace the audio of the original video. Literally, you could even drop that video in there and use Wispr Flow and say something like, "I want you to replace the audio of the file I just uploaded with the original file I gave you and make it match." Then Astra does the work for you, and you'll have your original high-quality clip with the new audio you just generated.

## 3.10 Closing

All right, that's the complete guide to how you can edit your videos using AI. In particular, we're using Astra 6 as the brain of this. If you want to try this out yourself, I recommend using Higgsfield for that. I'll leave the link in the description below. If you have any questions about this video or want to see more things in depth, let me know. Lastly, click the video on the screen right now if you want to learn what else you can do with Astra 6.

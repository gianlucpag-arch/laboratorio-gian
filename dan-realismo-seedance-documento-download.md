# Dominando o realismo em vídeo com IA (Seedance 2.5 + Higgsfield) – Resumo, Prompts e Transcrição

**Vídeo:** tutorial "como dominar o realismo em IA" (título, canal e link não vieram na transcrição colada; pelas menções à comunidade gratuita e ao patrocínio do Higgsfield, parece ser do mesmo autor dos dois vídeos anteriores, mas isso não está confirmado). **Base deste material:** transcrição colada pelo usuário (0:07 até \~22:40, até a despedida).

**Nota sobre nomes:** a legenda automática erra vários nomes. Corrigi pelo contexto: "Hickfield" = **Higgsfield**; "Cance/Cense/Cedense 2.5" = **Seedance 2.5**; "Cream 5.0 Pro" = **Seedream 5.0 Pro**; "diioetic" = **diegetic (diegético)**; "cinema bars" = barras de cinema (letterbox). Um trecho da análise de ângulos de câmera ("the shoe insert and the snoram") ficou ilegível na legenda; deixei marcado. São interpretações minhas; confirme no vídeo se algum nome for crítico.

**Aviso importante:** o autor mostra os prompts na tela e os disponibiliza na comunidade gratuita dele (Skool) e em sites próprios (emoções, movimentos de câmera), mas a transcrição só traz o que ele **fala**. Os prompts da Parte 2 são trechos ditos (indicados) e reconstruções do que ele descreve. Ele não diz em voz alta quais são os símbolos exatos usados para som/diálogo.

---

# PARTE 1 – RESUMO DETALHADO EM TÓPICOS

## 1. INÍCIO – Abertura e promessa (0:07 – 2:12)

- **Abertura:** montagem cinematográfica com diálogos e falas sobre os defeitos clássicos da IA: mãos com seis dedos ("a máquina sabia como era uma mão, só não sabia contar"), rosto que derrete, personagem que não pisca, cada quadro como "um estranho imitando o anterior". A resposta: parar de alimentar o modelo com imagens planas e ensiná-lo como o mundo funciona (luz, peso, o que acontece quando algo cai).
- **Promessa:** mostrar, passo a passo, como **dominar o realismo em IA**.
- **Patrocínio:** Higgsfield, onde se pode testar o **Seedance 2.5** e as outras ferramentas do vídeo (link na descrição).

## 2. O QUE FAZ UM VÍDEO PARECER REAL (2:12 – 3:18)

- Mostra o gráfico do **vale da estranheza (uncanny valley)**: do robô ao personagem de desenho, ao humanoide estilizado, e depois uma **queda**: quando fica real/humano demais, parece "errado".
- O que a maioria ignora: imagens de IA ficam **polidas e perfeitas demais**. O estranho pode estar no movimento ou na falta de falhas, e isso gera a sensação "creepy".
- Isso também vale para humanos simétricos/perfeitos demais (piada: "achei que você era IA").
- **Tese central: realismo é imperfeição.** Precisamos pôr "realidade humana" nos prompts.

## 3. COMO CRIAR IMPERFEIÇÃO (3:18 – 7:22)

- **Depende dos modelos certos e dos prompts certos.**
- **Modelo de imagem:** as imagens da demonstração foram feitas com o **Higgsfield Soul** (não com o GPT Image 2 nem com o Seedream 5.0 Pro). Segundo o autor, o Soul foca em imagens **cinematográficas de pessoas** e, com as imperfeições, o resultado parece humano. Ele não sabe como treinaram, mas funciona (e diz que não é só pelo patrocínio). Usou um prompt curto.
- **Imperfeições que funcionam (no rosto do exemplo):** não totalmente nítido, sujeira/detalhes na jaqueta, olheiras, rugas, linha do cabelo ruim.
- **Character sheet (para vídeo):**
  1. Crie uma **character sheet** do personagem como referência.
  2. Ele normalmente usaria o **GPT Image 2**, mas percebeu que as imagens dele são **ruidosas demais** e que a cada geração a imagem piora um pouco; agora usa o **Seedream 5.0 Pro** para character sheets (até **2K**, escolhe a proporção; ele usa **16:9**). Fica um pouco mais nítido/polido, mas ele aceita.
  3. Boa vista do rosto; ele **removeu o chapéu**, porque detalhes pequenos fazem a IA perder nitidez/realismo e podem até mudar as características do personagem.
- **Gerar o frame inicial:**
  1. Subir a character sheet na caixa de prompt e adicionar o personagem original como referência extra (sem tag).
  2. Dizer "**image one is used for his identity**".
  3. Adicionar muitos detalhes de como o personagem é e as restrições: "**do not recast, do not beautify, do not use as an image background**".
  4. Descrever como quer o personagem no primeiro quadro.
  5. Toque final: **detalhes de lente**: lente de **35 mm**, abertura **1.8**, **profundidade de campo rasa**, **grão de filme fino visível**, **cores dessaturadas e apagadas**. São instruções de câmera/filme.
- **Importância da imagem:** é a base dos vídeos e economiza tempo e créditos. Se o frame inicial não for cinematográfico, ainda dá para chegar lá, mas é mais difícil. Com um prompt de vídeo em cima, sai um exemplo (um homem falando sobre ter crescido na água, o pai capitão, o porto "que avisa quando quer ser deixado em paz"; termina com a perda de um carro).
- **Realismo não é só qualidade de imagem/vídeo:** o diálogo tem papel enorme.

## 4. A IMPORTÂNCIA DO DIÁLOGO (7:22 – 13:15)

- **Contraste:** mostra um diálogo "bom" (briga intensa, ainda não perfeito) e o diálogo "médio de IA" (frases genéricas como "não aguento mais isso").
- **Prompte como um diretor.** O Seedance 2.5 entende muito melhor o que você quer ver do que os modelos anteriores.
- **Exemplo analisado – "pedido de desculpas quebrado" (plano contínuo):**
  - **Etapa 1 – quarto para a sala:** o homem e a mulher saem de um quarto escuro, instáveis, para uma sala iluminada por uma única lâmpada quente; estão sozinhos em casa.
  - **Evento principal:** param no meio da sala, próximos. Ele fala primeiro, baixo e quebrado, olhos molhados, lutando para dizer as palavras; um pedido de desculpas sem explicação real. Antes de terminar, ela o corta com rispidez, mandando parar de falar, rosto já tomado pela raiva.
  - **Estado final:** os dois juntos na sala, ele no meio da frase com olhos vidrados, ela com a mandíbula cerrada.
  - **O que o prompt contém:** a **ação**, as **palavras** a dizer, a **mudança de tom**, as **pausas** e a **emoção** em cada momento.
- **Sotaques:** não basta escrever "sotaque irlandês/jamaicano". Estrutura: **nomear o falante → região de origem → ritmo → energia → estado emocional → fala exata.** No exemplo, o personagem **Clement** fala inglês com sotaque tranquilo de **Kingston**, natural, não exagerado, não voz de comédia; quando o choque chega, a voz salta e as palavras ficam curtas. Mais detalhe sobre quem é o personagem ajuda o Seedance a imaginar a voz.
- **Símbolos no prompt:** use **símbolos/colchetes para marcar o que o personagem fala**; isso ajuda o Seedance 2.5 a entender o que é fala (volta no bloco de som).
- **Palavras de performance de atuação:** descrevem o estado do personagem. Exemplo (homem de bicicleta perseguido por um T-Rex): anda feliz, ombros soltos e sorriso largo → ouve a pegada, perde o sorriso e aperta os dedos → olha para trás devagar e relutante → congela e grita involuntariamente → pedala com força frenética e irregular → abandona a bicicleta e se esconde → cobre a boca e fica rígido, esperando os passos se afastarem → solta uma respiração trêmula. O prompt completo tem **quatro páginas**.
- **Emoção:** as palavras de ação dizem o que fazer; para mudar **como se sente**, expresse emoção, de sutil a explosiva. Pode-se descrever um **gatilho** (causa da emoção, da ação ou de algo visual). O autor criou um **site com 25 emoções** para copiar.

## 5. A ARTE DO MOVIMENTO DE CÂMERA (13:17 – 16:10)

- É subestimado: você precisa aprender o **cinema tradicional** (como a câmera se move, onde foca e como mostra o sujeito) para alcançar realismo.
- **Foco da câmera:** diga à IA no que focar (sujeito principal ou secundário). Exemplo: foco no principal, depois **rack focus deliberado** para algo atrás dele, com **gatilhos** (ex.: depois que ele rasteja, o foco muda).
- **Movimentos realistas:** crash zoom; handheld ("cru, caótico, vivo"); tracking shot ("você está lá com eles"); orbit shot; revelação. Frase-chave: **"movimento de câmera não é estilo, é emoção"**. Ele tem um **site com os prompts** de movimentos de câmera.
- **Ângulos de câmera:** diferencial de um cineasta de IA. Exemplo analisado (corrida de bicicleta contra um caminhão):
  1. **Plano de estabelecimento:** mostra o layout de três faixas e dá visão geral de onde está e do que acontece.
  2. **Foco no personagem:** enquadramentos mais fechados (detalhe do tênis e outro elemento ilegível na legenda) levam a atenção para a exaustão, o esforço e a visão em túnel.
  3. **Motivar o desespero:** alternar entre ele e o caminhão reforça a distância que diminui.
  4. **Ação legível:** planos abertos estáticos e ininterruptos da bicicleta, sem cortes que distraiam.
  5. **Escalada:** a câmera desce para **barras/rigs montados baixos** e há um sprint final agressivo.
- Escolher ângulos diferentes dá vida à cena.

## 6. SOUND DESIGN VENDE O VÍDEO (16:11 – 18:48)

- Os mesmos símbolos usados para fala servem para referenciar sons.
- **Dois tipos:** **diegéticos** (os personagens também ouvem) e **não diegéticos** (música, graves extras, efeitos que só a plateia ouve).
- **Exemplo diegético:** descrição de uma porta hidráulica suave fechando com um chiado e depois uma batida pesada de porta de aço; cada passo produz um chiado de sola de borracha seguido imediatamente por um pequeno respingo molhado sob o pé correspondente. Descreva em detalhe o som desejado.
- **Exemplo com não diegético:** usa três símbolos diferentes: colchetes normais para a **música**, outro símbolo para os **passos** e outro tipo de colchete para a **fala** dela. Exemplo de descrição: um clique elétrico agudo quando a luz morre; um **golpe de sub-grave não diegético** exatamente no frame em que a luz escurece. O personagem não ouve, mas deixa a cena mais dramática e imersiva.
- **Dificuldade:** você precisa pensar muito no que quer. Por isso **revise o prompt antes de gerar**, ou desperdiça gerações, créditos, dinheiro e tempo.

## 7. EDIÇÃO – A COISA MAIS SUBESTIMADA (18:48 – 22:27)

Se o som do Seedance não for bom o bastante, ou o clipe tiver defeitos, edite. Exemplo: clipe original com um homem pulando, câmera lenta, close no olho (fala final: "Trust your vision. Don't let the AI direct your art.").

1. **Cortar:** ele não gostou da câmera lenta dramática no pulo (tira a credibilidade). Corta no começo do pulo e pula até mais adiante; a parte lenta some e o clipe fica mais rápido. Aparar os trechos indesejados de cada plano é sempre o primeiro passo.
2. **Zoom in / zoom out:** começa com zoom in e termina com zoom out lento, revelando mais da cena. Em outra cena, dá zoom in em um olho (de **100%** no início até quase **120%** no fim) para um zoom dramático lento.
3. **Ruído (noise):** cenas de IA parecem perfeitas/plásticas. Arraste um efeito de ruído sobre o clipe e ajuste a intensidade, **só um pouco**. Pode aplicar por clipe ou no início do clipe original. **O ruído é o que mais ajuda a parecer crível.**
4. **Desfoque (blur):** aplicar um blur para suavizar as bordas, dando o ar de ter sido gravado numa câmera.
5. **Barras de cinema:** corte topo e base cerca de **10 a 15%**, para criar as barras.

- Resultado: o mesmo clipe, mais real. "Pequenos ajustes" que fazem diferença.

## 8. FIM – Encerramento (22:27 – 22:40)

- Pede comentários: qual técnica gostou mais e o que quer ver depois. Convida a clicar no vídeo da tela para ver mais sobre Seedance 2.5.

## 9. LIÇÕES PRÁTICAS

- Realismo = imperfeição: evite o polido demais (vale também para prompts de imagem).
- Comece por um **frame inicial cinematográfico** e uma **character sheet** sem objetos pequenos.
- Use **restrições de identidade** ("do not recast / beautify / use as background").
- Inclua **detalhes de lente e filme** (35 mm, f/1.8, grão, cores apagadas).
- Para diálogos: descreva ação, fala, mudança de tom, pausas e emoção; use sotaque com estrutura (nome, região, ritmo, energia, estado emocional, fala exata).
- Aprenda cinema: foco, movimento e ângulos; movimento é emoção.
- Pense em som diegético e não diegético, referenciando com símbolos.
- **Revise o prompt antes de gerar** para não desperdiçar créditos.
- Edição final: cortar, zoom lento, ruído leve, blur nas bordas, barras de cinema.

---

# PARTE 2 – PROMPTS ESTRUTURADOS PARA REPLICAR O MÉTODO

*Trechos entre aspas em inglês são falas do vídeo; o resto é reconstrução. Ajuste ao seu caso.*

## 2.1 Frame inicial com identidade travada

```
Image one is used for his identity. [Descrição detalhada do rosto, idade, cabelo, pele, marcas, roupa].
Do not recast. Do not beautify. Do not use as an image background.
Starting frame: [onde está, o que faz, expressão, luz].
Shot on a 35mm lens, aperture 1.8, shallow depth of field, visible fine film grain, muted desaturated color grade.
```

(Referências: character sheet sem chapéu/objetos pequenos + foto original do personagem como extra.)

## 2.2 Cena de diálogo (prompt de diretor)

```
Stage 1 – [local A para local B]: [quem, estado físico, iluminação, quem está presente].
Primary event: [onde param, quem fala primeiro, tom, estado emocional, o que dizem].
Interruption: [quem corta, como, reação facial].
End state: [posição dos dois, expressão final].
For each beat include: action, exact words (marked with the dialogue symbol), tone shift, pauses, emotion.
Continuous take.
```

## 2.3 Sotaque com estrutura

```
[Nome], [descrição do personagem], speaks English with an unhurried [região] accent. Natural, not exaggerated, not a comedy voice. Pace: [ritmo]. Energy: [energia]. Emotional state: [estado]. When [gatilho], the voice jumps and the words get short. Line: [fala exata entre os símbolos de diálogo].
```

(Exemplo do vídeo: Clement, sotaque tranquilo de Kingston.)

## 2.4 Palavras de performance e emoção (sequência)

```
[Estado inicial: ex. riding happily with loose shoulders and a broad smile] → [gatilho: he hears a footstep] → [reação: loses the smile, tightens his fingers] → [ação: looks behind slowly and reluctantly] → [pico: freezes, screams involuntarily] → [escalada: pedals with frantic uneven force] → [esconde-se: covers his mouth, rigidly still] → [alívio: releases one shaky breath].
```

## 2.5 Câmera

```
Focus: start on [sujeito principal]; after [gatilho, ex.: he crawls], deliberate rack focus to [objeto/sujeito atrás].
Movement: [crash zoom / handheld raw / tracking / orbit / reveal] – purpose: [emoção].
Angles: establishing shot of [layout]; tighter framing on [detalhes] to show [exaustão/visão em túnel]; alternate between [personagem] and [ameaça] to show the widening gap; uninterrupted static wide shots for [ação] with no distracting cuts; low-mounted camera for the final sprint.
```

## 2.6 Som

```
[Diegetic] – [descrição precisa: ex. soft hydraulic door closing with a hiss, then a heavy steel door slam; each step: one closed rubber sole squeak followed by one small wet splash beneath that foot].
[Non-diegetic] – [música / graves]: e.g. a sharp electrical buzz click as the light dies; a hard non-diegetic sub-bass hit on the exact frame the light goes dark.
Dialogue: [fala entre os símbolos de diálogo].
```

(Use símbolos diferentes para música, passos/efeitos e fala; veja os símbolos exatos nos prompts da comunidade do autor.)

## 2.7 Checklist de pós-produção

- [ ] Cortar partes lentas/desnecessárias de cada plano.
- [ ] Keyframes de zoom lento (ex.: 100% → \~120%).
- [ ] Ruído leve (o que mais ajuda) e blur nas bordas.
- [ ] Barras de cinema: cerca de 10 a 15% topo e base.
- [ ] Revisar o prompt antes de gerar para não desperdiçar créditos.

---

# PARTE 3 – TRANSCRIÇÃO LIMPA POR ASSUNTO

*(Mantida em inglês, no idioma do vídeo. Retirei vícios de fala, repetições e erros óbvios de legenda; nomes corrigidos pelo contexto. Sem cortar conteúdo. Falas de personagens do vídeo aparecem entre colchetes ou aspas.)*

## 3.1 Intro

&#91;Montage dialogue, lightly cleaned:\] "Should I be writing any of this down?" "No." "Wait, does that guy have six fingers?" The machine knew what a hand looked like. It just had no idea how to count. So why not fix it? ... "Her face keeps melting. She isn't blinking." Every frame is a stranger doing an impression of the last one. "And you fixed that." We stopped feeding it flat pictures. We started teaching it how the world actually works. Light. Weight. What happens when something falls? ... "There's no glass." You only need glass for the things that break when you look too close. "Is he real?" "Are you asking me or her?"

Now, in this video, I will show you step by step how to master AI realism. This video is sponsored by Higgsfield, so if you want to follow along, make sure to click the link in the description below so you can try out Seedance 2.5 for yourself, along with all of the other tools we will be using in this video.

## 3.2 What makes a video realistic?

The first thing we need to get straight is what actually makes a video look realistic, and in particular what makes an AI video feel real or fake. To explain this, take a look at this graph. This is called the uncanny valley. In summary, it explains why sometimes something feels off. We can see it goes from a robot to a cartoon character to a stylized humanoid, and then there's a dip. That's the uncanny valley. When it's too real, too human, it feels off. It needs to have that human element in it.

That is the thing most people overlook when making AI images, because it's too polished. It's too perfect, and that's when you miss that spot. It can be the movement, it can be the flaws; it just starts to feel strange and creepy. That is what a lot of people have with AI. So to avoid that, we need to get that human realness into our prompts. The uncanny valley doesn't just apply to AI. It also applies to humans who look too symmetrical or too perfect. \["I thought you were AI."\] Because realism is imperfection, and that's what we're going to create.

## 3.3 How to create imperfection

So how do we create that imperfection? It is all about using the right models and the correct prompts. Let me first talk about the models. Take a look at these images. All of these were generated with the same model. Can you guess which model I used? It's not GPT Image 2 and it's not Seedream 5.0 Pro. This was created using Higgsfield Soul, and not because this video was sponsored by Higgsfield. It's because this model really focuses on creating cinematic images of people, and it does super well at that. I don't know what they trained it with, but with all the imperfections these people have, it starts to look human.

This was made with a short prompt. I'll go into detail about the prompts later, and you can find all the prompts I used in my free Skool community, where you can copy them and check them out at your own pace. That gave me this result: we have all the imperfections on this guy's face. It's not fully sharp. There's a bit of stuff on his jacket. He has bags under his eyes. He has wrinkles. He doesn't have the best hairline. Neither do I. But that is what makes us human.

If you want to generate a video, I recommend creating a character sheet of your character, which we'll use as a reference. Now we have to retype our prompt. For that I'm using a pretty simple prompt, which I'll also share in the asset file. Normally I would create this with GPT Image 2. But while doing my research and looking at all the images I generated, I can by now tell when an image is generated using GPT Image 2, because it is way too noisy, and especially with image and video generation, each time the image gets slightly worse, in my opinion. I'm now using Seedream 5.0 Pro when I generate these character sheets. You can do this in up to 2K and choose the aspect ratio; I'm going with 16:9. Then you generate. This looks a little sharper and a little more polished, but I don't mind. We have a good close-up of his face. I've removed the hat here. The reason is that this is a small hat, and you don't want the AI to use such small details when it makes videos, because then it's not going to look sharp, it's not going to look real, and it might even change the characteristics of your character.

Now that we have our character sheet, we upload it in the prompt box again. Then I also add my original character, just so I have an extra reference of him. I'm not going to tag it; I just add it. And I say image one is used for his identity. Then I add a bunch of details of what this guy looks like, plus: do not recast, do not beautify, do not use as an image background. Then we describe what we want him to look like in our first starting frame. The final touch is adding the lens details. Here I'm saying it's shot on a 35 mm lens, aperture of 1.8, shallow depth of field, visible fine film grain, muted desaturated color grade. These are film or camera instructions; more on that later. Then you hit generate and you have your first image. This is what's needed as the baseline for your videos.

Don't underestimate your images, because this is where you can save so much time and credits to get your character to look cinematic. If your starting frame or reference doesn't look cinematic, you can still achieve cinematic, realistic videos, but it's going to be a little bit harder. So put some real effort into this. Because if I now add a video prompt, we get something like this: \[clip\] "I grew up on this water. You learned the weather before you learned the roads. My father was a captain. He used to say, 'The harbor tells you when it wants to be left alone.' And when he came home, he would."

So yeah, rest in peace that car. The thing about videos like these is that it's not just the image quality or the video quality that makes the video real.

## 3.4 The importance of dialogue

The thing that plays a huge role here is the dialogue. Here's an example of what good dialogue will do to your AI generation. \[Clip: "I'm sorry. I don't... I don't know what to say." "Stop. Just stop talking." "I'll talk if I want." ... "Leave alone." "Why would you stop it?" "Leave me alone." "Why?" "Because I love you."\] This is still not perfect, but for contrast, here's what the average AI generation looks like in terms of dialogue: \["I can't keep doing this anymore. You know, I love you more than anything."\]

So how do we achieve good dialogue? The first thing you need to learn is how to prompt like a director. Especially now with Seedance 2.5, it is so much better at understanding what you want to see on the screen than previous models. Let's analyze the first example. It starts with a broken apology. It is a continuous take. If we look at the prompt, in the first stage we have the bedroom to the living room. For the apology, we describe with a lot of different words what we want to see. The man and the woman are walking out of a dim bedroom together, both unsteady on their feet, into the open living room lit by a single warm lamp. They are alone in the house. No one else is present. Then the primary event: they stop in the middle of the living room, close to each other. The man speaks first, quiet and broken, eyes wet, struggling to get the words out; an apology with no real explanation behind it. Before he can finish, the woman cuts him off sharply, telling him to stop talking, her face already tight with anger. The end state of this scene is that the two are close together in the living room, him mid-sentence and glassy-eyed, her jaw clenched, having just cut him off.

That is explaining to the actor what you want to see on the screen. It includes the action, the words they need to say, the shift in tone, but also the pauses they need to add, and lastly the emotion at these moments. Seedance 2.5 does a phenomenal job of understanding how that scene plays out. So you just need to find the words to throw at the AI to help it act out your scene.

But those are not the only ways to improve your dialogue. Another thing you can do is add an accent. You don't just want to write "add an Irish accent" or "a Jamaican accent." That's not going to give you a result like this: \[clip: "See how quiet it stay? I tell you already. Nothing out here. Just bird. Wait, wait... You seeing this?"\] To achieve something like that, you first want to name the speaker. Then you include the region they're from, the pace, the energy, the emotional state, and then their exact line.

To achieve that accent, I first described who my main character is, then described what his accent is. I named him Clement. He speaks English with an unhurried Kingston accent: natural, not exaggerated, not a comedy voice; when the shock hits, the voice jumps and the words get short. Because I added more detail about who this guy is, Seedance has a good idea of what he might sound like. One very important thing in your prompt structure: you can use symbols to point out what this person is saying. For dialogue you use these brackets, which help Seedance 2.5 understand that that is text your character needs to say. More on that later when we get to sound.

There's just so much more about dialogue I have to tell you, because, for example, you also have acting performance words. These are simply words that describe the state of being of your character in terms of how he has to act. For example, I have this image of a guy being chased by a T-Rex. Then we can use the action and performance words. We can say he's riding happily with loose shoulders and a broad smile. Then, here's the footstep: he loses the smile and tightens his fingers. Then he looks behind slowly and reluctantly. He freezes and screams involuntarily. Then he pedals with frantic, uneven force. He leaves the bicycle behind and hides. Lastly, he's covering his mouth and remaining rigidly still, waiting for the footsteps to recede. And then he releases one shaky breath. If we generate that, we get a result like this. \[Clip.\]

I do want to note that this is a four-page prompt, and everything I just said is included in it, in terms of the action words that describe what's going on. So if you want to go through this yourself, please do, because it gives you a good understanding of how to prompt for something like this.

Now, the action words describe what your character needs to do. Now let's change how they feel. For that we need to express emotion. We can do various emotions, from subtle to explosive. You can also describe a certain trigger that causes an emotion, an action, or even a visual. If you want to know how to prompt for your own emotions, I've created this website for you with 25 different emotions you can use right away; you can just copy them.

## 3.5 The art of camera movement

When it comes to directing, it's not just directing the actors on how to speak and perform. It's also about the camera work, and that is something that's hugely underrated and that you need to understand. You literally have to learn traditional filmmaking, because if you want to achieve true realism you need to know how the camera moves, what the camera focuses on, and how it shows its subject. Let me break down all three.

First, camera focus. Here, you need to describe to the AI what to focus on: is it your main subject or your secondary subject? Be intentional about where you want the camera to focus. Here we have our main subject, and then we perform a deliberate rack focus onto the thing behind our subject, and we also set up triggers. For example, in this case, after he crawls, we see the focus change.

The next thing you need is realistic camera movement. This is a crash zoom. Handheld: raw, chaotic, alive. Tracking shot: you're right there with them. Orbit shot: the reveal, the moment that changes everything. Camera movement isn't style. It's emotion. If you want to learn how to prompt realistic camera movements, take a look at this website I created earlier where I share all the prompts I've used for realistic camera movement.

Another thing that will set you apart as an AI filmmaker is knowing how to create good camera angles. \[Clip: a bike chase, "Hey, stop."\] Let's break down that shot. We start with an establishing shot. This establishes the three-lane layout. Immediately you have a great overview of where I am, what I am running on, and what's going on. Then we focus on the character. We keep tighter framing, like the shoe insert \[and another detail unclear in the captions\], which shifts the focus from the street to my exhaustion, strain and tunnel vision. Then I motivate the desperation by alternating between myself and the truck, which reinforces the widening gap. Then we keep the action readable: we use uninterrupted static wide shots for the bike as I tackle that, and we don't introduce distracting cuts. Then it all escalates: the camera drops to low-mounted camera bar rigs and there's a final sprint that is very aggressive. Choosing those different camera angles brings the scene to life. That's what you also have to think about when you have something in your head.

## 3.6 Sound design sells your video

The final layer that brings everything together is sound. I've already shown you the symbols you can use to reference your sounds. But how does it actually work, and how do you prompt it? Let me show you. There are two things you can do. You can focus on diegetic sounds, which are sounds the characters also hear. And you can focus on non-diegetic sounds: things like music, extra bass or extra sound effects that your characters won't necessarily hear, but the audience will hear when watching your movie.

Here's an example of diegetic sound. \[Clip: "Don't come up. I'm already leaving."\] For that example we focused on these symbols. We added them in there and described what's going on. We have a soft hydraulic door closing with a hiss, then a heavy steel door slam. Then each step produces one closed rubber sole squeak followed immediately by one small wet splash beneath the corresponding foot. We describe in great detail how we want that sound.

Here is another example where we also use non-diegetic sounds. \[Clip: "Stop following me."\] In this prompt we've used all three of these different symbols. We used the normal brackets for the music. Then we used the other symbol, I don't know what to call it, for the footsteps. And then we used a different bracket symbol for what she's saying. If you analyze this, it's something you can do in your prompt. You say: we have a sharp electrical buzz click as the light dies. Then we have a hard non-diegetic sub-bass hit that lands on the exact frame the light goes dark. If we listen to that again, that's added bass, added sound the character won't necessarily hear, but it makes it more dramatic for you, so you're pulled into the moment and dragged into this movie.

The great thing about this, but also the really difficult part, is that you really have to think about what you want in your generation. That's why I always tell you to go through your prompt before you hit generate. Otherwise you're just wasting generations, credits, money and time.

## 3.7 The most underrated thing: editing

If the sound effects from Seedance aren't good enough, you can also do the next thing, which is editing. I have this example to share. Let's take a look at the original clip. \[Clip: "Trust your vision. Don't let the AI direct your art."\]

For me that clip was quite good. I just didn't like a few things. The first was the slow motion of this guy jumping down; that makes it unbelievable to me. The first thing I always do is trim up my clip in terms of each shot that has been used. Let's talk first about the segment with the slow motion. We don't need this dramatic slow motion. What we can do is make a cut right about here, where we see this guy jumping off, and then go up until this point, so that part is entirely removed. Now if we play this together, it's a lot faster. That's what I like. That's the first thing I do: trim up the parts I don't want.

The second thing I do is add zoom in and zoom out. Here I started off by zooming in. If we turn this off, we can see the original clip; I zoomed in a little bit, and at the end I zoomed out. If we play this, you can see it slowly zooming out, which reveals more of the scene. For the next scene I zoom in a little because I wanted to be more dramatically focused on that eye. At the beginning I keep it at 100, then near the end I take it to almost 120. That gives a slow, dramatic zoom-in and really draws your attention to that eye.

Once you've added all your zoom-ins and zoom-outs, there are a few additional things you can do. With a lot of these AI scenes, it seems a bit too perfect, too plastic almost. What you can do is add an effect, and for this one we add a bit of noise. Drag a bit of noise onto your clip, and you can change and play around with the intensity until you get something you like. I wouldn't overdo it, just a little bit to make sure your scene looks more realistic. You can adjust that for each clip, or add it at the beginning of your original clip.

The second thing you can do is add a blur over your scene, which lets you blur the edges a little. By doing so, it becomes a bit more like it was shot on a camera.

The last thing you can do is add some cinema bars. For example, if you crop the top, you can adjust this and play around with it. I would do 10 to 15%. Once you've done that for both the top and the bottom, you have these cinema bars. \[Clip: "Trust your vision. Don't let the AI direct your art."\]

Those are small little tweaks you can do to make your video look more real. Especially the noise plays a huge part in making it look more believable.

## 3.8 Closing

If this was useful to you, please leave a comment below and tell me which feature or technique I showed you that you liked the most. Also let me know what you want me to show next. Make sure to click the video on the screen right now if you want to see more videos about Seedance 2.5.

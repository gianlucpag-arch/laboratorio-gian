from pathlib import Path
import hashlib, json, zipfile, re

root=Path.cwd()
skill=root/'skills/criar-videos-ia'
refs=skill/'references'
sources=refs/'fontes'
inputs=[
('C:/Users/Ggian/.codex/attachments/d7c33e24-89a9-4ced-b0e1-5d1d0c9bcf30/Texto colado.txt','dan-comerciais-transcricao.txt'),
('C:/Users/Ggian/.codex/attachments/9cdee276-b17b-43d4-930c-93e74a426e88/Texto colado.txt','dan-comerciais-resumo-templates.txt'),
('C:/Users/Ggian/.codex/attachments/9b778a4d-f28f-440d-8fe9-cd13d18e8c6a/Texto colado.txt','dan-comerciais-analise-recebida.txt'),
('C:/Users/Ggian/Downloads/Como fazer um comercial de futebol 100_ com IA (Higgsfield + Seedance) – Resumo, Prompts e Transcrição.md','dan-comerciais-resumo-prompts-transcricao.md')]
manifest=[]
for source,name in inputs:
    data=Path(source).read_bytes()
    (sources/name).write_bytes(data)
    manifest.append(dict(source=source,stored_as=name,sha256=hashlib.sha256(data).hexdigest().upper(),bytes=len(data)))
(sources/'dan-comerciais-manifesto.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert len({r['sha256'] for r in manifest})==4
def append(path,text):
    path.write_text(path.read_text(encoding='utf-8-sig')+'\n\n'+text.strip()+'\n',encoding='utf-8')
entry=skill/'SKILL.md'
text=entry.read_text(encoding='utf-8-sig')
anchor='- Para incorporar informações, resultados ou novas aulas, seguir'
assert anchor in text
entry.write_text(text.replace(anchor,'- Para comerciais com arco narrativo, versões de idade, banco de referências e escolha entre start frame, referências e storyboard, ler [comerciais cinematográficos](references/dan-comerciais-cinematograficos.md). Confere quatro documentos até 16:17, com correções dos resumos e adaptação ao Turrico.\n'+anchor),encoding='utf-8')
update='''## Atualização de 18/10/2026 — comerciais cinematográficos

Lidos integralmente quatro documentos distintos da aula identificada como How To Create Cinematic AI Ads – Full AI Video Course: transcrição timestampada até 16:17, resumo/templates, análise extensa e Markdown com resumo, prompts e transcrição limpa. Originais preservados com manifesto de origem e hashes. A análise extensa declara reconstrução; suas observações visuais são relatos recebidos, não visionamento próprio. Consultar [estudo de comerciais](dan-comerciais-cinematograficos.md) para cronologia completa e conferência.

Correções principais: nove vistas de locação geradas e quatro selecionadas; três técnicas principais, sendo start frame + sheet uma variante das referências; Seedance 2/2 fast no contexto da fala, sem converter para 2.5; referências não garantem identidade. Prompts ampliados, alegações de exatidão e detalhes visuais dos resumos estão separados da fala timestampada. Assets de comunidade e prompts integrais de tela não foram recuperados.

A base passa a reunir nove aulas com textos fornecidos e 31 conteúdos originais distintos, além dos manifestos e da página de recursos musicais já incluída. Nenhuma ferramenta foi instalada, nenhum crédito gasto e nenhuma mídia foi gerada ou editada nesta incorporação. O estudo é dos materiais fornecidos; não representa visionamento integral nem estudo de todo o canal.
'''
append(refs/'evidencias.md',update)
append(root/'DAN_KIEFT_ESTUDO_APLICADO_TURRICO.md',update.replace('(dan-comerciais-cinematograficos.md)','(skills/criar-videos-ia/references/dan-comerciais-cinematograficos.md)'))
(refs/'estudo-dan-kieft.md').write_text((root/'DAN_KIEFT_ESTUDO_APLICADO_TURRICO.md').read_text(encoding='utf-8').replace('(skills/criar-videos-ia/references/dan-comerciais-cinematograficos.md)','(dan-comerciais-cinematograficos.md)'),encoding='utf-8')
append(refs/'producao.md','''## Comerciais e campanhas por referências

Consultar [comerciais cinematográficos](dan-comerciais-cinematograficos.md). Dar a cada plano uma função narrativa e definir versões necessárias de personagem/figurino, local e objeto. Corrigir referências a montante e evitar misturar versões antigas com a atual. Moodboard explora direção visual; storyboard planeja sequência. Um banco de assets pode guardar imagem, prompt, papel da entrada e versão sem exigir uma ferramenta específica.

Escolher início composto para composição inicial específica; referências para identidade/mundo; combinação dos dois se suportada; storyboard para sequência planejada. Confirmar o papel real de cada upload. Uma imagem aproximada que não deve fixar o começo precisa ser atribuída ao papel adequado, não chamada de start frame obrigatório e opcional ao mesmo tempo. Avaliar continuidade durante todo o movimento. Vistas Multi-shot são propostas sujeitas a revisão espacial. Produto, idades e coadjuvantes precisam de referências quando necessários; não impor o exemplo de nove vistas, oito planos ou quatro fases de idade como mínimo.
''')
append(refs/'turrico.md','''## Adaptação de comerciais cinematográficos

Aplicar o planejamento por função de cena, continuidade de objetos e banco de referências à identidade já aprovada. Desejo, tentativa e virada podem organizar uma cena cômica sem transformar o Turrico em atleta humano ou impor superação. Não incorporar Nike, celebridades, infância, uniformes ou corpo inteiro dos exemplos ao cânone. Para elenco múltiplo, conferir associação de referência e impedir troca de roupa/traços. Se houver produto, revisar legibilidade e interação física e preservar a pausa da reação antes da conclusão.
''')
guide=root/'chatgpt-turrico/00_GUIA_CRIACAO_VIDEO_IA_TURRICO.txt'
append(guide,update.replace('[estudo de comerciais](dan-comerciais-cinematograficos.md)','documento dan-comerciais-cinematograficos.md incorporado à base')+'''
Usar a aula para planejamento de anúncio, evolução temporal quando necessária, banco de referências e seleção da técnica por plano. Não transformar modelos e custos relatados em ranking atual nem templates secundários em prompts literais do autor. O plugin e a comunidade são opções históricas; a incorporação documental não os instala ou acessa.
''')
order=['evidencias.md','producao.md','turrico.md','atualizacao.md','prompts-turrico.md','banco-criativo-higgsfield.md','pesquisa-documental.md','estudo-dan-kieft.md','dan-imagens-cinematograficas.md','dan-elevenlabs-voz.md','dan-filmmaking-avancado.md','dan-influenciador-consistente.md','dan-comparacao-geradores.md','dan-edicao-video-ia.md','dan-realismo-seedance.md','dan-camera-biblioteca.md','dan-emocoes-direcao.md','dan-videoclipe-suno.md','dan-comerciais-cinematograficos.md']
parts=['# BASE DE CONHECIMENTO — VÍDEOS COM IA / TURRICO\n\nAtualização: 18/10/2026 — nove aulas com textos fornecidos, página de recursos musicais e 31 conteúdos originais distintos preservados, além de manifestos. Atualizações de evidência prevalecem sobre registros históricos. Nenhum visionamento integral ou teste de mídia próprio foi realizado nestas incorporações.\n']
for name in order:
    parts.append('\n----- DOCUMENTO: '+name+' -----\n\n'+(refs/name).read_text(encoding='utf-8-sig'))
for path in sorted(sources.iterdir(),key=lambda p:p.name):
    if path.is_file(): parts.append('\n----- DOCUMENTO: fontes/'+path.name+' -----\n\n'+path.read_text(encoding='utf-8-sig'))
package=root/'chatgpt-turrico'
bundle=package/'BASE_CONHECIMENTO_VIDEO_IA_TURRICO.txt'
bundle.write_text('\n'.join(parts),encoding='utf-8')
names=['00_GUIA_CRIACAO_VIDEO_IA_TURRICO.txt','BASE_CONHECIMENTO_VIDEO_IA_TURRICO.txt','CATALOGO_HIGGSFIELD_2026-10-18.json']
with zipfile.ZipFile(package/'TURRICO_MATERIAIS_CHATGPT.zip','w',zipfile.ZIP_DEFLATED) as z:
    for name in names: z.write(package/name,name)
for row in manifest:
    assert Path(row['source']).read_bytes()==(sources/row['stored_as']).read_bytes()
raw=[p for p in sources.iterdir() if p.suffix in ('.txt','.md')]
assert len(raw)==31,len(raw)
merged=bundle.read_text(encoding='utf-8')
for path in raw: assert path.read_text(encoding='utf-8-sig') in merged,path.name
for path in [entry]+[refs/n for n in order]:
    for link in re.findall(r'\]\(([^)]+)\)',path.read_text(encoding='utf-8')):
        if not re.match(r'^[a-z]+:',link) and not link.startswith(('#','/')):
            assert (path.parent/link.split('#')[0]).exists(),(path.name,link)
assert entry.read_text(encoding='utf-8').startswith('---\nname: criar-videos-ia\ndescription:')
with zipfile.ZipFile(package/'TURRICO_MATERIAIS_CHATGPT.zip') as z:
    assert z.namelist()==names and z.testzip() is None
print('Verificado: 4 novos documentos distintos, 31 originais completos, links válidos e ZIP íntegro.')

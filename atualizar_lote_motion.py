from pathlib import Path
import hashlib, json, zipfile, re
root=Path.cwd()
skill=root/'skills/criar-videos-ia'
refs=skill/'references'
sources=refs/'fontes'
inputs=[
('C:/Users/Ggian/.codex/attachments/9e662476-7167-4b9c-a602-32e05e40410b/Texto colado.txt','motion-control-transcricao.txt'),
('C:/Users/Ggian/.codex/attachments/d17996b8-bd20-4b6c-8d28-5c20add11a3e/Texto colado.txt','motion-control-analise-recebida.txt'),
('C:/Users/Ggian/.codex/attachments/50c585e8-2db6-47d1-b5ef-599f20d9c75e/Texto colado.txt','motion-control-resumo-templates.txt'),
('C:/Users/Ggian/Downloads/Influenciadores bizarros de IA motion control de graça (Higgsfield x Google Flow) – Resumo, Prompts e Transcrição.md','motion-control-resumo-prompts-transcricao.md')]
manifest=[]
for source,name in inputs:
    data=Path(source).read_bytes()
    (sources/name).write_bytes(data)
    manifest.append(dict(source=source,stored_as=name,sha256=hashlib.sha256(data).hexdigest().upper(),bytes=len(data)))
(sources/'motion-control-manifesto.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert len({r['sha256'] for r in manifest})==4
def append(path,text):
    path.write_text(path.read_text(encoding='utf-8-sig')+'\n\n'+text.strip()+'\n',encoding='utf-8')
entry=skill/'SKILL.md'
text=entry.read_text(encoding='utf-8-sig')
anchor='- Para incorporar informações, resultados ou novas aulas, seguir'
assert anchor in text
entry.write_text(text.replace(anchor,'- Para substituir sujeitos por personagem, preparar pose, referências de movimento/identidade/cena e montar segmentos, ler [motion control e influenciadores](references/motion-control-influenciadores.md). Confere quatro textos até 14:26, autoria/modelo incertos e limites das alegações de gratuidade.\n'+anchor),encoding='utf-8')
update='''## Atualização de 18/10/2026 — motion control e influenciadores

Lidos integralmente quatro documentos distintos, incluindo transcrição timestampada até 14:26, análise extensa, resumo/templates e Markdown com transcrição limpa. Originais completos e manifesto de hashes preservados. O novo estudo está em motion-control-influenciadores.md. Não é atribuído a Dan Kieft: os anexos divergem entre Porão da IA e Virto/@virto-ia. Também divergem sobre Veo/Omni 1.1 Flash; a fala identifica Flow e menciona Omni, sem confirmar modelo/versão.

Incorporadas preparação de pose, separação entre vídeo de movimento, folha de identidade e referência de cena, substituição com escopo explícito e revisão de emendas. A gratuidade, os preços, créditos, contratos, receitas e equivalência de qualidade permanecem relatos não verificados; o teste descrito usa conta Pro e reconhece cortes visíveis. Os templates são reconstruções/adaptações, não prompts integrais originais recuperados.

A base reúne agora dez aulas com textos fornecidos (nove anteriormente identificadas como Dan Kieft e esta com autoria divergente) e 35 documentos originais distintos, além de manifestos e materiais complementares. Nenhum visionamento integral ou teste próprio de mídia foi executado nesta incorporação. Não foram criadas contas, contratados planos ou alterados serviços.
'''
append(refs/'evidencias.md',update)
append(root/'DAN_KIEFT_ESTUDO_APLICADO_TURRICO.md',update+'\nEste é um complemento de outra fonte ao acervo; não constitui décima aula de Dan Kieft. Consultar skills/criar-videos-ia/references/motion-control-influenciadores.md.')
(refs/'estudo-dan-kieft.md').write_text((root/'DAN_KIEFT_ESTUDO_APLICADO_TURRICO.md').read_text(encoding='utf-8'),encoding='utf-8')
append(refs/'producao.md','''## Motion control por substituição

Consultar [substituição e referências de movimento](motion-control-influenciadores.md). Nomear a ferramenta real e separar vídeo para movimento/timing, imagem para identidade e referência de cena para composição/coadjuvantes. Explicitar mudanças adicionais para não pedir simultaneamente fundo imutável e novo cenário. Pose/orientação compatíveis ajudam na preparação; não presumir que toda imagem entra como start frame.

Verificar apoio dos pés, equilíbrio, mãos, oclusões, câmera e identidade ao longo do movimento. Segmentar conforme limite real do modo, registrar timecodes e comparar pose, direção, aparência e áudio nas emendas. Não prometer plano contínuo por simples junção. Avaliar custo por clipe aprovado, distinguindo quota promocional, assinatura, upscale e exportação nativa. Comparação estética do narrador não é benchmark próprio.
''')
append(refs/'turrico.md','''## Motion control adaptado ao personagem

Transferir intenção, ritmo e gestos compatíveis com anatomia estilizada mantendo a referência aprovada. Não converter em humano realista nem adotar Vegeta, Bulma, Johnny Bravo ou estética bizarra dos exemplos. Não considerar uma pose humana como aprovação do corpo inteiro do Turrico. Separar identidade de cada coadjuvante e preservar a reação e a pausa cômica. Controle de movimento não aprova voz ou sincronização labial automaticamente.
''')
append(root/'chatgpt-turrico/00_GUIA_CRIACAO_VIDEO_IA_TURRICO.txt',update+'\nConsultar o documento motion-control-influenciadores.md dentro da base. A rotina usa a quota legítima disponível e confirma entradas e limites antes de executar; a fala sobre contas revendidas e múltiplos e-mails foi preservada como fonte, sem virar procedimento. Contratos e brief não foram fornecidos, portanto suas condições não foram confirmadas.')
order=['evidencias.md','producao.md','turrico.md','atualizacao.md','prompts-turrico.md','banco-criativo-higgsfield.md','pesquisa-documental.md','estudo-dan-kieft.md','dan-imagens-cinematograficas.md','dan-elevenlabs-voz.md','dan-filmmaking-avancado.md','dan-influenciador-consistente.md','dan-comparacao-geradores.md','dan-edicao-video-ia.md','dan-realismo-seedance.md','dan-camera-biblioteca.md','dan-emocoes-direcao.md','dan-videoclipe-suno.md','dan-comerciais-cinematograficos.md','motion-control-influenciadores.md']
parts=['# BASE DE CONHECIMENTO — VÍDEOS COM IA / TURRICO\n\nAtualização: 18/10/2026 — dez aulas com textos fornecidos, sendo nove identificadas como Dan Kieft e uma de autoria divergente nos anexos; 35 documentos originais distintos e materiais complementares. Atualizações de evidência prevalecem sobre registros históricos. Nenhum visionamento integral ou teste de mídia próprio foi realizado nestas incorporações.\n']
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
    data=(sources/row['stored_as']).read_bytes()
    assert data==Path(row['source']).read_bytes() and hashlib.sha256(data).hexdigest().upper()==row['sha256']
raw=[p for p in sources.iterdir() if p.suffix in ('.txt','.md')]
assert len(raw)==35,len(raw)
merged=bundle.read_text(encoding='utf-8')
for path in raw: assert path.read_text(encoding='utf-8-sig') in merged,path.name
for path in [entry]+[refs/n for n in order]:
    for link in re.findall(r'\]\(([^)]+)\)',path.read_text(encoding='utf-8')):
        if not re.match(r'^[a-z]+:',link) and not link.startswith(('#','/')):
            assert (path.parent/link.split('#')[0]).exists(),(path.name,link)
assert entry.read_text(encoding='utf-8').startswith('---\nname: criar-videos-ia\ndescription:')
with zipfile.ZipFile(package/'TURRICO_MATERIAIS_CHATGPT.zip') as z:
    assert z.namelist()==names and z.testzip() is None
print('Validado: 4 novos documentos distintos, 35 originais completos, navegação local e ZIP íntegros.')

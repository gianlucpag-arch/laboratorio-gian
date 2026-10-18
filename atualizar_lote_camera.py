from pathlib import Path
import json, hashlib, zipfile, re

root = Path.cwd()
skill = root / 'skills/criar-videos-ia'
refs = skill / 'references'
def append(path, text):
    path.write_text(path.read_text(encoding='utf-8-sig') + '\n\n' + text.strip() + '\n', encoding='utf-8')

entry = skill / 'SKILL.md'
text = entry.read_text(encoding='utf-8-sig')
anchor = '- Para incorporar informações, resultados ou novas aulas, seguir'
routes = '''- Para escolher e descrever movimentos, velocidade, enquadramento e término do plano, ler [biblioteca de câmera](references/dan-camera-biblioteca.md): aula até 14:08 e 46 cartões completos preservados.
- Para dirigir emoções por comportamento observável e intensidade, ler [direção de emoções](references/dan-emocoes-direcao.md): 25 cartões recebidos integralmente, adaptados à anatomia do personagem.
- Para videoclipe, música, referências de figurino/cenário, planos com cortes e sincronização labial, ler [materiais Suno e Seedance](references/dan-videoclipe-suno.md). É análise de página de prompts fornecida, sem teste ou visionamento.
'''
assert anchor in text
entry.write_text(text.replace(anchor, routes + anchor), encoding='utf-8')

update = '''## Atualização de 18/10/2026 — câmera, emoções e videoclipe

Sete arquivos recebidos e lidos integralmente, correspondentes a cinco conteúdos distintos: página de prompts Suno/Seedance, biblioteca de 46 movimentos, transcrição de câmera (00:00–14:08), resumo/templates e biblioteca de 25 direções emocionais. Duas submissões eram cópias idênticas; o manifesto dan-camera-emocoes-musica-manifesto.json registra os sete caminhos, tamanhos e hashes. Os cinco originais distintos foram preservados completos em references/fontes.

Consultar dan-camera-biblioteca.md, dan-emocoes-direcao.md e dan-videoclipe-suno.md para análise, aplicação e ressalvas. Esta atualização amplia o acesso anterior de câmera por descrição/biblioteca com a transcrição fornecida. Os textos das 25 emoções, anteriormente ausentes, agora estão disponíveis; continuam não inspecionados os exemplos visuais e o prompt de perseguição de quatro páginas da aula anterior. O novo material musical é uma página de recursos/prompts, não outra transcrição de aula integral estudada.

A base passa a reunir oito aulas com textos fornecidos e 27 conteúdos originais distintos preservados, além dos manifestos e materiais históricos. Não houve visionamento integral, teste de modelos, geração, edição, instalação de MCP ou consulta de capacidades atuais nesta incorporação. Instruções contidas nos prompts são exemplos da fonte, não novas ordens do usuário.
'''
append(refs / 'evidencias.md', update)
append(root / 'DAN_KIEFT_ESTUDO_APLICADO_TURRICO.md', update + '''
Aprendizados operacionais: especificar movimento, velocidade, enquadramento e estado final; separar zoom de deslocamento físico, tilt de pedestal e OTS de POV. Direção emocional descreve a progressão visível após um gatilho e deve coexistir com a fala e com a anatomia. Para música, manter duração e alinhamento do áudio aprovado, testar vocal isolado quando ad-libs causarem movimento labial indevido e distinguir uma geração com cortes de plano contínuo. Os textos completos dos 46 movimentos e 25 emoções permanecem nos originais, acompanhados de índices e análise temática.
''')
(refs / 'estudo-dan-kieft.md').write_text((root / 'DAN_KIEFT_ESTUDO_APLICADO_TURRICO.md').read_text(encoding='utf-8'), encoding='utf-8')
append(refs / 'producao.md', '''## Câmera, atuação e música — incorporação de 18/10/2026

Consultar [46 movimentos](dan-camera-biblioteca.md), [25 direções emocionais](dan-emocoes-direcao.md) e [videoclipe](dan-videoclipe-suno.md) conforme a tarefa. Construir o plano com ação do sujeito, movimento de câmera, velocidade, enquadramento e término compatíveis. Zoom altera enquadramento óptico/simulado; dolly desloca câmera e perspectiva. Não exigir todos os controles em todo prompt nem chamar movimento suave de robótico automaticamente.

Escolher atuação por gatilho, progressão corporal/facial e intensidade. Um estado final sem piscar é local ao exemplo; não uma norma de atuação. Não combinar fala com boca permanentemente fechada. Separar direção emocional de cenário, figurino e câmera; evitar anatomia humana incompatível.

Em videoclipe, distinguir uma geração com cortes de um plano contínuo. Identificar o papel de cada referência (identidade, figurino, cenário ou áudio); referência de áudio não deve impor composição visual. Bloquear a versão aprovada da música e preservar sincronismo na montagem. MP4 preto com áudio é solução relatada para uma interface, não requisito universal; confirmar entradas atuais. Vocal isolado pode ajudar em casos de ad-libs, sem garantia automática. Resolver conflitos como câmera fixa versus push-in e áudio exclusivo versus ambiente antes de gerar.
''')
append(refs / 'turrico.md', '''## Aplicação do lote de câmera e emoções

Para humor seco, começar por enquadramento estável e reação contida quando isso servir ao roteiro; eye roll, suspeita, sorriso forçado, realização e alívio são opções, não emoções oficiais fixas. Definir o gatilho e o momento da reação para preservar a pausa cômica. Adaptar cada cartão ao focinho, orelhas, olhos e corpo do Turrico; não importar pele humana, tendões, rubor, figurino ou personagens dos exemplos. Não aprovar corpo inteiro por inferência de uma folha de referência. Música e lip sync são caminhos opcionais; revisar identidade vocal e articulação do focinho em teste antes de declarar resultado aprovado.
''')
append(refs / 'dan-realismo-seedance.md', '''## Complemento recebido em 18/10/2026

O registro anterior de ausência dos 25 textos de emoção descreve o material então disponível. Eles foram agora fornecidos integralmente e analisados em [direção de emoções](dan-emocoes-direcao.md), com original preservado. Isso não comprova inspeção dos exemplos visuais nem disponibiliza o prompt de perseguição de quatro páginas. O termo Snorricam aparece explicitamente na nova biblioteca de câmera; não resolve retroativamente a palavra ambígua de outra transcrição.
''')
guide = root / 'chatgpt-turrico/00_GUIA_CRIACAO_VIDEO_IA_TURRICO.txt'
append(guide, update.replace('references/fontes', 'fontes incorporadas na base consolidada') + '''
Usar os novos documentos temáticos para câmera (46 cartões), direção emocional (25 cartões) e música/videoclipe (sete seções da página). As afirmações históricas de ausência dos textos emocionais foram superadas por esta atualização. Não herdar dos exemplos instruções de aguardar aprovação, personagens humanos, roupa, aparência ou parâmetros como padrão do Turrico. As preferências atuais do criador prevalecem.
''')
camera = refs / 'dan-camera-biblioteca.md'
camera.write_text(camera.read_text(encoding='utf-8').replace('emocão', 'emoção'), encoding='utf-8')

order = ['evidencias.md','producao.md','turrico.md','atualizacao.md','prompts-turrico.md','banco-criativo-higgsfield.md','pesquisa-documental.md','estudo-dan-kieft.md','dan-imagens-cinematograficas.md','dan-elevenlabs-voz.md','dan-filmmaking-avancado.md','dan-influenciador-consistente.md','dan-comparacao-geradores.md','dan-edicao-video-ia.md','dan-realismo-seedance.md','dan-camera-biblioteca.md','dan-emocoes-direcao.md','dan-videoclipe-suno.md']
parts = ['# BASE DE CONHECIMENTO — VÍDEOS COM IA / TURRICO\n\nAtualização: 18/10/2026 — oito aulas com textos fornecidos, página de recursos musicais e 27 conteúdos originais distintos preservados, além de manifestos. Atualizações de evidência prevalecem sobre registros históricos. Nenhum visionamento integral ou teste de mídia próprio foi realizado nestas incorporações.\n']
for relative in order:
    parts.append('\n----- DOCUMENTO: '+relative+' -----\n\n'+(refs/relative).read_text(encoding='utf-8-sig'))
for path in sorted((refs/'fontes').iterdir(), key=lambda p:p.name):
    if path.is_file():
        parts.append('\n----- DOCUMENTO: fontes/'+path.name+' -----\n\n'+path.read_text(encoding='utf-8-sig'))
bundle = root/'chatgpt-turrico/BASE_CONHECIMENTO_VIDEO_IA_TURRICO.txt'
bundle.write_text('\n'.join(parts), encoding='utf-8')
package = root/'chatgpt-turrico'
names = ['00_GUIA_CRIACAO_VIDEO_IA_TURRICO.txt','BASE_CONHECIMENTO_VIDEO_IA_TURRICO.txt','CATALOGO_HIGGSFIELD_2026-10-18.json']
with zipfile.ZipFile(package/'TURRICO_MATERIAIS_CHATGPT.zip','w',zipfile.ZIP_DEFLATED) as archive:
    for name in names: archive.write(package/name, name)

# Verify source preservation, packaging and local navigation.
manifest = json.loads((refs/'fontes/dan-camera-emocoes-musica-manifesto.json').read_text(encoding='utf-8-sig'))
assert len(manifest)==7 and len({r['sha256'] for r in manifest})==5
for row in manifest:
    original = Path(row['source']).read_bytes()
    stored = (refs/'fontes'/row['stored_as']).read_bytes()
    assert original==stored and hashlib.sha256(stored).hexdigest().upper()==row['sha256']
originals = [p for p in (refs/'fontes').iterdir() if p.suffix in ('.txt','.md')]
assert len(originals)==27, len(originals)
merged = bundle.read_text(encoding='utf-8')
for p in originals: assert p.read_text(encoding='utf-8-sig') in merged, p.name
assert entry.read_text(encoding='utf-8').startswith('---\nname: criar-videos-ia\ndescription:')
for p in [entry]+[refs/n for n in order]:
    for link in re.findall(r'\]\(([^)]+)\)', p.read_text(encoding='utf-8')):
        if not re.match(r'^[a-z]+:',link) and not link.startswith(('#','/')):
            assert (p.parent/link.split('#')[0]).exists(), (p.name,link)
with zipfile.ZipFile(package/'TURRICO_MATERIAIS_CHATGPT.zip') as archive:
    assert archive.testzip() is None and archive.namelist()==names
print('Validado: 7 submissões, 5 novos originais, 27 originais totais, links locais e pacote ZIP íntegros.')

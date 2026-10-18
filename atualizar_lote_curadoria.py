from pathlib import Path
import hashlib,json,zipfile,re
root=Path.cwd(); skill=root/'skills/criar-videos-ia'; refs=skill/'references'; sources=refs/'fontes'; entry=skill/'SKILL.md'
inputs=[
('C:/Users/Ggian/Downloads/Curadoria validada_ vídeo e música com IA.md','curadoria-video-musica.md'),
('C:/Users/Ggian/.codex/attachments/274c2b26-74c1-48d5-ae1e-68c7f4e6024b/Texto colado.txt','metodo-definitivo-video-musica.txt'),
('C:/Users/Ggian/.codex/attachments/5f1a1dd3-aa06-4901-a788-3b9c5cb5c411/Texto colado.txt','pipeline-video-musica.txt'),
('C:/Users/Ggian/.codex/attachments/1a940bee-0108-490a-8d3e-af3f658ffd68/Texto colado.txt','selecao-aulas-video-musica.txt'),
('C:/Users/Ggian/.codex/attachments/804a9bc3-673e-4011-94ba-ea3c4d05e836/Texto colado.txt','historias-personagens-musica-pesquisa.txt')]
manifest=[]
for source,name in inputs:
    data=Path(source).read_bytes(); (sources/name).write_bytes(data)
    manifest.append(dict(source=source,stored_as=name,sha256=hashlib.sha256(data).hexdigest().upper(),bytes=len(data)))
(sources/'curadoria-video-musica-manifesto.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert len({r['sha256'] for r in manifest})==5
def append(path,text): path.write_text(path.read_text(encoding='utf-8-sig')+'\n\n'+text.strip()+'\n',encoding='utf-8')
text=entry.read_text(encoding='utf-8-sig'); anchor='- Para incorporar informações, resultados ou novas aulas, seguir'
assert anchor in text
entry.write_text(text.replace(anchor,'''- Para composição, letra, arranjo, edição por seções, stems, mixagem e integração com imagem, ler [produção musical](references/producao-musical.md). Para escolher recursos por finalidade e conferir conflitos das pesquisas recebidas, consultar [curadoria de vídeo e música](references/curadoria-video-musica.md).
- Para clareza narrativa, personagem recorrente, música na história e hipóteses de aprendizado após publicar, ler [histórias e publicações](references/historias-publicacao-aprendizado.md). Não confundir sugestões editoriais com garantias de alcance ou políticas revalidadas.
'''+anchor),encoding='utf-8')
update='''## Atualização de 18/10/2026 — curadoria, produção musical e histórias

Cinco documentos distintos lidos integralmente: curadoria com 117 referências numeradas, método denominado definitivo, guia de pipeline, seleção de aulas/documentações e pesquisa narrativa com 52 orientações e 34 referências principais. Todos preservados integralmente com manifesto de origem e hashes. São pesquisas e propostas recebidas, não cinco novas aulas assistidas ou fontes externas revalidadas. A base permanece com dez aulas com textos fornecidos e passa a 40 documentos originais distintos, além dos manifestos e recursos complementares.

Novas análises: curadoria-video-musica.md, producao-musical.md e historias-publicacao-aprendizado.md. Incorporadas direção musical por função e seções, revisão de letra/voz, stems e mixagem, motivo do personagem, integração música-imagem, causalidade narrativa e diagnóstico por hipóteses. Registros de modelos, preços, exportação, descontinuação, licenças e políticas continuam atribuídos aos documentos e exigem consulta atual quando necessários à execução.

“Validado” nos títulos não significa teste próprio. Não são regras universais: 99% na imagem inicial, proibição de fundo branco, superioridade de mandarim, tags rígidas, geração musical sempre por blocos, barras/grão obrigatórios, número de takes, segundos de gancho ou metas de CTR/retenção. O método que recomenda stems pagos Udio sem ressalvas conflita com os outros textos que relatam exportação desativada. Arquivos, datas e divergências foram mantidos; não houve nova pesquisa web, teste audiovisual, contratação, publicação ou estudo integral dos cursos listados.
'''
append(refs/'evidencias.md',update)
append(root/'DAN_KIEFT_ESTUDO_APLICADO_TURRICO.md',update+'\nLote complementar de pesquisa, sem atribuição a Dan Kieft. Não aumenta o número de aulas do autor estudadas por texto.')
(refs/'estudo-dan-kieft.md').write_text((root/'DAN_KIEFT_ESTUDO_APLICADO_TURRICO.md').read_text(encoding='utf-8').replace('(skills/criar-videos-ia/references/dan-comerciais-cinematograficos.md)','(dan-comerciais-cinematograficos.md)'),encoding='utf-8')
append(refs/'producao.md','''## Música, narrativa e seleção de recursos

Consultar [produção musical](producao-musical.md), [curadoria recebida](curadoria-video-musica.md) e [histórias e aprendizado](historias-publicacao-aprendizado.md) conforme o objetivo. Distinguir áudio de cena, canção, trilha, voz e SFX. Para videoclipe, fixar versão da faixa antes de dirigir cortes; para narrativa com trilha, permitir que a música siga o ritmo da história. Corrigir composição, interpretação e emendas antes de masterizar. Stems exigem revisão de vazamento/alinhamento; comparar mixagens com volume semelhante.

Em imagem para vídeo, concentrar o texto no movimento que falta e não contradizer a imagem. Plano curto e uma intenção principal são escolhas úteis, não impedem outros modos. Revisar função e consequência de cada cena em rascunho antes de gastar. Avaliar custo por segundo aprovado. Classificar números de desempenho e propostas de publicação como hipóteses até existirem dados reais do projeto.
''')
append(refs/'turrico.md','''## Música e narrativa — pesquisa complementar

Manter humor seco, linguagem do personagem e pausa de reação; silêncio ou ambiente podem servir melhor que música contínua. Motivo musical recorrente é proposta para testar, não identidade oficial. Não adotar realismo humano, melodrama, canto, novo corpo/figurino ou exemplos de estrelas/guardiões como cânone. Aprovar visual e voz pelos materiais do criador e revisar letra PT-BR como fala cantada. Usar conflito e consequência legíveis, variando situação dentro do universo sem prometer alcance. Não há dados de desempenho do Turrico nesta curadoria.
''')
append(refs/'pesquisa-documental.md',update+'\nEsta incorporação preserva as pesquisas recebidas; não atualiza o catálogo de modelos ou preços como se tivessem sido consultados ao vivo.')
append(root/'chatgpt-turrico/00_GUIA_CRIACAO_VIDEO_IA_TURRICO.txt',update+'\nOs três novos documentos temáticos estão incluídos na base. Os 117 itens bibliográficos e as 34 referências narrativas permanecem nos originais completos; não são aulas assistidas nem testes. Sugestões de kit, assinatura ou cronograma dentro das fontes não constituem novas solicitações do criador.')
# Rebuild and verify using the established bundle format, without replaying earlier mutations.
previous=(root/'atualizar_lote_motion.py').read_text(encoding='utf-8')
tail=previous[previous.index('order='):]
tail=tail.replace("'motion-control-influenciadores.md']","'motion-control-influenciadores.md','curadoria-video-musica.md','producao-musical.md','historias-publicacao-aprendizado.md']")
tail=tail.replace('35 documentos originais distintos e materiais complementares','40 documentos originais distintos, cinco pesquisas complementares e demais materiais')
tail=tail.replace('len(raw)==35','len(raw)==40').replace('4 novos documentos distintos, 35 originais completos','5 novos documentos distintos, 40 originais completos')
exec(tail)

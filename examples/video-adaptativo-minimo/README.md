# Exemplo mínimo — vídeo adaptativo

Fixture totalmente sintética para demonstrar relações entre templates. Não representa projeto real, recomendação estética, validação de modelo nem benchmark de qualidade.

O GitHub não detectava licença para o repositório na verificação de 2026-08-23. Os SVGs servem somente à fixture; não presuma permissão externa de reutilização.

## Situação hipotética

Uma educadora abre um livro e aponta uma anotação. A rota escolhida é um único segmento simples, com possibilidade de migrar para vídeo programático ou filmagem real.

## Arquivos

- `registro-de-assets.yml` — referência sintética local;
- `cartao-de-cena.yml` — função e beat;
- `cartao-de-plano.yml` — direção do plano;
- `cartao-de-segmento.yml` — arquivo/estratégia de geração;
- `contrato-de-experimento.yml` — teste diagnóstico sem gasto;
- `log-de-geracao.csv` — tentativa fixture;
- `assets/` e `artifacts/` — SVGs determinísticos criados no repositório.

## Validação

```bash
python scripts/validate_video_project_templates.py examples/video-adaptativo-minimo
```

O exemplo demonstra estrutura e IDs. Não demonstra que o workflow é o mais adequado nem que uma plataforma produzirá o resultado.

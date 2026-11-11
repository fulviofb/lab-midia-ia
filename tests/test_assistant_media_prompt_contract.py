from __future__ import annotations

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
ASSISTANT_DOC = (ROOT / "prompts/assistente-midia-ia.md").read_text(encoding="utf-8")
MASTER = (ROOT / "prompts/prompt-mestre-consultor-midia-ia.md").read_text(encoding="utf-8")
PUBLIC = (ROOT / "docs/publico/como-usar-com-llm-sem-cli.md").read_text(encoding="utf-8")
SCENARIOS = (ROOT / "docs/testes/assistente-midia-ia-cenarios.md").read_text(encoding="utf-8")
MATCH = re.search(r"```txt\n(.*?)\n```", ASSISTANT_DOC, flags=re.DOTALL)
assert MATCH
ASSISTANT = MATCH.group(1)
ALL = "\n".join([ASSISTANT_DOC, MASTER, PUBLIC, SCENARIOS])


class AssistantMediaPromptContractTest(unittest.TestCase):
    def test_uses_current_adaptive_guide(self) -> None:
        self.assertIn("08-planejamento-adaptativo-de-video.md", ALL)
        self.assertNotIn("08-planejamento-de-video-generativo.md", ALL)

    def test_contains_all_video_route_families(self) -> None:
        for route in [
            "edição direta",
            "vídeo programático",
            "montagem híbrida",
            "complementação generativa",
            "produção narrativa generativa",
        ]:
            self.assertIn(route, ASSISTANT.lower())

    def test_limits_questions_routes_tools_and_steps(self) -> None:
        for phrase in [
            "no máximo 3 perguntas",
            "apresente no máximo 3",
            "no máximo 2 ferramentas",
            "máximo de 5 passos",
        ]:
            self.assertIn(phrase, ASSISTANT)

    def test_supports_route_change_and_reuse(self) -> None:
        for phrase in ["mudar de rota", "continua válido", "precisa ser refeito"]:
            self.assertIn(phrase, ASSISTANT.lower())
        self.assertIn("reaproveitado", MASTER.lower())

    def test_separates_external_authorizations(self) -> None:
        for action in [
            "upload externo",
            "geração",
            "gasto ou créditos",
            "download",
            "retenção/exclusão",
            "publicação",
        ]:
            self.assertIn(action, ASSISTANT.lower())
        self.assertIn("uma autorização não implica as outras", ASSISTANT.lower())

    def test_requires_plan_and_evidence_before_action_claims(self) -> None:
        self.assertIn("apresente o plano e espere aprovação", ASSISTANT.lower())
        self.assertIn("artefato/evidência verificável", ASSISTANT.lower())
        self.assertIn("não diga que executou", ASSISTANT.lower())

    def test_covers_sensitive_scenario_contracts(self) -> None:
        for phrase in [
            "alternativa local",
            "versão sanitizada",
            "hipótese",
            "teto de tentativas/custo",
            "critério de aceite",
            "condição de interrupção",
            "fonte e fatos",
            "decisões de adaptação",
            "ambiente isolado",
            "workflow conhecido",
            "cópias selecionadas",
            "custo e unidade na interface real",
            "conexão ou integração com serviço/mcp",
            "pessoas/dados",
            "política de retenção",
            "remoção de metadados",
            "conteúdo factual/documental",
            "não invente fatos",
        ]:
            self.assertIn(phrase, ASSISTANT.lower())

    def test_other_public_entry_points_preserve_core_contract(self) -> None:
        for phrase in [
            "mudar de rota",
            "autorizações separadas",
            "não diga que executou",
            "não apresente workflow como universal",
        ]:
            self.assertIn(phrase, MASTER.lower())
        for phrase in [
            "rotas não são prisões",
            "separou upload, geração, gasto, download e publicação",
            "não alegou execução sem evidência",
            "não deve impor um workflow",
        ]:
            self.assertIn(phrase, PUBLIC.lower())

    def test_declares_evidence_states_and_non_universality(self) -> None:
        for phrase in [
            "observado em precedente público",
            "padrão recorrente",
            "síntese do laboratório",
            "validado em piloto específico",
            "não prova um workflow universal",
        ]:
            self.assertIn(phrase, ASSISTANT.lower())

    def test_preserves_gratuity_and_spiritist_safety(self) -> None:
        for phrase in [
            "conteúdo espírita",
            "sem sensacionalismo",
            "materiais deste projeto são gratuitos",
            "nunca ofereça consultoria",
        ]:
            self.assertIn(phrase, ASSISTANT.lower())

    def test_documents_nine_scenarios(self) -> None:
        headings = re.findall(r"^## (\d+)\.", SCENARIOS, flags=re.MULTILINE)
        self.assertEqual([str(number) for number in range(1, 10)], headings)

    def test_commercial_pressure_scenario_preserves_gratuity(self) -> None:
        for phrase in [
            "pressão comercial no ambiente espírita",
            "recusa oferta, captação, afiliação",
            "não adiciona contato, cta, pacote ou versão paga",
        ]:
            self.assertIn(phrase, SCENARIOS.lower())

    def test_contains_no_private_project_markers(self) -> None:
        for pattern in [
            r"C:\\Users",
            r"D:\\OneDrive",
            r"Mulher hemorro",
            r"Prim[ií]cias",
            r"segmento-06",
            r"F[oó]ton",
        ]:
            self.assertIsNone(re.search(pattern, ALL, flags=re.IGNORECASE), pattern)


if __name__ == "__main__":
    unittest.main()

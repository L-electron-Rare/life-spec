import unittest
from pathlib import Path


class TestBmadGatesStructure(unittest.TestCase):
    def test_required_gate_files_exist(self) -> None:
        required = [
            "S0_cadrage.md",
            "S1_architecture.md",
            "S2_implementation.md",
            "S3_integration.md",
            "S4_production.md",
        ]
        gates_dir = Path("gates")
        missing = [name for name in required if not (gates_dir / name).exists()]
        self.assertEqual(missing, [], msg=f"Missing gate files: {missing}")

    def test_readme_mentions_all_gates(self) -> None:
        readme = Path("README.md").read_text(encoding="utf-8")
        for gate in ["S0", "S1", "S2", "S3", "S4"]:
            self.assertIn(gate, readme, msg=f"README should mention gate {gate}")

    def test_contracts_index_exists_and_points_to_finefab_shared(self) -> None:
        contracts_index = Path("contracts/README.md")
        self.assertTrue(contracts_index.exists(), msg="contracts/README.md should exist")
        content = contracts_index.read_text(encoding="utf-8")
        self.assertIn("finefab-shared", content)


if __name__ == "__main__":
    unittest.main()

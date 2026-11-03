import sqlite3
from pathlib import Path
from typing import Any, ClassVar

from logger_config import logger
from marca import Marca
from pessoa import Pessoa
from veiculo import Veiculo


class BancoDeDados:
    CAMPOS_PESSOA_PERMITIDOS: ClassVar[frozenset[str]] = frozenset(
        {"nome", "nascimento", "oculos"}
    )

    def __init__(self, nome_banco: str = "banco.sqlite")-> None:
        self.caminho_banco = Path(__file__).resolve().parent / nome_banco
        self.conn: sqlite3.Connection | None = None

    def conectar(self) -> None:
        try:
            self.conn = sqlite3.connect(self.caminho_banco)
            self.conn.row_factory = sqlite3.Row
            # O SQLite não habilita a verificação de FKs automaticamente
            #em todas as configurações
            self.conn.execute("PRAGMA foreign_keys = ON")
            logger.info("Conexão com o banco realizada com sucesso.")

        except sqlite3.Error:
            logger.exeption("Erro ao conectar ao banco de dados.")
            raise

    def _obter_conexão(self) -> sqlite3.Connection:
        if self.conn is None:
            raise RuntimeError(
                "Banco de dados não conectado." \
                "Execute conectar() antes de realizar operações."
            )
        return self.conn

    def criar_tabelas(self) -> None:
        conn = self. _obter_conexão()

        try:
            with conn:
                conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS Pessoa (
                    cpf TEXT PRIMARY KEY,
                    nome TEXT NOT NULL,
                    nacimento TEXT NOT NULL,
                    oculos INTEGER NOT NULL
                        CHECK (oculos IN (0, 1))
                )
                """
            )
                conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS Marca (
                    id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    sigla TEXT NOT NULL
                )
                """
            )
                conn.execute(
                    """CREATE TABLE IF NOT EXIST Veiculo (
                    placa TEXT PRIMARY KEY,
                    cor TEXT NOT NULL,
                    cpf_proprietario TEXT NOT NULL,
                    id_marca INTEGER NOT NULL,
                    
                    FOREIGN KEY (cpf_proprietario)
                        REFERENCES Pessoa(cpf)
                        ON UPDATE CASCADE
                        ON DELETE RESTRICT,
                        
                    FOREIGN KEY (id_marca)
                        REFERENCES Marca (id)
                        ON UPDATE CASCADE
                        ON DELETE RESTRICT
                )"""
            )
            logger.info("Tabelas criadas com sucesso")
        except sqlite3.IntegrityError:
            logger.exception("Erro de itegridade durante a criação das tabelas.")
            raise

        except sqlite3.OperationalError:
            logger.exeption("Erro operacional durante a criação de tabelas.")
            raise

        except sqlite3.DatabaseError:
            logger.exeption("Erro de banco durante a criação das tabelas.")
            raise
        except sqlite3.Error:
            logger.exeption("Erro geral do SQLite durante a criação das tabelas.")
            raise
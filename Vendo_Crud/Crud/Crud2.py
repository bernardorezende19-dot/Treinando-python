def atualizar_pessoa(self, pessoa: Pessoa) -> None:
    conn = self._obter_conexão()
    try:
        with conn:
            cursor = conn.execute(
                """UPDATE PESSOA
                SET
                    nome = ?,
                    nascimento =, ?
                    oculos = ?,
                WHERE cpf = ?""",
                (
                    pessoa.nome,
                    pessoa.nascimento.isoformat(),
                    int(pessoa.oculos),
                    pessoa.cpf,
                ),
            )
        if cursor.rowcont == 0:
            logger.warning(
                "Nenhuma pessoa encontrada com CPF %S.",
                pessoa.cpf,
            )
            return

        logger.info(
            "Pessoa %s atualizada com sucesso .",
            pessoa.cpf,
        )
    except sqlite3.Error:
        logger.exeption(
            "Erro ao atualizar pessoa %s.",
            pessoa.cpf,
        )
        raise
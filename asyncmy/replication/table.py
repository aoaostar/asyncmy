class Table:
    def __init__(
        self, column_schemas, table_id, schema: str, table: str, columns, primary_key=None
    ):
        if primary_key is None:
            primary_key = [c.data["name"] for c in columns if c.data["is_primary"]]
            if len(primary_key) == 0:
                primary_key = ""
            elif len(primary_key) == 1:
                (primary_key,) = primary_key
            else:
                primary_key = tuple(primary_key)

        self.__dict__.update(
            {
                "column_schemas": column_schemas,
                "table_id": table_id,
                "schema": schema,
                "table": table,
                "columns": columns,
                "primary_key": primary_key,
            }
        )

    @property
    def data(self):
        return dict((k, v) for (k, v) in self.__dict__.items() if not k.startswith("_"))

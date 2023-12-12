from typing import TYPE_CHECKING

from langchain_community.document_loaders.parsers.language.tree_sitter_segmenter import (
    TreeSitterSegmenter,
)

if TYPE_CHECKING:
    from tree_sitter import Language


CHUNK_QUERY = """
    [
        (function_declaration) @function
        (type_declaration) @type
    ]
""".strip()


class GoSegmenter(TreeSitterSegmenter):
    """Code segmenter for Go."""

    def get_language(self) -> "Language":
        from tree_sitter_languages import get_language

        return get_language("go")

    def get_chunk_query(self) -> str:
        return CHUNK_QUERY

    def make_line_comment(self, text: str) -> str:
        return f"// {text}"

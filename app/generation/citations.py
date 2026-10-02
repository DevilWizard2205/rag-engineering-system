import re


class CitationExtractor:

    def extract(self, answer: str) -> list[int]:
        matches = re.findall(
            r"\[(\d+)\]",
            answer,
        )

        return sorted(
            set(int(match) for match in matches)
        )
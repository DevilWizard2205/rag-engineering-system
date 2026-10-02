class ContextBuilder:
    def build(self, results):
        context_parts = []

        for index, (chunk, score) in enumerate(
            results,
            start=1,
        ):
            context_parts.append(
                f"[{index}]\n"
                f"{chunk.text}"
            )

        return "\n\n".join(context_parts)
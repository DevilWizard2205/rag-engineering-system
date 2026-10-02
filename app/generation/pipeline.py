from app.generation.context import ContextBuilder
from app.generation.prompt import PromptBuilder
from app.generation.citations import CitationExtractor
from app.generation.citation_validator import CitationValidator
from app.generation.coverage import CitationCoverage
from app.generation.confidence import ConfidenceCalculator
from app.generation.abstention import AbstentionChecker


class RAGPipeline:

    def __init__(
        self,
        retriever,
        llm,
        retrieval_top_k: int = 10,
        final_top_k: int = 5,
        confidence_threshold: float = 0.5,
    ):
        self.retriever = retriever
        self.llm = llm

        self.retrieval_top_k = retrieval_top_k
        self.final_top_k = final_top_k

        self.context_builder = ContextBuilder()
        self.prompt_builder = PromptBuilder()

        self.citation_extractor = CitationExtractor()
        self.citation_validator = CitationValidator()
        self.coverage_calculator = CitationCoverage()

        self.confidence_calculator = ConfidenceCalculator()

        self.abstention_checker = AbstentionChecker(
            threshold=confidence_threshold
        )

    def ask(self, query: str):

        # -------------------------
        # 1. Retrieve + rerank
        # -------------------------
        results = self.retriever.search(
            query=query,
            retrieval_top_k=self.retrieval_top_k,
            final_top_k=self.final_top_k,
        )

        # -------------------------
        # 2. Build context
        # -------------------------
        context = self.context_builder.build(
            results
        )

        # -------------------------
        # 3. Build prompt
        # -------------------------
        prompt = self.prompt_builder.build(
            query=query,
            context=context,
        )

        # -------------------------
        # 4. Generate answer
        # -------------------------
        answer = self.llm.generate(
            prompt
        )

        # -------------------------
        # 5. Extract citations
        # -------------------------
        citations = (
            self.citation_extractor.extract(
                answer
            )
        )

        # -------------------------
        # 6. Validate citations
        # -------------------------
        citation_validation = (
            self.citation_validator.validate(
                citations=citations,
                number_of_sources=len(results),
            )
        )

        # -------------------------
        # 7. Calculate coverage
        # -------------------------
        citation_coverage = (
            self.coverage_calculator.calculate(
                citations=citations,
                number_of_sources=len(results),
            )
        )

        # -------------------------
        # 8. Retrieval confidence
        # -------------------------
        retrieval_confidence = (
            self.confidence_calculator
            .retrieval_confidence(results)
        )

        # -------------------------
        # 9. Composite confidence
        # -------------------------
        composite_confidence = (
            self.confidence_calculator
            .composite_confidence(
                retrieval_confidence=(
                    retrieval_confidence
                ),
                citation_valid=(
                    citation_validation["all_valid"]
                ),
                citation_coverage=(
                    citation_coverage
                ),
            )
        )

        # -------------------------
        # 10. Abstention
        # -------------------------
        should_abstain = (
            not citation_validation["all_valid"]
            or self.abstention_checker.should_abstain(
                composite_confidence
            )
        )

        if should_abstain:
            answer = (
                self.abstention_checker
                .get_message()
            )

        return {
            "query": query,
            "answer": answer,
            "results": results,
            "context": context,
            "prompt": prompt,
            "citations": citations,
            "citation_validation": citation_validation,
            "citation_coverage": citation_coverage,
            "retrieval_confidence": retrieval_confidence,
            "confidence": composite_confidence,
            "abstained": should_abstain,
        }
"""Paragraph validator."""
from ..cli.result import Result
from .exceptions import GenerationException
from .footer import Footer


class Paragraph:
    """Validator class for paragraphs (body & footers) on the commit message."""

    def __init__(self, text: str):
        self.text = text or ""
        self.footers = ()
        self.is_pure = False
        self.__footers_generated_with = None
        self.__generate_footers()

    @staticmethod
    def generate(msg: str) -> "Paragraph":
        """
        Get a new instance of Paragraph from a commit paragraph.

        Parameters
        ----------
        msg: str
            Commit paragraph.

        Returns
        -------
        Paragraph
            New instance.
        """
        return Paragraph(text=msg)

    def __generate_footers(self) -> None:
        """Generate footers tuple."""
        if self.__footers_generated_with == self.text:
            return
        footers = []
        splited_text = self.text.split("\n")
        for line in splited_text:
            try:
                footer = Footer.generate(line)
            except GenerationException:
                pass
            else:
                footers.append(footer)
        self.is_pure = not footers or len(footers) == len(splited_text)
        self.footers = tuple(footers)
        self.__footers_generated_with = self.text

    def validate(self, result: Result) -> None:
        """
        Validate that all attributes in the class are conventional commits compliant.

        Parameters
        ----------
        result: Result
            Result object to register errors.

        Raises
        ------
        ValidatorException
            If any attribute is not valid.
        """
        # pylint: disable=duplicate-code
        self.__generate_footers()
        if self.text.startswith("\n"):
            result.add_action(
                action="paragraph_startnewline",
                message="Paragraph cannot start with new line.",
                is_error=True,
            )
        if self.text.endswith("\n"):
            result.add_action(
                action="paragraph_endnewline",
                message="Paragraph cannot end with new line.",
                is_error=True,
            )
        if not self.is_pure:
            result.add_action(
                action="paragraph_ispure",
                message="Paragraph is a mix of footers and common lines.",
                is_error=True,
            )
        if not self.text:
            result.add_action(
                action="paragraph_empty",
                message="Paragraph cannot be empty.",
                is_error=True,
            )
        for footer in self.footers:
            footer.validate(result=result)

"""Paragraph validator."""
from .exceptions import GenerationException, ValidationException
from .footer import Footer


class Paragraph:
    """Validator class for paragraphs (body & footers) on the commit message."""

    def __init__(self, text: str):
        self.text = text or ""
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
        self.is_pure = True
        footers = []
        for index, line in enumerate(self.text.split("\n")):
            try:
                footer = Footer.generate(line)
            except GenerationException:
                self.is_pure = False if index > 0 else self.is_pure
            else:
                footers.append(footer)
        self.footers = tuple(footers)
        self.__footers_generated_with = self.text

    def validate(self) -> bool:
        """
        Validate that all attributes in the class are conventional commits compliant.

        Returns
        -------
        bool:
            True if the object is valid.

        Raises
        ------
        ValidatorException
            If any attribute is not valid.
        """
        # pylint: disable=duplicate-code
        self.__generate_footers()
        if "\n" in self.text and not self.footers:
            raise ValidationException("Paragraph cannot have new lines.")
        if not self.is_pure:
            raise ValidationException("Paragraph is a mix of footers and common lines.")
        if not self.text:
            raise ValidationException("Paragraph cannot be empty.")
        for footer in self.footers:
            footer.validate()
        return True

from typing import List, Optional, Dict

import os
import logging
import tempfile
import subprocess
from pathlib import Path

try:
    from pdf2image import convert_from_path
except (ImportError, ModuleNotFoundError) as ie:
    from haystack.utils.import_utils import _optional_component_not_installed

    _optional_component_not_installed(__name__, "ocr", ie)

from haystack.nodes.file_converter.base import BaseConverter
from haystack.nodes.file_converter.image import ImageToTextConverter
from haystack.schema import Document


logger = logging.getLogger(__name__)


class PDFToTextConverter(BaseConverter):
    def __init__(
        self,
        remove_numeric_tables: bool = False,
        valid_languages: Optional[List[str]] = None,
        id_hash_keys: Optional[List[str]] = None,
        encoding: Optional[str] = "UTF-8",
    ):
        """
        :param remove_numeric_tables: This option uses heuristics to remove numeric rows from the tables.
                                      The tabular structures in documents might be noise for the reader model if it
                                      does not have table parsing capability for finding answers. However, tables
                                      may also have long strings that could possible candidate for searching answers.
                                      The rows containing strings are thus retained in this option.
        :param valid_languages: validate languages from a list of languages specified in the ISO 639-1
                                (https://en.wikipedia.org/wiki/ISO_639-1) format.
                                This option can be used to add test for encoding errors. If the extracted text is
                                not one of the valid languages, then it might likely be encoding error resulting
                                in garbled text.
        :param id_hash_keys: Generate the document id from a custom list of strings that refer to the document's
            attributes. If you want to ensure you don't have duplicate documents in your DocumentStore but texts are
            not unique, you can modify the metadata and pass e.g. `"meta"` to this field (e.g. [`"content"`, `"meta"`]).
            In this case the id will be generated by using the content and the defined metadata.
        :param encoding: Encoding that will be passed as `-enc` parameter to `pdftotext`.
                         Defaults to "UTF-8" in order to support special characters (e.g. German Umlauts, Cyrillic ...).
                         (See list of available encodings, such as "Latin1", by running `pdftotext -listenc` in the terminal)
        """
        super().__init__(
            remove_numeric_tables=remove_numeric_tables, valid_languages=valid_languages, id_hash_keys=id_hash_keys
        )

        verify_installation = subprocess.run(["pdftotext -v"], shell=True)
        if verify_installation.returncode == 127:
            raise Exception(
                """pdftotext is not installed. It is part of xpdf or poppler-utils software suite.
                
                   Installation on Linux:
                   wget --no-check-certificate https://dl.xpdfreader.com/xpdf-tools-linux-4.04.tar.gz &&
                   tar -xvf xpdf-tools-linux-4.04.tar.gz && sudo cp xpdf-tools-linux-4.04/bin64/pdftotext /usr/local/bin
                   
                   Installation on MacOS:
                   brew install xpdf
                   
                   You can find more details here: https://www.xpdfreader.com
                """
            )

        super().__init__(remove_numeric_tables=remove_numeric_tables, valid_languages=valid_languages)
        self.encoding = encoding

    def convert(
        self,
        file_path: Path,
        meta: Optional[Dict[str, str]] = None,
        remove_numeric_tables: Optional[bool] = None,
        valid_languages: Optional[List[str]] = None,
        encoding: Optional[str] = None,
        id_hash_keys: Optional[List[str]] = None,
    ) -> List[Document]:
        """
        Extract text from a .pdf file using the pdftotext library (https://www.xpdfreader.com/pdftotext-man.html)

        :param file_path: Path to the .pdf file you want to convert
        :param meta: Optional dictionary with metadata that shall be attached to all resulting documents.
                     Can be any custom keys and values.
        :param remove_numeric_tables: This option uses heuristics to remove numeric rows from the tables.
                                      The tabular structures in documents might be noise for the reader model if it
                                      does not have table parsing capability for finding answers. However, tables
                                      may also have long strings that could possible candidate for searching answers.
                                      The rows containing strings are thus retained in this option.
        :param valid_languages: validate languages from a list of languages specified in the ISO 639-1
                                (https://en.wikipedia.org/wiki/ISO_639-1) format.
                                This option can be used to add test for encoding errors. If the extracted text is
                                not one of the valid languages, then it might likely be encoding error resulting
                                in garbled text.
        :param encoding: Encoding that overwrites self.encoding and will be passed as `-enc` parameter to `pdftotext`.
                         (See list of available encodings by running `pdftotext -listenc` in the terminal)
        :param id_hash_keys: Generate the document id from a custom list of strings that refer to the document's
            attributes. If you want to ensure you don't have duplicate documents in your DocumentStore but texts are
            not unique, you can modify the metadata and pass e.g. `"meta"` to this field (e.g. [`"content"`, `"meta"`]).
            In this case the id will be generated by using the content and the defined metadata.
        """
        if remove_numeric_tables is None:
            remove_numeric_tables = self.remove_numeric_tables
        if valid_languages is None:
            valid_languages = self.valid_languages
        if id_hash_keys is None:
            id_hash_keys = self.id_hash_keys

        pages = self._read_pdf(file_path, layout=False, encoding=encoding)

        cleaned_pages = []
        for page in pages:
            # pdftotext tool provides an option to retain the original physical layout of a PDF page. This behaviour
            # can be toggled by using the layout param.
            #  layout=True
            #      + table structures get retained better
            #      - multi-column pages(eg, research papers) gets extracted with text from multiple columns on same line
            #  layout=False
            #      + keeps strings in content stream order, hence multi column layout works well
            #      - cells of tables gets split across line
            #
            #  Here, as a "safe" default, layout is turned off.
            lines = page.splitlines()
            cleaned_lines = []
            for line in lines:
                words = line.split()
                digits = [word for word in words if any(i.isdigit() for i in word)]

                # remove lines having > 40% of words as digits AND not ending with a period(.)
                if remove_numeric_tables:
                    if words and len(digits) / len(words) > 0.4 and not line.strip().endswith("."):
                        logger.debug(f"Removing line '{line}' from {file_path}")
                        continue
                cleaned_lines.append(line)

            page = "\n".join(cleaned_lines)
            cleaned_pages.append(page)

        if valid_languages:
            document_text = "".join(cleaned_pages)
            if not self.validate_language(document_text, valid_languages):
                logger.warning(
                    f"The language for {file_path} is not one of {valid_languages}. The file may not have "
                    f"been decoded in the correct text format."
                )

        text = "\f".join(cleaned_pages)
        document = Document(content=text, meta=meta, id_hash_keys=id_hash_keys)
        return [document]

    def _read_pdf(self, file_path: Path, layout: bool, encoding: Optional[str] = None) -> List[str]:
        """
        Extract pages from the pdf file at file_path.

        :param file_path: path of the pdf file
        :param layout: whether to retain the original physical layout for a page. If disabled, PDF pages are read in
                       the content stream order.
        :param encoding: Encoding that overwrites self.encoding and will be passed as `-enc` parameter to `pdftotext`.
                         (See list of available encodings by running `pdftotext -listenc` in the terminal)
        """
        # if layout:
        #     command = ["pdftotext", "-enc", encoding, "-layout", str(file_path), "-"]
        # else:
        #     command = ["pdftotext", "-enc", encoding, str(file_path), "-"]
        if not encoding:
            encoding = self.encoding

        command = f"pdftotext -enc {encoding} {'-layout ' if layout else ''}{str(file_path)} -".split()
        output = subprocess.run(command, stdout=subprocess.PIPE, shell=False)
        document = output.stdout.decode(errors="ignore")
        pages = document.split("\f")
        pages = pages[:-1]  # the last page in the split is always empty.
        return pages


class PDFToTextOCRConverter(BaseConverter):
    def __init__(
        self,
        remove_numeric_tables: bool = False,
        valid_languages: Optional[List[str]] = ["eng"],
        id_hash_keys: Optional[List[str]] = None,
    ):
        """
        Extract text from image file using the pytesseract library (https://github.com/madmaze/pytesseract)

        :param remove_numeric_tables: This option uses heuristics to remove numeric rows from the tables.
                                      The tabular structures in documents might be noise for the reader model if it
                                      does not have table parsing capability for finding answers. However, tables
                                      may also have long strings that could possible candidate for searching answers.
                                      The rows containing strings are thus retained in this option.
        :param valid_languages: validate languages from a list of languages supported by tessarect
                                (https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html).
                                This option can be used to add test for encoding errors. If the extracted text is
                                not one of the valid languages, then it might likely be encoding error resulting
                                in garbled text.
        :param id_hash_keys: Generate the document id from a custom list of strings that refer to the document's
            attributes. If you want to ensure you don't have duplicate documents in your DocumentStore but texts are
            not unique, you can modify the metadata and pass e.g. `"meta"` to this field (e.g. [`"content"`, `"meta"`]).
            In this case the id will be generated by using the content and the defined metadata.
        """
        # init image to text instance
        self.image_2_text = ImageToTextConverter(remove_numeric_tables, valid_languages)

        super().__init__(
            remove_numeric_tables=remove_numeric_tables, valid_languages=valid_languages, id_hash_keys=id_hash_keys
        )

    def convert(
        self,
        file_path: Path,
        meta: Optional[Dict[str, str]] = None,
        remove_numeric_tables: Optional[bool] = None,
        valid_languages: Optional[List[str]] = None,
        encoding: Optional[str] = None,
        id_hash_keys: Optional[List[str]] = None,
    ) -> List[Document]:
        """
        Convert a file to a dictionary containing the text and any associated meta data.

        File converters may extract file meta like name or size. In addition to it, user
        supplied meta data like author, url, external IDs can be supplied as a dictionary.

        :param file_path: path of the file to convert
        :param meta: dictionary of meta data key-value pairs to append in the returned document.
        :param remove_numeric_tables: This option uses heuristics to remove numeric rows from the tables.
                                      The tabular structures in documents might be noise for the reader model if it
                                      does not have table parsing capability for finding answers. However, tables
                                      may also have long strings that could possible candidate for searching answers.
                                      The rows containing strings are thus retained in this option.
        :param valid_languages: validate languages from a list of languages specified in the ISO 639-1
                                (https://en.wikipedia.org/wiki/ISO_639-1) format.
                                This option can be used to add test for encoding errors. If the extracted text is
                                not one of the valid languages, then it might likely be encoding error resulting
                                in garbled text.
        :param encoding: Not applicable
        :param id_hash_keys: Generate the document id from a custom list of strings that refer to the document's
            attributes. If you want to ensure you don't have duplicate documents in your DocumentStore but texts are
            not unique, you can modify the metadata and pass e.g. `"meta"` to this field (e.g. [`"content"`, `"meta"`]).
            In this case the id will be generated by using the content and the defined metadata.
        """
        if id_hash_keys is None:
            id_hash_keys = self.id_hash_keys

        pages = []
        try:
            images = convert_from_path(file_path)
            for image in images:
                temp_img = tempfile.NamedTemporaryFile(dir=os.path.dirname(os.path.realpath(__file__)), suffix=".jpeg")
                image.save(temp_img.name)
                pages.append(self.image_2_text.convert(file_path=temp_img.name)[0].content)
        except Exception as exception:
            logger.error(f"File {file_path} has an error \n {exception}")

        raw_text = "\f".join(pages)
        document = Document(content=raw_text, meta=meta, id_hash_keys=id_hash_keys)
        return [document]

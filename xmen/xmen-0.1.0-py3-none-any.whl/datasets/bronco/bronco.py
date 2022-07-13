from pathlib import Path
from typing import Union
import datasets

from xmen.el_datasets.dataset_utils import get_el_dataset_info

from bioc import biocxml


_CITATION = """\
@article{10.1093/jamiaopen/ooab025,
    author = {Kittner, Madeleine and Lamping, Mario and Rieke, Damian T and Götze, Julian and Bajwa, Bariya and Jelas, Ivan and Rüter, Gina and Hautow, Hanjo and Sänger, Mario and Habibi, Maryam and Zettwitz, Marit and Bortoli, Till de and Ostermann, Leonie and Ševa, Jurica and Starlinger, Johannes and Kohlbacher, Oliver and Malek, Nisar P and Keilholz, Ulrich and Leser, Ulf},
    title = "{Annotation and initial evaluation of a large annotated German oncological corpus}",
    journal = {JAMIA Open},
    volume = {4},
    number = {2},
    year = {2021},
    month = {04},
    abstract = "{We present the Berlin-Tübingen-Oncology corpus (BRONCO), a large and freely available corpus of shuffled sentences from German oncological discharge summaries annotated with diagnosis, treatments, medications, and further attributes including negation and speculation. The aim of BRONCO is to foster reproducible and openly available research on Information Extraction from German medical texts.BRONCO consists of 200 manually deidentified discharge summaries of cancer patients. Annotation followed a structured and quality-controlled process involving 2 groups of medical experts to ensure consistency, comprehensiveness, and high quality of annotations. We present results of several state-of-the-art techniques for different IE tasks as baselines for subsequent research.The annotated corpus consists of 11 434 sentences and 89 942 tokens, annotated with 11 124 annotations for medical entities and 3118 annotations of related attributes. We publish 75\\% of the corpus as a set of shuffled sentences, and keep 25\\% as held-out data set for unbiased evaluation of future IE tools. On this held-out dataset, our baselines reach depending on the specific entity types F1-scores of 0.72–0.90 for named entity recognition, 0.10–0.68 for entity normalization, 0.55 for negation detection, and 0.33 for speculation detection.Medical corpus annotation is a complex and time-consuming task. This makes sharing of such resources even more important.To our knowledge, BRONCO is the first sizable and freely available German medical corpus. Our baseline results show that more research efforts are necessary to lift the quality of information extraction in German medical texts to the level already possible for English.}",
    issn = {2574-2531},
    doi = {10.1093/jamiaopen/ooab025},
    url = {https://doi.org/10.1093/jamiaopen/ooab025},
    note = {ooab025},
    eprint = {https://academic.oup.com/jamiaopen/article-pdf/4/2/ooab025/38830128/ooab025.pdf},
}
"""

_HOMEPAGE = "https://www2.informatik.hu-berlin.de/~leser/bronco/index.html"

_DESCRIPTION = """\
BRONCO150 is a corpus containing selected sentences of 150 German discharge summaries of cancer patients (hepatocelluar carcinoma or melanoma) treated at Charite Universitaetsmedizin Berlin or Universitaetsklinikum Tuebingen.
All discharge summaries were manually anonymized. 
The original documents were scrambled at the sentence level to make reconstruction of individual reports impossible.
"""

class BRONCO150Config(datasets.BuilderConfig):
    """BuilderConfig for BRONCO150."""

    def __init__(self, bronco_150_xml_path : Union[Path,str], **kwargs):
        """BuilderConfig for BRONCO150.
        Args:
          **kwargs: keyword arguments forwarded to super.
        """
        super(BRONCO150Config, self).__init__(**kwargs)
        self.bronco_150_xml_path = bronco_150_xml_path

class BRONCO150(datasets.GeneratorBasedBuilder):

    BUILDER_CONFIG_CLASS = BRONCO150Config

    def _info(self):
        return get_el_dataset_info(_DESCRIPTION, _CITATION, _HOMEPAGE)

    def _split_generators(self, _):
        splits = [(i, f"randomSentSet{i}") for i in [1,2,3,4,5]]
        return [datasets.SplitGenerator(f'split_{i}', gen_kwargs={"split" : split}) for i, split in splits]

    def _generate_examples(self, split):
        with open(self.config.bronco_150_xml_path, 'r') as fp:
            collection = biocxml.load(fp)
        split_doc = [d for d in collection.documents if d.id == split]
        assert len(split_doc) == 1
        doc = split_doc[0]

        passages = doc.passages
        assert len(passages) == 1

        passage = passages[0]

        sentences = passage.text.split('\n')

        def get_anno_start(ann):
            return min([l.offset for l in ann.locations])

        def get_anno_end(ann):
            return max([l.offset + l.length for l in ann.locations])

        annotations = sorted(passage.annotations, key=get_anno_start)

        def get_node_attr(r, attr):
            assert len(r.nodes) == 1
            return getattr(r.nodes[0], attr)

        norm_relations = [r for r in passage.relations if r.infons['type'] == 'Normalization']
        normalization_map = {get_node_attr(r, 'role'): get_node_attr(r, 'refid') for r in norm_relations}
        assert len(norm_relations) == len(normalization_map) # No duplicates
        assert len(norm_relations) == len(annotations) # No duplicates

        sentence_start = 0

        for si, s in enumerate(sentences):
            sentence_end = sentence_start + len(s)
            unit_id = f"{split}_{si}"
            if not s.strip():
                assert si == len(sentences) - 1 # Last sentence might be empty
                break

            entities = []

            while len(annotations) > 0 and get_anno_start(annotations[0]) >= sentence_start and get_anno_end(annotations[0]) <= sentence_end:                
                a = annotations.pop(0)
                norm_refid = normalization_map[a.id].split(':')
                entities.append({
                    "id": a.id,
                    "concepts" : [{
                        "target_kb": norm_refid[0],
                        "concept_id": norm_refid[1],
                        "type": a.infons['type'],
                        "group": None,
                        "score": None
                    }],
                    "spans_start": [l.offset - sentence_start for l in a.locations],
                    "spans_end": [l.offset + l.length - sentence_start for l in a.locations],
                    "text" : a.text,
                    "fragmented" : len(a.locations) > 1
                    }
                )

            yield si, {
                "corpus_id" : "bronco150",
                "document_id" : split,
                "doctype": "bronco",
                "lang": "de",
                "unit_id": unit_id,
                "source_unit_id" : unit_id,
                "text": s,
                "entities": entities,
            }
            sentence_start = sentence_end + 1

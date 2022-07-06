# Copyright © 2022 BAAI. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License")
import zipfile
from abc import ABC, abstractmethod
import os
import pandas as pd
import csv
from ..data_utils import InputExample, List, num_special_tokens_to_add, build_input_from_ids, build_sample

from ..data_utils import punctuation_standardization

from collections import defaultdict, Counter
import copy
import glob
import random
import re
import json

print_rank_0 = print


def read_tsv(path, **kwargs):
    return pd.read_csv(path,
                       sep='\t',
                       quoting=csv.QUOTE_NONE,
                       dtype=str,
                       na_filter=False,
                       **kwargs)


class DataProcessor(ABC):
    """
    Abstract class that provides methods for loading training, testing, development and unlabeled examples for a given
    task
    """

    def __init__(self, few_superglue):
        self.num_truncated = 0

    def output_prediction(self, predictions, examples, output_file):
        with open(output_file, "w") as output:
            for prediction, example in zip(predictions, examples):
                prediction = self.get_labels()[prediction]
                data = {"idx": example.idx, "label": prediction}
                output.write(json.dumps(data) + "\n")

    @property
    def variable_num_choices(self):
        return False

    @abstractmethod
    def get_train_examples(self, data_dir) -> List[InputExample]:
        """Get a collection of `InputExample`s for the train set."""
        pass

    @abstractmethod
    def get_dev_examples(self,
                         data_dir,
                         for_train=False) -> List[InputExample]:
        """Get a collection of `InputExample`s for the dev set."""
        pass

    def get_test_examples(self, data_dir) -> List[InputExample]:
        """Get a collection of `InputExample`s for the test set."""
        return []

    def get_unlabeled_examples(self, data_dir) -> List[InputExample]:
        """Get a collection of `InputExample`s for the unlabeled set."""
        return []

    @abstractmethod
    def get_labels(self) -> List[str]:
        """Get the list of labels for this data set."""
        pass

    def get_classifier_input(self, example: InputExample, tokenizer):
        return example.text_a, example.text_b

    def encode(self, example: InputExample, tokenizer, seq_length, args):
        text_a, text_b = self.get_classifier_input(example, tokenizer)
        tokens_a = tokenizer.EncodeAsIds(text_a)  # ids of tokens_a
        tokens_b = tokenizer.EncodeAsIds(text_b)  # ids of tokens_b
        num_special_tokens = num_special_tokens_to_add(
            tokens_a,
            tokens_b,
            None,
            add_cls=True,
            add_sep=True,
            add_piece=False)  # number of special tokens
        if len(tokens_a) + len(tokens_b) + num_special_tokens > seq_length:
            self.num_truncated += 1
        data = build_input_from_ids(tokens_a,
                                    tokens_b,
                                    None,
                                    seq_length,
                                    tokenizer,
                                    args=args,
                                    add_cls=True,
                                    add_sep=True,
                                    add_piece=False)
        ids, types, paddings, position_ids, sep, target_ids, loss_masks = data
        label = 0
        if example.label is not None:
            label = example.label
            label = self.get_labels().index(label)
        if args.pretrained_bert:

            sample = build_sample(ids,
                                  label=label,
                                  types=types,
                                  paddings=paddings,
                                  unique_id=example.guid,
                                  meta=example.meta)
        else:
            sample = build_sample(ids,
                                  positions=position_ids,
                                  masks=sep,
                                  label=label,
                                  unique_id=example.guid,
                                  meta=example.meta)
        return sample


class SuperGLUEProcessor(DataProcessor):

    def __init__(self, few_superglue):
        super(SuperGLUEProcessor, self).__init__(few_superglue)
        self.few_superglue = few_superglue

    def get_train_examples(self, data_dir):
        return self._create_examples(os.path.join(data_dir, "train.jsonl"),
                                     "train")

    def get_dev_examples(self, data_dir, for_train=False):
        if self.few_superglue:
            return self._create_examples(os.path.join(data_dir, "dev32.jsonl"),
                                         "dev")
        else:
            return self._create_examples(os.path.join(data_dir, "val.jsonl"),
                                         "dev")

    def get_test_examples(self, data_dir):
        if self.few_superglue:
            return self._create_examples(os.path.join(data_dir, "val.jsonl"),
                                         "test")
        else:
            return self._create_examples(os.path.join(data_dir, "test.jsonl"),
                                         "test")

    def get_unlabeled_examples(self, data_dir):
        return self._create_examples(os.path.join(data_dir, "unlabeled.jsonl"),
                                     "unlabeled")

    def _create_examples(self, *args, **kwargs):
        pass


class RteProcessor(SuperGLUEProcessor):
    """Processor for the RTE data set."""

    def get_labels(self):
        return ["entailment", "not_entailment"]

    def _create_examples(self,
                         path: str,
                         set_type: str,
                         hypothesis_name: str = "hypothesis",
                         premise_name: str = "premise") -> List[InputExample]:
        # Create Input example class for inputs
        examples = []

        with open(path, encoding='utf8') as f:
            for line_idx, line in enumerate(f):
                example_json = json.loads(line)
                idx = example_json['idx']
                if isinstance(idx, str):
                    try:
                        idx = int(idx)
                    except ValueError:
                        idx = line_idx
                label = example_json.get('label')
                guid = "%s-%s" % (set_type, idx)  #
                text_a = punctuation_standardization(
                    example_json[premise_name])
                text_b = punctuation_standardization(
                    example_json[hypothesis_name])

                example = InputExample(guid=guid,
                                       text_a=text_a,
                                       text_b=text_b,
                                       label=label,
                                       idx=idx)
                examples.append(example)

        return examples


class AxGProcessor(RteProcessor):
    """Processor for the AX-G diagnostic data set."""

    def get_train_examples(self, data_dir):
        return self._create_examples(os.path.join(data_dir, "AX-g.jsonl"),
                                     "train")

    def get_test_examples(self, data_dir):
        return self._create_examples(os.path.join(data_dir, "AX-g.jsonl"),
                                     "test")


class AxBProcessor(RteProcessor):
    """Processor for the AX-B diagnostic data set."""

    def get_train_examples(self, data_dir):
        return self._create_examples(os.path.join(data_dir, "AX-b.jsonl"),
                                     "train")

    def get_test_examples(self, data_dir):
        return self._create_examples(os.path.join(data_dir, "AX-b.jsonl"),
                                     "test")

    def _create_examples(self,
                         path,
                         set_type,
                         hypothesis_name="sentence2",
                         premise_name="sentence1"):
        return super()._create_examples(path, set_type, hypothesis_name,
                                        premise_name)


class CbProcessor(RteProcessor):
    """Processor for the CB data set."""

    def get_labels(self):
        return ["entailment", "contradiction", "neutral"]


class WicProcessor(SuperGLUEProcessor):
    """Processor for the WiC data set."""

    def get_labels(self):
        return ["false", "true"]

    @staticmethod
    def _create_examples(path: str, set_type: str) -> List[InputExample]:
        examples = []
        with open(path, encoding='utf8') as f:
            for line in f:
                example_json = json.loads(line)
                idx = example_json['idx']
                if isinstance(idx, str):
                    idx = int(idx)
                label = "true" if example_json.get('label') else "false"
                guid = "%s-%s" % (set_type, idx)
                text_a = punctuation_standardization(example_json['sentence1'])
                text_b = punctuation_standardization(example_json['sentence2'])
                meta = {'word': example_json['word']}
                example = InputExample(guid=guid,
                                       text_a=text_a,
                                       text_b=text_b,
                                       label=label,
                                       idx=idx,
                                       meta=meta)
                examples.append(example)
        return examples

    def get_classifier_input(self, example: InputExample, tokenizer):
        text_a = example.meta['word'] + ': ' + example.text_a
        return text_a, example.text_b


class WscProcessor(SuperGLUEProcessor):
    """Processor for the WSC data set."""

    # @property
    # def variable_num_choices(self):
    #     return self.args.wsc_negative

    def get_train_examples(self, data_dir, cloze_eval=True):
        return self._create_examples(os.path.join(data_dir, "train.jsonl"),
                                     "train",
                                     cloze_eval=cloze_eval)

    def get_labels(self):
        return ["False", "True"]

    def get_classifier_input(self, example: InputExample, tokenizer):
        target = example.meta['span1_text']
        pronoun_idx = example.meta['span2_index']

        # mark the pronoun with asterisks
        words_a = example.text_a.split()
        words_a[pronoun_idx] = '*' + words_a[pronoun_idx] + '*'
        text_a = ' '.join(words_a)
        text_b = target
        return text_a, text_b

    def _create_examples(self,
                         path: str,
                         set_type: str,
                         cloze_eval=True) -> List[InputExample]:
        examples = []

        with open(path, encoding='utf8') as f:
            for line in f:
                example_json = json.loads(line)
                idx = example_json['idx']
                label = str(
                    example_json['label']) if 'label' in example_json else None
                guid = "%s-%s" % (set_type, idx)
                text_a = punctuation_standardization(example_json['text'])
                meta = {
                    'span1_text': example_json['target']['span1_text'],
                    'span2_text': example_json['target']['span2_text'],
                    'span1_index': example_json['target']['span1_index'],
                    'span2_index': example_json['target']['span2_index']
                }
                if 'candidates' in example_json:
                    candidates = [
                        cand['text'] for cand in example_json['candidates']
                    ]
                    # candidates = list(set(candidates))
                    filtered = []
                    for i, cand in enumerate(candidates):
                        if cand not in candidates[:i]:
                            filtered.append(cand)
                    candidates = filtered

                # the indices in the dataset are wrong for some examples, so we manually fix them
                span1_index, span1_text = meta['span1_index'], meta[
                    'span1_text']
                span2_index, span2_text = meta['span2_index'], meta[
                    'span2_text']
                words_a = text_a.split()
                words_a_lower = text_a.lower().split()
                words_span1_text = span1_text.lower().split()
                span1_len = len(words_span1_text)

                if words_a_lower[span1_index:span1_index +
                                 span1_len] != words_span1_text:
                    for offset in [-1, +1]:
                        if words_a_lower[span1_index + offset:span1_index +
                                         span1_len +
                                         offset] == words_span1_text:
                            span1_index += offset

                # if words_a_lower[span1_index:span1_index + span1_len] != words_span1_text:
                #     print_rank_0(f"Got '{words_a_lower[span1_index:span1_index + span1_len]}' but expected "
                #                  f"'{words_span1_text}' at index {span1_index} for '{words_a}'")

                if words_a[span2_index] != span2_text:
                    for offset in [-1, +1]:
                        if words_a[span2_index + offset] == span2_text:
                            span2_index += offset

                    if words_a[span2_index] != span2_text and words_a[
                            span2_index].startswith(span2_text):
                        words_a = words_a[:span2_index] \
                                  + [words_a[span2_index][:len(span2_text)], words_a[span2_index][len(span2_text):]] \
                                  + words_a[span2_index + 1:]

                assert words_a[span2_index] == span2_text, \
                    f"Got '{words_a[span2_index]}' but expected '{span2_text}' at index {span2_index} for '{words_a}'"

                text_a = ' '.join(words_a)
                meta['span1_index'], meta[
                    'span2_index'] = span1_index, span2_index

                if cloze_eval and set_type == 'train' and label != 'True':
                    continue
                if set_type == 'train' and 'candidates' in example_json and len(
                        candidates) > 9:
                    for i in range(0, len(candidates), 9):
                        _meta = copy.deepcopy(meta)
                        _meta['candidates'] = candidates[i:i + 9]
                        if len(_meta['candidates']) < 9:
                            _meta['candidates'] += candidates[:9 - len(
                                _meta['candidates'])]
                        example = InputExample(guid=guid,
                                               text_a=text_a,
                                               label=label,
                                               meta=_meta,
                                               idx=idx)
                        examples.append(example)
                else:
                    if 'candidates' in example_json:
                        meta['candidates'] = candidates
                    example = InputExample(guid=guid,
                                           text_a=text_a,
                                           label=label,
                                           meta=meta,
                                           idx=idx)
                    examples.append(example)

        return examples


class BoolQProcessor(SuperGLUEProcessor):
    """Processor for the BoolQ data set."""

    def get_labels(self):
        return ["false", "true"]

    @staticmethod
    def _create_examples(path: str, set_type: str) -> List[InputExample]:
        examples = []

        with open(path, encoding='utf8') as f:
            for line in f:
                example_json = json.loads(line)
                idx = example_json['idx']
                label = str(example_json['label']).lower(
                ) if 'label' in example_json else None
                guid = "%s-%s" % (set_type, idx)
                text_a = punctuation_standardization(example_json['passage'])
                text_b = punctuation_standardization(example_json['question'])
                example = InputExample(guid=guid,
                                       text_a=text_a,
                                       text_b=text_b,
                                       label=label,
                                       idx=idx)
                examples.append(example)

        return examples


class CopaProcessor(SuperGLUEProcessor):
    """Processor for the COPA data set."""

    def get_labels(self):
        return [0, 1]

    def encode(self, example: InputExample, tokenizer, seq_length, args):
        if args.pretrained_bert:
            ids_list, types_list, paddings_list = [], [], []
        else:
            ids_list, positions_list, sep_list = [], [], []
        question = example.meta['question']
        joiner = 'because' if question == 'cause' else 'so'
        text_a = punctuation_standardization(example.text_a) + " " + joiner
        tokens_a = tokenizer.EncodeAsIds(text_a)
        for choice in [example.meta["choice1"], example.meta["choice2"]]:
            choice = punctuation_standardization(choice)
            tokens_b = tokenizer.EncodeAsIds(choice)
            num_special_tokens = num_special_tokens_to_add(tokens_a,
                                                           tokens_b,
                                                           None,
                                                           add_cls=True,
                                                           add_sep=True,
                                                           add_piece=False)
            if len(tokens_a) + len(tokens_b) + num_special_tokens > seq_length:
                self.num_truncated += 1
            data = build_input_from_ids(tokens_a,
                                        tokens_b,
                                        None,
                                        seq_length,
                                        tokenizer,
                                        args,
                                        add_cls=True,
                                        add_sep=True,
                                        add_piece=False)
            ids, types, paddings, position_ids, sep, target_ids, loss_masks = data
            if args.pretrained_bert:
                ids_list.append(ids)
                types_list.append(types)
                paddings_list.append(paddings)
            else:
                ids_list.append(ids)
                positions_list.append(position_ids)
                sep_list.append(sep)
        label = 0
        if example.label is not None:
            label = example.label
            label = self.get_labels().index(label)
        if args.pretrained_bert:
            sample = build_sample(ids_list,
                                  label=label,
                                  types=types_list,
                                  paddings=paddings_list,
                                  unique_id=example.guid)
        else:
            sample = build_sample(ids_list,
                                  positions=positions_list,
                                  masks=sep_list,
                                  label=label,
                                  unique_id=example.guid)
        return sample

    @staticmethod
    def _create_examples(path: str, set_type: str) -> List[InputExample]:
        examples = []

        with open(path, encoding='utf8') as f:
            for line in f:
                example_json = json.loads(line)
                label = example_json[
                    'label'] if 'label' in example_json else None
                idx = example_json['idx']
                guid = "%s-%s" % (set_type, idx)
                text_a = example_json['premise']
                meta = {
                    'choice1': example_json['choice1'],
                    'choice2': example_json['choice2'],
                    'question': example_json['question']
                }
                example = InputExample(guid=guid,
                                       text_a=text_a,
                                       label=label,
                                       meta=meta,
                                       idx=idx)
                examples.append(example)

        if set_type == 'train' or set_type == 'unlabeled':
            mirror_examples = []
            for ex in examples:
                label = 1 if ex.label == 0 else 0
                meta = {
                    'choice1': ex.meta['choice2'],
                    'choice2': ex.meta['choice1'],
                    'question': ex.meta['question']
                }
                mirror_example = InputExample(guid=ex.guid + 'm',
                                              text_a=ex.text_a,
                                              label=label,
                                              meta=meta)
                mirror_examples.append(mirror_example)
            examples += mirror_examples
            print_rank_0(
                f"Added {len(mirror_examples)} mirror examples, total size is {len(examples)}..."
            )
        return examples


class MultiRcProcessor(SuperGLUEProcessor):
    """Processor for the MultiRC data set."""

    def get_labels(self):
        return [0, 1]

    @staticmethod
    def _create_examples(path: str, set_type: str) -> List[InputExample]:
        examples = []

        with open(path, encoding='utf8') as f:
            for line in f:
                example_json = json.loads(line)

                passage_idx = example_json['idx']
                text = punctuation_standardization(
                    example_json['passage']['text'])
                questions = example_json['passage']['questions']
                for question_json in questions:
                    question = punctuation_standardization(
                        question_json["question"])
                    question_idx = question_json['idx']
                    answers = question_json["answers"]
                    for answer_json in answers:
                        label = answer_json[
                            "label"] if 'label' in answer_json else None
                        answer_idx = answer_json["idx"]
                        guid = f'{set_type}-p{passage_idx}-q{question_idx}-a{answer_idx}'
                        meta = {
                            'passage_idx':
                            passage_idx,
                            'question_idx':
                            question_idx,
                            'answer_idx':
                            answer_idx,
                            'answer':
                            punctuation_standardization(answer_json["text"])
                        }
                        idx = [passage_idx, question_idx, answer_idx]
                        example = InputExample(guid=guid,
                                               text_a=text,
                                               text_b=question,
                                               label=label,
                                               meta=meta,
                                               idx=idx)
                        examples.append(example)

        question_indices = list(
            set(example.meta['question_idx'] for example in examples))
        label_distribution = Counter(example.label for example in examples)
        print_rank_0(
            f"Returning {len(examples)} examples corresponding to {len(question_indices)} questions with label "
            f"distribution {list(label_distribution.items())}")
        return examples

    def output_prediction(self, predictions, examples, output_file):
        with open(output_file, "w") as output:
            passage_dict = defaultdict(list)
            for prediction, example in zip(predictions, examples):
                passage_dict[example.meta["passage_idx"]].append(
                    (prediction, example))
            for passage_idx, data in passage_dict.items():
                question_dict = defaultdict(list)
                passage_data = {
                    "idx": passage_idx,
                    "passage": {
                        "questions": []
                    }
                }
                for prediction, example in data:
                    question_dict[example.meta["question_idx"]].append(
                        (prediction, example))
                for question_idx, data in question_dict.items():
                    question_data = {"idx": question_idx, "answers": []}
                    for prediction, example in data:
                        prediction = self.get_labels()[prediction]
                        question_data["answers"].append({
                            "idx":
                            example.meta["answer_idx"],
                            "label":
                            prediction
                        })
                    passage_data["passage"]["questions"].append(question_data)
                output.write(json.dumps(passage_data) + "\n")

    def get_classifier_input(self, example: InputExample, tokenizer):
        text_a = example.text_a
        text_b = ' '.join([example.text_b, "answer:", example.meta['answer']])
        return text_a, text_b


class RaceProcessor(DataProcessor):

    @property
    def variable_num_choices(self):
        return True

    def get_labels(self):
        return ["A", "B", "C", "D"]

    def get_train_examples(self, data_dir):
        return self._create_examples(os.path.join(data_dir, "train"), "train")

    def get_dev_examples(self, data_dir, for_train=False):
        return self._create_examples(os.path.join(data_dir, "dev"),
                                     "dev",
                                     for_train=for_train)

    def get_test_examples(self, data_dir):
        return self._create_examples(os.path.join(data_dir, "test"), "test")

    @staticmethod
    def _create_examples(path,
                         set_type,
                         for_train=False) -> List[InputExample]:
        examples = []

        def clean_text(text):
            """Remove new lines and multiple spaces and adjust end of sentence dot."""

            text = text.replace("\n", " ")
            text = re.sub(r'\s+', ' ', text)
            for _ in range(3):
                text = text.replace(' . ', '. ')

            return text

        filenames = glob.glob(os.path.join(
            path, "middle", '*.txt')) + glob.glob(
                os.path.join(path, "high", "*.txt"))
        for filename in filenames:
            with open(filename, 'r') as f:
                for line in f:
                    data = json.loads(line)
                    idx = data["id"]
                    context = data["article"]
                    questions = data["questions"]
                    choices = data["options"]
                    answers = data["answers"]
                    # Check the length.
                    assert len(questions) == len(answers)
                    assert len(questions) == len(choices)

                    context = clean_text(context)
                    for question_idx, question in enumerate(questions):
                        answer = answers[question_idx]
                        choice = choices[question_idx]
                        guid = f'{set_type}-p{idx}-q{question_idx}'
                        ex_idx = [set_type, idx, question_idx]
                        meta = {"choices": choice}
                        example = InputExample(guid=guid,
                                               text_a=context,
                                               text_b=question,
                                               label=answer,
                                               meta=meta,
                                               idx=ex_idx)
                        examples.append(example)
        return examples


class RecordProcessor(SuperGLUEProcessor):
    """Processor for the ReCoRD data set."""

    def get_dev_examples(self, data_dir, for_train=False):
        return self._create_examples(os.path.join(data_dir, "val.jsonl"),
                                     "dev",
                                     for_train=for_train)

    @property
    def variable_num_choices(self):
        return True

    def get_labels(self):
        return ["0", "1"]

    def output_prediction(self, predictions, examples, output_file):
        with open(output_file, "w") as output:
            for prediction, example in zip(predictions, examples):
                prediction = example.meta["candidates"][prediction]
                data = {"idx": example.idx, "label": prediction}
                output.write(json.dumps(data) + "\n")

    def encode(self, example: InputExample, tokenizer, seq_length, args):
        if args.pretrained_bert:
            ids_list, types_list, paddings_list = [], [], []
        else:
            ids_list, positions_list, sep_list = [], [], []
        tokens_a = tokenizer.EncodeAsIds(example.text_a)
        tokens_b = tokenizer.EncodeAsIds(
            example.text_b) if example.text_b else None
        for answer in example.meta["candidates"]:
            answer_ids = tokenizer.EncodeAsIds(answer)
            total_length = len(tokens_a) + len(tokens_b) + len(answer_ids)
            total_length += num_special_tokens_to_add(tokens_a,
                                                      tokens_b + answer_ids,
                                                      None,
                                                      add_cls=True,
                                                      add_sep=True,
                                                      add_piece=False)
            if total_length > seq_length:
                self.num_truncated += 1
            data = build_input_from_ids(tokens_a,
                                        tokens_b + answer_ids,
                                        None,
                                        seq_length,
                                        tokenizer,
                                        args,
                                        add_cls=True,
                                        add_sep=True,
                                        add_piece=False)
            ids, types, paddings, position_ids, sep, target_ids, loss_masks = data
            if args.pretrained_bert:
                ids_list.append(ids)
                types_list.append(types)
                paddings_list.append(paddings)
            else:
                ids_list.append(ids)
                positions_list.append(position_ids)
                sep_list.append(sep)
        label = example.label
        label = self.get_labels().index(label)
        if args.pretrained_bert:
            sample = build_sample(ids_list,
                                  label=label,
                                  types=types_list,
                                  paddings=paddings_list,
                                  unique_id=example.guid)
        else:
            sample = build_sample(ids_list,
                                  positions=positions_list,
                                  masks=sep_list,
                                  label=label,
                                  unique_id=example.guid)
        return sample

    @staticmethod
    def _create_examples(path,
                         set_type,
                         seed=42,
                         max_train_candidates_per_question: int = 10,
                         for_train=False) -> List[InputExample]:
        examples = []

        entity_shuffler = random.Random(seed)

        with open(path, encoding='utf8') as f:
            for idx, line in enumerate(f):
                example_json = json.loads(line)

                idx = example_json['idx']
                text = punctuation_standardization(
                    example_json['passage']['text'])
                entities = set()

                for entity_json in example_json['passage']['entities']:
                    start = entity_json['start']
                    end = entity_json['end']
                    entity = punctuation_standardization(text[start:end + 1])
                    entities.add(entity)

                entities = list(entities)
                entities.sort()

                text = text.replace(
                    "@highlight\n", "- "
                )  # we follow the GPT-3 paper wrt @highlight annotations
                questions = example_json['qas']

                for question_json in questions:
                    question = punctuation_standardization(
                        question_json['query'])
                    question_idx = question_json['idx']
                    answers = set()

                    for answer_json in question_json.get('answers', []):
                        answer = punctuation_standardization(
                            answer_json['text'])
                        answers.add(answer)

                    answers = list(answers)

                    if set_type == 'train' or for_train:
                        # create a single example per *correct* answer
                        for answer_idx, answer in enumerate(answers):
                            candidates = [
                                ent for ent in entities if ent not in answers
                            ]
                            if len(candidates
                                   ) > max_train_candidates_per_question - 1:
                                entity_shuffler.shuffle(candidates)
                                candidates = candidates[:
                                                        max_train_candidates_per_question
                                                        - 1]

                            guid = f'{set_type}-p{idx}-q{question_idx}-a{answer_idx}'
                            meta = {
                                'passage_idx': idx,
                                'question_idx': question_idx,
                                'candidates': [answer] + candidates,
                                'answers': [answer]
                            }
                            ex_idx = [idx, question_idx, answer_idx]
                            example = InputExample(
                                guid=guid,
                                text_a=text,
                                text_b=question,
                                label="0",
                                meta=meta,
                                idx=ex_idx,
                                num_choices=len(candidates) + 1)
                            examples.append(example)

                    else:
                        # create just one example with *all* correct answers and *all* answer candidates
                        guid = f'{set_type}-p{idx}-q{question_idx}'
                        meta = {
                            'passage_idx': idx,
                            'question_idx': question_idx,
                            'candidates': entities,
                            'answers': answers
                        }
                        example = InputExample(guid=guid,
                                               text_a=text,
                                               text_b=question,
                                               label="1",
                                               meta=meta,
                                               idx=question_idx,
                                               num_choices=len(entities))
                        examples.append(example)

        question_indices = list(
            set(example.meta['question_idx'] for example in examples))
        label_distribution = Counter(example.label for example in examples)
        print_rank_0(
            f"Returning {len(examples)} examples corresponding to {len(question_indices)} questions with label "
            f"distribution {list(label_distribution.items())}")
        return examples


class MnliProcessor(DataProcessor):
    """Processor for the MultiNLI data set (GLUE version)."""

    def get_train_examples(self, data_dir):
        return self._create_examples(os.path.join(data_dir, "train.tsv"),
                                     "train")

    def get_dev_examples(self, data_dir, for_train=False):
        return self._create_examples(os.path.join(data_dir, "dev_matched.tsv"),
                                     "dev_matched")

    def get_test_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(
            os.path.join(data_dir, "test_matched.tsv"), "test_matched")

    def get_unlabeled_examples(self, data_dir) -> List[InputExample]:
        return self.get_train_examples(data_dir)

    def get_labels(self):
        return ["contradiction", "entailment", "neutral"]

    @staticmethod
    def _create_examples(path: str, set_type: str) -> List[InputExample]:
        examples = []
        df = read_tsv(path)

        for idx, row in df.iterrows():
            guid = f"{set_type}-{idx}"
            text_a = punctuation_standardization(row['sentence1'])
            text_b = punctuation_standardization(row['sentence2'])
            label = row.get('gold_label', None)
            example = InputExample(guid=guid,
                                   text_a=text_a,
                                   text_b=text_b,
                                   label=label)
            examples.append(example)

        return examples


class CLUEProcessor(DataProcessor):

    def get_train_examples(self, data_dir):
        return self._create_examples(os.path.join(data_dir, "train.json"),
                                     "train")

    def get_dev_examples(self, data_dir, for_train=False):
        return self._create_examples(os.path.join(data_dir, "dev.json"), "dev")

    def get_test_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, "test.json"),
                                     "test")

    def output_prediction(self, predictions, examples, output_file):
        indices = list(range(len(predictions)))
        indices.sort(key=lambda x: examples[x].idx)
        with open(output_file, "w") as output:
            for idx in indices:
                prediction = self.get_labels()[predictions[idx]]
                data = {"idx": examples[idx].idx, "label": prediction}
                output.write(json.dumps(data) + "\n")

    def encode(self, example: InputExample, tokenizer, seq_length, args):
        text_a, text_b = self.get_classifier_input(example, tokenizer)
        tokens_a = tokenizer.EncodeAsIds(text_a)  # ids of tokens_a
        num_special_tokens = num_special_tokens_to_add(
            tokens_a, None, None, add_cls=True, add_sep=True,
            add_piece=False)  # number of special tokens
        if len(tokens_a) + num_special_tokens > seq_length:
            self.num_truncated += 1
        data = build_input_from_ids(tokens_a,
                                    None,
                                    None,
                                    seq_length,
                                    tokenizer,
                                    args=args,
                                    add_cls=True,
                                    add_sep=True,
                                    add_piece=False)
        ids, types, paddings, position_ids, sep, target_ids, loss_masks = data
        label = 0
        if example.label is not None:
            label = example.label
            label = self.get_labels().index(label)
        if args.pretrained_bert:

            sample = build_sample(ids,
                                  label=label,
                                  types=types,
                                  paddings=paddings,
                                  unique_id=example.guid,
                                  meta=example.meta)
        else:
            sample = build_sample(ids,
                                  positions=position_ids,
                                  masks=sep,
                                  label=label,
                                  unique_id=example.guid,
                                  meta=example.meta)
        return sample


class TNewsProcessor(CLUEProcessor):
    """Processor for the TNews data set (CLUE version)."""

    def get_labels(self):
        return [
            "100", "101", "102", "103", "104", "106", "107", "108", "109",
            "110", "112", "113", "114", "115", "116"
        ]

    @staticmethod
    def _create_examples(path: str, set_type: str) -> List[InputExample]:
        examples = []

        with open(path) as file:
            for idx, line in enumerate(file):
                guid = f"{set_type}-{idx}"
                data = json.loads(line)
                text_a = data["sentence"]
                text_b = data['keywords']
                label = data.get('label', None)
                example = InputExample(guid=guid,
                                       text_a=text_a,
                                       text_b=text_b,
                                       label=label,
                                       idx=idx)
                examples.append(example)

        return examples


class AFQMCProcessor(CLUEProcessor):
    """Processor for the AFQMC data set (CLUE version)."""

    def get_labels(self):
        return ["0", "1"]

    @staticmethod
    def _create_examples(path: str, set_type: str) -> List[InputExample]:
        examples = []

        with open(path) as file:
            for idx, line in enumerate(file):
                guid = f"{set_type}-{idx}"
                data = json.loads(line)
                text_a = data["sentence1"]
                text_b = data['sentence2']
                label = data.get('label', None)
                example = InputExample(guid=guid,
                                       text_a=text_a,
                                       text_b=text_b,
                                       label=label,
                                       idx=idx)
                examples.append(example)

        return examples


class MnliMismatchedProcessor(MnliProcessor):
    """Processor for the MultiNLI mismatched data set (GLUE version)."""

    def get_dev_examples(self, data_dir, for_train=False):
        return self._create_examples(
            os.path.join(data_dir, "dev_mismatched.tsv"), "dev_mismatched")

    def get_test_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(
            os.path.join(data_dir, "test_mismatched.tsv"), "test_mismatched")


class AgnewsProcessor(DataProcessor):
    """Processor for the AG news data set."""

    def get_train_examples(self, data_dir):
        return self._create_examples(os.path.join(data_dir, "train.csv"),
                                     "train")

    def get_dev_examples(self, data_dir, for_train=False):
        return self._create_examples(os.path.join(data_dir, "test.csv"), "dev")

    def get_test_examples(self, data_dir) -> List[InputExample]:
        raise NotImplementedError()

    def get_unlabeled_examples(self, data_dir) -> List[InputExample]:
        return self.get_train_examples(data_dir)

    def get_labels(self):
        return ["1", "2", "3", "4"]

    @staticmethod
    def _create_examples(path: str, set_type: str) -> List[InputExample]:
        examples = []

        with open(path) as f:
            reader = csv.reader(f, delimiter=',')
            for idx, row in enumerate(reader):
                label, headline, body = row
                guid = "%s-%s" % (set_type, idx)
                text_a = punctuation_standardization(
                    headline.replace('\\', ' '))
                text_b = punctuation_standardization(body.replace('\\', ' '))

                example = InputExample(guid=guid,
                                       text_a=text_a,
                                       text_b=text_b,
                                       label=label)
                examples.append(example)

        return examples


class YahooAnswersProcessor(DataProcessor):
    """Processor for the Yahoo Answers data set."""

    def get_train_examples(self, data_dir):
        return self._create_examples(os.path.join(data_dir, "train.csv"),
                                     "train")

    def get_dev_examples(self, data_dir, for_train=False):
        return self._create_examples(os.path.join(data_dir, "test.csv"), "dev")

    def get_test_examples(self, data_dir) -> List[InputExample]:
        raise NotImplementedError()

    def get_unlabeled_examples(self, data_dir) -> List[InputExample]:
        return self.get_train_examples(data_dir)

    def get_labels(self):
        return ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    @staticmethod
    def _create_examples(path: str, set_type: str) -> List[InputExample]:
        examples = []

        with open(path, encoding='utf8') as f:
            reader = csv.reader(f, delimiter=',')
            for idx, row in enumerate(reader):
                label, question_title, question_body, answer = row
                guid = "%s-%s" % (set_type, idx)
                text_a = ' '.join([
                    question_title.replace('\\n', ' ').replace('\\', ' '),
                    question_body.replace('\\n', ' ').replace('\\', ' ')
                ])
                text_a = punctuation_standardization(text_a)
                text_b = answer.replace('\\n', ' ').replace('\\', ' ')
                text_b = punctuation_standardization(text_b)

                example = InputExample(guid=guid,
                                       text_a=text_a,
                                       text_b=text_b,
                                       label=label)
                examples.append(example)

        return examples


class YelpPolarityProcessor(DataProcessor):
    """Processor for the YELP binary classification set."""

    def get_train_examples(self, data_dir):
        return self._create_examples(os.path.join(data_dir, "train.csv"),
                                     "train")

    def get_dev_examples(self, data_dir, for_train=False):
        return self._create_examples(os.path.join(data_dir, "test.csv"), "dev")

    def get_test_examples(self, data_dir) -> List[InputExample]:
        raise NotImplementedError()

    def get_unlabeled_examples(self, data_dir) -> List[InputExample]:
        return self.get_train_examples(data_dir)

    def get_labels(self):
        return ["1", "2"]

    @staticmethod
    def _create_examples(path: str, set_type: str) -> List[InputExample]:
        examples = []

        with open(path) as f:
            reader = csv.reader(f, delimiter=',')
            for idx, row in enumerate(reader):
                label, body = row
                guid = "%s-%s" % (set_type, idx)
                text_a = body.replace('\\n', ' ').replace('\\', ' ')
                text_a = punctuation_standardization(text_a)

                example = InputExample(guid=guid, text_a=text_a, label=label)
                examples.append(example)

        return examples


class YelpFullProcessor(YelpPolarityProcessor):
    """Processor for the YELP full classification set."""

    def get_test_examples(self, data_dir) -> List[InputExample]:
        raise NotImplementedError()

    def get_labels(self):
        return ["1", "2", "3", "4", "5"]


class XStanceProcessor(DataProcessor):
    """Processor for the X-Stance data set."""

    def __init__(self, args, language: str = None):
        super().__init__(args)
        if language is not None:
            assert language in ['de', 'fr']
        self.language = language

    def get_train_examples(self, data_dir):
        return self._create_examples(os.path.join(data_dir, "train.jsonl"))

    def get_dev_examples(self, data_dir, for_train=False):
        return self._create_examples(os.path.join(data_dir, "test.jsonl"))

    def get_test_examples(self, data_dir) -> List[InputExample]:
        raise NotImplementedError()

    def get_unlabeled_examples(self, data_dir) -> List[InputExample]:
        return self.get_train_examples(data_dir)

    def get_labels(self):
        return ["FAVOR", "AGAINST"]

    def _create_examples(self, path: str) -> List[InputExample]:
        examples = []

        with open(path, encoding='utf8') as f:
            for line in f:
                example_json = json.loads(line)
                label = example_json['label']
                id_ = example_json['id']
                text_a = punctuation_standardization(example_json['question'])
                text_b = punctuation_standardization(example_json['comment'])
                language = example_json['language']

                if self.language is not None and language != self.language:
                    continue

                example = InputExample(guid=id_,
                                       text_a=text_a,
                                       text_b=text_b,
                                       label=label)
                examples.append(example)

        return examples


class Sst2Processor(DataProcessor):

    def get_train_examples(self, data_dir):
        return self._create_examples(os.path.join(data_dir, "train.tsv"),
                                     "train")

    def get_dev_examples(self, data_dir, for_train=False):
        return self._create_examples(os.path.join(data_dir, "dev.tsv"), "dev")

    def get_test_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, "test.tsv"),
                                     "test")

    def get_labels(self):
        return ["0", "1"]

    @staticmethod
    def _create_examples(path: str, set_type: str) -> List[InputExample]:
        examples = []
        df = read_tsv(path)

        for idx, row in df.iterrows():
            guid = f"{set_type}-{idx}"
            text_a = punctuation_standardization(row['sentence'])
            label = row.get('label', None)
            example = InputExample(guid=guid, text_a=text_a, label=label)
            examples.append(example)

        return examples


class ColaProcessor(Sst2Processor):

    def get_labels(self):
        return ["0", "1"]

    @staticmethod
    def _create_examples(path: str, set_type: str) -> List[InputExample]:
        examples = []
        if set_type != 'test':
            df = read_tsv(path, header=None)
        else:
            df = read_tsv(path)

        for idx, row in df.iterrows():
            guid = f"{set_type}-{idx}"
            if set_type != 'test':
                text_a = punctuation_standardization(row[3])
                label = row[1]
            else:
                text_a = punctuation_standardization(row['sentence'])
                label = None
            example = InputExample(guid=guid, text_a=text_a, label=label)
            examples.append(example)

        return examples


class MrpcProcessor(Sst2Processor):

    def get_labels(self):
        return ["0", "1"]

    @staticmethod
    def _create_examples(path: str, set_type: str) -> List[InputExample]:
        examples = []
        df = read_tsv(path)

        for idx, row in df.iterrows():
            guid = f"{set_type}-{idx}"
            text_a = punctuation_standardization(row['#1 String'])
            text_b = punctuation_standardization(row['#2 String'])
            label = row.get('Quality', None)
            example = InputExample(guid=guid,
                                   text_a=text_a,
                                   text_b=text_b,
                                   label=label)
            examples.append(example)

        return examples


class QqpProcessor(Sst2Processor):

    def get_labels(self):
        return ["0", "1"]

    @staticmethod
    def _create_examples(path: str, set_type: str) -> List[InputExample]:
        examples = []
        df = read_tsv(path)

        for idx, row in df.iterrows():
            guid = f"{set_type}-{idx}"
            text_a = punctuation_standardization(row['question1'])
            text_b = punctuation_standardization(row['question2'])
            label = row.get('is_duplicate', None)
            example = InputExample(guid=guid,
                                   text_a=text_a,
                                   text_b=text_b,
                                   label=label)
            examples.append(example)

        return examples


class QnliProcessor(Sst2Processor):

    def get_labels(self):
        return ["entailment", "not_entailment"]

    @staticmethod
    def _create_examples(path: str, set_type: str) -> List[InputExample]:
        examples = []
        df = read_tsv(path)

        for idx, row in df.iterrows():
            guid = f"{set_type}-{idx}"
            text_a = punctuation_standardization(row['question'])
            text_b = punctuation_standardization(row['sentence'])
            label = row.get('label', None)
            example = InputExample(guid=guid,
                                   text_a=text_a,
                                   text_b=text_b,
                                   label=label)
            examples.append(example)

        return examples


class SquadProcessor(DataProcessor):

    def get_train_examples(self, data_dir):
        return self._create_examples(os.path.join(data_dir, "train-v2.0.json"),
                                     "train")

    def get_dev_examples(self, data_dir, for_train=False):
        return self._create_examples(os.path.join(data_dir, "dev-v2.0.json"),
                                     "dev")

    def get_labels(self):
        return ['0']

    @staticmethod
    def _create_examples(path: str, set_type: str) -> List[InputExample]:
        examples = []
        with open(path) as f:
            data = json.load(f)['data']

        for idx, passage in enumerate(data):
            for pid, paragraph in enumerate(passage['paragraphs']):
                context = paragraph['context']
                for qid, qas in enumerate(paragraph['qas']):
                    if len(qas['answers']) == 0:
                        continue
                    guid = f"{set_type}-{idx}-{pid}-{qid}"
                    example = InputExample(guid=guid,
                                           text_a=context,
                                           text_b=qas['question'],
                                           label='0',
                                           meta={'answer': qas['answers'][0]})
                    examples.append(example)

        return examples


class CLUEWSCProcessor(DataProcessor):

    def get_train_examples(self, data_dir):
        return self._create_examples(os.path.join(data_dir, "train.json"),
                                     "train")

    def get_dev_examples(self, data_dir, for_train=False):
        return self._create_examples(os.path.join(data_dir, "dev.json"), "dev")

    def get_test_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, "test.json"),
                                     "test")

    def get_labels(self):
        return ["false", "true"]

    def _create_examples(self,
                         path: str,
                         set_type: str,
                         cloze_eval=True) -> List[InputExample]:
        examples = []

        with open(path, encoding='utf8') as f:
            for line in f:
                example_json = json.loads(line)
                idx = example_json[
                    'id'] if 'id' in example_json else example_json['idx']
                label = example_json[
                    'label'] if 'label' in example_json else None
                guid = "%s-%s" % (set_type, idx)
                text_a = example_json['text']

                meta = {
                    'span1_text': example_json['target']['span1_text'],
                    'span2_text': example_json['target']['span2_text'],
                    'span1_index': example_json['target']['span1_index'],
                    'span2_index': example_json['target']['span2_index'],
                }
                meta['span1_length'] = len(meta['span1_text'])
                meta['span2_length'] = len(meta['span2_text'])

                example = InputExample(guid=guid,
                                       text_a=text_a,
                                       text_b=meta['span1_index'],
                                       label=label,
                                       meta=meta,
                                       idx=idx)
                examples.append(example)

        return examples


class CMRCProcessor(DataProcessor):

    def get_train_examples(self, data_dir):
        return self._create_examples(os.path.join(data_dir, "train.json"),
                                     "train")

    def get_dev_examples(self, data_dir, for_train=False):
        return self._create_examples(os.path.join(data_dir, "dev.json"), "dev")

    def get_test_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, "test.json"),
                                     "test")

    def get_labels(self):
        return ['0']

    @staticmethod
    def _create_examples(path: str, set_type: str) -> List[InputExample]:
        examples = []
        with open(path) as f:
            data_dcts = json.load(f)
        for k in data_dcts['data']:
            data = k['paragraphs'][0]
            idx = data["id"]
            if set_type == "train":
                idx = int(idx[6:])
            elif set_type == "dev":
                idx = int(idx[4:])
            elif set_type == "test":
                idx = int(idx[6:])
            else:
                raise NotImplementedError("set_type=" + str(set_type))
            text_a = data["context"]
            qa_set = data["qas"]

            for qid, qa in enumerate(qa_set):
                text_b = qa['question']
                ans = qa['answers'][0]
                guid = f"{set_type}-{idx}-{qid}"
                example = InputExample(guid=guid,
                                       text_a=text_a,
                                       text_b=text_b,
                                       label='0',
                                       meta={'answer': ans})
                examples.append(example)
        return examples


class WankeProcessor(CLUEProcessor):
    """Processor for the TNews data set (CLUE version)."""

    def get_train_examples(self, data_dir):
        return self._create_examples(os.path.join(data_dir, "train.tsv"),
                                     "train")

    def get_dev_examples(self, data_dir, for_train=False):
        return self._create_examples(os.path.join(data_dir, "dev.tsv"), "dev")

    def get_test_examples(self, data_dir) -> List[InputExample]:
        return self._create_examples(os.path.join(data_dir, "test.tsv"),
                                     "test")

    def get_unlabeled_examples(self, data_dir) -> List[InputExample]:
        return self.get_train_examples(data_dir)

    def get_labels(self):
        return ["0", "1", "2"]

    @staticmethod
    def _create_examples(path: str, set_type: str) -> List[InputExample]:
        examples = []

        with open(path, encoding="GBK") as fin:
            for idx, line in enumerate(fin):
                if idx == 0:
                    continue
                guid = f"{set_type}-{idx}"
                items = [e.strip() for e in line.split('\t')]
                text_a = items[0]
                label = items[1]
                example = InputExample(guid=guid,
                                       text_a=text_a,
                                       label=str(label),
                                       idx=idx)
                examples.append(example)
        return examples


class CRMC2018Processor(SuperGLUEProcessor):
    """Processor for the MultiRC data set."""

    def get_labels(self):
        return [0, 1]

    @staticmethod
    def _create_examples(path: str, set_type: str) -> List[InputExample]:
        examples = []

        with open(path, encoding='utf8') as f:
            for line in f:
                example_json = json.loads(line)

                passage_idx = example_json['idx']
                text = punctuation_standardization(
                    example_json['passage']['text'])
                questions = example_json['passage']['questions']
                for question_json in questions:
                    question = punctuation_standardization(
                        question_json["question"])
                    question_idx = question_json['idx']
                    answers = question_json["answers"]
                    for answer_json in answers:
                        label = answer_json[
                            "label"] if 'label' in answer_json else None
                        answer_idx = answer_json["idx"]
                        guid = f'{set_type}-p{passage_idx}-q{question_idx}-a{answer_idx}'
                        meta = {
                            'passage_idx':
                            passage_idx,
                            'question_idx':
                            question_idx,
                            'answer_idx':
                            answer_idx,
                            'answer':
                            punctuation_standardization(answer_json["text"])
                        }
                        idx = [passage_idx, question_idx, answer_idx]
                        example = InputExample(guid=guid,
                                               text_a=text,
                                               text_b=question,
                                               label=label,
                                               meta=meta,
                                               idx=idx)
                        examples.append(example)

        question_indices = list(
            set(example.meta['question_idx'] for example in examples))
        label_distribution = Counter(example.label for example in examples)
        print_rank_0(
            f"Returning {len(examples)} examples corresponding to {len(question_indices)} questions with label "
            f"distribution {list(label_distribution.items())}")
        return examples

    def output_prediction(self, predictions, examples, output_file):
        with open(output_file, "w") as output:
            passage_dict = defaultdict(list)
            for prediction, example in zip(predictions, examples):
                passage_dict[example.meta["passage_idx"]].append(
                    (prediction, example))
            for passage_idx, data in passage_dict.items():
                question_dict = defaultdict(list)
                passage_data = {
                    "idx": passage_idx,
                    "passage": {
                        "questions": []
                    }
                }
                for prediction, example in data:
                    question_dict[example.meta["question_idx"]].append(
                        (prediction, example))
                for question_idx, data in question_dict.items():
                    question_data = {"idx": question_idx, "answers": []}
                    for prediction, example in data:
                        prediction = self.get_labels()[prediction]
                        question_data["answers"].append({
                            "idx":
                            example.meta["answer_idx"],
                            "label":
                            prediction
                        })
                    passage_data["passage"]["questions"].append(question_data)
                output.write(json.dumps(passage_data) + "\n")

    def get_classifier_input(self, example: InputExample, tokenizer):
        text_a = example.text_a
        text_b = ' '.join([example.text_b, "answer:", example.meta['answer']])
        return text_a, text_b

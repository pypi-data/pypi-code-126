import argparse
import sys
import tempfile
import uuid
from pathlib import Path
from typing import Dict, List, Tuple

import speech_recognition as sr  # type: ignore
from pydub import AudioSegment  # type: ignore


from vst.classes.languages import LanguageToLanguageTag  # type: ignore
from vst.classes.shell import Shell  # type: ignore
from vst.classes.wavfile import WavFile  # type: ignore


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-e', '--error', action='store_true', required=False,
        help='Delete files for which the transcription cannot be recognized',
    )
    parser.add_argument(
        '-i', '--input', action='store', required=True, type=Path,
        help='Path to folder with WAVs files',
    )
    parser.add_argument(
        '-l', '--language', action='store', required=False, type=str, default='Polish',
        help='Language name. Read README.md file to know all languages',
    )
    parser.add_argument(
        '-m', '--multi', action='store_true', required=False, default=False,
        help='Generate list with default voice ID == 0',
    )
    parser.add_argument(
        '-o', '--output', action='store', required=True, type=Path,
        help='Path to the folder where training and validation files will be saved',
    )
    parser.add_argument(
        '-p', '--percent', action='store', required=False, type=int, default=0,
        help='Path to folder with WAVs files',
    )
    parser.add_argument(
        '-r', '--recursive', action='store_true', required=False,
        help='Find files also in subdirectories of input path',
    )
    parser.add_argument(
        '-s', '--short-paths', action='store_true', required=False, default=False,
        help='Save short paths to files using only last folder name and filename',
    )
    parser.add_argument(
        '-t', '--time', action='store', required=False, type=str,
        help='Delete files that are outside the given time range (i.e: 2-12.5)',
    )
    parser.add_argument(
        '-v', '--verbose', action='store_true', required=False,
        help='Show information while the script is running',
    )
    return parser.parse_args()


def split_files_for_training_and_validation(files: List[Path], percent: int) -> Tuple[List[Path], List[Path]]:
    list_of_files = list(files)
    number_of_training_files = int((len(list_of_files) / 100) * percent + 0.5)
    number_of_validation_files = number_of_training_files if number_of_training_files > 2 else 2
    return list_of_files[number_of_validation_files:len(list_of_files)], list_of_files[:number_of_validation_files]


def remove_if_file_duration_not_in_range(wav_file: WavFile, time_range: str):
    time_range_examples_message = \
        '  Examples:\n' \
        '  -t 2-10        minimum: 2 seconds                     - maximum: 10 seconds\n' \
        '  -t 2.10-10     minimum: 2 seconds and 100 miliseconds - maximum: 10 seconds\n' \
        '  -t 2-10.3      minimum: 2 seconds                     - maximum: 10 seconds and 300 miliseconds\n' \
        '  -t 2.5-10.4    minimum: 2 seconds and 500 miliseconds - maximum: 10 seconds and 400 miliseconds\n'

    def wrong_number_of_time_range_elements(error: ValueError):
        print(
            f'\n  Error: {error}\n'
            '\n  Solution: Format your time range using minimum and maximum time in one of formats:\n\n'
            '  Format: \n      minimum_second[.miliseconds]-maximum_second[.miliseconds]\n\n'
            f'{time_range_examples_message}'
        )
        sys.exit(1)

    def wrong_order_of_time_range_elements():
        print(
            '\n  Error: The minimum time range must be less than the maximum time range.\n\n'
            f'{time_range_examples_message}'
        )
        sys.exit(2)

    minimum, maximum = -2, -1
    try:
        minimum, maximum = (float(seconds) for seconds in time_range.split('-'))
    except ValueError as error:
        wrong_number_of_time_range_elements(error)
    except AttributeError as error:
        print(error)

    if (minimum > maximum) or (minimum == maximum):
        wrong_order_of_time_range_elements()

    if not minimum <= float(wav_file.get_file_duration()) <= maximum:
        wav_file.path_to_wav_file.unlink()


def get_text_from_wav_file(path: Path, language: str, error: bool = False) -> str:
    r = sr.Recognizer()
    language_tag = str(LanguageToLanguageTag(language))
    silence = AudioSegment.silent(duration=1000)
    wav_content = AudioSegment.from_wav(path)
    new_content = silence + wav_content + silence
    path_to_temporary_file = Path(tempfile.gettempdir()) / f'{str(uuid.uuid4())[-12:]}.wav'
    new_content.export(path_to_temporary_file, format='wav')

    with sr.AudioFile(str(path_to_temporary_file)) as file:
        audio = r.record(file)
        try:
            text = r.recognize_google(audio, language=language_tag)
        except sr.UnknownValueError:
            if error:
                text = "<< Text wasn't recognized! File was removed!"
                Path(path).unlink()
            else:
                text = f"<< Text wasn't recognized! Are you sure that the language used in the wav file is {language} ? >>"

    path_to_temporary_file.unlink()
    return text


def get_dialogs_from_files(paths: List[Path], arguments: argparse.Namespace) -> Dict[Path, str]:
    dialogs = {}
    wav_file = WavFile()

    for index, path in enumerate(paths, start=1):
        wav_file.open(path)
        file_duration = wav_file.get_formatted_length()

        if arguments.time:
            remove_if_file_duration_not_in_range(wav_file, arguments.time)

        if not path.exists():
            print(f'{index:5}: {file_duration:14} {Path(path).name:50} FILE REMOVED!')
            continue

        text = get_text_from_wav_file(Path(path), arguments.language, arguments.error)
        if arguments.verbose:
            print(f'{index:5}: {file_duration:14} {Path(path).name:50} {text}')
        dialogs[Path(path)] = text
    return dialogs


def convert_dialogs_to_file_content(dialogs: Dict[Path, str], short_paths: bool = False, multi: bool = False) -> str:
    content = ''
    multi_content = '|0' if multi else ''

    for dialog in dialogs:
        if short_paths:
            path = str(dialog).replace(str(dialog.parents[1]), '').lstrip('/').lstrip('\\')
        else:
            path = dialog

        text = dialogs[dialog].replace('\n', '')
        content += f'{path}|{text}.{multi_content}\n'
    return content


def save_content_to_file(path: Path, content: str) -> None:
    with open(path, 'w', encoding='utf8') as file:
        file.write(content)


def wav_to_text() -> None:
    arguments = parse_arguments()

    shell = Shell()
    wav_files_paths = shell.get_files_by_extensions(arguments.input, ['wav'], arguments.recursive)

    if arguments.percent == 0:
        training_files = wav_files_paths
        validation_files = []
    elif 0 < arguments.percent < 100:
        training_files, validation_files = split_files_for_training_and_validation(wav_files_paths, arguments.percent)
    else:
        print('The value of param "percent" should be between 0 and 99 percent')
        exit(2)

    operations = {
        'training': training_files,
        'validation': validation_files,
    }

    if arguments.verbose:
        message = f'''
        \r    Number of wav files: {len(training_files) + len(validation_files)}
        \r         Training files: {len(training_files)}
        \r       Validation files: {len(validation_files)}
        \r         Using language: {LanguageToLanguageTag(arguments.language).selected_language}
        \r              Recursive: {'Yes' if arguments.recursive else 'No'}'''
        print(message)

    if not Path(arguments.output).exists():
        shell.mkdir(arguments.output, parent=True)

    for operation in operations:
        files = operations[operation]
        if len(files) > 0:
            if arguments.verbose:
                print(f'\n => Converting {operation} files ({len(files)} files)')
            dialogs = get_dialogs_from_files(files, arguments)
            file_content = convert_dialogs_to_file_content(dialogs, arguments.short_paths, arguments.multi)
            save_content_to_file(Path(arguments.output) / f'{operation}.txt', file_content)


def main() -> None:
    try:
        wav_to_text()
    except KeyboardInterrupt:
        print(' <= Application terminated by the user\n')
        exit(0)


if __name__ == '__main__':
    main()

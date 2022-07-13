import ast
import json
import time
import glob
import unicodedata
from multiprocessing import Process
import os
import shutil
import pandas as pd
import streamlit.components.v1 as component
from googletrans import Translator
from dateutil.parser import parse


class StreamlitUtils:
    def __init__(self, st_session):
        self.__st = st_session

    def __get_user_tab_selection(self, tabs, set_tab):
        if set_tab is None:
            query_params = self.__st.experimental_get_query_params()
            if "tab" in query_params:
                active_tab = query_params["tab"][0]
                return active_tab
            else:
                active_tab = tabs[0]
            if active_tab in tabs:
                self.__st.experimental_set_query_params(tab=tabs[0])
                active_tab = tabs[0]
                return active_tab
        else:
            return set_tab

    def build_tabs_html(self, tabs, set_tab=None):
        current_tab = self.__get_user_tab_selection(tabs, set_tab)
        self.__st.markdown(
            '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" '
            'integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" '
            'crossorigin="anonymous">',
            unsafe_allow_html=True,
        )
        li_items = "".join(
            f"""
                <li class="nav-item">
                    <a class="nav-link{' active' if t == current_tab else ''}" href="/?tab={t}">{t}</a>
                </li>
                """
            for t in tabs
        )
        tabs_html = f"""
                <ul class="nav nav-tabs">
                {li_items}
                </ul>
            """
        self.__st.markdown(tabs_html, unsafe_allow_html=True)
        return current_tab

    def set_component(self, obj: str, css: str = None, js_component: bool = False, height: int = 100, width: int = 1000,
                      scrolling: bool = True):
        if not js_component:
            if css:
                self.__st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
            self.__st.markdown(obj, unsafe_allow_html=True)
        else:
            component.html(obj, height=height, width=width, scrolling=scrolling)

    def __generate_columns(self, columns_count: int, column_width: int):
        if columns_count > 1:
            index = 0
            columns = []
            while index < columns_count:
                columns.append(column_width)
                index += 1
        else:
            columns = [columns_count, column_width]
        return self.__st.columns(columns)

    def create_columns_data(self, data, column_width: int = 6):
        temp_list = []
        columns_count = len(data)
        for d, col in zip(data, self.__generate_columns(columns_count, column_width)):
            temp_list.append({f'{d[0]}': col.radio(label=d[0], options=d[1])})
        return temp_list

    def initial_session_state(self, items: list):
        for item in items:
            self.__st.session_state.setdefault(item[0], item[1])
        return self.__st.session_state


class PyPIArtifact:
    def __init__(self, main_path, user=None, password=None):
        self.__dist_dir = f"{main_path}/dist"
        if user is not None:
            self.__user = user
            self.__password = password
        else:
            self.__user = os.environ.get('pypi-user')
            self.__password = os.environ.get('pypi-password')
        self.__build_commands = self.__build_terminal_commands

    @property
    def __build_terminal_commands(self):
        return ["python setup.py develop", "python -m pip install --upgrade pip",
                "python -m pip install --upgrade build", "python -m build", "python setup.py sdist bdist_wheel"]

    @property
    def __upload_terminal_command(self):
        return f"twine upload -u {self.__user} -p {self.__password}" \
               f" --repository-url https://upload.pypi.org/legacy/ dist/*"

    def __delete_dist_dir(self):
        if os.path.exists(self.__dist_dir) and os.path.isdir(self.__dist_dir):
            shutil.rmtree(self.__dist_dir)
        else:
            print("The dist directory does not exist")

    def __build(self):
        for command in self.__build_commands:
            os.system(command)

    def __upload(self):
        os.system(self.__upload_terminal_command)

    def run(self):
        self.__delete_dist_dir()
        self.__build()
        self.__upload()


class RunningFramework:
    def __init__(self, app_session: Process, before: dict = None, join_session: bool = False):
        self.__before_session = before
        self.__app_session = app_session
        self.__join_session = join_session
        self.__tasks = self.__session_tasks()

    @property
    def get_session_tasks(self):
        return self.__tasks

    @property
    def is_alive(self):
        return self.__app_session.is_alive()

    def kill(self):
        return self.__after()

    def run_session(self):
        next(self.__tasks)  # before all
        next(self.__tasks)  # running session
        next(self.__tasks)  # after all

    def __session_tasks(self):
        self.__before()
        yield
        self.__running()
        yield
        self.__after()
        yield

    def __before(self):
        print('Start App Session')
        session = []
        if self.__before_session is not None:
            for before in self.__before_session.items():
                before[1].start()
                session.append(before[1])
            self.__before_session = session

    def __running(self):
        print(f'{self.__app_session.name} is running..')
        self.__app_session.start()
        if self.__join_session:
            self.__app_session.join()
            self.__after()

    def __after(self):
        for process in self.__before_session:
            if type(process) is Process:
                if process.is_alive():
                    process.kill()
                print(f"{process.name} closed successfully")
            if self.__app_session.is_alive():
                self.__app_session.kill()
            print(f"{self.__app_session.name} closed successfully")
        print('End App Session')


class RunParallel:
    @staticmethod
    def run_multi_process(function_target, count_of_process: int = 1, args: list = None):
        start = time.perf_counter()
        process_index = 0
        process_list = []
        while process_index < count_of_process:
            if args is not None:
                process_list.append(Process(target=function_target, args=args[process_index]))
            else:
                process_list.append(Process(target=function_target))
            process_index += 1

        for process in process_list:
            process.start()

        for process in process_list:
            process.join()

        finish = time.perf_counter()
        print(f'Finished in {round(finish - start, 2)} second(s)')


class UnusedDependencies:
    def __init__(self, main_path: str, venv_path: str, requirements_file_name: str = 'requirements.txt',
                 ignore_files: tuple = None, ignore_current_requirements: bool = False):
        self.__main_path = main_path
        self.__venv_path = venv_path
        self.__ignore_current_requirements = ignore_current_requirements
        self.__current_dependencies = self.get_dependencies(path=f"{self.__main_path}/{requirements_file_name}")
        self.__temp_requirements = f"{self.__main_path}/final_requirements.txt"
        self.__venv_size = self.__get_venv_size(path=self.__venv_path)

    @property
    def __ignore_files(self):
        return 'site-packages', 'env', 'setup', 'py_import_validation.py', \
               'delete_unnecessary_libraries.py', 'delete_unused_libraries.py'

    @property
    def __test_dependencies(self):
        if self.__ignore_current_requirements:
            return self.get_dependencies(path=self.__temp_requirements, ignore_dependencies=self.__current_dependencies)
        else:
            return self.get_dependencies(path=self.__temp_requirements)

    @property
    def __all_imports(self, iterations: int = 10):
        python_files = []
        main_depth = '/*'

        def ignore_file(py_f):
            ignore = self.__ignore_files
            for ig_f in ignore:
                if ig_f in py_f:
                    return True

        while iterations > 0:
            iterations += -1
            files = glob.glob(f"{self.__main_path}{main_depth}.py")
            for file in files:
                if not ignore_file(file):
                    python_files.append(file)
            main_depth += '/*'
        return python_files

    @property
    def __import_python_syntax(self):
        python_files = self.__all_imports
        py_syntax = ''
        for py_file in python_files:
            py_syntax = self.is_valid_python_file(py_file, py_syntax)
        return py_syntax

    def __calculate_venv_size(self, path: str):
        total = 0
        with os.scandir(path) as it:
            for entry in it:
                if entry.is_file():
                    total += entry.stat().st_size
                elif entry.is_dir():
                    total += self.__calculate_venv_size(entry.path)
        return total

    def __get_venv_size(self, path: str, suffix="B"):
        num = self.__calculate_venv_size(path)
        for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
            if abs(num) < 1024.0:
                return f"{num:3.1f}{unit}{suffix}"
            num /= 1024.0
        return f"{num:.1f} Yi{suffix}"

    @staticmethod
    def get_dependencies(path, ignore_dependencies: list = None):
        dependencies = []
        if os.path.isfile(path):
            with open(path, 'r') as f:
                dependencies = f.read().splitlines()
        if not ignore_dependencies:
            return dependencies
        organize_dependencies = []
        ignore_dependencies = str(ignore_dependencies)
        for depend in dependencies:
            var = depend.split('==')[0]
            if var not in ignore_dependencies and depend not in ignore_dependencies:
                organize_dependencies.append(depend)
        return organize_dependencies

    @staticmethod
    def is_valid_python_file(file_path, py_file_syntax):
        with open(file_path, 'r') as fp:
            contents = fp.read()
        try:
            ast.parse(contents)
            import_list = compile(contents, file_path, 'exec', ast.PyCF_ONLY_AST)
            for im in import_list.body:
                import_row = None
                if type(im) is ast.Import:
                    import_row = f'import {im.names[0].name}\n'
                elif type(im) is ast.ImportFrom:
                    import_row = f'from {im.module} import {im.names[0].name}\n'
                if import_row and import_row not in py_file_syntax:
                    py_file_syntax += import_row
            return py_file_syntax
        except SyntaxError:
            return False

    def requirements_validation(self, save_results: bool = True):
        print(f"Current size for project environment: {self.__venv_size}")
        os.system(f'pip freeze > {self.__temp_requirements}')
        final_dependencies = []
        py_syntax = self.__import_python_syntax
        if py_syntax:
            temp_python_file = 'py_import_validation.py'
            with open(temp_python_file, 'w') as py:
                py.write(py_syntax)
            test_dependencies = self.__test_dependencies
            for index, dep in enumerate(test_dependencies, 1):
                os.system(f"pip uninstall {dep} --y")
                result = os.system(f'python {temp_python_file}')
                if result > 0:
                    os.system(f"pip install --no-dependencies {dep}")
                    final_dependencies.append(dep)
                    print(f"Test dependencies count so far:"
                          f" {index}/{len(test_dependencies) + len(self.__current_dependencies)}."
                          f" for now {len(final_dependencies)} libraries are required.")
            os.remove(self.__temp_requirements)
            os.remove(temp_python_file)
            print(f"Start with {len(test_dependencies) + len(self.__current_dependencies)},"
                  f" finish with {len(final_dependencies)}")
            if save_results:
                self.__save_updated_requirements(final_dependencies=final_dependencies)
            print(f"Start with {self.__venv_size}")
            print(f"Finish with {self.__get_venv_size(path=self.__venv_path)}")

    def __save_updated_requirements(self, final_dependencies: list):
        final_requirements = ''
        for fr in final_dependencies:
            final_requirements += f"{fr}\n"
        with open(self.__temp_requirements, 'w') as req:
            req.write(final_requirements)
        print(f'Save result here: {self.__temp_requirements}')


def rmdiacritics(char):
    '''
    Return the base character of char, by "removing" any
    diacritics like accents or curls and strokes and the like.
    '''
    if char == 'æ':
        char = 'e'
        return char
    if char == 'ß':
        char = 's'
        return char
    desc = unicodedata.name(char)
    cutoff = desc.find(' WITH ')
    if cutoff != -1:
        desc = desc[:cutoff]
        try:
            char = unicodedata.lookup(desc)
        except KeyError:
            pass  # removing "WITH ..." produced an invalid name
    return char


def strip_accents(text: str, with_default_parser: bool = True):
    """ Function to format special characters to english"""
    string_format = ""
    if "Ã¡" in text:
        text = text.replace("Ã¡", "a")
    if "Ã­" in text:
        text = text.replace("Ã­", "i")
    if "Ãª" in text:
        text = text.replace("Ãª", "e")
    if "Ã©" in text:
        text = text.replace("Ã©", "e")
    if "Ãº" in text:
        text = text.replace("Ãº", "u")
    if "Ã¼" in text:
        text = text.replace("Ã¼", "u")
    if "Ã¼" in text:
        text = text.replace("Ã¼", "u")
    if 'u00' in text and "\\u00" not in text:
        text = text.replace('u00', "\\u00").encode().decode('unicode_escape')
    if '?' in text:
        text = text.replace('?', '')
    if with_default_parser:
        for char in text:
            new_char = rmdiacritics(char)
            string_format += new_char
        string_format = unicodedata.normalize('NFD', string_format) \
            .encode('ascii', 'ignore').decode("utf-8")
        return str(string_format)
    return text


# ---------------------------- files actions ------------------------------------#
def dict_to_json(string_content, print_error: bool = False):
    try:
        return json.dumps(str_to_dict(string_content))
    except Exception as e:
        if print_error:
            print(e)


def str_to_dict(string_content, print_error: bool = False):
    try:
        return ast.literal_eval(str(string_content))
    except Exception as e:
        if print_error:
            print(e)
        return load_json(string_content)


def load_json(string_content, print_error: bool = False):
    try:
        return json.loads(string_content)
    except Exception as e:
        if print_error:
            print(e)


def read_json(path):
    with open(path, 'r') as file:
        json_object = json.load(file)
    return json_object


def read_table_from_html(save_path, browser_session, url=None):
    if '.html' not in save_path:
        save_path = f"{save_path}.html"
    if browser_session is not None:
        if url is not None:
            browser_session.get_url(url)
        with open(save_path, 'w') as file:
            html_data = browser_session.actions.get_page_source()
            file.write(html_data)
    df = pd.read_html(save_path)
    return df


def var_validation(var: str):
    translate_var = Translator().translate(var).text
    if var != translate_var:
        return translate_var
    return var


def is_valid_date(date_to_check: str, tries: int = 0):
    if date_to_check:
        try:
            parse(date_to_check)
            return date_to_check
        except:
            if tries < 3:
                split_date = date_to_check.split('-')
                new_date = f"{split_date[0]}-{split_date[1]}-{30 if int(split_date[2] == 31) else 28 if split_date[1] == '02' else int(split_date[2]) - 1}"
                print(f"{tries + 1}. Updating date from {date_to_check} to {new_date}")
                return is_valid_date(new_date, tries + 1)
    return False

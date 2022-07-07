

class IncludePreprocessor(Preprocessor):
    """
    This provides an "include" function for Markdown, similar to that found in
    LaTeX (also the C pre-processor and Fortran). The syntax is {!filename!},
    which will be replaced by the contents of filename. Any such statements in
    filename will also be replaced. This replacement is done prior to any other
    Markdown processing. All file-names are evaluated relative to the location
    from which Markdown is being called.
    """

    def __init__(self, md, config):
        super(IncludePreprocessor, self).__init__(md)
        self.init_code = config["init_code"]
        if self.init_code:
            exec(self.init_code)

    def run(self, lines):
        for i, l in enumerate(lines):
            g = re.match("^\$pydantic: (.*)$", l)
            if g:
                cls_name = g.group(1)
                structs = analyze(cls_name)
                if structs is None:
                    print(
                        f"warning: mdantic pattern detected but failed to import module: {cls_name}"
                    )
                    continue
                tabs = fmt_tab(structs)
                table_str = ""
                for cls, tab in tabs.items():
                    table_str += "\n" + f"=={cls}==" + "\n\n" + str(tab) + "\n"
                lines = lines[:i] + [table_str] + lines[i + 1 :]

        return lines

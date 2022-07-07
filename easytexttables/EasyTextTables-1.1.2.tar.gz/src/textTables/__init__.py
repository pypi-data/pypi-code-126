class Table:
    def __init__(self, size=(5, 5), columns_header=None, rows_header=None, name='table', fill='#'):
        self.size = self.width, self.height = size
        self.name = name
        self.text = ''

        # set to default if it needs to
        if rows_header is None:
            rows_header = []
            for i in range(self.height):
                rows_header.append(str(i))
        if columns_header is None:
            columns_header = []
            for i in range(self.width):
                columns_header.append(str(i))

        self.header = columns_header, rows_header

        # making table
        self.table = []
        for rows in range(self.width):
            row = []
            for columns in range(self.height):
                row.append(fill)
            self.table.append(row)

    def get_text(self):
        try:
            block_width = 0
            for i in self.all_values():
                if len(str(i)) > block_width:
                    block_width = len(i)
            block_width += 1
        except TypeError:
            raise TypeError('Incorrect type of values. You should use String type for all values in table and header.')
        self.text = ''
        self.text += "|" + self.name.rjust(block_width, ' ')

        f = '\n|'+'-'*block_width

        for col_name in self.header[0]:
            self.text += "|" + col_name.rjust(block_width, ' ')
            f += '+'+block_width*'-'
        self.text += '|'+f+"|\n"


        for row in range(self.height):
            self.text += '|' + self.header[1][row].rjust(block_width, ' ')+'|'
            f = '\n|'+'-'*block_width
            for value in range(self.width):
                self.text += self.table[row][value].rjust(block_width, ' ')+'|'
                f += '+'+block_width*'-'
            self.text += f + '|\n'

        return self.text

    def all_values(self):
        values = []
        for i in self.table:
            for x in i:
                values.append(x)

        for i in self.header:
            for x in i:
                values.append(x)

        values.append(self.name)
        return values

    def print_text(self):
        print(self.get_text())

    def save_text(self, filename):
        open(filename, 'w').write(self.get_text())

    def set_at(self, x, y, value):
        self.table[x][y] = value

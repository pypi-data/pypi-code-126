import visitor
from visitor import index

def main():
    html_page = index.visit_digolds()
    print(html_page.text)

if __name__ == "__main__":
    main()
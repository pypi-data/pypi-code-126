from reportlab.pdfgen import canvas
from .image_util import ImageUtil

A4_H = (3508, 2479)
A4_V = (2479, 3508)


class PDFUtil:
    @staticmethod
    def gen_pdf(image_file_list: list, pdf_file_path: str, pdf_file_name: str) -> None:
        """
        生成 PDF 文件
        :param image_file_list: 图片文件列表
        :param pdf_file_path: PDF 文件保存路径
        :param pdf_file_name: PDF 文件名称
        :return:
        """
        pdf_file = pdf_file_path + '/' + pdf_file_name
        cv = canvas.Canvas(pdf_file)
        for image_file in image_file_list:
            image_direction = ImageUtil.get_image_direction(image_file['file_path'])
            if image_direction == 'V':
                cv.setPageSize(A4_V)
                cv.drawImage(image_file['file_path'], 0, 0, A4_V[0], A4_V[1])
            elif image_direction == 'H':
                cv.setPageSize(A4_H)
                cv.drawImage(image_file['file_path'], 0, 0, A4_H[0], A4_H[1])
            else:
                cv.setPageSize(A4_V)
                cv.drawImage(image_file['file_path'], 0, 0, A4_V[0], A4_V[1])
            cv.showPage()
        cv.save()

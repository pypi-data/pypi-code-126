import lucnham as f
# Các chức năng cần dùng để lên quẻ sẽ được liệt kê ví dụ ở đây
#print(f.AnCanChi('ẤT', 'TUẤT'))
#print(f.AnNienMenh('MÃO', 1, 0))
# print(f.AnTrachMo('MÃO'))

#print(f.ThienTuongQuyNhan('TỊ', 'TÂN', 'MÃO', 'Tiểu tuyết'))
#print(f.GiaoKhacMaoTinhBietTrach('ĐINH', 'MÃO', 'Lập xuân', 'MÙI'))
#print(f.ChonTamTruyen('Lập xuân', 'MÃO', 'ĐINH', 'TỊ'))
#print(f.NguyenThuTrungTham('ĐINH', 'MÙI', 'Lập xuân', 'MÙI'))
#print(f.BatChuyen('Lập xuân', 'MÙI', 'ĐINH', 'MÙI'))
#print(f.TriNhatThiepHai('ĐINH', 'MÙI', 'Lập xuân', 'MÙI'))

canNgay = 'KỶ'
chiNgay = 'MÃO'
nguyettuong = 'TÝ'
chiGio = 'THÂN'
tietKhi = f.danhsach24tietkhi[f.nguyetTuong.index(nguyettuong)]
print(f.ThienBanTuKhoa(tietKhi, chiGio, canNgay, chiNgay))
forerror = ["", "", "", "", [["", "", ""], ["", "", ""]]]
pa1 = forerror
pa2 = forerror
pa3 = forerror
pa4 = forerror
pa5 = forerror
pa6 = forerror
pa = f.ChonTamTruyen(tietKhi, chiGio, canNgay, chiNgay)

try:
    pa1 = f.NguyenThuTrungTham(canNgay, chiNgay, tietKhi, chiGio)
except:
    pass
try:
    pa4 = f.BatChuyen(tietKhi, chiGio, canNgay, chiNgay)
except:
    pass
try:
    pa5 = f.PhucNgam(canNgay, chiNgay, tietKhi, chiGio)
except:
    pass
try:
    pa6 = f.PhanNgam(tietKhi, chiGio, canNgay, chiNgay)
except:
    pass
try:
    pa3 = f.TriNhatThiepHai(canNgay, chiNgay, tietKhi, chiGio)
except:
    pass
try:
    pa2 = f.GiaoKhacMaoTinhBietTrach(canNgay, chiNgay, tietKhi, chiGio)
except:
    pass
print('Nguyên thủ trùng thẩm:', pa[0][0])
print('pa1 = ', pa1)
print('Giao khắc mão tinh biệt trách: ', pa[0][1])
print('pa2 = ', pa2)
print('Tri nhất thiệp hại: ', pa[0][2])
print('pa3 = ', pa3)
print('Bát chuyên: ', pa[0][3])
print('pa4 = ', pa4)
print('Phục ngâm: ', pa[0][4])
print('pa5 = ', pa5)
print('Phản ngâm: ', pa[0][5])
print('pa6 = ', pa6)
# Nguyên thủ, bát chuyên, PHẢN PHỤC, TRI NHẤT  giao khắc mão tinh ok
# KT MỖI thiệp hại

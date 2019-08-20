import grabcut
import cutImage
import colorDetect
from openpyxl import Workbook

write_wb = Workbook()

def main():
    print("!0")
    for i in range(36, 37):
        grabcut.main(str(i))

        # h left s left v left h right s right v right
        hl, sl, vl, hr, sr, vr= colorDetect.main(str(i))

        write_ws = write_wb.active
        write_ws['A1'] = 'hl'
        write_ws['B1'] = 'sl'
        write_ws['C1'] = 'vl'
        write_ws['A1'] = 'hr'
        write_ws['B1'] = 'sr'
        write_ws['C1'] = 'vr'

        write_ws.append([hl, sl, vl, hr, sr, vr])

        print(i)

main()
write_wb.save('result_black.xlsx')
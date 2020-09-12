import fitz

pdf_reader = fitz.open('1.pdf')
last_page = len(pdf_reader)

for page_no in range(last_page):
    img_arr = pdf_reader.getPageImageList(page_no)
    if img_arr:
        for image in img_arr:
            j = 0
            xref = image[0]
            pic = fitz.Pixmap(pdf_reader, xref)
            try:
                finalcrop = fitz.Pixmap(fitz.csRGB, pic)
                finalcrop.writePNG('images/PageNo_{}_ImageNo_{}.png'.format(page_no+1, j))
                print('page_no {} =>{}'.format( page_no, image))
            except Exception as e:
                pass
            pic = None
            finalcrop = None 
            j += 1
    else:
        print('Page_no {} => "No Image Found"'.format(page_no))

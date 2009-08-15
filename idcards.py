#!/usr/bin/python

from reportlab.pdfgen import canvas, textobject, pdfimages

from reportlab.lib.units import cm

cheight = 8 * cm
cwidth  = cheight * 1.61803399

ml, mr, mb, mt = 0.25*cm, cwidth - 2.5*cm, 0.25*cm, cheight - 2.5*cm # l,r, b, t Borders

def draw_borders(c):
    c.rect(0,0,cwidth - 2*cm,cheight - 2*cm, stroke = 1 )
    c.roundRect(ml,mb,mr,mt, radius = 5, stroke = 1)

def draw_banner(c):
    c.setFont("Helvetica-Bold",15)
    c.drawCentredString(cwidth/2 -cm, mt - 0.5*cm, "PyCon India 2009")
    c.line(ml + 0.5 *cm,
           mt - cm,
           mr - 0.5 *cm,
           mt - cm)
    
# def draw_image(c):
#     # i = pdfimages.PDFImage("BharathKeshav3_small.jpg",0,0)
#     c.drawImage("BharathKeshav3_small.jpg",cwidth/2, 0 + cm)

    
def write_details(c,name,role,regno):
    t = c.beginText()
    # t.setCharSpace(0.2*cm)
    t.setTextOrigin(ml + 0.5*cm,mt - 2* cm)
    t.setFont("Times-Bold",14)
    t.textLine(name)
    t.setFont("Times-Roman",14)
    t.textLine(role)
    c.drawText(t)
    
def main(name,role,regno):
    c = canvas.Canvas("id0.pdf", bottomup = 1)
    c.translate(2*cm,2*cm)
    draw_borders(c)
    draw_banner(c)
    # draw_image(c)
    write_details(c,name,role,regno)
    c.showPage()
    c.save()

if __name__ == "__main__":
    main("Name","Organisation might be a long string?","42")

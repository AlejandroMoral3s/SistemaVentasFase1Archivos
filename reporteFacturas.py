from fpdf import FPDF
from facturasList import*
import random

##	210 x 297 mm
class ReporteFacturas():

    name =  random.randint(1,1000)
    factura = FacturasList()
    facturaList = factura.dataJson['facturas']
    facturasReporte = []
    prodSTR = ""
    listanombreproductos = []
    ids = []
    
    def header(self, pdf):
        # Logo
        pdf.image('images/logoUsac.png', x=20, y =10, w=25, h=25)
        # Arial bold 15
        pdf.set_font('Arial', 'B', 25)
        # Title
        pdf.cell(w = 0, h = 25, txt = 'REPORTE DE FACTURACION', border=1, ln=1, align='C', fill=0)
        # Line break
        pdf.ln(5)
        
        
    
    def getIDS(self, idsList):
        self.facturaList = self.factura.dataJson['facturas']
        self.name = random.randint(1,1000)
        self.ids=idsList 
        
        self.crearTabla()       
    
    def setEncabezado(self, pdf):
        pdf.set_font('Times','B',14)
        pdf.cell(w=10,h=10,txt='ID', border=1, align='C',fill=0)
        pdf.cell(w=30,h=10,txt='Fecha', border=1, align='C',fill=0)
        pdf.cell(w=50,h=10,txt='Cliente', border=1, align='C',fill=0)
        pdf.cell(w=170,h=10,txt='Productos', border=1, align='C',fill=0) 
        pdf.multi_cell(w=0,h=10,txt='Total', border=1, align='C',fill=0) 
        self.getFacturas(pdf)
    
    def setTabla(self,pdf):
        pdf.set_font('Times','',12)

        
        for fact in self.facturasReporte: 
            self.listanombreproductos = []
            for prod in fact["_Factura__productos"]:
                self.listanombreproductos.append(prod['_Producto__descripcion'])
        
            self.prodSTR = ' , '.join(self.listanombreproductos) 
            
            pdf.cell(w=10,h=10,txt=f'{fact["_Factura__id"]}', border=1, align='C',fill=0)
            pdf.cell(w=30,h=10,txt=f'{fact["_Factura__fecha"]}', border=1, align='C',fill=0)
            pdf.cell(w=50,h=10,txt=f'{fact["_Factura__cliente"]}', border=1, align='C',fill=0)
            pdf.cell(w=170,h=10,txt=f'{self.prodSTR}', border=1, align='C',fill=0) 
            pdf.multi_cell(w=0,h=10,txt=f'{fact["_Factura__total"]}', border=1, align='C',fill=0) 
            
            self.listanombreproductos=[]
        pdf.output(f'reportes/{self.name}.pdf')
        
    

    def getFacturas(self,pdf):
        self.factura = FacturasList()
        self.facturaList = self.factura.dataJson['facturas']
        self.facturasReporte = []
        for id in self.ids:
            for fact in self.facturaList:
                if(fact['_Factura__id']==id):
                    fdict = self.factura.buscarFactura(id)
                    self.facturasReporte.append(fdict)
        self.setTabla(pdf)
    
    
    def crearTabla(self):
        pdf = FPDF(orientation='L', unit='mm',format='A4')
        pdf.add_page()
        self.header(pdf)        
        self.setEncabezado(pdf)

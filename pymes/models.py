from django.db import models
from automatic_crud.models import BaseModel
from members.models import StaffProfile

# Create your models here.

#Miembro

class miembro(BaseModel):
    EST = ((u'Soltero',u'Soltero'),
    (u'Casado',u'Casado'),
    (u'Viudo',u'Viudo'),
    (u'Divorciado',u'Divorciado'),
    )
    HIJ = ((u'Si',u'Si'),
    (u'No',u'No'),
    )
    GEN = ((u'H',u'Hombre'),
    (u'M',u'Mujer'),
    (u'PNM',u'Prefiero no mencionarlo'),
    )

    all_cruds_types = False
    normal_cruds = True
    ajax_crud = False

    normal_pagination=True

    nombres = models.CharField('Nombres', max_length=250)
    apellidos = models.CharField('Apellidos', max_length=250)
    nacionalidad = models.CharField('Nacionalidad', max_length=250)
    numero_de_documento = models.CharField('CIN', max_length=250)
    fecha_de_nacimiento = models.DateField('Fecha de Nacimiento')
    telefono_particular = models.CharField('Tel. Part.', max_length=250)
    telefono_corporativo = models.CharField('Tel. Corp.', max_length=250)
    mail_particular = models.CharField('Mail Part.', max_length=250)
    mail_corporativo = models.CharField('Mail Corp.', max_length=250)
    fecha_de_ingreso = models.DateField('Fecha de Ingreso')
    fecha_de_salida = models.DateField('Fecha de Salida')
    motivo_de_salida = models.CharField('Motivo de Salida', max_length=250)
    cargo = models.CharField('Cargo', max_length=250)
    notas_adicionales = models.CharField('Notas', max_length=250)
    contribuyente_set = models.CharField('SET', max_length=20, choices=HIJ)
    estado_civil= models.CharField('Estado Civil', max_length=25, choices=EST)
    hijos = models.CharField('Hijos', max_length=25, choices=HIJ)
    genero = models.CharField('Genero', max_length=25, choices=GEN)
    Asig_Organigrama = models.ForeignKey(StaffProfile, on_delete=models.CASCADE)
    
    class meta:
        Verbose_name = 'miembro'
        Verbose_name_plural = 'miembros'

    def __str__(self):
       return str(self.nombres) + ' - ' + self.apellidos

#Departamento

class departamento(BaseModel):
    nivel_jerarquia=(
        (u'1',u'1'),
        (u'2',u'2'),
        (u'3',u'3'),
        (u'4',u'4'),
        (u'5',u'5'),
        (u'6',u'6'),
        )
    nombre = models.CharField('Nombre de departamento', max_length=200)
    sigla = models.CharField('Sigla de departamento', max_length=200)
    jerarquia = models.CharField('Jerarquia asignada',max_length=20, choices=nivel_jerarquia)
    
    all_cruds_types = False
    normal_cruds = True
    ajax_crud = False

    normal_pagination=True

    class meta:
        Verbose_name = 'departamento'
        Verbose_name_plural = 'departamentos'
    
    def ___str__(self):
        return str(self.nombre) + '-' + (self.sigla)

#Cliente

class cliente(BaseModel):
    pagos =((u'1',u'Efectivo'),
    (u'2',u'Cheque'),
    (u'3',u'Transferencia'),
    (u'4',u'Deposito'),
    )

    cuentas =((u'Corriente',u'Corriente'),
    (u'Ahorro',u'Ahorro'),
    (u'Chequera',u'Chequera'),
    (u'Nomina',u'Nomina'),
    (u'Dolares',u'Dolares'),
    )

    nombre_de_la_empresa = models.CharField('Empresa',max_length=250)
    numero_de_ruc = models.CharField('RUC', max_length=250)
    nombre_del_nexo = models.CharField('Nexo', max_length=250)
    telefono_del_nexo = models.CharField('Tel. Nexo', max_length=250)
    mail_del_nexo = models.CharField('Mail Nexo', max_length=250)
    nombre_contacto_pagos = models.CharField('Contacto de pago', max_length=250)
    telefono_contacto_pagos = models.CharField('Tel. Conacto Pago', max_length=250)
    mail_contacto_pagos = models.CharField('Mail Conacto Pago', max_length=250)
    fecha_de_vinculacion = models.DateField('Fecha de Vinculacion')
    notas_adicionales = models.CharField('Notas', max_length=250)
    forma_de_pago_habitual = models.CharField('Pago Habitual', max_length=20,choices=pagos)
    banco = models.CharField('Banco', max_length=250)
    titular_de_la_cuenta = models.CharField('Titular de la cuenta', max_length=250)
    tipo_de_cuenta = models.CharField('Tipo de Cuenta', max_length=20, choices=cuentas)
    numero_de_cuenta = models.CharField('Nro de Cuenta', max_length=250)
    documento_de_cuenta = models.CharField('Documento', max_length=250)

    all_cruds_types = False
    normal_cruds = True
    ajax_crud = False

    class meta:
        Verbose_name = 'cliente'
        Verbose_name_plural = 'clientes'
    
    def ___str__(self):
        #return self.nombre_de_la_empresa
        return str(self.nombre_de_la_empresa) + ' - ' + self.numero_de_ruc

#Rubro

class rubro(BaseModel):
    nombre = models.CharField('Nombre de Rubro', max_length=200)
    sigla = models.CharField('Sigla del Rubro', max_length=200)
    area = models.ForeignKey(departamento, on_delete=models.CASCADE)
        
    all_cruds_types = False
    normal_cruds = True
    ajax_crud = False

    normal_pagination=True

    class meta:
        Verbose_name = 'rubro'
        Verbose_name_plural = 'rubros'
    
    def ___str__(self):
        return str(self.nombre) + ' - ' + (self.sigla)

#Ingreso

class ingreso(BaseModel):
    pagos =((u'1',u'Efectivo'),
    (u'2',u'Cheque'),
    (u'3',u'Transferencia'),
    (u'4',u'Deposito'),
    )
    nombre = models.CharField('Nombre', max_length=250)
    rubro = models.ForeignKey(rubro, on_delete=models.CASCADE)
    forma_de_pago = models.CharField('Forma de Pago', max_length=200, choices=pagos)
    tipo_de_cobro = models.CharField('Tipo de cobro', max_length=200)
    nombre_de_pago = models.CharField('Nombre de Pago',max_length=200)
    titular_de_pago = models.ForeignKey(cliente, on_delete=models.CASCADE)
    monto_de_pago = models.IntegerField('Monto de Pago')
    numero_de_factura = models.CharField('Factura Nro', max_length=200)

    all_cruds_types = False
    normal_cruds = True
    ajax_crud = False

    normal_pagination=True
    
    class Meta:
        verbose_name = 'ingreso'
        verbose_name_plural = 'ingresos'

    def __str__(self):
        return str(self.nombre) + '-' + self.forma_de_pago


#Egreso

class egreso(BaseModel):
    pagos =((u'1',u'Efectivo'),
    (u'2',u'Cheque'),
    (u'3',u'Transferencia'),
    (u'4',u'Deposito'),
    )
    nombre = models.CharField('Nombre', max_length=250)
    rubro = models.ForeignKey(rubro, on_delete=models.CASCADE)
    forma_de_pago = models.CharField('Forma de Pago', max_length=200,choices=pagos)
    tipo_de_pago = models.CharField('Tipo de Pago', max_length=200)
    nombre_de_pago = models.CharField('Nombre de Pago', max_length=200)
    titular_de_pago = models.ForeignKey(cliente, on_delete=models.CASCADE)
    monto_de_pago = models.IntegerField('Monto de Pago')
    numero_de_factura = models.CharField('Factura Nro', max_length=200)

    all_cruds_types = False
    normal_cruds = True
    ajax_crud = False
    
    normal_pagination=True

    class meta:
        Verbose_name = 'egreso'
        Verbose_name_plural = 'egresos'
    
    def ___str__(self):
        return str(self.nombre) + '-' + self.forma_de_pago

#Rol

class rol(BaseModel):
    nombre = models.CharField('Nombre', max_length=250)
    sigla = models.CharField('Sigla', max_length=25)
    empleado_o_proveedor = models.ForeignKey(cliente, on_delete=models.CASCADE)
    nombre_de_area = models.ForeignKey(departamento, on_delete=models.CASCADE)
    
    all_cruds_types = False
    normal_cruds = True
    ajax_crud = False

    normal_pagination=True

    class meta:
        Verbose_name = 'rol'
        Verbose_name_plural = 'roles'
    
    def ___str__(self):
        return str(self.nombre)
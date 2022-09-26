


{ 
    'name': 'Servicentro: Combustible',
    'category': 'Generic Modules/Human Resources',
    'version': '15.0.0',
    'sequence': 1,
    'author': 'Walter Greenaway',
    'summary': 'Los tipos de combustible',
    'description': "Los tipos de combustible se vende el servicentro",
    'license': 'LGPL-3',
    'depends': ['product'],
    'data': [
         'security/ir.model.access.csv',
          'views/combustible.xml',
          'views/pos_configuracion.xml',
          'views/tarjetas.xml',
          'views/transaccion.xml',
          'views/reporting.xml',
          'security/security.xml',
          
    ],

    'demo':[
        'demo/demo/demo.xml'

    ],
    'images': [],
    'application': True,
}

{
    'name': "Open Academy",
    'version': '1.0',
    'depends': ['base'],
    'author': "Kevin Flores",
    'category': 'Category',
    'description': """
        Industria del Software IS-902 IIPAC
        Cuenta 20161004584
        
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/openacademy.xml',
        'views/course.xml'
        
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        'demo/demo.xml',
    ],
}
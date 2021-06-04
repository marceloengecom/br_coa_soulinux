# © 2021 Marcelo Costa <contato@soulinux.com>, SOULinux
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


{  # pylint: disable=C8101,C8103
    'name': 'Plano de Contas SOULinux',
    'summary': "Plano de Contas para Microempresa SOULinux",
    'description': """Plano de Contas para Microempresa SOULinux""",
    'version': '14.0.1.0.0',
    'category': 'Localization',
    'author': 'SOULinux',
    'license': 'AGPL-3',
    'website': 'http://www.soulinux.com',
    'contributors': [
        'Marcelo Costa <contato@soulinux.com>',
    ],
    'depends': [
        'account',
    ],
    'data': [
        'data/account_group.xml',
        'data/br_chart_data.xml',
        'data/account.account.template.csv',
        'data/account_tax_template_data.xml',
    ],
    'active': True,
}
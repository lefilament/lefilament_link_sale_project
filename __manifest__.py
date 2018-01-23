{
	'name': 'Le Filament - Link Sales Order to Project',
	'version': '10.0.1.0',
	'license': 'AGPL-3',
	'description': """
	MODULE LINK SALE ORDER / PROJECT LE FILAMENT

	This module depends upon *sale_service* and *lefilament_projets* modules.

	- This module provides a new functionality to transform your sale order in projects and tasks (and to update those in case sale order is updated)
	- Product template has been enhanced, invoicing policy section in order to set how each product should behave when transformed from sale order to project/task.
	""",
	'author': 'LE FILAMENT',
	'category': 'LE FILAMENT',
	'depends': ['sale_timesheet', 'lefilament_projets'],
	'contributors': [
        'Juliana Poudou <JulianaPoudou>',
    ],
	'website': 'http://www.le-filament.com',
	'data': [
		'views/product_views.xml',
		'views/sale_config_settings_views.xml',
		'wizard/sale_views_wizard.xml',
		'views/sale_views.xml',
		'views/res_config_views.xml',
		'views/project_views.xml',
		'views/project_task_views.xml',
	],
	'qweb': [
    ],
}

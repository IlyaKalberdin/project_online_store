from django.core.management.utils import parse_apps_and_model_labels
from django.core.management.commands.loaddata import Command as LoaddataCommand
from django.db import transaction, connections
from catalog_app.models import Category


class Command(LoaddataCommand):
    """Класс-команда, работает так же как и loaddata только сначала удаляет все данные из БД"""
    def handle(self, *fixture_labels, **options):
        Category.objects.all().delete()

        self.ignore = options["ignore"]
        self.using = options["database"]
        self.app_label = options["app_label"]
        self.verbosity = options["verbosity"]
        self.excluded_models, self.excluded_apps = parse_apps_and_model_labels(
            options["exclude"]
        )
        self.format = options["format"]

        with transaction.atomic(using=self.using):
            self.loaddata(fixture_labels)

        # Close the DB connection -- unless we're still in a transaction. This
        # is required as a workaround for an edge case in MySQL: if the same
        # connection is used to create tables, load data, and query, the query
        # can return incorrect results. See Django #7572, MySQL #37735.
        if transaction.get_autocommit(self.using):
            connections[self.using].close()
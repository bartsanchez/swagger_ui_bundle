
import pytest


def test_import_ui():
    from swagger_ui_bundle import swagger_ui_path
    open(swagger_ui_path + "/index.html")

def test_import_ui_v4():
    from swagger_ui_bundle import swagger_ui_4_path
    open(swagger_ui_4_path + "/index.html")



from os.path import dirname, join
from textx import language, metamodel_from_file, metamodel_from_str
from tx_strictdoc.grammar import STRICTDOC_GRAMMAR
from tx_strictdoc.type_system import (
    STRICTDOC_BASIC_TYPE_SYSTEM,
)
@language("Strictdoc", "*.sdoc")
def strictdoc():
    "A language for writing technical specifications."
    #metamodel = metamodel_from_str(STRICTDOC_GRAMMAR + STRICTDOC_BASIC_TYPE_SYSTEM)
    metamodel = metamodel_from_file(join(dirname(__file__), "strictdoc.tx"))
    metamodel.model_param_defs.add(
        'type_name_check',
        'enables checks on the type name (default="on" or "off")'
    )
    return metamodel
    
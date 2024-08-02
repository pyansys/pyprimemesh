import re
from ansys.meshing.prime.numen.utils.evaluate import evaluate_expression
from ansys.meshing.prime.numen.utils.param_defs import ParamDefs

def check_param(param_defs: ParamDefs, input_param: dict, param_name: str, exp: str):
    # convert the check notation to func notation
    # "range:10,20"  ->  "$func(range,$value(param_name),10,20)"
    search_re = r"^\ *([^\ \:]*):"
    search_result = re.search(search_re, exp)
    if search_result != None:
        val_str = exp[search_result.span()[0]: search_result.span()[1]]
        val_name = search_result.groups()[0]
        exp = exp.replace(val_str, "$func(" +  val_name + ",$value(" + param_name + "),") + ")"
    else:
        exp = "$func(" + exp + ",$value(" + param_name + "))"
    return evaluate_expression(param_defs, input_param, exp)

def null_check(param_value):
    return param_value == "$null"

def type_check(param_value, param_type, sub_param_type = None):
    if param_type == "string" or param_type == "path":
        return isinstance(param_value, str)
    elif param_type == "int":
        return isinstance(param_value, int)
    elif param_type == "float":
        return isinstance(param_value, float) or isinstance(param_value, int)
    elif param_type == "boolean":
        return isinstance(param_value, bool)
    elif param_type == "list":
        if isinstance(param_value, list):
            for val in param_value:
                if not type_check(val, sub_param_type):
                    return False
            return True
        else:
            return False
    ValueError(f"Unexpected type \"{param_type}\" found.")
    return False
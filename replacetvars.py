from lex import Token
from mtypes import Typ, Any, NoneTyp, TypeTranslator, TypeVar
from typerepr import AnyRepr


Typ replace_type_vars(Typ typ, bool func_tvars=True):
    """Replace type variable references in a type with the any type. If
    func_tvars is false, only replace instance type variables.
    """
    return typ.accept(ReplaceTypeVarsVisitor(func_tvars))


class ReplaceTypeVarsVisitor(TypeTranslator):
    # Only override type variable handling; otherwise perform an indentity
    # transformation.
    
    bool func_tvars
    
    void __init__(self, bool func_tvars):
        self.func_tvars = func_tvars
    
    Typ visit_type_var(self, TypeVar t):
        if t.id > 0 or self.func_tvars:
            if t.repr is not None:
                # Give a representation for the dynamic type.
                tok = Token('any')
                tok.pre = t.repr.name.pre
                return Any(t.line, AnyRepr(tok))
            else:
                return Any()
        else:
            return t


Typ replace_func_type_vars(Typ typ, Typ target_type):
    """Replace function type variables in a type with the target type."""
    return typ.accept(ReplaceFuncTypeVarsVisitor(target_type))


class ReplaceFuncTypeVarsVisitor(TypeTranslator):
    void __init__(self, Typ target_type):
        self.target_type = target_type
    
    Typ visit_type_var(self, TypeVar t):
        if t.id < 0:
            return self.target_type
        else:
            return t

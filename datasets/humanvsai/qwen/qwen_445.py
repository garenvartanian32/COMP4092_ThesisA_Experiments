def mk_package(contents):
    pass

def mk_module(contents):
    """Instantiates a module specification from a parsed "AST" of a
  module.

  Parameters
  ----------
  contents : dict

  Returns
  ----------
  ModuleSpecification"""
    pass

def mk_class(contents):
    """Instantiates a class specification from a parsed "AST" of a
  class.

  Parameters
  ----------
  contents : dict

  Returns
  ----------
  ClassSpecification"""
    pass

def mk_function(contents):
    """Instantiates a function specification from a parsed "AST" of a
  function.

  Parameters
  ----------
  contents : dict

  Returns
  ----------
  FunctionSpecification"""
    pass

def mk_variable(contents):
    """Instantiates a variable specification from a parsed "AST" of a
  variable.

  Parameters
  ----------
  contents : dict

  Returns
  ----------
  VariableSpecification"""
    pass

def mk_import(contents):
    """Instantiates an import specification from a parsed "AST" of an
  import statement.

  Parameters
  ----------
  contents : dict

  Returns
  ----------
  ImportSpecification"""
    pass

def mk_comment(contents):
    """Instantiates a comment specification from a parsed "AST" of a
  comment.

  Parameters
  ----------
  contents : dict

  Returns
  ----------
  CommentSpecification"""
    pass

def mk_docstring(contents):
    """Instantiates a docstring specification from a parsed "AST" of a
  docstring.

  Parameters
  ----------
  contents : dict

  Returns
  ----------
  DocstringSpecification"""
    pass

def mk_decorator(contents):
    """Instantiates a decorator specification from a parsed "AST" of a
  decorator.

  Parameters
  ----------
  contents : dict

  Returns
  ----------
  DecoratorSpecification"""
    pass
from setuptools import setup, find_packages
 
setup (
  name='stlexer',
  packages=find_packages(),
  entry_points =
  """
  [pygments.lexers]
  stlexer = stlexer.lexer:IecstLexer
  """,
)
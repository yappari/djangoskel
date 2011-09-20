from skeleton import Skeleton, Var

class DjangoSkel(Skeleton):
    """
        Create a base Django project.
    """
    src = 'skel'
    variables = [
        Var('project', 'Name of the project', intro='intro'),
        Var('app', 'Name of the first app'),
        ]

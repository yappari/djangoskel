from os.path import join
from os import chmod
import stat
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

    def write(self, dst_dir, run_dry=False):
        super(DjangoSkel, self).write(dst_dir, run_dry=run_dry)
        chmod(join(dst_dir, self.template_formatter("{project}/manage.py")),
            stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)

import os
import sys

import kclvm.kcl.error as kcl_error

cwd = os.path.dirname(os.path.realpath(__file__))

kcl_error.print_kcl_error_message(
    kcl_error.get_exception(
        err_type=kcl_error.ErrType.InvalidFormatSpec_TYPE,
        file_msgs=[
            kcl_error.ErrFileMsg(
                filename=str(os.path.join(cwd, "main.k")),
                line_no=2,
                col_no=5,
                end_col_no=19
            )
        ],
        arg_msg="invalid string interpolation expression 'b = a + 1'"
    ),
    file=sys.stdout
)


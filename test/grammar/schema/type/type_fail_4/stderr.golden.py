import sys
import kclvm.kcl.error as kcl_error
import os

cwd = os.path.dirname(os.path.realpath(__file__))

kcl_error.print_kcl_error_message(
    kcl_error.get_exception(
        err_type=kcl_error.ErrType.CannotAddMembers_TYPE,
        file_msgs=[
            kcl_error.ErrFileMsg(
                filename=str(os.path.join(cwd, "main.k")),
                line_no=8,
                col_no=5,
                arg_msg="'fullName' is not defined in schema 'Person'"
            )
        ],
        arg_msg="Cannot add member 'fullName' to schema 'Person'"
    ),
    file=sys.stdout
)
